<script setup lang="ts">
import cohort1 from '@images/cohort/cohort1.png';

</script>

<template>
  <VCard class="position-relative" title="Когортный анализ">
    <VCardText style="flex: 1;">
      <VImg
        :src="cohort1"
      />
    </VCardText>

    <!-- Trophy -->
  </VCard>
</template>

<style lang="scss">
.v-card .trophy {
  position: absolute;
  inline-size: 5.188rem;
  inset-block-end: 1.25rem;
  inset-inline-end: 1.25rem;
}
</style>
