%global source0_hash df9f515ee159804b0d5a75d5adb93c4584c7ec401d8c59c27e9f73925d8dac68
Name:       perl-Text-PDF
Version:    0.31
Release:        28%{?dist}
License:    GPL-1.0-or-later OR Artistic-1.0-Perl
Summary:        Module for manipulating PDF files
Source0:        https://cpan.metacpan.org/authors/id/B/BH/BHALLISSY/Text-PDF-%{version}.tar.gz
Patch0:     Text-PDF-0.29-formats.patch
Url:        https://metacpan.org/release/Text-PDF
BuildArch:  noarch
Requires:      pdf-tools = %{version}-%{release}
%{?perl_default_filter}
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::Simple)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module allows interaction with existing PDF files directly. It
includes various tools:

    pdfbklt   - make booklets out of existing PDF files
    pdfrevert - remove edits from a PDF file
    pdfstamp  - stamp text on each page of a PDF file

%package -n pdf-tools
License:    GPL-1.0-or-later OR Artistic-1.0-Perl
Summary:    Manipulate PDF files
Requires:   %{name} = %{version}-%{release}
%description -n pdf-tools
This package allows existing PDF files to be modified; and includes various
tools:

    pdfbklt   - make booklets out of existing PDF files
    pdfrevert - remove edits from a PDF file
    pdfstamp  - stamp text on each page of a PDF file

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Text-PDF-%{version}
find . -type f -exec chmod -c -x     {} ';'
sed -i 's/\r//' examples/CD.CFG
%patch -P 0 -p1

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*
%oreon_autofiles pdf-tools usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make test
%files -f %{oreon_filedir}/main.list
%files -n pdf-tools -f %{oreon_filedir}/pdf-tools.list

%changelog

%autochangelog
