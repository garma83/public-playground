from shapely.geometry import LineString, Polygon, MultiPolygon, Point

def skikit_merge_holes_tuples(polygons):

    exteriorPolygons = []  # List to store tuples of (exterior polygon, associated interior polygons)
    # print("Start merging holes: Step 1")

    # Step 1: Identify exterior polygons and associate them with interior polygons
    polygons = sorted(polygons, key=lambda x: x.area or x.boundingBoxSize)
    for polygon in polygons:

        # print("Processing polygon with", len(polygon.exterior.coords), "points")

        isExterior = True
        first_point = Point(polygon.exterior.coords[0])

        for otherPolygon in polygons:
            if polygon != otherPolygon and otherPolygon.contains(first_point):
                isExterior = False
                
        if isExterior:
            # print("Polygon is exterior")
            associatedInteriors = []

            # find all holes in this polygon
            for otherPolygon in polygons:
                other_first_point = Point(otherPolygon.exterior.coords[0])
                if polygon != otherPolygon and polygon.contains(other_first_point):
                    associatedInteriors.append(otherPolygon)

            # print("Found", len(associatedInteriors), "holes")
            exteriorPolygons.append((polygon, associatedInteriors))

    # print("Start merging holes: Step 2")
    # Step 2: Separate holes from interior polygons and update exteriorPolygons
    for i, (exteriorPolygon, interiorPolygonsList) in enumerate(exteriorPolygons):

        holes = []  # List to store polygons that are holes
        childrenOfHoles = []  # List to store polygons that are not directly descendant from the exterior
    
        for interiorPolygon in interiorPolygonsList:
            interior_first_point = Point(interiorPolygon.exterior.coords[0])

            for otherInteriorPolygon in interiorPolygonsList:
                if interiorPolygon != otherInteriorPolygon and otherInteriorPolygon.contains(interior_first_point):
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