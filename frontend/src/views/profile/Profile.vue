<template>
	<div class="d-flex justify-content-center align-items-center wrapper" v-if="!user_found && !isLoading">
		<h1>@{{ profile_username }} topilmadi..</h1>
	</div>
	<div class="wrapper d-flex justify-content-center align-items-center" v-else-if="isLoading">
		<loader/>
	</div>
	<div v-else>
		<div class="wrapper">
		<div class="profile-card js-profile-card">
			<div class="profile-card__img">
				<img :src="baseUrl + user_datails.profile_photo" alt="profile card">
			</div>

			<div class="profile-card__cnt js-profile-cnt">
				<div class="profile-card__name">{{ user_datails.first_name }}</div>
				<h3 class="profile-card__name text-dark">@{{ user_datails.username }}</h3>
				<div class="profile-card__txt">{{ user_datails.bio }}</div>

				<div class="profile-card-social">
					<a v-if="user_datails.facebook" :href="'https://www.facebook.com/' + user_datails.facebook"
						class="profile-card-social__item facebook" target="_blank">
						<span class="icon-font">
							<svg class="icon">
								<use xlink:href="#icon-facebook"></use>
							</svg>
						</span>
					</a>

					<a v-if="user_datails.twitter" :href="'https://twitter.com/' + user_datails.twitter"
						class="profile-card-social__item twitter" target="_blank">
						<span class="icon-font">
							<svg class="icon">
								<use xlink:href="#icon-twitter"></use>
							</svg>
						</span>
					</a>

					<a v-if="user_datails.instagram" :href="'https://www.instagram.com/' + user_datails.instagram"
						class="profile-card-social__item instagram" target="_blank">
						<span class="icon-font">
							<svg class="icon">
								<use xlink:href="#icon-instagram"></use>
							</svg>
						</span>
					</a>


					<a v-if="user_datails.github" :href="'https://github.com/' + user_datails.github"
						class="profile-card-social__item github" target="_blank">
						<span class="icon-font">
							<svg class="icon">
								<use xlink:href="#icon-github"></use>
							</svg>
						</span>
					</a>

					<a v-if="user_datails.website" :href="user_datails.website" class="profile-card-social__item link"
						target="_blank">
						<span class="icon-font">
							<svg class="icon">
								<use xlink:href="#icon-link"></use>
							</svg>
						</span>
					</a>

				</div>

				<div class="profile-card-ctr">
					<button v-if="profile_username == username" @click="editProfileBtn"
						class="profile-card__button button--blue js-message-btn">Edit Profile</button>
					<!-- <a :href="'mailto:'+user_datails.email" v-else class="profile-card__button button--orange js-message-btn">Email</a> -->
				</div>

			</div>

			<div class="profile-card-message js-message p-5">
				<form class="profile-card-form" @submit.prevent>
					<div class="profile-card-form__container p-2">
						<div class="row">
							<div >
							<input class="form-control mt-1" type="text" placeholder="Username" v-model="user_datails.username">
							<input class="form-control mt-1" type="text" placeholder="Bio" v-model="user_datails.bio">
							<input class="form-control mt-1" type="text" placeholder="First name" v-model="user_datails.first_name">
							<input class="form-control mt-1" type="text" placeholder="Last name" v-model="user_datails.last_name">
						</div>
						<div>
							<input class="form-control mt-1" type="text" placeholder="instagram username" v-model="user_datails.instagram">
							<input class="form-control mt-1" type="text" placeholder="twitter username" v-model="user_datails.twitter">
							<input class="form-control mt-1" type="text" placeholder="github username" v-model="user_datails.github">
							<input class="form-control mt-1" type="text" placeholder="facebook username" v-model="user_datails.facebook">
							<input class="form-control mt-1" type="text" placeholder="website link" v-model="user_datails.website">
						</div>
						</div>
					</div>

					<div class="profile-card-form__bottom">
						<button
						@click="editProfile"
						class="profile-card__button button--blue js-message-close">
							Edit
						</button>

						<button @click="editProfileBtn" class="profile-card__button button--gray js-message-close">
							Cancel
						</button>
					</div>
				</form>
			</div>

		</div>

	</div>

	<svg hidden="hidden">
		<defs>
			<symbol id="icon-github" viewBox="0 0 32 32">
				<title>github</title>
				<path
					d="M16.192 0.512c-8.832 0-16 7.168-16 16 0 7.072 4.576 13.056 10.944 15.168 0.8 0.16 1.088-0.352 1.088-0.768 0-0.384 0-1.632-0.032-2.976-4.448 0.96-5.376-1.888-5.376-1.888-0.736-1.856-1.792-2.336-1.792-2.336-1.44-0.992 0.096-0.96 0.096-0.96 1.6 0.128 2.464 1.664 2.464 1.664 1.44 2.432 3.744 1.728 4.672 1.344 0.128-1.024 0.544-1.728 1.024-2.144-3.552-0.448-7.296-1.824-7.296-7.936 0-1.76 0.64-3.168 1.664-4.288-0.16-0.416-0.704-2.016 0.16-4.224 0 0 1.344-0.416 4.416 1.632 1.28-0.352 2.656-0.544 4-0.544s2.72 0.192 4 0.544c3.040-2.080 4.384-1.632 4.384-1.632 0.864 2.208 0.32 3.84 0.16 4.224 1.024 1.12 1.632 2.56 1.632 4.288 0 6.144-3.744 7.488-7.296 7.904 0.576 0.512 1.088 1.472 1.088 2.976 0 2.144-0.032 3.872-0.032 4.384 0 0.416 0.288 0.928 1.088 0.768 6.368-2.112 10.944-8.128 10.944-15.168 0-8.896-7.168-16.032-16-16.032z">
				</path>
				<path
					d="M6.24 23.488c-0.032 0.064-0.16 0.096-0.288 0.064-0.128-0.064-0.192-0.16-0.128-0.256 0.032-0.096 0.16-0.096 0.288-0.064 0.128 0.064 0.192 0.16 0.128 0.256v0z">
				</path>
				<path
					d="M6.912 24.192c-0.064 0.064-0.224 0.032-0.32-0.064s-0.128-0.256-0.032-0.32c0.064-0.064 0.224-0.032 0.32 0.064s0.096 0.256 0.032 0.32v0z">
				</path>
				<path
					d="M7.52 25.12c-0.096 0.064-0.256 0-0.352-0.128s-0.096-0.32 0-0.384c0.096-0.064 0.256 0 0.352 0.128 0.128 0.128 0.128 0.32 0 0.384v0z">
				</path>
				<path
					d="M8.384 26.016c-0.096 0.096-0.288 0.064-0.416-0.064s-0.192-0.32-0.096-0.416c0.096-0.096 0.288-0.064 0.416 0.064 0.16 0.128 0.192 0.32 0.096 0.416v0z">
				</path>
				<path
					d="M9.6 26.528c-0.032 0.128-0.224 0.192-0.384 0.128-0.192-0.064-0.288-0.192-0.256-0.32s0.224-0.192 0.416-0.128c0.128 0.032 0.256 0.192 0.224 0.32v0z">
				</path>
				<path
					d="M10.912 26.624c0 0.128-0.16 0.256-0.352 0.256s-0.352-0.096-0.352-0.224c0-0.128 0.16-0.256 0.352-0.256 0.192-0.032 0.352 0.096 0.352 0.224v0z">
				</path>
				<path
					d="M12.128 26.4c0.032 0.128-0.096 0.256-0.288 0.288s-0.352-0.032-0.384-0.16c-0.032-0.128 0.096-0.256 0.288-0.288s0.352 0.032 0.384 0.16v0z">
				</path>
			</symbol>

			<symbol id="icon-facebook" viewBox="0 0 32 32">
				<title>facebook</title>
				<path d="M19 6h5v-6h-5c-3.86 0-7 3.14-7 7v3h-4v6h4v16h6v-16h5l1-6h-6v-3c0-0.542 0.458-1 1-1z"></path>
			</symbol>

			<symbol id="icon-instagram" viewBox="0 0 32 32">
				<title>instagram</title>
				<path
					d="M16 2.881c4.275 0 4.781 0.019 6.462 0.094 1.563 0.069 2.406 0.331 2.969 0.55 0.744 0.288 1.281 0.638 1.837 1.194 0.563 0.563 0.906 1.094 1.2 1.838 0.219 0.563 0.481 1.412 0.55 2.969 0.075 1.688 0.094 2.194 0.094 6.463s-0.019 4.781-0.094 6.463c-0.069 1.563-0.331 2.406-0.55 2.969-0.288 0.744-0.637 1.281-1.194 1.837-0.563 0.563-1.094 0.906-1.837 1.2-0.563 0.219-1.413 0.481-2.969 0.55-1.688 0.075-2.194 0.094-6.463 0.094s-4.781-0.019-6.463-0.094c-1.563-0.069-2.406-0.331-2.969-0.55-0.744-0.288-1.281-0.637-1.838-1.194-0.563-0.563-0.906-1.094-1.2-1.837-0.219-0.563-0.481-1.413-0.55-2.969-0.075-1.688-0.094-2.194-0.094-6.463s0.019-4.781 0.094-6.463c0.069-1.563 0.331-2.406 0.55-2.969 0.288-0.744 0.638-1.281 1.194-1.838 0.563-0.563 1.094-0.906 1.838-1.2 0.563-0.219 1.412-0.481 2.969-0.55 1.681-0.075 2.188-0.094 6.463-0.094zM16 0c-4.344 0-4.887 0.019-6.594 0.094-1.7 0.075-2.869 0.35-3.881 0.744-1.056 0.412-1.95 0.956-2.837 1.85-0.894 0.888-1.438 1.781-1.85 2.831-0.394 1.019-0.669 2.181-0.744 3.881-0.075 1.713-0.094 2.256-0.094 6.6s0.019 4.887 0.094 6.594c0.075 1.7 0.35 2.869 0.744 3.881 0.413 1.056 0.956 1.95 1.85 2.837 0.887 0.887 1.781 1.438 2.831 1.844 1.019 0.394 2.181 0.669 3.881 0.744 1.706 0.075 2.25 0.094 6.594 0.094s4.888-0.019 6.594-0.094c1.7-0.075 2.869-0.35 3.881-0.744 1.050-0.406 1.944-0.956 2.831-1.844s1.438-1.781 1.844-2.831c0.394-1.019 0.669-2.181 0.744-3.881 0.075-1.706 0.094-2.25 0.094-6.594s-0.019-4.887-0.094-6.594c-0.075-1.7-0.35-2.869-0.744-3.881-0.394-1.063-0.938-1.956-1.831-2.844-0.887-0.887-1.781-1.438-2.831-1.844-1.019-0.394-2.181-0.669-3.881-0.744-1.712-0.081-2.256-0.1-6.6-0.1v0z">
				</path>
				<path
					d="M16 7.781c-4.537 0-8.219 3.681-8.219 8.219s3.681 8.219 8.219 8.219 8.219-3.681 8.219-8.219c0-4.537-3.681-8.219-8.219-8.219zM16 21.331c-2.944 0-5.331-2.387-5.331-5.331s2.387-5.331 5.331-5.331c2.944 0 5.331 2.387 5.331 5.331s-2.387 5.331-5.331 5.331z">
				</path>
				<path
					d="M26.462 7.456c0 1.060-0.859 1.919-1.919 1.919s-1.919-0.859-1.919-1.919c0-1.060 0.859-1.919 1.919-1.919s1.919 0.859 1.919 1.919z">
				</path>
			</symbol>

			<symbol id="icon-twitter" viewBox="0 0 32 32">
				<title>twitter</title>
				<path
					d="M32 7.075c-1.175 0.525-2.444 0.875-3.769 1.031 1.356-0.813 2.394-2.1 2.887-3.631-1.269 0.75-2.675 1.3-4.169 1.594-1.2-1.275-2.906-2.069-4.794-2.069-3.625 0-6.563 2.938-6.563 6.563 0 0.512 0.056 1.012 0.169 1.494-5.456-0.275-10.294-2.888-13.531-6.862-0.563 0.969-0.887 2.1-0.887 3.3 0 2.275 1.156 4.287 2.919 5.463-1.075-0.031-2.087-0.331-2.975-0.819 0 0.025 0 0.056 0 0.081 0 3.181 2.263 5.838 5.269 6.437-0.55 0.15-1.131 0.231-1.731 0.231-0.425 0-0.831-0.044-1.237-0.119 0.838 2.606 3.263 4.506 6.131 4.563-2.25 1.762-5.075 2.813-8.156 2.813-0.531 0-1.050-0.031-1.569-0.094 2.913 1.869 6.362 2.95 10.069 2.95 12.075 0 18.681-10.006 18.681-18.681 0-0.287-0.006-0.569-0.019-0.85 1.281-0.919 2.394-2.075 3.275-3.394z">
				</path>
			</symbol>

			<symbol id="icon-link" viewBox="0 0 32 32">
				<title>link</title>
				<path
					d="M17.984 11.456c-0.704 0.704-0.704 1.856 0 2.56 2.112 2.112 2.112 5.568 0 7.68l-5.12 5.12c-2.048 2.048-5.632 2.048-7.68 0-1.024-1.024-1.6-2.4-1.6-3.84s0.576-2.816 1.6-3.84c0.704-0.704 0.704-1.856 0-2.56s-1.856-0.704-2.56 0c-1.696 1.696-2.624 3.968-2.624 6.368 0 2.432 0.928 4.672 2.656 6.4 1.696 1.696 3.968 2.656 6.4 2.656s4.672-0.928 6.4-2.656l5.12-5.12c3.52-3.52 3.52-9.248 0-12.8-0.736-0.672-1.888-0.672-2.592 0.032z">
				</path>
				<path
					d="M29.344 2.656c-1.696-1.728-3.968-2.656-6.4-2.656s-4.672 0.928-6.4 2.656l-5.12 5.12c-3.52 3.52-3.52 9.248 0 12.8 0.352 0.352 0.8 0.544 1.28 0.544s0.928-0.192 1.28-0.544c0.704-0.704 0.704-1.856 0-2.56-2.112-2.112-2.112-5.568 0-7.68l5.12-5.12c2.048-2.048 5.632-2.048 7.68 0 1.024 1.024 1.6 2.4 1.6 3.84s-0.576 2.816-1.6 3.84c-0.704 0.704-0.704 1.856 0 2.56s1.856 0.704 2.56 0c1.696-1.696 2.656-3.968 2.656-6.4s-0.928-4.704-2.656-6.4z">
				</path>
			</symbol>
		</defs>
	</svg>
	</div>
