<script setup lang="ts">
  import { useRouter } from 'vue-router'
  import { useAppStore } from '@/store/app'
  import { useCartStore } from '@/store/cart'

  const router = useRouter()
  const appStore = useAppStore()
  const cartStore = useCartStore()

  const removeItem = (item: any) => {
    const index = cartStore.items.indexOf(item)
    cartStore.items.splice(index, 1)

    localStorage.setItem('cart', JSON.stringify(cartStore.items))
  }
  const goToCheckout = () => router.push({ name: 'Checkout' })
</script>

<template>
  <div>
    <v-menu
      v-if="appStore.isLoggedIn"
      location="bottom"
      width="400"
    >
      <template v-slot:activator="{ props }">
        <v-btn
          v-bind="props"
          rounded="xl"
        >
          <v-badge
            :model-value="!!cartStore.items.length"
            :content="cartStore.items.length"
          >
            <v-icon
              icon="mdi-cart"
              size="x-large"
            />
          </v-badge>
        </v-btn>
      </template>

      <v-card class="pa-4">
        <v-container
          class="pa-0"
          v-if="cartStore.items.length"
        >
          <v-list class="mb-4">
            <v-list-item
              v-for="(item, index) in cartStore.items"
              :key="index"
              :title="item.title"
              :subtitle="item.author"
            >
              <template #prepend>
                <v-avatar class="w-10">
                  <v-img
                    :src="item.get_thumbnail"
                    class="w-10"
                  />
                </v-avatar>
              </template>
              <template #append>
                <v-btn
                  rounded="xl"
                  @click="removeItem(item)"
                >
                  <v-icon
                    icon="mdi-close-circle"
                    size="x-large"
                  />
                </v-btn>
              </template>
            </v-list-item>
          </v-list>
          <v-btn
            variant="text"
            @click="goToCheckout"
          >
            Checkout
          </v-btn>
        </v-container>
        <v-container v-else> Looks like your cart is empty</v-container>
      </v-card>
    </v-menu>
  </div>
</template>
