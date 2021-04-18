$("#loginForm").submit(function() {
	var usrname = $('#username').val();
	var pword = $('#password').val();
	var shouldRemember = $('#remember').prop('checked');

	// disable everything
	$('#submitBtn').prop('disabled', true);
	login(usrname, pword, shouldRemember);
	$('#submitBtn').prop('disabled', false);
});

function login(usrname, pword, shouldRemember) {

	var emailQuery = null;
	// check if username is email
	if (hasEmail(usrname)) {
		emailQuery = `email: "${usrname}"`;
	} else {
		emailQuery = `username: "${usrname}"`;
	}

	const query = `
		mutation {
			tokenAuth (password: "${pword}" ${emailQuery}) {
				token
				refreshToken
				success
				errors
				user {
					username
					id
				}
			}
		}`;

	// const url = location.protocol + '//' + location.hostname + ':8000/graphql';
	const url = `${location.protocol}//${Settings.serverHost}:${Settings.serverPort}/graphql`
	const options = {
		method: 'POST',
		headers: { 'Content-Type': 'application/json' },
		body: JSON.stringify({ query: query }),
	};

	fetch(url, options)
		.then(response => response.json())
		.then(data => {

			if (data.data.tokenAuth.success) {
				const token = data.data.tokenAuth.token;
				const refreshToken = data.data.tokenAuth.refreshToken;
				const userID = data.data.tokenAuth.user.id;

				if (shouldRemember) {
					Cookies.set('remember', true);
					Cookies.set('auth_token', token);
					Cookies.set('refresh_token', refreshToken);
					// Cookies.set('userID', userID)
				} else {
					Cookies.set('remember', false);
					Cookies.remove('auth_token');
					Cookies.remove('refresh_token');
					Cookies.remove('userID');
					sessionStorage.setItem('auth_token', token);
					sessionStorage.setItem('refresh_token', refreshToken);
					// sessionStorage.setItem('userID', userID);
				}

				alert(`login successful`);
        		window.location = '/dashboard';

			} else {
				alert(data.data.tokenAuth.errors.nonFieldErrors[0].message);
			}

		});
}