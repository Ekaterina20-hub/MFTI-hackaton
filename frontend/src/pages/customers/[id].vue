<script lang="ts" setup>
import { useApi } from '@/composables/useApi';
import AccountSettingsAccount from '@/views/pages/account-settings/AccountSettingsAccount.vue';
import { useRoute } from 'vue-router';

const route = useRoute()

const $api = useApi()
const $route = useRoute()
const $router = useRouter()
const isLoading = ref(true)
const activeTab = ref(route.params.tab)
const customerProfile = ref<any|null>(null)
const customerId = ref<number|null>($route.params.id ? Number($route.params.id) : null)
const MLModels = ref<Array<any>|null>(null)
const mainMLModel = ref<any|null>(null)

// tabs
const tabs = [
  { title: 'О клинете', icon: 'ri-group-line', tab: 'account' },
  // { title: 'Исследования', icon: 'ri-lock-line', tab: 'security' },
  // { title: 'Предсказания ML моделей', icon: 'ri-notification-3-line', tab: 'notification' },
]

const loadData = () => {
  isLoading.value = true
  // if (metricaFilter.value) {
  //   url += '&threshold=' + metricaFilter.value.threshold
  // }
  $api.get(`/api/customers/${customerId.value}/`)
    .then(response => {
      customerProfile.value = response.data
      isLoading.value = false
    })
  $api.get('/api/ml-models/list')
    .then(response => {
      MLModels.value = response.data
      mainMLModel.value = MLModels.value?.find(x => x.is_main)
    })
}

  onMounted(() => {
    loadData()
  })

</script>

<template>
  <div>
    
    <AccountSettingsAccount :customerProfile="customerProfile" />

    <!-- <VTabs
      v-model="activeTab"
      show-arrows
      class="v-tabs-pill"
    >
      <VTab
        v-for="item in tabs"
        :key="item.icon"
        :value="item.tab"
      >
        <VIcon
          size="20"
          start
          :icon="item.icon"
        />
        {{ item.title }}
      </VTab>
    </VTabs>

    
    <VWindow
      v-model="activeTab"
      class="mt-5 disable-tab-transition"
      :touch="false"
    >
      <VWindowItem value="account">
        <AccountSettingsAccount :customerProfile="customerProfile" />
      </VWindowItem>

      <VWindowItem value="security">
        <AccountSettingsSecurity :customerProfile="customerProfile" />
      </VWindowItem>

      <VWindowItem value="notification">
        <AccountSettingsNotification :customerProfile="customerProfile" />
      </VWindowItem>
    </VWindow> -->
  </div>
</template>
