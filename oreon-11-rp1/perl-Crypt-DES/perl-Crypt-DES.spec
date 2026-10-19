%global source0_hash 149cdc0a14e944b4cc5eefb7560c78d8cb25254f9f9774547c880355a7e9f40c
%bcond_without  perl_Crypt_DES_enables_optional_test
Name:           perl-Crypt-DES
Version:        2.09
Release:        1%{?dist}
Summary:        Perl DES encryption module
License:        BSD-Systemics
URL:            https://metacpan.org/release/Crypt-DES
Source0:        https://cpan.metacpan.org/authors/id/T/TI/TIMLEGGE/Crypt-DES-%{version}.tar.gz
Patch0:         perl-Crypt-DES-init-braces.patch
Patch99:        perl-Crypt-DES-fedora-c99.patch
%if %{with perl_Crypt_DES_enables_optional_test}
%endif
%{?perl_default_filter}
Provides:       perl(Crypt::DES)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(Benchmark)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Crypt::CBC)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
DES encryption module. The module implements the Crypt::CBC interface.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
