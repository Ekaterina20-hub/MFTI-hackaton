<script setup lang="ts">

  const $props = defineProps({
    currentPage: {
      type: Number,
      required: true
    },
    servicesData: {
      type: Array as () => Array<any>|null,
      required: true
    },
    isLoading: {
      type: Boolean,
      default: true
    },
  })
  const headers = [
    { title: 'Наименование категории', key: 'product_category_name' },
    { title: 'Размер', key: 'product_length_cm' },
    { title: 'Количество фотографий', key: 'product_photos_qty' },
    { title: 'ABC', key: 'abc' },
    { title: 'XYZ', key: 'xyz' },
  ]

</script>

<template>

  <VDataTableServer
    :items-per-page="15"
    :page="currentPage"
    :headers="headers"
    :items="servicesData ?? []"
    :loading="isLoading"
    :items-length="servicesData?.length ?? 0"
    class="text-no-wrap"
    :disable-sort="true"
    no-data-text="Продукты не найдены"
  >
    <template #item.product_category_name="{ item }">
      <div class="d-flex align-center gap-x-4" style="min-width: 250px; line-height: 1.2;">
        <div class="d-flex flex-column">
          <a class="text-capitalize"
            style="white-space: wrap;"
          >
            {{ item.product_category_name }}
        </a>
          <span class="text-body-2">
            {{ item.product_id }}
          </span>
        </div>
      </div>
    </template>

    <!-- category -->
    <template #item.abc="{ item }">
      <VChip color="success" class="text-uppercase">
        A
      </VChip>
    </template>

    <template #item.xyz="{ item }">
      <VChip color="primary" class="text-uppercase">
        X
      </VChip>
    </template>

    <template #item.product_photos_qty="{ item }">
      <div class="text-center">
        {{ item.product_photos_qty }}
      </div>
    </template>

    <template #item.product_length_cm="{ item }">
      <div class="text-center">
        {{ item.product_length_cm }}
        x
        {{ item.product_height_cm }}
        x
        {{ item.product_width_cm }}
      </div>
    </template>

    <!-- Actions -->
    <template #item.actions="{ item }">
      <!-- <IconBtn>
        <VIcon icon="ri-edit-2-fill" :to="'/account/service/' + item.id" />
      </IconBtn> -->
      <VBtn  icon="ri-edit-2-fill" :to="'/customers/' + item.id" variant="plain" />
    </template>
    <template #bottom>
    </template>
  </VDataTableServer>
</template>
