const registerUser = () => {
	const mail = $('#mail').val();
	const usrname = $('#usrname').val();
	const pw1 = $('#pw1').val();
	const pw2 = $('#pw2').val();
	const url = `${location.protocol}//${Settings.serverHost}:${Settings.serverPort}/graphql`;
	const graph = `
		mutation {
			register (
			email: "` + mail + `"
			username: "` + usrname + `"
			password1: "` + pw1 + `"
			password2: "` + pw2 + `"
		) {
			success
			errors
			refreshToken
			token
		}
	}`;

	const options = {
		method: 'POST',
		headers: { 'Content-Type': 'application/json' },
		body: JSON.stringify({ query: graph }),
	};

	fetch(url, options)
		.then(response => response.json()) // parse response to json
		.then(data => {
			if (data.data.register.errors !== null) {
				alert(JSON.stringify(data.data.register.errors));
			} else if (data.data.register.success) {
				// verify user automativally :p
				// alert('Login successful, redirecting to login page');
				const token = data.data.register.token;

				// find remember settings if it exists to know where to store token
				if (Cookies.get('remember') === undefined || Cookies.get('remember') === true) {
					Cookies.set('auth_token', token);
				} else {
					sessionStorage.setItem('auth_token', token);
				}

				// VA = verify account
				const vaGraph = `
					mutation {
						verifyAccount(token: "`+ token +`") {
							success
							errors
						}
					}
				`;
				/* fetch(url, {
					method: 'POST',
					headers: { 'Content-Type': 'application/json' },
					body: JSON.stringify({ query: vaGraph }),
				})
				.then(response => response.json())
				.then(data => console.log(data.data)); */


				`
				Verifying account from above produces an error because
				I don't know how to get verification code from CLI message :/
				
				TEMPORARY SOULUTION: just redirect to login page
				`
				$(location).attr('href', 'dashboard/');
			}
		});
}

$('#register-form').submit(() => {
	// disable submit button
	$('#submitBtn').prop('disabled', true);
	registerUser();
	// enable submit button
	$('#submitBtn').prop('disabled', false);
});