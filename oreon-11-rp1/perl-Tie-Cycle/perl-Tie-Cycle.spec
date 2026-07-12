%global source0_hash 043d0bef0afba404eaff236a400a17265cbb609aa2112743212e1f9ee29039f1

Name:           perl-Tie-Cycle
Version:        1.233
Release:        %autorelease
Summary:        Cycle through a list of values via a scalar
License:        Artistic-2.0
URL:            https://metacpan.org/release/Tie-Cycle
Source0:        https://cpan.metacpan.org/authors/id/B/BR/BRIANDFOY/Tie-Cycle-1.233.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
# Tests
BuildRequires:  perl(Test::More) >= 1.00
# Optional tests
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage)

Provides:       perl(Tie::Cycle)
%description
This Perl module can be used to go through a list over and over again.
Once you get to the end of the list, you go back to the beginning.  You
do not have to worry about any of this since the magic of tie does that
for you.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Tie-Cycle-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes README.pod CONTRIBUTING.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
