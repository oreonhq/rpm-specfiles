%global source0_hash 2db1ebb5837b4cb20051c0ee5b733b4453e3137df0a92306034c867621edd7e7

# Perform optional tests
%if 0%{?rhel} > 8
%bcond_with  perl_Crypt_DES_enables_optional_test
%else
%bcond_without  perl_Crypt_DES_enables_optional_test
%endif

Name:           perl-Crypt-DES
Version:        2.07
Release:        43%{?dist}
Summary:        Perl DES encryption module
License:        BSD-Systemics
URL:            https://metacpan.org/release/Crypt-DES
Source0:        https://cpan.metacpan.org/modules/by-module/Crypt/Crypt-DES-%{version}.tar.gz

Patch0:         perl-Crypt-DES-init-braces.patch
Patch99:        perl-Crypt-DES-fedora-c99.patch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(Benchmark)
BuildRequires:  perl(Data::Dumper)
%if %{with perl_Crypt_DES_enables_optional_test}
# Optional tests:
BuildRequires:  perl(Crypt::CBC) > 1.22
%endif

%{?perl_default_filter}

%description
DES encryption module. The module implements the Crypt::CBC interface.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n Crypt-DES-%{version}

# Fix "warning: missing braces around initializer [-Wmissing-braces]"
%patch -P 0

# Fix C99 compatibility (CPAN RT#133363)
%patch -P 99 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="%{optflags}"
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license COPYRIGHT
%doc README
%{perl_vendorarch}/auto/Crypt/
%{perl_vendorarch}/Crypt/
%{_mandir}/man3/Crypt::DES.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.07-43
- Prepare for Oreon 11 (RP1)
