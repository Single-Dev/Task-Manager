<template>
  <div class="sidebar" :class="isOpened ? 'open' : ''" :style="cssVars">
    <div class="logo-details" style="margin: 6px 14px 0 14px">
      <i class='bx icon bx-task'></i>
      <div class="logo_name">
        Task Manager
      </div>
      <i class="bx" :class="isOpened ? 'bx-menu-alt-right' : 'bx-menu'" id="btn" @click="isOpened = !isOpened" />
    </div>

    <div class="side_bar_div">
      <div id="my-scroll" style="margin: 6px 14px 0 14px">
        <ul class="nav-list" style="overflow: visible">
          <li id="links_search" v-if="isSearch" @click="isOpened = true">
            <i class="bx bx-search"/>
            <input
            type="text"
            placeholder="Search for user"
            min="3"
            @input="$emit('UpdateTerm', $event.target.value)"
            >
            <span data-target="links_search" class="tooltip">
              Search
            </span>
          </li>
          <div v-if="isLoggedIn == false">
            <li id="login">
              <router-link to="/login">
                <i class="bx bxs-log-in bx-square-rounded"></i>
                <span class="links_name">Login</span>
              </router-link>
              <span data-target="login" class="tooltip">
                Login
              </span>
            </li>
            <li id="signup">
              <router-link to="/signup">
                <i class="bx bx-user-plus bx-square-rounded"></i>
                <span class="links_name">Signup</span>
              </router-link>
              <span data-target="signup" class="tooltip">
                Signup
              </span>
            </li>
          </div>
          <div v-else>
            <li id="profile">
              <router-link :to="'/@' + username">
                <i class="bx bx-user bx-square-rounded"></i>
                <span class="links_name">Profile</span>
              </router-link>
              <span data-target="profile" class="tooltip">
                Profile
              </span>
            </li>
            <li v-for="(menuItem, index) in menuItems" :id="index">
              <router-link :to="menuItem.link">
                <i class="bx" :class="menuItem.icon || 'bx-square-rounded'" />
                <span class="links_name">{{ menuItem.name }}</span>
              </router-link>

              <span :data-target="index" class="tooltip">{{
                menuItem.tooltip || menuItem.name
              }}</span>
            </li>
          </div>
        </ul>
      </div>

      <div v-if="isLoggedIn" class="profile align-items-center">
        <router-link :to="'/@' + username" class="profile-details">
          <i class="bx bxs-user-rectangle" />
          <div class="name_job">
            <div class="name">
              @{{ username }}
            </div>
          </div>
        </router-link>

        <i class="bx bx-log-out mt-2" id="log_out" @click="$emit('onExit')" />
      </div>
    </div>
  </div>

</template>
  
<script>
export default {
  name: 'SidebarMenu',
  props: {
    //! Search
    isSearch: {
      type: Boolean,
      default: true,
    },
    searchTooltip: {
      type: String,
      default: 'Search',
    },
    isLoggedIn: {
      type: Boolean,
      required: true
    },
    username: {
      type: String,
      required: true
    },
    term:{
      type: String,
      required: true
     }
  },
  data() {
    return {
      isOpened: false,
      // term:'',
      menuItems: [
        {
          link: "/",
          name: "Home",
          tooltip: "Home",
          icon: "bx-home-alt"
        },
        {
          link: "/shared-tasks",
          name: "Shared Tasks",
          tooltip: "Shared Tasks",
          icon: "bx-share-alt"
        }
      ]
    }
  },
  computed: {
    cssVars() {
      return {
        '--bg-color': '#11101d',
        '--secondary-color': '#1d1b31',
        '--home-section-color': '#e4e9f7',
        '--logo-title-color': '#fff',
        '--icons-color': '#fff',
        '--items-tooltip-color': '#e4e9f7',
        '--serach-input-text-color': '#fff',
        '--menu-items-hover-color': '#fff',
        '--menu-items-text-color': '#fff',
        '--menu-footer-text-color': '#fff',
      }
    },
  },
  watch: {
    isOpened(val) {
      window.document.body.style.paddingLeft =
        this.isOpened && true
          ? '250px'
          : '78px'
    },
  },
  methods: {
    tooltipAttached() {
      const tooltips = document.querySelectorAll('.tooltip')
      tooltips.forEach(tooltip => {
        document.body.appendChild(tooltip)
      })
      document.querySelectorAll('.tooltip').forEach(tooltip => {
        const targetID = tooltip.dataset.target
        const target = document.querySelector(`#${targetID}`)
        if (!target) return
        target.addEventListener('mouseenter', () => {
          const targetPosition = target.getBoundingClientRect()
          if (this.isOpened) return
          tooltip.style.top = `${targetPosition.top + window.scrollY}px`
          tooltip.style.left = `${targetPosition.left + targetPosition.width + 20
            }px`
          tooltip.classList.add('active')
        })
        target.addEventListener('mouseleave', () => {
          tooltip.classList.remove('active')
        })
      })
    },
  },
}
</script>
  
