%global source0_hash fde689da209df6d3ea96009ff3622075c2c09b59d8837e3bdb14805a955156d7

%global pkgname Spreadsheet-XLSX

Summary:        Perl extension for reading Microsoft Excel 2007 files
Name:           perl-Spreadsheet-XLSX
Version:        0.18
Release:        5%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/%{pkgname}
Source0:        https://cpan.metacpan.org/authors/id/A/AS/ASB/%{pkgname}-%{version}.tar.gz
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl(Archive::Zip) >= 1.18
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Spreadsheet::ParseExcel) >= 0.45
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Warnings)
BuildRequires:  perl(Test::NoWarnings)
BuildArch:      noarch

%description
The Spreadsheet::XLSX module is a emulation of Spreadsheet::ParseExcel for
Excel 2007 (.xlsx) file format in a quick and dirty way. It supports styles
and many of the Excel's quirks, but not all. It populates the classes from
Spreadsheet::ParseExcel for interoperability; including workbook, worksheet
and cell.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{pkgname}-%{version}

# Change strange upstream file permissions
chmod 0644 Changes README lib/Spreadsheet/{*,*/*}.pm

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build

%install
%make_install
chmod -R u+w $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/Spreadsheet/
%{_mandir}/man3/*.3pm*

%changelog
%autochangelog
