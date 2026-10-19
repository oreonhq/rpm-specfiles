%global source0_hash 8b481ceedbf0ae4a83effb80581550008bfdd3885ef01145e3733c7097c00a08
Name:           perl-Ima-DBI
Version:        0.35
Release:        1%{?dist}
Summary:        Database connection caching and organization
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Ima-DBI
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PERRIN/Ima-DBI-%{version}.tar.gz
BuildArch:      noarch
Requires:  perl(Carp)
Requires:  perl(Class::Data::Inheritable) >= 0.02
Requires:  perl(DBI) >= 1.2
Requires:  perl(DBIx::ContextualFetch) >= 0.02
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((Class::Data::Inheritable|DBI)\\)
Provides:       perl(Ima::DBI)
Provides:       perl(Ima::DBI)
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Data::Inheritable)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(DBI)
BuildRequires:  perl(DBIx::ContextualFetch)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
