<script lang="ts" setup>
import { TresCanvas } from '@tresjs/core'
import { OrbitControls } from '@tresjs/cientos'
import { NoToneMapping } from 'three'
</script>

<template>
  <TresCanvas :tone-mapping="NoToneMapping">
    <TresPerspectiveCamera />
    <OrbitControls />
    <TresAmbientLight :intensity="1"/>
    <TresDirectionalLight :intensity="1"/>
    <TresMesh>
      <TresTorusGeometry :args="[1, 0.5, 16, 32]" />
      <TresMeshLambertMaterial :color="'#ff0000'" />
    </TresMesh>
  </TresCanvas>
</template>

<style>
html,
body {
  margin: 0;
  padding: 0;
  height: 100%;
  width: 100%;
  background-color: red;
}
#app {
  height: 100%;
  width: 100%;
}
</style>


<!-- <template>
  <div ref="canvasContainer" class="webgl-container"></div>
</template>

<script setup lang="ts">
import { ref, onMounted, onBeforeUnmount } from 'vue';
import * as THREE from 'three';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js';

const canvasContainer = ref<HTMLElement | null>(null);

let scene: THREE.Scene, camera: THREE.PerspectiveCamera, renderer: THREE.WebGLRenderer;
let controls: OrbitControls, animationFrameId: number;

onMounted(() => {
  if (!canvasContainer.value) return;

  // Scene
  scene = new THREE.Scene();

  // Camera
  camera = new THREE.PerspectiveCamera(
    75,
    canvasContainer.value.clientWidth / canvasContainer.value.clientHeight,
    0.1,
    1000
  );
  camera.position.set(2, 2, 5);

  // Renderer
  renderer = new THREE.WebGLRenderer({ antialias: true });
  renderer.setSize(canvasContainer.value.clientWidth, canvasContainer.value.clientHeight);
  renderer.toneMapping = THREE.NoToneMapping;
  canvasContainer.value.appendChild(renderer.domElement);

  // Lights
  const ambientLight = new THREE.AmbientLight(0xffffff, 1);
  scene.add(ambientLight);

  const directionalLight = new THREE.DirectionalLight(0xffffff, 1);
  directionalLight.position.set(5, 5, 5);
  scene.add(directionalLight);

  // Geometry & Material
  const geometry = new THREE.TorusGeometry(1, 0.5, 16, 32);
  const material = new THREE.MeshStandardMaterial({ color: 0xffffff });
  const torus = new THREE.Mesh(geometry, material);
  scene.add(torus);

  // Controls
  controls = new OrbitControls(camera, renderer.domElement);

  // Animation loop
  const animate = () => {
    animationFrameId = requestAnimationFrame(animate);
    controls.update();
    renderer.render(scene, camera);
  };
  animate();

  // Handle resize
  const onResize = () => {
    camera.aspect = canvasContainer.value!.clientWidth / canvasContainer.value!.clientHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(canvasContainer.value!.clientWidth, canvasContainer.value!.clientHeight);
  };
  window.addEventListener('resize', onResize);

  onBeforeUnmount(() => {
    cancelAnimationFrame(animationFrameId);
    window.removeEventListener('resize', onResize);
    controls.dispose();
    renderer.dispose();
  });
});
</script>

<style>
.webgl-container {
  width: 100%;
  height: 100vh;
  background-color: black;
}
</style> -->