<template>
  <section
    class="profile container mx-auto bg-gray-100 px-12 py-12 border border-slate-200 rounded-lg mt-24"
  >
    <h1 class="text-gray-700 text-lg font-bold">Annmarie Locher</h1>
    <p>Past Medical History</p>
    <div class="text-gray-500">
      Lorem, ipsum dolor sit amet consectetur adipisicing elit. Iusto libero ex
      nulla esse ipsum nisi perspiciatis cum qui, sint ab, vitae optio inventore
      sequi vero nemo doloremque natus tempora atque!
    </div>
  </section>
  <section
    class="container mx-auto bg-gray-100 px-12 py-12 border border-slate-200 rounded-lg"
  >
    <div>
      <UButton
        label="Add a reading"
        @click="isOpen = true"
        icon="i-solar-add-circle-bold-duotone"
      />

      <UModal v-model="isOpen" class="">
        <div class="mx-6 my-20 py-6 min-w-3xl max-w-4xl">
          <form class="flex flex-col items-center gap-3">
            <p class="text-gray-700 text-lg mb-12">
              Type your Blood Pressure & Pulse Rate
            </p>
            <div class="w-full px-2">
              <UInput
                type="date"
                icon="i-solar-calendar-date-bold-duotone"
                size="xl"
                color="amber"
                v-model="date"
              />
            </div>
            <div class="flex gap-4 px-2">
              <UInput
                icon="i-solar-spedometer-low-bold"
                color="sky"
                size="xl"
                name="systolic"
                v-model="systolic"
                placeholder="Systolic BP e.g. null"
                type="number"
              />
              <UInput
                icon="i-solar-spedometer-low-bold"
                color="sky"
                size="xl"
                name="diastolic"
                v-model="diastolic"
                placeholder="Diastolic BP e.g. 80"
                type="number"
                class="text-gray-500"
              />
            </div>

            <UInput
              icon="i-solar-spedometer-low-bold"
              color="sky"
              size="xl"
              name="pulse_rate"
              v-model="pr"
              placeholder="pulse rate"
              class="w-full px-2"
              :trailing="true"
            />
            <UButton
              color="sky"
              @click="set_current_reading"
              icon="i-solar-ruler-cross-pen-bold-duotone"
              >Save
            </UButton>
          </form>
        </div>
      </UModal>
    </div>
  </section>
  <section
    class="results container mx-auto bg-gray-50 px-12 py-12 border border-slate-200 rounded-lg"
  >
    <div class="">Blood Pressure Table</div>
    <div class="text-sm text-gray-500 justify-end">
      <p>last upated</p>
      <p>2023/12/12</p>
    </div>

    <!-- <div>{{ readings }}</div> -->
    <!-- <div>the readings are {{ systolic }},{{ diastolic }}, {{ pr }}</div> -->
    <div class="min-w-2xl max-w-2xl">
      <UTable :rows="readings" />
    </div>
  </section>
</template>

<script setup>
let route = useRoute();
let isOpen = ref(false);

let readings = ref([]);
let reading = ref({ systolic: null, diastolic: null, pulse_rate: null });

let date = ref("");
let systolic = ref();
let diastolic = ref();
let pr = ref();
async function set_current_reading() {
  readings.value.push({
    id: readings.value.length === 0 ? 1 : readings.value.length + 1,
    date: "",
    systolic: systolic.value,
    diastolic: diastolic.value,
    pr: pr.value,
  });
  // close the modal and reset all reactives to null
  isOpen.value = !isOpen.value;
  systolic.value = null;
  diastolic.value = null;
  pr.value = null;
  date.value = null;
}
</script>

<style scoped></style>
