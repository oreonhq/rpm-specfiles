# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 e8a98b0ee20c495a6ab894398a065ef580272dbd5a15b1b19e8bd1bc89d9f9fa
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

Name: texi2html
Version: 5.0
Release: 26%{?dist}
# GPLv2+ is for the code
# OFSFDL (Old FSF Documentation License) for the documentation
# CC-BY-SA or GPLv2 for the images
License: GPL-2.0-or-later AND LicenseRef-OFSFDL AND (CC-BY-SA-3.0 OR GPL-2.0-only)
Summary: A highly customizable texinfo to HTML and other formats translator
Source0: http://download.savannah.nongnu.org/releases/%{name}/%{name}-%{version}.tar.bz2
# Do not install bundled Unicode-EastAsianWidth, bug #1154436,
# <https://savannah.nongnu.org/bugs/?43456>
Patch0: texi2html-5.0-Do-not-install-Unicode-EastAsianWidth-if-external-is.patch
# Do not install bundled libintl-perl, <https://savannah.nongnu.org/bugs/?43457>
Patch1: texi2html-5.0-Do-not-install-libintl-perl-if-external-is-used.patch
URL: http://www.nongnu.org/texi2html/
Requires: perl-interpreter >= 5.004
Requires: latex2html
# autotools for the unbundling patches
BuildRequires: make
BuildRequires: autoconf automake
BuildRequires: gcc-c++
BuildRequires: latex2html texlive-tex4ht gettext
BuildRequires: perl-generators
BuildRequires: perl(Data::Dumper)
BuildRequires: perl(Locale::Messages)
BuildRequires: perl(Text::Unidecode)
BuildRequires: perl(Unicode::EastAsianWidth)
# not detected automatically because it is required at runtime based on
# user configuration
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
%oreon_verify_sources
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

# directories shared by all the texinfo implementations for common
# config files, like htmlxref.cnf
mkdir -p $RPM_BUILD_ROOT%{_datadir}/texinfo $RPM_BUILD_ROOT%{_sysconfdir}/texinfo

%find_lang %{name}
%find_lang %{name}_document

%check
#make check

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
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.0-26
- Prepare for Oreon 11 (RP1)
