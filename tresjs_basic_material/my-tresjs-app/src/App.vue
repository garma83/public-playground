<script lang="ts" setup>
import { TresCanvas } from '@tresjs/core'
import { OrbitControls } from '@tresjs/cientos'
</script>

<template>
  <TresCanvas>
    <TresPerspectiveCamera /><!-- Your scene goes here -->
    <OrbitControls />
    <TresMesh>
      <TresTorusGeometry :args="[1, 0.5, 16, 32]" />
      <TresMeshBasicMaterial color="'#ffffff'" />
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
}
#app {
  height: 100%;
  width: 100%;
}
</style>