%global source0_hash 0b5846f1f6ea1da7a6806d46aa06e3913d25a10ae52e87ba68ce3738267c557d

Name:           perl-URI-db
Version:        0.23
Release:        4%{?dist}
Summary:        Perl support for database URIs
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/URI-db/
Source0:        https://cpan.metacpan.org/authors/id/D/DW/DWHEELER/URI-db-%{version}.tar.gz

BuildArch:      noarch
# build deps
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(warnings)
# run deps
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(URI::Nested) >= 0.10
# test deps
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(URI) >= 1.40
BuildRequires:  perl(URI::QueryParam)
BuildRequires:  perl(utf8)

%{?perl_default_filter}

%description
This class provides support for database URIs. They're inspired by
JDBC URIs and PostgreSQL URIs, though they're a bit more formal.
The specification for their format is documented in README.md.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n URI-db-%{version}

%build
/usr/bin/perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README README.md
%{perl_vendorlib}/URI*
%{_mandir}/man3/URI*

%changelog
%autochangelog
