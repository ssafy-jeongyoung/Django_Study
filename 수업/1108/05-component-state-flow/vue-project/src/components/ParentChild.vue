<template>
    <div>
        <p>{{ myMsg }}</p>
        <p>{{ dynamicProps }}</p>
        
        <ParentGrandChild :my-msg="danger" 
        @update-name="updateName" 
        />
        <button @click="$emit('someEvent')">클릭</button>
        <button @click="buttonClick">클릭</button>
        <button @click="emitArgs">추가 인자</button>
    </div>
</template>

<script setup>
import ParentGrandChild from '@/components/ParentGrandChild.vue'

    // defineProps(['myMsg'])

// defineProps({
//     myMsg: String,
//     // myMsg: {
//     //     type: String,
//     //     required: true,
//     // }
// })

// const props = defineProps({
//     myMsg: String,
//     dynamicProps: String,
// })
// console.log(props)
// console.log(props.myMsg)

// 다양한 객체 선언 방식
defineProps({
    myMsg: {
        type: String,
        required: true,
        // validator(value) {
        //     return ['success', 'warning', 'danger'].includes(value)
        // }
        validator(value) {
            const validValues = ['success', 'warning', 'danger']
            if (validValues.includes(value)) {
                console.error('에러 남')
                return false
            }
            return true
        }
    }
})

// emit 선언 방식
const emit = defineEmits(['someEvent', 'emitArgs', 'updateName'])
const buttonClick = function () {
    emit('someEvent')
}
const emitArgs= function() {
    emit('emitArgs', 1, 2, 3)
}

// 3. ParentGrandChild의 이벤트 발생 들음(위의 emit에 추가 후 함수 작성)
const updateName = function() {
    emit('updateName')
}

</script>

<style scoped>

</style>