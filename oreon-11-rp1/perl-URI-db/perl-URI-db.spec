%global source0_hash 0b5846f1f6ea1da7a6806d46aa06e3913d25a10ae52e87ba68ce3738267c557d
Name:           perl-URI-db
Version:        0.23
Release:        1%{?dist}
Summary:        Perl support for database URIs
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/URI-db/
Source0:        https://cpan.metacpan.org/authors/id/D/DW/DWHEELER/URI-db-%{version}.tar.gz
BuildArch:      noarch
%{?perl_default_filter}
# oreon:deps
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::Nested)
BuildRequires:  perl(URI::QueryParam)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
