export const useUser = () =>
  useState("user", () => {
    let state_object = ref({
      role: "guest",
      has_account: false,
      identity: null,
      email: null,
      created_at: null,
      activated: false,
      logged_in: false,
      has_token: false,
      is_token_valid: false,
    });
    return state_object;
  });
