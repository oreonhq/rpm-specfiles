%global source0_hash cdbbbfe241b8fe5f3a1d0b16e73115125e264a9c94d25fce9e2fcf43429efab9

%global debug_package %{nil}

Name:		pinta
Version:	1.7.1
Release:	12%{?dist}
Summary:	An easy to use drawing and image editing program

# the code is licensed under the MIT license while the icons are licensed as CC-BY
# Automatically converted from old format: MIT and CC-BY - review is highly recommended.
License:	LicenseRef-Callaway-MIT AND LicenseRef-Callaway-CC-BY
URL:		http://pinta-project.com/

Source0:	http://github.com/PintaProject/Pinta/releases/download/%{version}/%{name}-%{version}.tar.gz

# Mono only available on these:
ExclusiveArch:	%mono_arches

# Pinta fails to build on armv7hl. Mono crashes.
# https://bugzilla.redhat.com/show_bug.cgi?id=1869214
ExcludeArch:	armv7hl

BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	mono-devel
BuildRequires:	mono-addins-devel
BuildRequires:	gtk-sharp2-devel
BuildRequires:	gettext
BuildRequires:	intltool
BuildRequires:	desktop-file-utils
BuildRequires:	libappstream-glib
Requires:	hicolor-icon-theme
Requires:	mono-addins

%description
Pinta is an image drawing/editing program.
It's goal is to provide a simplified alternative to GIMP for casual users.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure
%make_build

%install
%make_install

# Validate desktop file
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

# Validate AppData file
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml

%find_lang %name

%files -f %{name}.lang
%license license-mit.txt license-pdn.txt
%doc readme.md
%{_libdir}/%{name}
%{_libdir}/pkgconfig/%{name}.pc
%{_bindir}/%{name}
%{_metainfodir}/%{name}.appdata.xml
%exclude %{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/%{name}.*
%{_datadir}/man/man1/%{name}*
%{_datadir}/pixmaps/%{name}*

%changelog
%autochangelog
