%global source0_hash 97225bd42b90203c7b4980145e797e25624f312a72ae2f3c75692e6acdd99432
Name:           perl-DateTime-Format-XSD
Version:        0.4
Release:        1%{?dist}
Summary:        Format DateTime according to xsd:dateTime
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/DateTime-Format-XSD
Source0:        https://cpan.metacpan.org/authors/id/T/TI/TIMLEGGE/DateTime-Format-XSD-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(DateTime::Format::ISO8601)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
