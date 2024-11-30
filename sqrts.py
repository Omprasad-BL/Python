class SQRT:
    def sqrt(cls,num):
        if num==0 or num==1:
            return num
        start=1
        end=num/2
        ans=0 
        while(start<=end):
            mid=int(start+(end-start)/2)
            square=mid*mid
            if square==num:
                return int(mid)
            if square<num:
                start=mid+1
                ans=mid
            else:
                end=mid-1
        return int(ans)            
        
if __name__ == "__main__":
    obj=SQRT()
    print(obj.sqrt(25))


