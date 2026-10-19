%global source0_hash a64482584ef3ba8f84aced78d696048b87e25ca7fb3c91a50df391157212c4bd
Name:           perl-Net-DNS-SEC
Version:        1.27
Release:        1%{?dist}
Summary:        DNSSEC modules for Perl
License:        HPND-MIT-disclaimer
URL:            https://metacpan.org/release/Net-DNS-SEC
Source0:        https://cpan.metacpan.org/authors/id/N/NL/NLNETLABS/Net-DNS-SEC-%{version}.tar.gz
Patch0:         Net-DNS-SEC-1.25-Skip-SHA-1-signature-tests-if-OpenSSL-errors.patch
Requires:       perl(Carp) >= 1.1
Requires:       perl(DynaLoader) >= 1.09
Requires:       perl(Exporter) >= 5.63
Requires:       perl(File::Spec) >= 3.29
Requires:       perl(IO::File) >= 1.14
Requires:       perl(MIME::Base64) >= 3.07
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Carp|DynaLoader|Exporter|File::Spec|IO::File|MIME::Base64|Test::Builder|Test::More)\\)$
%global __requires_exclude %{__requires_exclude}|^perl\\(TestToolkit\\)
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(NonFatal|TestToolkit\\)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Net::DNS)
BuildRequires:  perl(Net::DNS::ZoneFile)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(integer)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  pkgconf-pkg-config
BuildRequires:  pkgconfig(libcrypto)
# /oreon:deps
%description
Net::DNS::SEC is installed as an extension to an existing Net::DNS
installation providing packages to support DNSSEC as specified in
RFC4033, RFC4034, RFC4035 and related documents.

It also provides support for SIG0 which is useful for dynamic updates.

It implements cryptographic signature generation and verification functions
using RSA, DSA, ECDSA, and Edwards curve algorithms.

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       coreutils
Requires:       perl-Test-Harness
Requires:       perl(Carp) >= 1.1
Requires:       perl(Exporter) >= 5.63
Requires:       perl(IO::File) >= 1.14
Requires:       perl(Test::Builder) >= 0.80
Requires:       perl(Test::More) >= 0.8
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n Net-DNS-SEC-%{version}
chmod a+x t/*.t

%build

unset OPENSSL_INCLUDE OPENSSL_LIB OPENSSL_PREFIX
export NETDNSSEC_ENABLE_DSA_SIGNATURES=1
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}%{_libexecdir}/%{name}/t/00-install.t
rm %{buildroot}%{_libexecdir}/%{name}/t/00-pod.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
set -e
DIR=$(mktemp -d)
cp -a %{_libexecdir}/%{name}/* "$DIR"
pushd "$DIR"
prove -I t -j 1
popd
rm -r "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Net-DNS-SEC-tests -f %{oreon_filedir}/perl-Net-DNS-SEC-tests.list

%changelog

%autochangelog
