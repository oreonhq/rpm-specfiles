%global source0_hash e320f141b736b3a6468e7d0c08a93961db6615e9eb4d533d554eea31c3fa845a
Summary:        3-dimensional perspective star map viewer
Name:		starplot
Version:	0.95.5
Release:        43%{?dist}
License:	GPL-2.0-or-later
URL:		http://starplot.org/
Source0:        http://starplot.org/downloads/%{name}-%{version}.tar.gz
Patch0:		%{name}-%{version}-desktop.patch
Patch1:         %{name}-%{version}-rhbz1037339.patch
Patch2:         %{name}-%{version}-rhbz1308152.patch
Patch3:		starplot-0.95.5-qsort_vs_new-bz1322030.patch
Patch4:		starplot-0.95.5-specclass-init-at-operator.patch
Requires:	xdg-utils
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  gtk2-devel
BuildRequires:  make
BuildRequires:  xdg-utils
# /oreon:deps
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
rm -f ./doc/examples/*.stars
%find_lang %{name}
%oreon_autofiles main

%check

desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
