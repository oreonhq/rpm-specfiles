%global source0_hash 1020d39695e957bc7636607d91b6ecc76858add82405d6b523df053e1f0e8b98

Name:           perl-Queue-DBI
Version:        2.7.0
Release:        27%{?dist}
Summary:        A queueing module with an emphasis on safety, using DBI as a storage system
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Queue-DBI
Source0:        https://cpan.metacpan.org/authors/id/A/AU/AUBERTG/Queue-DBI-v%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBI)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::Dist::VersionSync)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::FailWarnings)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Type)
BuildRequires:  perl(Try::Tiny)

%{?perl_default_filter}

%description
Queue-DBI allows you to safely use a queueing system by preventing
backtracking, infinite loops and data loss. An emphasis of this distribution
is to provide an extremely reliable dequeueing mechanism without having to
use transactions.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Queue-DBI-v%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README.md
%license LICENSE
%{perl_vendorlib}/Queue*
%{_mandir}/man3/Queue*

%changelog
%autochangelog