</template>
<script>
import axios from 'axios';
export default {
	name: 'profile',
	data() {
		return {
			isLoading: false,
			profile_username: '',
			user_found: false,
			user_datails: [],
			baseUrl: axios.defaults.baseURL
		}
	},
	props: {
		username: {
			type: String,
			required: false
		}
	},
	methods: {
		async getUser() {
			try {
				this.isLoading = true
				const users = await axios.get('/api/users/')
				this.profile_username = this.$route.params.username
				users.data.forEach(e => {
					if (this.profile_username == e.username) {
						this.user_found = true
					}
				});
			} catch (error) {
				this.user_found = false
				console.log(error.message);
			} finally {
				this.isLoading = false
			}
		},
		async getUserDetails() {
			try {
				this.isLoading = true
				const user = await axios.get(`/api/users/${this.$route.params.username}/`)
				const profile = await axios.get(`/api/profiles/${user.data.id}/`)
				let user_details_arr = {
					id: user.data.id,
					email: user.data.email,
					username: user.data.username,
					first_name: user.data.first_name,
					last_name: user.data.last_name,
					gender: user.data.gender,
					profile_photo: profile.data.profile_photo,
					bio: profile.data.bio,
					verifyed: profile.data.verifyed,
					instagram: profile.data.instagram,
					twitter: profile.data.twitter,
					facebook: profile.data.facebook,
					github: profile.data.github,
					website: profile.data.website,
				}
				this.user_datails = user_details_arr
			} catch (error) {
				console.log(error.message)
			} finally {
				this.isLoading = false
			}
		},
		editProfileBtn() {
			let card = document.querySelector('.js-profile-card')
			card.classList.toggle('active')
		},
		async editProfile(){
			const userFormData= {
				id: this.user_datails.id,
				email: this.user_datails.email,
				username: this.user_datails.username.toLowerCase(),
				gender: this.user_datails.gender,
				last_name: this.user_datails.last_name,
				first_name: this.user_datails.first_name
			}
			const profileFormData=
				{
					bio: this.user_datails.bio,
					verifyed: this.user_datails.verifyed,
					instagram: this.user_datails.instagram,
					twitter: this.user_datails.twitter,
					github: this.user_datails.github,
					facebook: this.user_datails.facebook,
					website: this.user_datails.website,
					user: this.user_datails.id
				}
			try {
				await axios.post(`/api/users/updata/${this.user_datails.id}/`, userFormData )
				const reqponse = await axios.post(`/api/profiles/updata/${this.user_datails.id}/`, profileFormData)
				console.log(reqponse);
			} catch (error) {
				alert(error.message)
			}finally{
				this.$router.push('@'+ this.user_datails.username.toLowerCase())
				this.editProfileBtn()
			}
		}
	},

	mounted() {
		this.getUser()
		this.getUserDetails()
	}
}
</script>
<style scoped>
@import url('https://fonts.googleapis.com/css?family=Quicksand:400,500,700&subset=latin-ext');

