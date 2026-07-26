%global source0_hash 930521d4327997c5651506e616a9c7a6b2168dee7eca8cdd05a18f289a0518b3

Name:           perl-Net-ASN
Version:        1.08
Release:        4%{?dist}
Summary:        Perl extension for manipulating autonomous system numbers
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Net-ASN
Source0:        https://cpan.metacpan.org/authors/id/D/DF/DFREEDMAN/Net-ASN-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(Test::More)
Requires:       perl(Exporter)

%description
Net::ASN provides functions for parsing autonomous system numbers (ASNs) as
defined in RFC 1771 and extended by RFC 4893, also converting between
formats discussed in RFC 5396.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n Net-ASN-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I .
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
make test

%files
%doc Changes examples README
%dir %{perl_vendorlib}/Net
%{perl_vendorlib}/Net/ASN.pm
%{_mandir}/man3/Net::ASN.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
