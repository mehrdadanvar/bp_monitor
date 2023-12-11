<template>
  <UContainer>
    <div
      class="register flex flex-row rounded-2xl border border-blue-200 shadow-slate-300 shadow-xl px-6 py-2 max-w-3xl mx-auto my-auto mt-12"
    >
      <form @submit.prevent class="mx-auto mt-6 flex flex-col gap-y-20">
        <h1 class="text-2xl text-gray-700">Welcome to BP Monitor</h1>
        <p>Lets create an account</p>
        <div class="flex flex-col mx-auto gap-y-10">
          <UInput
            size="xl"
            color="blue"
            placeholder="Email Address"
            v-model="email"
            icon="i-solar-letter-broken"
            trailing
          />
          <div class="flex flex-row gap-3">
            <UInput
              size="xl"
              color="blue"
              placeholder="More than 6 characters"
              type="password"
              v-model="password"
              icon="i-solar-lock-password-bold-duotone"
              trailing
            />
            <UInput
              size="xl"
              color="blue"
              placeholder="Repeat Password"
              icon="i-solar-lock-password-bold-duotone"
              trailing
            />
          </div>
        </div>
        <div class="flex flex-col items-center gap-6">
          <UButton
            size="xl"
            label="Create Account"
            color="blue"
            variant="solid"
            @click="createUser"
            >Create Account</UButton
          >

          <NuxtLink to="/login"
            >Already a Member?
            <span class="text-blue-500 italic">Login</span></NuxtLink
          >
        </div>
      </form>
    </div>
  </UContainer>
</template>

<script setup>
let email = ref("");
let password = ref("");

async function createUser() {
  console.log("user data about to be sent");
  console.log(firstname.value, lastname.value, email.value, password.value),
    specialty.value;
  try {
    let response = await fetch("http://localhost:8000/users/signup", {
      method: "POST",
      body: JSON.stringify({
        firstname: firstname.value,
        lastname: lastname.value,
        email: email.value,
        password: password.value,
        specialty: specialty.value,
      }),
      headers: {
        "Content-Type": "application/json",
      },
    });
    let data = await response.json();
    console.log(data);
  } catch (error) {
    console.log(error);
  }
}
</script>

<style scoped>
.register {
}
</style>