<style scoped>
/* Google Font Link */
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@200;300;400;500;600;700&display=swap');
@import url('https://unpkg.com/boxicons@2.0.7/css/boxicons.min.css');

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: 'Poppins', sans-serif;
}

body {
  transition: all 0.5s ease;
}

#log_out {
  cursor: pointer;
}

.name_job {
  margin-bottom: 5px;
}

.menu-logo {
  width: 30px;
  margin: 0 10px 0 10px;
}

.sidebar {
  position: relative;
  display: flex;
  flex-direction: column;
  position: fixed;
  left: 0;
  top: 0;
  height: 100%;
  min-height: min-content;
  /* overflow-y: auto; */
  width: 78px;
  background: var(--bg-color);
  /* padding: 6px 14px 0 14px; */
  z-index: 99;
  transition: all 0.5s ease;
}

.side_bar_div{
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  flex-grow: 1;
  max-height: calc(100% - 60px);
}

.sidebar.open {
  width: 250px;
}

.sidebar .logo-details {
  height: 60px;
  display: flex;
  align-items: center;
  position: relative;
}

.sidebar .logo-details .icon {
  opacity: 0;
  transition: all 0.5s ease;
}

.sidebar .logo-details .logo_name {
  color: var(--logo-title-color);
  font-size: 20px;
  font-weight: 600;
  opacity: 0;
  transition: all 0.5s ease;
}

.sidebar.open .logo-details .icon,
.sidebar.open .logo-details .logo_name {
  opacity: 1;
}

.sidebar .logo-details #btn {
  position: absolute;
  top: 50%;
  right: 0;
  transform: translateY(-50%);
  font-size: 22px;
  transition: all 0.4s ease;
  font-size: 23px;
  text-align: center;
  cursor: pointer;
  transition: all 0.5s ease;
}

.sidebar.open .logo-details #btn {
  text-align: right;
}

.sidebar i {
  color: var(--icons-color);
  height: 60px;
  min-width: 50px;
  font-size: 28px;
  text-align: center;
  line-height: 60px;
}

.sidebar .nav-list {
  margin-top: 20px;
  /* margin-bottom: 60px; */
  /* height: 100%; */
  /* min-height: min-content; */
}

.sidebar li {
  position: relative;
  margin: 8px 0;
  list-style: none;
}

.tooltip {
  position: absolute;
  /* top: -20px; */
  /* left: calc(100% + 15px); */
  z-index: 3;
  background: var(--items-tooltip-color);
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.3);
  padding: 6px 12px;
  border-radius: 4px;
  font-size: 15px;
  font-weight: 400;
  opacity: 0;
  white-space: nowrap;
  pointer-events: none;
  transition: 0s;
}

.tooltip.active {
  opacity: 1;
  pointer-events: auto;
  transition: all 0.4s ease;
  /* top: 50%; */
  transform: translateY(25%);
}

.sidebar.open li .tooltip {
  display: none;
}

.sidebar input {
  font-size: 15px;
  color: var(--serach-input-text-color);
  font-weight: 400;
  outline: none;
  height: 50px;
  width: 100%;
  width: 50px;
  border: none;
  border-radius: 12px;
  transition: all 0.5s ease;
  background: var(--secondary-color);
}

.sidebar.open input {
  padding: 0 20px 0 50px;
  width: 100%;
}

.sidebar .bx-search {
  position: absolute;
  top: 50%;
  left: 0;
  transform: translateY(-50%);
  font-size: 22px;
  background: var(--secondary-color);
  color: var(--icons-color);
}

.sidebar.open .bx-search:hover {
  background: var(--secondary-color);
  color: var(--icons-color);
}

.sidebar .bx-search:hover {
  background: var(--menu-items-hover-color);
  color: var(--bg-color);
}

