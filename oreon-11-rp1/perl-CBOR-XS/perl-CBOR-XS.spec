%global source0_hash eac15e730aaf612edd9edf71e6aa954653611bae5a1043b960aff5a9b1e571ff

Name:           perl-CBOR-XS
Version:        1.87
Release:        9%{?dist}
Summary:        Concise Binary Object Representation (CBOR)
# COPYING:      GPL-3.0 text
## Replaced by system header-only package
# ecb.h:        BSD-2-Clause OR GPL-2.0-or-later
License:        GPL-1.0-or-later AND (BSD-2-Clause OR GPL-2.0-or-later)
URL:            https://metacpan.org/release/CBOR-XS
Source0:        https://cpan.metacpan.org/authors/id/M/ML/MLEHMANN/CBOR-XS-%{version}.tar.gz
# Use system libecb
Patch0:         CBOR-XS-1.6-Include-ecb.h-from-system.patch
# Silent compiler warnings
Patch1:         CBOR-XS-1.84-Cast-char-and-U8-where-needed.patch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  libecb-static
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Canary::Stability)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(common::sense)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Math::BigFloat)
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(Math::BigRat)
BuildRequires:  perl(Time::Piece)
BuildRequires:  perl(Types::Serialiser)
BuildRequires:  perl(URI)
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Math::BigInt::FastCalc)
BuildRequires:  perl(Scalar::Util)
Requires:       perl(Math::BigFloat)
Requires:       perl(Math::BigInt)
Requires:       perl(Math::BigRat)
Requires:       perl(Time::Piece)
Requires:       perl(URI)

Provides:       perl(CBOR::XS)
Provides:       perl(CBOR::XS)
%description
This module converts Perl data structures to the Concise Binary Object
Representation (CBOR) and vice versa. CBOR is a fast binary serialization
format that aims to use an (almost) superset of the JSON data model, i.e.
when you can represent something useful in JSON, you should be able to
represent it in CBOR.

%package tests
Summary:        Tests for %{name}
License:        GPL-1.0-or-later
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Math::BigInt::FastCalc)

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n CBOR-XS-%{version}
# Remove bundled libecb
rm ecb.h
perl -i -ne 'print $_ unless m{^ecb\.h}' MANIFEST
# Copy libecb license because the license requires it.
install -m 0644 %{_datadir}/licenses/libecb-devel/LICENSE libecb.LICENSE

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS" </dev/null
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
%license COPYING libecb.LICENSE
%doc Changes README
%dir %{perl_vendorarch}/auto/CBOR
%{perl_vendorarch}/auto/CBOR/XS
%dir %{perl_vendorarch}/CBOR
%{perl_vendorarch}/CBOR/XS.pm
%{_mandir}/man3/CBOR::XS.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
