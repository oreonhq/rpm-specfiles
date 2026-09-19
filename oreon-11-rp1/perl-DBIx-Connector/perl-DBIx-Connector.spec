%global source0_hash ea783137c54b60ceac04ce5aa962427b21209e5593165ec7d1dde7cbe5d237b4

Name:           perl-DBIx-Connector
Version:        0.60
Release:        4%{?dist}
Summary:        Fast, safe DBI connection and transaction management
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/DBIx-Connector

Source0:        https://cpan.metacpan.org/authors/id/D/DW/DWHEELER/DBIx-Connector-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

# Run-time:
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(Carp)
BuildRequires:  perl(DBI) >= 1.614

# Testing
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(Test::More)

Requires:       perl(Carp)

%description
DBIx::Connector provides a simple interface for fast and safe DBI
connection and transaction management. It allows to keep a database
handle to maintain a connection in order to minimize overhead without
having to worry about dropped or corrupted connections.

Borrowing an interface from DBIx::Class, DBIx::Connector also offers
an API that handles the scoping of database transactions. In addition,
it offers an API for savepoints if a database supports them.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n DBIx-Connector-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
# skipped 't/svp_live.t' since requires a real db
make test

%files
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
