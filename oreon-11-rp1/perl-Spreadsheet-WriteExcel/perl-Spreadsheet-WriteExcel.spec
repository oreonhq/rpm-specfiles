%global source0_hash e356aad6866cf135731268ee0e979a197443c15a04878e9cf3e80d022ad6c07e
Name:			perl-Spreadsheet-WriteExcel
Version:		2.40
Release:        35%{?dist}
Summary:        Write formatted text and numbers to a cross-platform Excel binary file
License:		GPL-1.0-or-later OR Artistic-1.0-Perl
URL:			https://metacpan.org/release/Spreadsheet-WriteExcel
Source0:        https://cpan.metacpan.org/modules/by-module/Spreadsheet/Spreadsheet-WriteExcel-%{version}.tar.gz
Patch0:			Spreadsheet-WriteExcel-2.40-utf8.patch
BuildArch:		noarch
Requires:		perl(Date::Calc)
Requires:		perl(Date::Manip)
Requires:		perl(Digest::MD4)
Requires:		perl(Encode)
Requires:		perl(File::Temp)
Requires:		perl(OLE::Storage_Lite) >= 0.19
Requires:		perl(Parse::RecDescent)
%{?perl_default_filter:
%filter_requires_in %{perl_vendorlib}/Spreadsheet/WriteExcel/Examples.pm
%perl_default_filter
}
%global __requires_exclude_from %{?__requires_exclude_from:%__requires_exclude_from|}Spreadsheet/WriteExcel/Examples\\.pm$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Date::Calc)
BuildRequires:  perl(Date::Manip)
BuildRequires:  perl(Digest::MD4)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(OLE::Storage_Lite)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Parse::RecDescent)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(autouse)
BuildRequires:  perl(integer)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
The Spreadsheet::WriteExcel module can be used to create a cross-
platform Excel binary file. Multiple worksheets can be added to a
workbook and formatting can be applied to cells. Text, numbers,
formulas, hyperlinks and images can be written to the cells.

The Excel file produced by this module is compatible with 97,
2000, 2002 and 2003. Generated files are also compatible with the
spreadsheet applications Gnumeric and OpenOffice.org.

This module cannot be used to read an Excel file. See
Spreadsheet::ParseExcel or look at the main documentation for some
suggestions. This module cannot be used to write to an existing
Excel file.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Spreadsheet-WriteExcel-%{version} 

# Fix encoding of Changes file
%patch -P0

# Fix line endings
perl -pi -e 's/\r\n/\n/g' examples/*.txt

%build

perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
