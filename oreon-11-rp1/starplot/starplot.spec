%global source0_hash e320f141b736b3a6468e7d0c08a93961db6615e9eb4d533d554eea31c3fa845a

Summary:	3-dimensional perspective star map viewer
Name:		starplot
Version:	0.95.5
Release:	43%{?dist}

# See README
# SPDX confirmed
License:	GPL-2.0-or-later
URL:		http://starplot.org/
Source0:	http://starplot.org/downloads/%{name}-%{version}.tar.gz

Patch0:		%{name}-%{version}-desktop.patch
# Fix build with -Werror=format-security"
Patch1:         %{name}-%{version}-rhbz1037339.patch
# C++11 build fix
Patch2:         %{name}-%{version}-rhbz1308152.patch
# Fix segv on startup (bug 1322030)
Patch3:		starplot-0.95.5-qsort_vs_new-bz1322030.patch
# SpecClass::initialize: Fix invalid access when luminosity class ends at
# the end of the line (bug 2029228)
Patch4:		starplot-0.95.5-specclass-init-at-operator.patch

Requires:	xdg-utils

BuildRequires:  make
BuildRequires:	gcc-c++
BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	gtk2-devel
BuildRequires:	xdg-utils

%description
StarPlot is a GTK+ based program, written in C++, which can be used
interactively to view three-dimensional perspective charts of stars.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1
%patch -P1 -p1 -b .format
%patch -P2 -p1 -b .c++11
%patch -P3 -p1 -b .new_qsort
%patch -P4 -p1 -b .specclass_init

# Suppress rpmlint error.
iconv --from-code ISO8859-1 --to-code UTF-8 ./doc/examples/example.spec \
  --output example.utf-8 && mv example.utf-8 ./doc/examples/example.spec

# Fix "_STRING_H" name conflict
sed -i src/classes/strings.h \
	-e '\@def.*_STRINGS_H@s@_STRINGS_H@STARPLOT_STRINGS_H@'

%build
%configure \
  --docdir=%{_pkgdocdir} \
  --disable-rpath \
  --with-webbrowser=xdg-open
%make_build

%install
%make_install

# Remove *.stars files from documentation.
rm -f ./doc/examples/*.stars

%find_lang %{name}

%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

%files -f %{name}.lang
%doc AUTHORS
%doc ChangeLog
%license COPYING
%doc NEWS
%doc NLS-TEAM
%doc README
%doc TODO
%doc doc/examples
%doc doc/html

%{_bindir}/%{name}
%{_bindir}/starconvert
%{_bindir}/starpkg
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/pixmaps/%{name}32x32.xpm
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/starconvert.1*
%{_mandir}/man1/starpkg.1*

%dir %{_datadir}/%{name}
%{_datadir}/%{name}/sample.stars
%{_datadir}/%{name}/test.stars

%changelog
%autochangelog