html {
	position: relative;
	overflow-x: hidden !important;
}

* {
	box-sizing: border-box;
}

body {
	font-family: 'Quicksand', sans-serif;
	color: #324e63;
}

a,
a:hover {
	text-decoration: none;
}

.icon {
	display: inline-block;
	width: 1em;
	height: 1em;
	stroke-width: 0;
	stroke: currentColor;
	fill: currentColor;
}

.wrapper {
	width: 100%;
	height: auto;
	min-height: 100vh;
	padding: 50px 20px;
	padding-top: 100px;
	display: flex;
	background-image: linear-gradient(-20deg, #ff2846 0%, #6944ff 100%);
	display: flex;
}

@media screen and (max-width: 768px) {
	.wrapper {
		height: auto;
		min-height: 100vh;
		padding-top: 100px;
	}
}

.profile-card {
	width: 100%;
	min-height: 460px;
	margin: auto;
	box-shadow: 0px 8px 60px -10px rgba(13, 28, 39, 0.6);
	background: #fff;
	border-radius: 12px;
	max-width: 700px;
	position: relative;
}

.profile-card.active .profile-card__cnt {
	filter: blur(6px);
}

.profile-card.active .profile-card-message,
.profile-card.active .profile-card__overlay {
	opacity: 1;
	pointer-events: auto;
	transition-delay: 0.1s;
}

.profile-card.active .profile-card-form {
	transform: none;
	transition-delay: 0.1s;
}

.profile-card__img {
	width: 150px;
	height: 150px;
	margin-left: auto;
	margin-right: auto;
	transform: translateY(-50%);
	border-radius: 50%;
	overflow: hidden;
	position: relative;
	z-index: 4;
	box-shadow: 0px 5px 50px 0px #6c44fc, 0px 0px 0px 7px rgba(107, 74, 255, 0.5);
}

@media screen and (max-width: 576px) {
	.profile-card__img {
		width: 120px;
		height: 120px;
	}
}

.profile-card__img img {
	display: block;
	width: 100%;
	height: 100%;
	object-fit: cover;
	border-radius: 50%;
}

.profile-card__cnt {
	margin-top: -35px;
	text-align: center;
	padding: 0 20px;
	padding-bottom: 40px;
	transition: all 0.3s;
}

.profile-card__name {
	font-weight: 700;
	font-size: 24px;
	color: #6944ff;
	margin-bottom: 15px;
}

.profile-card__txt {
	font-size: 18px;
	font-weight: 500;
	color: #324e63;
	margin-bottom: 15px;
}

.profile-card__txt strong {
	font-weight: 700;
}

.profile-card-loc {
	display: flex;
	justify-content: center;
	align-items: center;
	font-size: 18px;
	font-weight: 600;
}

.profile-card-loc__icon {
	display: inline-flex;
	font-size: 27px;
	margin-right: 10px;
}

.profile-card-inf {
	display: flex;
	justify-content: center;
	flex-wrap: wrap;
	align-items: flex-start;
	margin-top: 35px;
}

.profile-card-inf__item {
	padding: 10px 35px;
	min-width: 150px;
}

@media screen and (max-width: 768px) {
	.profile-card-inf__item {
		padding: 10px 20px;
		min-width: 120px;
	}
}

.profile-card-inf__title {
	font-weight: 700;
	font-size: 27px;
	color: #324e63;
}

.profile-card-inf__txt {
	font-weight: 500;
	margin-top: 7px;
}

.profile-card-social {
	margin-top: 25px;
	display: flex;
	justify-content: center;
	align-items: center;
	flex-wrap: wrap;
}

.profile-card-social__item {
	display: inline-flex;
	width: 55px;
	height: 55px;
	margin: 15px;
	border-radius: 50%;
	align-items: center;
	justify-content: center;
	color: #fff;
	background: #405de6;
	box-shadow: 0px 7px 30px rgba(43, 98, 169, 0.5);
	position: relative;
	font-size: 21px;
	flex-shrink: 0;
	transition: all 0.3s;
}

@media screen and (max-width: 768px) {
	.profile-card-social__item {
		width: 50px;
		height: 50px;
		margin: 10px;
	}
}

@media screen and (min-width: 768px) {
	.profile-card-social__item:hover {
		transform: scale(1.2);
	}
}

.profile-card-social__item.facebook {
	background: linear-gradient(45deg, #3b5998, #0078d7);
	box-shadow: 0px 4px 30px rgba(43, 98, 169, 0.5);
}

.profile-card-social__item.twitter {
	background: linear-gradient(45deg, #1da1f2, #0e71c8);
	box-shadow: 0px 4px 30px rgba(19, 127, 212, 0.7);
}

.profile-card-social__item.instagram {
	background: linear-gradient(45deg, #405de6, #5851db, #833ab4, #c13584, #e1306c, #fd1d1d);
	box-shadow: 0px 4px 30px rgba(120, 64, 190, 0.6);
}

.profile-card-social__item.behance {
	background: linear-gradient(45deg, #1769ff, #213fca);
	box-shadow: 0px 4px 30px rgba(27, 86, 231, 0.7);
}

.profile-card-social__item.github {
	background: linear-gradient(45deg, #333, #626b73);
	box-shadow: 0px 4px 30px rgba(63, 65, 67, 0.6);
}

.profile-card-social__item.codepen {
	background: linear-gradient(45deg, #324e63, #414447);
	box-shadow: 0px 4px 30px rgba(55, 75, 90, 0.6);
}

.profile-card-social__item.link {
	background: linear-gradient(45deg, #d5135a, #f05924);
	box-shadow: 0px 4px 30px rgba(223, 45, 70, 0.6);
}

.profile-card-social .icon-font {
	display: inline-flex;
}

.profile-card-ctr {
	display: flex;
	justify-content: center;
	align-items: center;
	margin-top: 40px;
}

@media screen and (max-width: 576px) {
	.profile-card-ctr {
		flex-wrap: wrap;
	}
}

.profile-card__button {
	background: none;
	border: none;
	font-family: 'Quicksand', sans-serif;
	font-weight: 700;
	font-size: 19px;
	margin: 15px 35px;
	padding: 15px 40px;
	min-width: 201px;
	border-radius: 50px;
	min-height: 55px;
	color: #fff;
	cursor: pointer;
	backface-visibility: hidden;
	transition: all 0.3s;
}

@media screen and (max-width: 768px) {
	.profile-card__button {
		min-width: 170px;
		margin: 15px 25px;
	}
}

@media screen and (max-width: 576px) {
	.profile-card__button {
		min-width: inherit;
		margin: 0;
		margin-bottom: 16px;
		width: 100%;
		max-width: 300px;
	}

	.profile-card__button:last-child {
		margin-bottom: 0;
	}
}

.profile-card__button:focus {
	outline: none !important;
}

@media screen and (min-width: 768px) {
	.profile-card__button:hover {
		transform: translateY(-5px);
	}
}

.profile-card__button:first-child {
	margin-left: 0;
}

.profile-card__button:last-child {
	margin-right: 0;
}

.profile-card__button.button--blue {
	background: linear-gradient(45deg, #1da1f2, #0e71c8);
	box-shadow: 0px 4px 30px rgba(19, 127, 212, 0.4);
}

.profile-card__button.button--blue:hover {
	box-shadow: 0px 7px 30px rgba(19, 127, 212, 0.75);
}

.profile-card__button.button--orange {
	background: linear-gradient(45deg, #d5135a, #f05924);
	box-shadow: 0px 4px 30px rgba(223, 45, 70, 0.35);
}

.profile-card__button.button--orange:hover {
	box-shadow: 0px 7px 30px rgba(223, 45, 70, 0.75);
}

.profile-card__button.button--gray {
	box-shadow: none;
	background: #dcdcdc;
	color: #142029;
}

.profile-card-message {
	width: 100%;
	height: 100%;
	position: absolute;
	top: 0;
	left: 0;
	padding-top: 130px;
	padding-bottom: 100px;
	opacity: 0;
	pointer-events: none;
	transition: all 0.3s;
}

.profile-card-form {
	box-shadow: 0 4px 30px rgba(15, 22, 56, 0.35);
	max-width: 80%;
	margin-left: auto;
	margin-right: auto;
	height: 100%;
	background: #fff;
	border-radius: 10px;
	padding: 35px;
	transform: scale(0.8);
	position: relative;
	z-index: 3;
	transition: all 0.3s;
}

@media screen and (max-width: 768px) {
	.profile-card-form {
		max-width: 90%;
		height: auto;
	}
}

@media screen and (max-width: 576px) {
	.profile-card-form {
		padding: 20px;
	}
}

.profile-card-form__bottom {
	justify-content: space-between;
	display: flex;
	margin-left: -25px;
}

@media screen and (max-width: 576px) {
	.profile-card-form__bottom {
		flex-wrap: wrap;
	}
}


.profile-card__overlay {
	width: 100%;
	height: 100%;
	position: absolute;
	top: 0;
	left: 0;
	pointer-events: none;
	opacity: 0;
	background: rgba(22, 33, 72, 0.35);
	border-radius: 12px;
	transition: all 0.3s;
}

</style>