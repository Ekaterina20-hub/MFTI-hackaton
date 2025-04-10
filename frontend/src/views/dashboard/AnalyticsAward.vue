<script setup lang="ts">
</script>

<template>
  <VCard class="position-relative">
    <VCardText>
      <div class="mb-2">
        <h5 class="text-h5">
          Результаты анализа
        </h5>
        <div class="text-body-1">
          То что можно кратко описать
        </div>
      </div>
      <!-- <h4 class="text-h4 text-primary">
        $42.8k
      </h4>
      <div class="text-body-1 mb-2">
        78% of target <span class="text-high-emphasis">🚀</span>
      </div>
      <VBtn size="small">
        View Sales
      </VBtn> -->
    </VCardText>

    <!-- Trophy -->
    <!-- <VImg
      :src="trophy"
      class="trophy"
    /> -->
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