.sidebar li a {
  display: flex;
  height: 100%;
  width: 100%;
  border-radius: 12px;
  align-items: center;
  text-decoration: none;
  transition: all 0.4s ease;
  background: var(--bg-color);
}

.sidebar li a:hover {
  background: var(--menu-items-hover-color);
}

.sidebar li a .links_name {
  color: var(--menu-items-text-color);
  font-size: 15px;
  font-weight: 400;
  white-space: nowrap;
  opacity: 0;
  pointer-events: none;
  transition: 0.4s;
}

.sidebar.open li a .links_name {
  opacity: 1;
  pointer-events: auto;
}

.sidebar li a:hover .links_name,
.sidebar li a:hover i {
  transition: all 0.5s ease;
  color: var(--bg-color);
}

.sidebar li router-link {
  display: flex;
  height: 100%;
  width: 100%;
  border-radius: 12px;
  align-items: center;
  text-decoration: none;
  transition: all 0.4s ease;
  background: var(--bg-color);
}

.sidebar li router-link:hover {
  background: var(--menu-items-hover-color);
}

.sidebar li router-link .links_name {
  color: var(--menu-items-text-color);
  font-size: 15px;
  font-weight: 400;
  white-space: nowrap;
  opacity: 0;
  pointer-events: none;
  transition: 0.4s;
}

.sidebar.open li router-link .links_name {
  opacity: 1;
  pointer-events: auto;
}

.sidebar li router-link:hover .links_name,
.sidebar li router-link:hover i {
  transition: all 0.5s ease;
  color: var(--bg-color);
}

.sidebar li i {
  height: 50px;
  line-height: 50px;
  font-size: 18px;
  border-radius: 12px;
}

.sidebar div.profile {
  position: relative;
  height: 60px;
  width: 78px;
  /* left: 0;
      bottom: 0; */
  padding: 10px 14px;
  background: var(--secondary-color);
  transition: all 0.5s ease;
  overflow: hidden;
}

.sidebar.open div.profile {
  width: 250px;
}

.sidebar div .profile-details {
  display: flex;
  align-items: center;
  flex-wrap: nowrap;
}

.sidebar div img {
  height: 45px;
  width: 45px;
  object-fit: cover;
  border-radius: 6px;
  margin-right: 10px;
}

.sidebar div.profile .name,
.sidebar div.profile .job {
  font-size: 15px;
  font-weight: 400;
  color: var(--menu-footer-text-color);
  white-space: nowrap;
}

.sidebar div.profile .job {
  font-size: 12px;
}

.sidebar .profile #log_out {
  position: absolute;
  top: 50%;
  right: 0;
  transform: translateY(-50%);
  background: var(--secondary-color);
  width: 100%;
  height: 60px;
  line-height: 60px;
  border-radius: 0px;
  transition: all 0.5s ease;
}

.sidebar.open .profile #log_out {
  width: 50px;
  background: var(--secondary-color);
  opacity: 0;
}

.sidebar.open .profile:hover #log_out {
  opacity: 1;
}

.sidebar.open .profile #log_out:hover {
  opacity: 1;
  color: red;
}

.sidebar .profile #log_out:hover {
  color: red;
}

.home-section {
  position: relative;
  background: var(--home-section-color);
  min-height: 100vh;
  top: 0;
  left: 78px;
  width: calc(100% - 78px);
  transition: all 0.5s ease;
  z-index: 2;
}

.sidebar.open~.home-section {
  left: 250px;
  width: calc(100% - 250px);
}

.home-section .text {
  display: inline-block;
  color: var(--bg-color);
  font-size: 25px;
  font-weight: 500;
  margin: 18px;
}

.my-scroll-active {
  overflow-y: auto;
}

#my-scroll {
  overflow-y: auto;
  height: calc(100% - 60px);
}

#my-scroll::-webkit-scrollbar {
  display: none;
  /* background-color: rgba(255, 255, 255, 0.2); 
      width: 10px;
      border-radius:5px  */
}

/* #my-scroll::-webkit-scrollbar-thumb{
      background-color: red;
      border-radius:5px 
    }
    #my-scroll::-webkit-scrollbar-button:vertical:start:decrement{
      display:none;
    }
    #my-scroll::-webkit-scrollbar-button:vertical:end:increment{
      display:none;
    } */
@media (max-width: 420px) {
  .sidebar li .tooltip {
    display: none;
  }
}
</style>
  