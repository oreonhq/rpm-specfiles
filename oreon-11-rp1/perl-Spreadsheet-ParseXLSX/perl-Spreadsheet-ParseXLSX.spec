%global source0_hash 079530629d7cf0e65d7f098b6298236d05ceebf8bf4f4755246e01d5e708a210
Name:           perl-Spreadsheet-ParseXLSX
Version:        0.36
Release:        1%{?dist}
Summary:        Parse XLSX files
License:        MIT
URL:            https://github.com/MichaelDaum/spreadsheet-parsexlsx
Source0:        https://cpan.metacpan.org/authors/id/N/NU/NUDDLEGG/Spreadsheet-ParseXLSX-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Archive::Zip)
BuildRequires:  perl(Crypt::Mode::CBC)
BuildRequires:  perl(Crypt::Mode::ECB)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Graphics::ColorUtils)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(OLE::Storage_Lite)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Spreadsheet::ParseExcel)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XML::Twig)
BuildRequires:  perl(blib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module is an adaptor for <Spreadsheet::ParseExcel> that reads XLSX files.
For documentation about the various data that you can retrieve from these
classes, please see <Spreadsheet::ParseExcel>,
<Spreadsheet::ParseExcel::Workbook>, <Spreadsheet::ParseExcel::Worksheet>, and
<Spreadsheet::ParseExcel::Cell>.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Spreadsheet-ParseXLSX-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1 NO_PERLLOCAL=1
make %{?_smp_mflags}
%install
%make_install
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
