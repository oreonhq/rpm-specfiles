%global source0_hash e4575d787d44e49b3b59cc39eda2e461fe0606dd0e87d3a9c3df5011b133e702
Name:           perl-Crypt-OpenSSL-DSA
Version:        0.20
Release:        1%{?dist}
Summary:        Perl interface to OpenSSL for DSA
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Crypt-OpenSSL-DSA
Source0:        https://cpan.metacpan.org/authors/id/K/KM/KMX/Crypt-OpenSSL-DSA-%{version}.tar.gz
Patch0:         Crypt-OpenSSL-DSA-0.20-Make-tests-parallel-safe.patch
Patch1:         Crypt-OpenSSL-DSA-0.20-tests-Use-SHA-512-instead-of-SHA-1.patch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  openssl
BuildRequires:  perl(Config)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  pkgconf-pkg-config
BuildRequires:  pkgconfig(libcrypto)
# /oreon:deps
%description
Crypt::OpenSSL::DSA provides an access to Digital Signature Algorithm
implementation in OpenSSL library.

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       openssl
Requires:       perl-Test-Harness
Requires:       perl(Digest::SHA) >= 5.60
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir Crypt-OpenSSL-DSA-%{version}
%oreon_prep
%build

unset OPENSSL_LIB OPENSSL_PREFIX
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Crypt-OpenSSL-DSA-tests -f %{oreon_filedir}/perl-Crypt-OpenSSL-DSA-tests.list

%changelog

%autochangelog
