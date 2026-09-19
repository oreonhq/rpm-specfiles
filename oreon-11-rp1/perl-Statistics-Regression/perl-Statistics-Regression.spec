%global source0_hash 2cc53e3996dda4dceb5d7a794ba15107adb7a6614e19b485c0b8e47a5ab8b69a

%bcond check 1

Name:           perl-Statistics-Regression
Version:        0.53
Release:        %autorelease
Summary:        Weighted linear regression package (line+plane fitting)
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Statistics-Regression
Source0:        https://cpan.metacpan.org/authors/id/I/IA/IAWELCH/Statistics-Regression-%{version}.tar.gz
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(inc::Module::Install)
%if %{with check}
BuildRequires:  perl(Test::Pod)
%endif
BuildArch:      noarch

%description
Regression.pm is a multivariate linear regression package. That is, it
estimates the c coefficients for a line-fit of the type

y= c(0)*x(0) + c(1)*x1 + c(2)*x2 + ... + c(k)*xk

given a data set of N observations, each with k independent x variables
and one y variable. Naturally, N must be greater than k---and preferably
considerably greater. Any reasonable undergraduate statistics book will
explain what a regression is. Most of the time, the user will provide a
constant ('1') as x(0) for each observation in order to allow the
regression package to fit an intercept.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n Statistics-Regression-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" \
  NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build

%install
%make_install
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} '%{buildroot}'/*

%if %{with check}
%check
make test
%endif

%files
%doc README
%dir %{perl_vendorlib}/Statistics
%{perl_vendorlib}/Statistics/Regression.pm
%{_mandir}/man3/Statistics::Regression.3pm.*

%changelog
%autochangelog
