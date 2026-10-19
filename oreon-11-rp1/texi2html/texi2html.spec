%global source0_hash e8a98b0ee20c495a6ab894398a065ef580272dbd5a15b1b19e8bd1bc89d9f9fa
Name: texi2html
Version: 5.0
Release:        1%{?dist}
License: GPL-2.0-or-later AND LicenseRef-OFSFDL AND (CC-BY-SA-3.0 OR GPL-2.0-only)
Summary:        A highly customizable texinfo to HTML and other formats translator
Source0:        http://download.savannah.nongnu.org/releases/%{name}/%{name}-%{version}.tar.bz2
Patch0: texi2html-5.0-Do-not-install-Unicode-EastAsianWidth-if-external-is.patch
Patch1: texi2html-5.0-Do-not-install-libintl-perl-if-external-is-used.patch
URL: http://www.nongnu.org/texi2html/
Requires: perl-interpreter >= 5.004
Requires: latex2html
Requires: perl(Locale::Messages)
Requires: perl(Text::Unidecode)
Requires: perl(Unicode::EastAsianWidth)
BuildArch: noarch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  latex2html
BuildRequires:  make
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Locale::Messages)
BuildRequires:  perl(Text::Unidecode)
BuildRequires:  perl(Unicode::EastAsianWidth)
BuildRequires:  perl-generators
BuildRequires:  texlive-tex4ht
# /oreon:deps
%description
The basic purpose of texi2html is to convert Texinfo documents into HTML, 
and other formats.  Configuration files written in perl provide fine degree 
of control over the final output, allowing most every aspect of the final 
output not specified in the Texinfo input file to be specified.  

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q
%patch -P0 -p1
%patch -P1 -p1
# Remove bundled modules
rm -r lib
# Regenerate build script because of the patch
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
%oreon_autofiles main

%check

%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.0-26
- Prepare for Oreon 11 (RP1)
