%global source0_hash 7d58da745a0bd3f9efe7a46d581142e6d1c97ef9d709ef456a91a21497314b6b

Name:           perl-Apache-DBI-Cache
Version:        0.08
Release:        53%{?dist}
Summary:        Perl DBI connection cache
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Apache-DBI-Cache
Source0:        https://cpan.metacpan.org/authors/id/O/OP/OPI/Apache-DBI-Cache-%{version}.tar.gz
Patch0:         0001-DBI-dr-connect-can-clobber-the-arguments.patch

BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time
BuildRequires:  perl(base)
BuildRequires:  perl(BerkeleyDB)
BuildRequires:  perl(DBI) >= 1.37
BuildRequires:  perl(DBD::mysql)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(Class::DBI)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(Ima::DBI)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Deep)
Requires:       perl(DBI) >= 1.37

%{?perl_default_filter}

%global __requires_exclude %{?__requires_exclude:__requires_exclude|}^perl\\(DBI::st\\)$
%global __requires_exclude %__requires_exclude|^perl\\(DBI::db\\)$
%global __requires_exclude %__requires_exclude|^perl\\(DBI\\)$

%description
This module is an alternative to Apache::DBI module. As a drop-in
Apache::DBI replacement it provides persistent DBI connections
while overcoming certain limitations. It is compatible with mod_perl,
though it does not require it.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Apache-DBI-Cache-%{version}
%patch -P0 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
# Directories used as attribute 'f_dir' have to be created
mkdir tmp1 tmp2
make test
rmdir tmp1 tmp2

%files
%doc Changes
%{perl_vendorlib}/Apache/DBI/Cache*
%{_mandir}/man3/Apache::DBI::Cache*

%changelog
%autochangelog
