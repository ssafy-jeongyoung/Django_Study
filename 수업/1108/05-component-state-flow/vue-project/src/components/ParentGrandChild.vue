<template>
    <div>
        <p>{{ myMsg }}</p>
        <!-- 2. 이벤트 버튼 생성 -->
        <button @click="updateName">이름 변경!</button>
    </div>
</template>

<script setup>
defineProps({
    myMsg: String,
})

// 1. 이벤트 발생 시작 --------------------
const emit = defineEmits(['updateName'])

const updateName = function() {
    emit('updateName')
}
// ---------------------------------------
</script>

<style scoped>

</style>