%global source0_hash 75c2e0cb76e4f9e51a5cdf986be3bf1471d478ad7b215db2f5b7c8582ac17e33

Name:           perl-DBD-SQLite2
Version:        0.38
Release:        25%{?dist}
Summary:        Self Contained RDBMS in a DBI Driver (sqlite 2.x)
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/DBD-SQLite2
Source0:        https://cpan.metacpan.org/authors/id/M/MS/MSERGEANT/DBD-SQLite2-%{version}.tar.gz
Patch0:		DBD-SQLite2-systemlibs.patch
BuildRequires:  gcc
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-interpreter
BuildRequires:	perl-devel
BuildRequires:	perl-generators
BuildRequires:	perl(Config)
BuildRequires:	perl(DBI)
BuildRequires:	perl(DBI::DBD)
BuildRequires:	perl(DynaLoader)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Fatal)
BuildRequires:	perl(File::Copy)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(strict)
BuildRequires:	perl(Test)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(vars)
BuildRequires:	perl(warnings)
BuildRequires:	sqlite2-devel
BuildRequires:  perl(Fatal)

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n DBD-SQLite2-%{version}
%patch -P0 -p1

# Make sure to be using the system-wide version
rm sqlite.h

# https://rt.cpan.org/Public/Bug/Display.html?id=55636
# Unclear whether test is broken or not supposed to be executed
# Rename to avoid it being executed
mv t/ak-dbd.t t/ak-dbd.t.bak

%build
CFLAGS="$RPM_OPT_FLAGS" %{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags} OPTIMIZE="$RPM_OPT_FLAGS"

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
# t/ak-dbd.t doesn't work (c.f. above)
make test

%files
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/DBD
%{_mandir}/man3/*.3*

%changelog
%autochangelog
