%for = 0.01
p = 0.01;
Expected_Bn = zeros (1, 1000000000);  
Expected_Cn = zeros (1, 1000000000);  
Expected_Bn(2) = 1+3*p - p.^2;
denom_Expected_Cn = 1- (1-p).^ 2;
Expected_Cn(2) = (3*p - p.^2)/ (1- (1-p).^2);
n_div_Expected_Bn(2) = 2/ Expected_Bn(2);

n= 4;
while n < 1000000000
    probfirstpos = (1 - (1-p).^(n/2)) / (1- (1-p).^n);
    Expected_Cn(n) = 1+ probfirstpos * (Expected_Bn(n/2)) + Expected_Cn (n/2);
    Expected_Bn(n) = (1- (1-p).^n )* ( 1+ Expected_Cn(n)) + (1-p).^n;
    n_div_Expected_Bn(n) = n/ Expected_Bn(n) ;
    n=n*2;
end

[mValue , vIndex] = max(n_div_Expected_Bn);
no_of_optimal_groups_of_size64 = floor(10000/64);
disp(no_of_optimal_groups_of_size64 * Expected_Bn(64) + Expected_Bn(10000 - no_of_optimal_groups_of_size64* 64))


%for p = 0.04
p = 0.04;
Expected_Bn = zeros (1, 1000000000);  
Expected_Cn = zeros (1, 1000000000);  
Expected_Bn(2) = 1+3*p - p.^2;
denom_Expected_Cn = 1- (1-p).^ 2;
Expected_Cn(2) = (3*p - p.^2)/ (1- (1-p).^2);
n_div_Expected_Bn(2) = 2/ Expected_Bn(2);

n= 4;
while n < 1000000000
    probfirstpos = (1 - (1-p).^(n/2)) / (1- (1-p).^n);
    Expected_Cn(n) = 1+ probfirstpos * (Expected_Bn(n/2)) + Expected_Cn (n/2);
    Expected_Bn(n) = (1- (1-p).^n )* ( 1+ Expected_Cn(n)) + (1-p).^n;
    n_div_Expected_Bn(n) = n/ Expected_Bn(n) ;
    n=n*2;
end

[mValue , vIndex] = max(n_div_Expected_Bn);
no_of_optimal_groups_of_size16 = floor(10000/16);
disp(no_of_optimal_groups_of_size16 * Expected_Bn(16))

%for p = 0.07
p = 0.07;
Expected_Bn = zeros (1, 1000000000);  
Expected_Cn = zeros (1, 1000000000);  
Expected_Bn(2) = 1+3*p - p.^2;
denom_Expected_Cn = 1- (1-p).^ 2;
Expected_Cn(2) = (3*p - p.^2)/ (1- (1-p).^2);
n_div_Expected_Bn(2) = 2/ Expected_Bn(2);

n= 4;
while n < 1000000000
    probfirstpos = (1 - (1-p).^(n/2)) / (1- (1-p).^n);
    Expected_Cn(n) = 1+ probfirstpos * (Expected_Bn(n/2)) + Expected_Cn (n/2);
    Expected_Bn(n) = (1- (1-p).^n )* ( 1+ Expected_Cn(n)) + (1-p).^n;
    n_div_Expected_Bn(n) = n/ Expected_Bn(n) ;
    n=n*2;
end

[mValue , vIndex] = max(n_div_Expected_Bn);
no_of_optimal_groups_of_size8 = floor(10000/8);
disp(no_of_optimal_groups_of_size8 * Expected_Bn(8))


%for = 0.1
p = 0.1;
Expected_Bn = zeros (1, 1000000000);  
Expected_Cn = zeros (1, 1000000000);  
Expected_Bn(2) = 1+3*p - p.^2;
denom_Expected_Cn = 1- (1-p).^ 2;
Expected_Cn(2) = (3*p - p.^2)/ (1- (1-p).^2);
n_div_Expected_Bn(2) = 2/ Expected_Bn(2);

n= 4;
while n < 1000000000
    probfirstpos = (1 - (1-p).^(n/2)) / (1- (1-p).^n);
    Expected_Cn(n) = 1+ probfirstpos * (Expected_Bn(n/2)) + Expected_Cn (n/2);
    Expected_Bn(n) = (1- (1-p).^n )* ( 1+ Expected_Cn(n)) + (1-p).^n;
    n_div_Expected_Bn(n) = n/ Expected_Bn(n) ;
    n=n*2;
end

[mValue , vIndex] = max(n_div_Expected_Bn);
no_of_optimal_groups_of_size8 = floor(10000/8);
disp(no_of_optimal_groups_of_size8 * Expected_Bn(8))
