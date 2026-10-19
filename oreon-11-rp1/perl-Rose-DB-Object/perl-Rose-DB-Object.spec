%global source0_hash 22dcc78dc7780fd416f64cf5bb5b80f3b2353600b5fca6ec18ddc9c75d907afb
Name:		perl-Rose-DB-Object
Version:	0.822
Release:        1%{?dist}
Summary:        Extensible, high performance object-relational mapper (ORM)
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Rose-DB-Object
Source0:        https://cpan.metacpan.org/authors/id/J/JS/JSIRACUSA/Rose-DB-Object-%{version}.tar.gz
BuildArch:	noarch
%global __requires_exclude ^perl\\(Rose::(DB|Object)::
%{?perl_default_filter}
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Bit::Vector)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Clone)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBI)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Rose::DB)
BuildRequires:  perl(Rose::DateTime::Util)
BuildRequires:  perl(Rose::Object)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Memory::Cycle)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Time::Clock)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Rose::DB::Object is a base class for objects that encapsulate a single row
in a database table. Rose::DB::Object-derived objects are sometimes simply
called "Rose::DB::Object objects" in this documentation for the sake of
brevity, but be assured that derivation is the only reasonable way to use
this class.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Rose-DB-Object-%{version}
find . -type f -executable -exec chmod -x {} \;

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

export AUTOMATED_TESTING=1
make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
