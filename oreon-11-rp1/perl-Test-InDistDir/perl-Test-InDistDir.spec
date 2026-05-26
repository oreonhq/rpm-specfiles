Name:           perl-Test-InDistDir
Version:        1.112071
Release:        28%{?dist}
Summary:        Test environment setup for development with IDE
License:        WTFPL
URL:            https://metacpan.org/release/Test-InDistDir
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MITHALDU/Test-InDistDir-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 922c5c63314f406f4cbb35ec423ac2154d2c2b71a65addb7732c9d240a83fefb
%global source0_file Test-InDistDir-1.112071.tar.gz
# oreon url source checksums end
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.30
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(lib)
# Tests:
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test::More)

%description
This Perl module helps to run test scripts in integrated development
environments (IDE).

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Test-InDistDir-1.112071.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "922c5c63314f406f4cbb35ec423ac2154d2c2b71a65addb7732c9d240a83fefb" || { echo "oreon: Source0 SHA256 mismatch for Test-InDistDir-1.112071.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n Test-InDistDir-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README.mkdn
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.112071-28
- Prepare for Oreon 11 (RP1)
