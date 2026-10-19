%global source0_hash 9685ce7481baf0cb5ff1e694c2ae5ba6ae5e251dbb3dcf1300150fd08be6c3ac
Name:           perl-Text-CHM
Version:        0.01
Release:        1%{?dist}
Summary:        Perl extension for handling MS Compiled HtmlHelp Files
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Text-CHM
Source0:        https://cpan.metacpan.org/modules/by-module/Text/Text-CHM-%{version}.tar.gz
# oreon:deps
BuildRequires:  chmlib-devel
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Text::CHM is a module that implements a (partial) support for handling MS 
Compiled HtmlHelp Files (chm files for short) via CHMLib. 

Text::CHM allows you to open chm files, get their filelist, get the content 
of each file and close them; at the moment, no write support is available.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Text-CHM-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name '*.bs' -a -size 0 -delete
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
