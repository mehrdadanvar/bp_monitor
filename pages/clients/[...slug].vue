<template>
  <div>{{ route.params }}</div>
  <section
    class="container mx-auto bg-gray-100 px-12 py-12 border border-slate-200 rounded-lg"
  >
    <form class="max-w-2xl">
      <UInput
        icon="i-solar-spedometer-low-bold"
        color="cyan"
        size="xl"
        autofocus="true"
        name="systolic"
        placeholder="Systolic BP e.g. 120"
        type="number"
      />
      <UInput
        icon="i-solar-spedometer-low-bold"
        color="cyan"
        size="xl"
        placeholder="Diastolic BP e.g. 80"
      />
      <UInput icon="i-solar-spedometer-low-bold" color="cyan" size="xl" />
    </form>
    <UButton color="cyan" icon="i-solar-add-circle-bold"
      >Add a new record</UButton
    >
  </section>
  <section class=""></section>
</template>

<script setup>
let route = useRoute();
console.log(route);
</script>

<style lang="scss" scoped></style>
