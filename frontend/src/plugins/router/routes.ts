export const routes = [
  { path: '/' },
  {
    path: '/',
    component: () => import('@/layouts/default.vue'),
    children: [
      {
        path: '',
        component: () => import('@/pages/dashboard.vue'),
      },
      {
        path: 'analyzes/datalens/general',
        component: () => import('@/pages/analyzes/datalens/general.vue'),
      },
      {
        path: 'analyzes/abc-xyz',
        component: () => import('@/pages/analyzes/abc-xyz.vue'),
      },
      {
        path: 'analyzes/datalens/xyz',
        component: () => import('@/pages/analyzes/datalens/xyz.vue'),
      },
      {
        path: 'analyzes/datalens/abc',
        component: () => import('@/pages/analyzes/datalens/abc.vue'),
      },
      {
        path: 'analyzes/datalens/abc-xyz',
        component: () => import('@/pages/analyzes/datalens/abc-xyz.vue'),
      },
      {
        path: 'analyzes/datalens/many-abc-xyz',
        component: () => import('@/pages/analyzes/datalens/many-abc-xyz/index.vue'),
      },

      {
        path: 'analyzes/datalens/many-abc-xyz/1-xyz-categories',
        component: () => import('@/pages/analyzes/datalens/many-abc-xyz/1-xyz-categories.vue'),
      },
      {
        path: 'analyzes/datalens/many-abc-xyz/2-abc-xyz-categories',
        component: () => import('@/pages/analyzes/datalens/many-abc-xyz/2-abc-xyz-categories.vue'),
      },
      {
        path: 'analyzes/datalens/many-abc-xyz/3-abc-customers',
        component: () => import('@/pages/analyzes/datalens/many-abc-xyz/3-abc-customers.vue'),
      },
      {
        path: 'analyzes/datalens/many-abc-xyz/4-abc-states-customers',
        component: () => import('@/pages/analyzes/datalens/many-abc-xyz/4-abc-states-customers.vue'),
      },
      {
        path: 'analyzes/datalens/many-abc-xyz/5-abc-states-sellers',
        component: () => import('@/pages/analyzes/datalens/many-abc-xyz/5-abc-states-sellers.vue'),
      },


      {
        path: 'analyzes/rfm',
        component: () => import('@/pages/analyzes/rfm.vue'),
      },
      {
        path: 'analyzes/datalens/rfm',
        component: () => import('@/pages/analyzes/datalens/rfm.vue'),
      },
      {
        path: 'analyzes/geolocation',
        component: () => import('@/pages/analyzes/geolocation.vue'),
      },
      {
        path: 'analyzes/cohort',
        component: () => import('@/pages/analyzes/cohort.vue'),
      },
      {
        path: 'analyzes/datalens/cohort',
        component: () => import('@/pages/analyzes/datalens/cohort.vue'),
      },
      {
        path: 'analyzes/nlp',
        component: () => import('@/pages/analyzes/nlp.vue'),
      },
      {
        path: 'analyzes/cluster',
        component: () => import('@/pages/analyzes/cluster.vue'),
      },
      {
        path: 'analyzes/k-means',
        component: () => import('@/pages/analyzes/k-means.vue'),
      },
      {
        path: 'ml-models/time-machine',
        component: () => import('@/pages/ml-models/time-machine.vue'),
      },
      {
        path: 'ml-models/recall-precision-balance',
        component: () => import('@/pages/ml-models/recall-precision-balance.vue'),
      },
      {
        path: 'customers',
        component: () => import('@/pages/customers/index.vue'),
      },
      {
        path: 'about/dataset',
        component: () => import('@/pages/about/dataset.vue'),
      },

      {
        path: 'customers/:id',
        component: () => import('@/pages/customers/[id].vue'),
      },
      {
        path: 'typography',
        component: () => import('@/pages/typography.vue'),
      },
      {
        path: 'icons',
        component: () => import('@/pages/icons.vue'),
      },
      {
        path: 'cards',
        component: () => import('@/pages/cards.vue'),
      },
      {
        path: 'products',
        component: () => import('@/pages/products/index.vue'),
      },
      {
        path: 'form-layouts',
        component: () => import('@/pages/form-layouts.vue'),
      },
    ],
  },
  {
    path: '/',
    component: () => import('@/layouts/blank.vue'),
    children: [
      {
        path: 'login',
        component: () => import('@/pages/login.vue'),
      },
      {
        path: 'register',
        component: () => import('@/pages/register.vue'),
      },
      {
        path: '/:pathMatch(.*)*',
        component: () => import('@/pages/[...error].vue'),
      },
    ],
  },
]
