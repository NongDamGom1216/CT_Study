class Solution {
    fun solution(s: String): String {
        var answer = ""
        
        val all_length = s.length
        val answer_length = all_length / 2
        if(all_length % 2 == 0){
            answer = s[answer_length-1].toString() + s[answer_length].toString()
            
        } else {
            
            answer = s[answer_length].toString()
            
        }
        
        return answer
    }
}