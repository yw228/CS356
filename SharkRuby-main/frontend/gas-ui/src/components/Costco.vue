<script>
import { update } from 'idb-keyval';
import Price from './Price.vue'
export default {
    data() {
        return {
            star: false
        };
    },
    props: ["costco"],
    components: { Price },
    methods: {
        starred() {
            update('stars', (stars) => {
                if (stars.includes(this.costco.id)) {
                    const removal = stars.findIndex(element => element === this.costco.id)
                    this.star = false
                    stars.splice(removal, 1)
                }
                else {
                    this.star = true
                    stars.push(this.costco.id)
                }
                return stars
            })
        }
    },
    created() {
        update('stars', (stars) => {
            if (Array.isArray(stars)) {
                if (stars.includes(this.costco.id))
                {
                    this.star = true
                }
                return stars
            }
            else {
                return []
            }
        })
    }
}
</script>


<template>
    <div class="costco">
        <div class="header">
            <div class="local">
                <div class="name">{{costco.name}}</div>
                <div class="location">
                    <img class="pin" src="@/assets/gps.svg" />
                    <div class="address">{{costco.address}}<br>{{costco.city}}, {{costco.state}} {{costco.zip}}</div>
                </div>
            </div>
            <button class="star" :class="{starred: star}" @click="this.starred()">
                <img class="empty" src="@/assets/star.svg" />
                <img class="filled" src="@/assets/star-filled.svg" />
            </button>
        </div>
        <div class="prices" v-if="costco.gas.available">
            <Price v-if="costco.gas.regular" :price="costco.gas.regular" :type="'regular'"></Price>
            <Price v-if="costco.gas.premium" :price="costco.gas.premium" :type="'premium'"></Price>
            <Price v-if="costco.gas.diesel" :price="costco.gas.diesel" :type="'diesel'"></Price>
        </div>
    </div>
</template>


<style scoped>

    .header {
        display: grid;
        grid-template-columns: 1fr auto;
        align-items: center;
    }

    button {
        width: 40px;
        height: 40px;
        display: grid;
        align-content: center;
        align-items: center;
        background-color: white;
        border: 2px solid white;
        cursor: pointer;
        border-radius: 10px;
        transition: background-color 0.5s;
    }

    button.star > img {
        transition: opacity 0.5s;
        grid-column: 1;
        grid-row: 1;
    }

    button.star > img.filled {
        /* display: none; */
        opacity: 0;
    }

    button.star.starred > img.filled {
        /* display: block; */
        opacity: 1;
    }

    button.star > img.empty {
        /* display: block; */
        opacity: 1;
    }

    button.star.starred > img.empty {
        /* display: none; */
        opacity: 0;
    }

    .name {
        font-family: 'Fugaz One', cursive;
        font-size: 20px;
        margin-bottom: -2.5px;
        text-transform: uppercase;
    }
    .location{
        display: grid;
        grid-template-columns: auto 1fr;
        align-items: center;
        justify-items: start;
        align-content: center;
        justify-content: start;
        gap: 2px;
    }

    .pin{
        height: 20px;
    }

    .address{
        font-family: 'Secular One', sans-serif;
        line-height: 14px;
        font-size: 12px;
    }

    .prices{
        display: flex;
        flex-direction: row;
        flex-wrap: nowrap;
        align-content: center;
        justify-content: space-around;
        align-items: center;
        padding: 5px 0;
        gap: 5px;
    }
</style>