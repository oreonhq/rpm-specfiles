%global source0_hash 136d190c1620e2d3783c64c51339d69b841fa927acd9789f6cefbcf776e6a618

Name:           perl-Crypt-OpenSSL-EC
Version:        1.34
Release:        1%{?dist}
Summary:        Perl extension for OpenSSL EC (Elliptic Curves) library
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Crypt-OpenSSL-EC
Source0:        https://cpan.metacpan.org/authors/id/R/RA/RADIATOR/Crypt-OpenSSL-EC-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.5
BuildRequires:  perl(Config)
# Use ExtUtils::Constant to regenerate XS code
BuildRequires:  perl(ExtUtils::Constant)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# pkgconf-pkg-config for pkg-config tool
BuildRequires:  pkgconf-pkg-config
BuildRequires:  pkgconfig(libcrypto)
# Run-time:
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(Crypt::OpenSSL::Bignum) >= 0.04
BuildRequires:  perl(Crypt::OpenSSL::Bignum::CTX)
BuildRequires:  perl(Test::More)

%description
This package provides a Perl standard (non-object-oriented) interface to the
OpenSSL Elliptic Curve library. Some object-oriented calls are supported.

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Crypt::OpenSSL::Bignum) >= 0.04

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n Crypt-OpenSSL-EC-%{version}

%build
unset OPENSSL_INCLUDE OPENSSL_LIB OPENSSL_PREFIX
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%doc Changes README.md
%dir %{perl_vendorarch}/auto/Crypt
%dir %{perl_vendorarch}/auto/Crypt/OpenSSL
%{perl_vendorarch}/auto/Crypt/OpenSSL/EC
%dir %{perl_vendorarch}/Crypt
%dir %{perl_vendorarch}/Crypt/OpenSSL
%{perl_vendorarch}/Crypt/OpenSSL/EC.pm
%{_mandir}/man3/Crypt::OpenSSL::EC.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
