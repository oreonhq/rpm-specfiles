%global source0_hash b5fb16c2b7a3e76b709a72e3fc58b64b3b35f3c33249623044bb214cd886b069

Name:           perl-DBD-XBase
Version:        1.08
Release:        28%{?dist}
Summary:        Perl module for reading and writing the dbf files

# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            http://www.adelton.com/perl/DBD-XBase/
Source0:        http://www.adelton.com/perl/DBD-XBase/DBD-XBase-%{version}.tar.gz
Patch0:         DBD-XBase-0.241-indexdump.PL.patch

BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(DBI)
BuildRequires:  perl(ExtUtils::MakeMaker)

%description
This module can read and write XBase database files, known as dbf in
dBase and FoxPro world. It also transparently reads memo fields from
the dbt, fpt and smt files and works with index files (ndx, ntx, mdx, idx,
cdx and SDBM). This module XBase.pm provides simple native interface
to XBase files. For DBI compliant database access, see DBD::XBase and
DBI modules and their man pages.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n DBD-XBase-%{version}
%patch -P0 -p1
chmod a-x eg/*table

# We want to distribute dbfdump.pl, not dbfdump
find . -type f | xargs %{__perl} -i.theorig -pe 's/(?<!\$)\bdbfdump/dbfdump.pl/g'
find . -type f -name '*.theorig' | %{__perl} -pe 's/\.theorig$//' | while read i ; do touch -r $i.theorig $i ; done
find . -type f -name '*.theorig' -exec rm -f {} ';'
mv bin/dbfdump.PL bin/dbfdump.pl.PL

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
%doc Changes README ToDo driver_characteristics new-XBase
%doc eg/
%{_bindir}/*
%{perl_vendorlib}/DBD/
%{perl_vendorlib}/XBase*
%{_mandir}/man1/*.1*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
