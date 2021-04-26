# Simple linear regression 
> When our dependent variable  is  linear  and our feature of independent value is one we use simple linear regression
## Formula 
 - Least Square Method

       Y=M*X+C
        
        where as ,
             M   -Slope
             C   -Intercept
    
    
               Σ((X-X_mean)*(Y-Y_mean)) 
       M  =  _________________________ 
                  Σ(X-X_mean)^2 
             
             
       where as,
          X      -Independent variable 
          X_mean -Mean of Independent variable 
          Y      -Dependent variable 
          Y_mean -Mean of dependent variable 


        C=Y-M*X
     
     
  - Normal equation
         
         theta=(X*X.T)^-1*(X.T*Y)
         
         where as ,
              X  -Independent variable 
              Y  -Dependent variable 
## Library used
   - matplotlib -->
   - pandas
   - numpy
   - sklearn
      
