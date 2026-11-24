# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash e8a98b0ee20c495a6ab894398a065ef580272dbd5a15b1b19e8bd1bc89d9f9fa
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: texi2html
Version: 5.0
Release: %{autorelease}
License: GPL-2.0-or-later AND LicenseRef-OFSFDL AND (CC-BY-SA-3.0 OR GPL-2.0-only)
Summary: A highly customizable texinfo to HTML and other formats translator
Source0: http://download.savannah.nongnu.org/releases/%{name}/%{name}-%{version}.tar.bz2
Patch0: texi2html-5.0-Do-not-install-Unicode-EastAsianWidth-if-external-is.patch
Patch1: texi2html-5.0-Do-not-install-libintl-perl-if-external-is-used.patch
URL: http://www.nongnu.org/texi2html/
Requires: perl-interpreter >= 5.004
Requires: latex2html
BuildRequires: oreon-rpm-macros
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: latex2html
BuildRequires: texlive-tex4ht
BuildRequires: gettext
BuildRequires: perl-generators
BuildRequires: perl(Data::Dumper)
BuildRequires: perl(Locale::Messages)
BuildRequires: perl(Text::Unidecode)
BuildRequires: perl(Unicode::EastAsianWidth)
Requires: perl(Locale::Messages)
Requires: perl(Text::Unidecode)
Requires: perl(Unicode::EastAsianWidth)
BuildArch: noarch

%description
The basic purpose of texi2html is to convert Texinfo documents into HTML, 
and other formats.  Configuration files written in perl provide fine degree 
of control over the final output, allowing most every aspect of the final 
output not specified in the Texinfo input file to be specified.  

%prep
%oreon_sha256
%setup -q
%patch -P0 -p1
%patch -P1 -p1
rm -r lib
aclocal -I m4
automake --add-missing
autoconf

%build
%configure --with-external-libintl-perl=yes \
    --with-external-Unicode-EastAsianWidth=yes
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT 
rm -f $RPM_BUILD_ROOT%{_infodir}/dir

mkdir -p $RPM_BUILD_ROOT%{_datadir}/texinfo $RPM_BUILD_ROOT%{_sysconfdir}/texinfo

%find_lang %{name}
%find_lang %{name}_document

%check

%files -f %{name}.lang -f %{name}_document.lang
%doc AUTHORS COPYING ChangeLog NEWS README TODO %{name}.init
%{_bindir}/%{name}
%{_datadir}/texinfo/html/%{name}.html
%{_mandir}/man*/%{name}*
%{_infodir}/%{name}.info*
%{_datadir}/texinfo/init/*.init
%dir %{_datadir}/%{name}/i18n/
%{_datadir}/%{name}/i18n/*
%dir %{_datadir}/%{name}/images/
%{_datadir}/%{name}/images/*
%dir %{_datadir}/texinfo
%dir %{_sysconfdir}/texinfo

%changelog
%autochangelog
