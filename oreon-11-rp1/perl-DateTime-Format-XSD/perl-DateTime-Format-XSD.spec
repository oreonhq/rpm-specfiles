%global source0_hash 97225bd42b90203c7b4980145e797e25624f312a72ae2f3c75692e6acdd99432

Name:           perl-DateTime-Format-XSD
Version:        0.4
Release:        15%{?dist}
Summary:        Format DateTime according to xsd:dateTime
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/DateTime-Format-XSD
Source0:        https://cpan.metacpan.org/modules/by-module/DateTime/DateTime-Format-XSD-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(DateTime::Format::ISO8601)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(Test::More)
# Dependencies
# (none)

%description
XML Schema defines a usage profile that is a subset of the ISO8601
profile. This profile defines that
  'YYYY-MM-DD"T"HH:MI:SS(Z|[+-]zh:zm)' 
is the only possible representation for a dateTime, despite all other
options ISO provides.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n DateTime-Format-XSD-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/DateTime/
%{_mandir}/man3/DateTime::Format::XSD.3*

%changelog
%autochangelog
