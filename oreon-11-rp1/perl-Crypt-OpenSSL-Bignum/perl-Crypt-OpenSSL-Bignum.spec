%global source0_hash 234e72fb8396d45527e6fd45e43759c5c3f3a208cf8f29e6a22161a996fd42dc
Name:           perl-Crypt-OpenSSL-Bignum
Version:        0.09
Release:        32%{?dist}
Summary:        Perl interface to OpenSSL's multiprecision integer arithmetic
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Crypt-OpenSSL-Bignum
Source0:        https://cpan.metacpan.org/authors/id/K/KM/KMX/Crypt-OpenSSL-Bignum-%{version}.tar.gz
Provides:       perl(Crypt::OpenSSL::Bignum)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  pkgconf-pkg-config
BuildRequires:  pkgconfig(libcrypto)
# /oreon:deps
%description
Crypt::OpenSSL::Bignum provides access to OpenSSL multiprecision integer
arithmetic libraries. Presently, many though not all of the arithmetic
operations that OpenSSL provides are exposed to perl. In addition, this
module can be used to provide access to bignum values produced by other
OpenSSL modules, such as key parameters from Crypt::OpenSSL::RSA.

%package tests  
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Crypt-OpenSSL-Bignum-%{version}
chmod a-x LICENSE README Changes

%build

unset OPENSSL_LIB OPENSSL_PREFIX
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a test.pl %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . test.pl
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Crypt-OpenSSL-Bignum-tests -f %{oreon_filedir}/perl-Crypt-OpenSSL-Bignum-tests.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.09-32
- Prepare for Oreon 11 (RP1)
