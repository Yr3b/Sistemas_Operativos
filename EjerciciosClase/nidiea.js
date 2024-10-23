function solution(l,fares){
    carType = ["UberX","UberXL","UberPlus","UberBlack","UberSUV"]
    return carType[fares.findIndex(fare=>fare*l>20)-1]
}

console.log(solution(30,[0.3,0.5,0.7,1,1.3]))