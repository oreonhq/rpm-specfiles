%global source0_hash 9685ce7481baf0cb5ff1e694c2ae5ba6ae5e251dbb3dcf1300150fd08be6c3ac

Name:           perl-Text-CHM
Version:        0.01
Release:        58%{?dist}
Summary:        Perl extension for handling MS Compiled HtmlHelp Files
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Text-CHM
Source0:        https://cpan.metacpan.org/modules/by-module/Text/Text-CHM-%{version}.tar.gz
# Build
BuildRequires:  gcc
BuildRequires:  chmlib-devel
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
# Tests
BuildRequires:  perl(Test)

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

%check
make test

%files
%doc README Changes
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Text/
%{_mandir}/man3/*

%changelog
%autochangelog
