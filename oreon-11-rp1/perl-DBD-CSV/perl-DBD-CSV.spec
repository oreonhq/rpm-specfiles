%global source0_hash 0d9000e26c300fa23b056e3b65743ca16ceaae90997535d23b80fdea30ca568e

Name:           perl-DBD-CSV
Version:        0.63
Release:        1%{?dist}
Summary:        DBI driver for CSV files
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/DBD-CSV
Source0:        https://cpan.metacpan.org/authors/id/H/HM/HMBRAND/DBD-CSV-0.63.tgz
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(lib)
# Module Runtime
# The DBI and SQL::Statement are needed per DBD::CVS POD
BuildRequires:  perl(Carp)
BuildRequires:  perl(DBD::File) >= 0.45
BuildRequires:  perl(DBI) >= 1.649
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(SQL::Statement) >= 1.405
BuildRequires:  perl(strict)
BuildRequires:  perl(Text::CSV_XS) >= 1.62
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(charnames)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Test::More) >= 1.302222
# Dependencies
Requires:       perl(DBD::File) >= 0.44
Requires:       perl(DBI) >= 1.628
Requires:       perl(Exporter)
Requires:       perl(SQL::Statement) >= 1.405
Requires:       perl(Text::CSV_XS) >= 1.62

%global __requires_exclude %{?__requires_exclude:__requires_exclude|}^perl\\(DBD::File\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Text::CSV_XS\\)$

Provides:       perl(DBD::CSV)
%description
The DBD::CSV module is yet another driver for the DBI (Database
independent interface for Perl). This one is based on the SQL
"engine" SQL::Statement and the abstract DBI driver DBD::File
and implements access to so-called CSV files (Comma separated
values). Such files are mostly used for exporting MS Access and
MS Excel data.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n DBD-CSV-%{version}

chmod -c a-x ChangeLog README lib/DBD/*.pm lib/Bundle/DBD/*.pm

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc ChangeLog CONTRIBUTING.md README SECURITY.md
%{perl_vendorlib}/Bundle/
%{perl_vendorlib}/DBD/
%{_mandir}/man3/Bundle::DBD::CSV.3*
%{_mandir}/man3/DBD::CSV.3*

%changelog
%autochangelog
