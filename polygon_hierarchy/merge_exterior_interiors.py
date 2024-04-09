from shapely.geometry import LineString, Polygon, MultiPolygon, Point
from rtree import index

def skikit_merge_holes_tuples(polygons):

    exteriorPolygons = []  # List to store tuples of (exterior polygon, associated interior polygons)
    # print("Start merging holes: Step 1")

    idx = index.Index()
    for i, polygon in enumerate(polygons):
        idx.insert(i, polygon.bounds)

    # Step 1: Identify exterior polygons and associate them with interior polygons
    # polygons = sorted(polygons, key=lambda x: x.area or x.boundingBoxSize)
    for i, polygon in enumerate(polygons):

        isExterior = True
        first_point = Point(polygon.exterior.coords[0])

        for j in idx.intersection((first_point.x, first_point.y)):
            otherPolygon = polygons[j]
            if i != j and otherPolygon.contains(first_point):
                isExterior = False
                
        if isExterior:
            associatedInteriors = []

            # find all holes in this polygon
            for j in idx.intersection(polygon.bounds):
                otherPolygon = polygons[j]

                other_first_point = Point(otherPolygon.exterior.coords[0])
                if i != j and polygon.contains(other_first_point):
                    associatedInteriors.append(otherPolygon)

            exteriorPolygons.append((polygon, associatedInteriors))

    # Step 2: Separate holes from interior polygons and update exteriorPolygons
    for i, (exteriorPolygon, interiorPolygonsList) in enumerate(exteriorPolygons):

        holes = []  # List to store polygons that are holes
        childrenOfHoles = []  # List to store polygons that are not directly descendant from the exterior
    
        for j, interiorPolygon in enumerate(interiorPolygonsList):
            interior_first_point = Point(interiorPolygon.exterior.coords[0])

            for k, otherInteriorPolygon in enumerate(interiorPolygonsList):
                if j != k and otherInteriorPolygon.contains(interior_first_point):

                    # If interiorPolygon is inside any otherInteriorPolygon, it's not a hole
                    childrenOfHoles.append(interiorPolygon)
                    break
            else:

                # If interiorPolygon is not inside any other interiorPolygon, it's a hole
                holes.append(interiorPolygon)
                
        # Update the exterior polygon with just the direct holes
        exteriorPolygons[i] = (exteriorPolygon, holes)

        islandsAndHoles = skikit_merge_holes_tuples(childrenOfHoles)
        exteriorPolygons.extend(islandsAndHoles)

    return exteriorPolygons