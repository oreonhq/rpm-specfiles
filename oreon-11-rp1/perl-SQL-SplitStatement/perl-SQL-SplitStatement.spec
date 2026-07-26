%global source0_hash 1a748420cd2ad341c2524ef1185b76ef7172969f17a9e4bab6f4376f0de9f35e

Name:           perl-SQL-SplitStatement
Version:        1.00023
Release:        14%{?dist}
Summary:        Split any SQL code into atomic statements
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/SQL-SplitStatement
Source0:        https://cpan.metacpan.org/authors/id/V/VE/VEESH/SQL-SplitStatement-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators

BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Accessor::Fast)
BuildRequires:  perl(constant)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(Regexp::Common)
BuildRequires:  perl(SQL::Tokenizer) >= 0.22
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Script::Run)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

%description
This is a simple module which tries to split any SQL code, even including
non-standard extensions (for the details see the "SUPPORTED DBMSs" section
of the module documentation), into the atomic statements it is composed of.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n SQL-SplitStatement-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
# The LICENSE file is outdated and contains the wrong address for the FSF
# https://rt.cpan.org/Ticket/Display.html?id=107996
%license LICENSE
%{_bindir}/sql-split
%{perl_vendorlib}/SQL
%{_mandir}/man1/sql-split*
%{_mandir}/man3/SQL*

%changelog
%autochangelog
