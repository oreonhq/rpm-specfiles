%global source0_hash 1f7e7327aeccf01c503f895749507c3296521437115dc26e47e3a07ee6ccae5f

# Enable JSON support
%bcond_without perl_CryptX_enables_json
# Run optional test
%bcond_without perl_CryptX_enables_optional_test

Name:           perl-CryptX
Version:        0.090
Release:        1%{?dist}
Summary:        Cryptographic toolkit
# src/ltc/*:    Unlicense
# src/ltm/*:    Unlicense
# Other files:  GPL-1.0-or-later OR Artistic-1.0-Perl
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND Unlicense
URL:            https://metacpan.org/release/CryptX
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIK/CryptX-%{version}.tar.gz

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(XSLoader)
# Optional run-time:
%if %{with perl_CryptX_enables_json}
BuildRequires:  perl(JSON)
%endif
# Tests:
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
%if %{with perl_CryptX_enables_optional_test}
# Optional tests:
BuildRequires:  perl(File::Find)
BuildRequires:  perl(Math::BigFloat)
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(Math::Complex)
BuildRequires:  perl(Storable) >= 2.0
BuildRequires:  perl(Test::Pod)
%endif

Provides:       bundled(libtomcrypt) = 1.18.2-1.20260519gita68fa19b
Provides:       bundled(libtommath) = 1.2.0-1.20260420gitae40a87


# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Math::BigFloat|Math::BigInt|Storable)\\)$
# Remove private modules
%global __requires_exclude %{__requires_exclude}|^perl\\(\\.::

Provides:       perl(Crypt::Cipher::AES)
Provides:       perl(Crypt::PK::Ed25519)
Provides:       perl(CryptX)
%description
This Perl library provides a cryptography based on LibTomCrypt library.

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       coreutils
Requires:       perl-Test-Harness
%if %{with perl_CryptX_enables_json}
Requires:       perl(JSON)
%endif
%if %{with perl_CryptX_enables_optional_test}
Requires:       perl(File::Find)
Requires:       perl(Math::BigFloat)
Requires:       perl(Math::BigInt)
Requires:       perl(Math::Complex)
Requires:       perl(Storable) >= 2.0
%endif

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n CryptX-%{version}
# https://github.com/DCIT/perl-CryptX/issues/96
sed -i -e's/1\.999842/1.999840/g' t/mbi_ltm_since_1.999842.t
# Fix permissions
chmod -x t/data/openssl_rsa-x509.pem
# Remove unsed tests
%if !%{with perl_CryptX_enables_optional_test}
for F in t/002_all_pm.t t/003_all_pm_pod.t t/mbi_ltm_bigfltpm.t \
        t/mbi_ltm_bigintpm.t t/mbi_ltm_biglog.t t/mbi_ltm_bigroot.t \
        t/mbi_ltm/bigintpm.inc t/mbi_ltm/bigfltpm.inc t/mbi_ltm_storable.t; do
    rm "${F}"
    perl -i -ne 'print $_ unless m{\A\Q'"${F}"'\E}' MANIFEST
done
%endif
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done
# Handle license files for libtomcrypt and libtommath
cp -a src/ltc/LICENSE LICENSE.libtomcrypt
cp -a src/ltm/LICENSE LICENSE.libtommath

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}

%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name '*.bs' -empty -delete
%{_fixperms} $RPM_BUILD_ROOT/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
%if %{with perl_CryptX_enables_optional_test}
rm %{buildroot}%{_libexecdir}/%{name}/t/{002_all_pm,003_all_pm_pod}.t
%endif
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# t/crypt-misc.t writes into CWD
DIR=$(mktemp -d)
cp -a %{_libexecdir}/%{name}/t "$DIR"
pushd "$DIR"
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -r "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE LICENSE.libtomcrypt LICENSE.libtommath
%doc Changes README.md
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Crypt
%{perl_vendorarch}/CryptX.pm
%{perl_vendorarch}/Math
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
