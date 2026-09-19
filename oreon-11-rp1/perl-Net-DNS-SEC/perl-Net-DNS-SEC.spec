%global source0_hash a64482584ef3ba8f84aced78d696048b87e25ca7fb3c91a50df391157212c4bd

Name:           perl-Net-DNS-SEC
Version:        1.27
Release:        1%{?dist}
Summary:        DNSSEC modules for Perl
License:        HPND-MIT-disclaimer
URL:            https://metacpan.org/release/Net-DNS-SEC
Source0:        https://cpan.metacpan.org/authors/id/N/NL/NLNETLABS/Net-DNS-SEC-%{version}.tar.gz
# Adapt tests to a crypto policy without SHA-1, proposed to the upstream,
# bug #2299447, CPAN RT#154526
Patch0:         Net-DNS-SEC-1.25-Skip-SHA-1-signature-tests-if-OpenSSL-errors.patch
# Build
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.9
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  pkgconf-pkg-config
BuildRequires:  pkgconfig(libcrypto)
# Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(Carp) >= 1.1
BuildRequires:  perl(DynaLoader) >= 1.09
BuildRequires:  perl(Exporter) >= 5.63
BuildRequires:  perl(File::Spec) >= 3.29
BuildRequires:  perl(integer)
BuildRequires:  perl(IO::File) >= 1.14
BuildRequires:  perl(MIME::Base64) >= 3.07
BuildRequires:  perl(Net::DNS) >= 1.08
BuildRequires:  perl(Net::DNS::ZoneFile)
# Tests only
BuildRequires:  perl(File::Find) >= 1.13
BuildRequires:  perl(Test::Builder) >= 0.80
BuildRequires:  perl(Test::More) >= 0.8
# Optional tests:
BuildRequires:  perl(Test::Pod) => 1.45
Requires:       perl(Carp) >= 1.1
Requires:       perl(DynaLoader) >= 1.09
Requires:       perl(Exporter) >= 5.63
Requires:       perl(File::Spec) >= 3.29
Requires:       perl(IO::File) >= 1.14
Requires:       perl(MIME::Base64) >= 3.07

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Carp|DynaLoader|Exporter|File::Spec|IO::File|MIME::Base64|Test::Builder|Test::More)\\)$
# Remove private modules
%global __requires_exclude %{__requires_exclude}|^perl\\(TestToolkit\\)
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(NonFatal|TestToolkit\\)

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
# Until OpenSSL disables DSA at built-time, we need to keep it enabled here
# because users can modify a default crypto policy at run-time.
export NETDNSSEC_ENABLE_DSA_SIGNATURES=1
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
# Remove tests useless out of build tree
rm %{buildroot}%{_libexecdir}/%{name}/t/00-install.t
rm %{buildroot}%{_libexecdir}/%{name}/t/00-pod.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/usr/bin/bash
set -e
# Tests write into CWD.
DIR=$(mktemp -d)
cp -a %{_libexecdir}/%{name}/* "$DIR"
pushd "$DIR"
prove -I t -j 1
popd
rm -r "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
# Makefile.PL resets HARNESS_OPTIONS to enforce serial testing. Probably
# because of writing to files. But they do not clash. At least now.
make test

%files
%license LICENSE
%doc Changes demo README WARNING
%dir %{perl_vendorarch}/Net
%dir %{perl_vendorarch}/Net/DNS
%{perl_vendorarch}/Net/DNS/SEC
%{perl_vendorarch}/Net/DNS/SEC.pm
%dir %{perl_vendorarch}/auto/Net
%dir %{perl_vendorarch}/auto/Net/DNS
%{perl_vendorarch}/auto/Net/DNS/SEC
%{_mandir}/man3/Net::DNS::SEC.*
%{_mandir}/man3/Net::DNS::SEC::*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
