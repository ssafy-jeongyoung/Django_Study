<template>
    <div>
        <ParentChild
        my-msg="message"
        :dynamicProps="name"
        @some-event="someCallback" 
        @emit-args="getNumbers" 
        @update-name="updateName"
        />
    </div>
</template>

<script setup>
    import ParentChild from '@/components/ParentChild.vue';
    import { ref } from 'vue'

    const name = ref('Alice')
    const someCallback = function() {
        console.log('emit 이벤트 수신 완료')
    }
    const getNumbers = function(...args) {
        console.log(args)
    }

    // 4. 
    const updateName= function() {
        name.value = 'Bella'
    }
</script>

<style scoped>

</style>