%global source0_hash 3b6a603acbec496202e4b601830aefbe3ef78037142cf496dd2c45de8635116d
%bcond_without perl_DBIx_XHTML_Table_enables_optional_test
Name:           perl-DBIx-XHTML_Table
Version:        1.49
Release:        1%{?dist}
Summary:        SQL query result set to XHTML table
License:        Artistic-2.0
URL:            https://metacpan.org/release/DBIx-XHTML_Table
Source0:        https://cpan.metacpan.org/authors/id/J/JE/JEFFA/DBIx-XHTML_Table-%{version}.tar.gz
BuildArch:      noarch
%if %{with perl_DBIx_XHTML_Table_enables_optional_test}
%endif
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(DBD::CSV)
BuildRequires:  perl(DBI)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(HTML::TableExtract)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
DBIx::XHTML_Table is a DBI extension that creates an XHTML table from a
database query result set. It was created to fill the gap between fetching
rows from a database and transforming them into a web browser renderable
table. DBIx::XHTML_Table is intended for programmers who want the
responsibility of presenting (decorating) data, easily. This module is
meant to be used in situations where the concern for presentation and logic
separation is overkill. Providing logic or editable data is beyond the
scope of this module, but it is capable of doing such.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n DBIx-XHTML_Table-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
