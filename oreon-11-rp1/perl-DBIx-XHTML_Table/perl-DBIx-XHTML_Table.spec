%global source0_hash 3b6a603acbec496202e4b601830aefbe3ef78037142cf496dd2c45de8635116d

# Run optional tests
%if 0%{?rhel}
%bcond_with perl_DBIx_XHTML_Table_enables_optional_test
%else
%bcond_without perl_DBIx_XHTML_Table_enables_optional_test
%endif
Name:           perl-DBIx-XHTML_Table
Version:        1.49
Release:        28%{?dist}
Summary:        SQL query result set to XHTML table
License:        Artistic-2.0
URL:            https://metacpan.org/release/DBIx-XHTML_Table
Source0:        https://cpan.metacpan.org/authors/id/J/JE/JEFFA/DBIx-XHTML_Table-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(DBI)
BuildRequires:  perl(vars)
# Tests
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(utf8)
%if %{with perl_DBIx_XHTML_Table_enables_optional_test}
# Optional tests
BuildRequires:  perl(DBD::CSV)
BuildRequires:  perl(HTML::TableExtract)
%endif

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

%check
make test

%files
%doc Changes readme.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
