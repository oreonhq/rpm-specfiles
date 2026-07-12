%global source0_hash 8b481ceedbf0ae4a83effb80581550008bfdd3885ef01145e3733c7097c00a08

Name:           perl-Ima-DBI
Version:        0.35
Release:        51%{?dist}
Summary:        Database connection caching and organization
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Ima-DBI
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PERRIN/Ima-DBI-%{version}.tar.gz

BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Data::Inheritable) >= 0.02
BuildRequires:  perl(DBI) >= 1.2
BuildRequires:  perl(DBIx::ContextualFetch) >= 1
BuildRequires:  perl(strict)
# Tests:
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Test::More) >= 0.18
Requires:  perl(Carp)
Requires:  perl(Class::Data::Inheritable) >= 0.02
Requires:  perl(DBI) >= 1.2
Requires:  perl(DBIx::ContextualFetch) >= 0.02

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((Class::Data::Inheritable|DBI)\\)

Provides:       perl(Ima::DBI)
Provides:       perl(Ima::DBI)
%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Ima-DBI-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes
%{perl_vendorlib}/Ima
%{_mandir}/man3/*.3*


%changelog
%autochangelog
