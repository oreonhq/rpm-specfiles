%global source0_hash e1971339a65fbac63ab87142d4b59d3d259d51417753c77cb58ea31a8233efaf

Name:           perl-URI-Nested
Version:        0.10
Release:        21%{?dist}
Summary:        Perl support for nested URIs
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/URI-Nested/
Source0:        http://www.cpan.org/authors/id/D/DW/DWHEELER/URI-Nested-%{version}.tar.gz

BuildArch:      noarch
# build deps
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(warnings)
# run deps
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
# test deps
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(URI) >= 1.40
BuildRequires:  perl(URI::QueryParam)
BuildRequires:  perl(base)
BuildRequires:  perl(utf8)

%description
This class provides support for nested URIs, where the scheme is a
prefix, and the remainder of the URI is another URI. Examples include
JDBC URIs and database URIs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n URI-Nested-%{version}

%build
%{__perl} Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README.md
%{perl_vendorlib}/URI*
%{_mandir}/man3/URI*

%changelog
%autochangelog
