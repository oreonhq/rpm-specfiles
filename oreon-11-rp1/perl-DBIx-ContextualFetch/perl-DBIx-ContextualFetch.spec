%global source0_hash 85e2f805bfc81cd738c294316b27a515397036f397a0ff1c6c8d754c38530306

Name:           perl-DBIx-ContextualFetch
Version:        1.03
Release:        55%{?dist}
Summary:        Add contextual fetches to DBI
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/DBIx-ContextualFetch
Source0:        https://cpan.metacpan.org/modules/by-module/DBIx/DBIx-ContextualFetch-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Module
BuildRequires:  perl(base)
BuildRequires:  perl(DBI)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test::More)
# Optional Tests
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 1.00
# Dependencies

%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(DBI::(st|db)\\)

Provides:       perl(DBIx::ContextualFetch)
%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n DBIx-ContextualFetch-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc Changes
%{perl_vendorlib}/DBIx/
%{_mandir}/man3/DBIx::ContextualFetch.3*

%changelog
%autochangelog
