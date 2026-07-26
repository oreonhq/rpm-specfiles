%global source0_hash f32bccde79f6947136f6179d7e349536e0ebdd83fd6b24616e859c28f0f09550

Name:		screenruler
Version:	1.2.1
Release:	6%{?dist}

Summary:	GNOME screen ruler
# SPDX confirmed
License:	GPL-2.0-or-later
URL:		https://salsa.debian.org/georgesk/screenruler

Source0:	https://salsa.debian.org/georgesk/screenruler/-/archive/upstream/%{version}/%{name}-upstream-%{version}.tar.bz2
Source2:	%{name}.appdata.xml
# Workaround for screenruler not showing window properly at startup
# bug 2275166
# Need reporting upstream
Patch0:	screenruler-1.2-gtkwidget-show_all-workaround.patch

BuildRequires:	make
BuildRequires:	desktop-file-utils
BuildRequires:	/usr/bin/appstream-util
BuildRequires:	/usr/bin/gettext
BuildRequires:	/usr/bin/msgmerge
BuildRequires:	/usr/bin/rxgettext

Requires:		rubygem(cairo)
Requires:		rubygem(gettext)
Requires:		rubygem(gtk3)

BuildArch:		noarch

%description
ScreenRuler lets you measure objects on your desktop
using six different metrics.

* Horizontal and vertical measurement in 6 different metrics: pixels,
  centimeters, inches, picas, points, and as a percentage of the ruler’s
  length.
* Color and font are customizable.
* Keyboard control for precise positioning.
* Ruler can be set to stay always on top of other windows.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-upstream-%{version}
%patch -P0 -p1

%build
%make_build

%install
%make_install

# Add AppStream metadata
mkdir -p %{buildroot}%{_metainfodir}
install -cpm 0644 %{SOURCE2} \
	%{buildroot}%{_metainfodir}/%{name}.appdata.xml

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml

%files
%license	COPYING
%doc	AUTHORS
%doc	README.md

%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_metainfodir}/%{name}.appdata.xml

%{_bindir}/%{name}
%dir	%{_datadir}/screenruler/
%{_datadir}/screenruler/*.glade
%{_datadir}/screenruler/*.png
%{_datadir}/screenruler/*.rb
%{_datadir}/screenruler/locale/
%{_datadir}/screenruler/utils/

%changelog
%autochangelog
