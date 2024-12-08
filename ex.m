function main_gauss(n,a,b,er,nrit,x0)
    k = 0
    for i =1:n
        x(i) = x0(i)
    end
    err = 1
    while(er > err )
        err = 0
        for i=1:n
            s = b(i)
            for j=1:n
                s = s - a(i,j) * x(j)
            end
        s = s + a(i,j) * x(i) /a(i,i)
        err = err + (s-x(i))^2
        x(i) = s
        end
        k = k + 1
        err = sqrt(err)
    end
    disp(x,k)
end
function gauss_seidel(n,a,b,er,nrit,x):
    k = 0
