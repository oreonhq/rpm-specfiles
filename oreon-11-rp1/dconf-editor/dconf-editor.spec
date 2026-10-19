%global source1_hash 956d2db8e692ceae9e7589193e364658e001f593b1c4a5cb1ed5064168f209c1
%global source0_hash 90a8ccfadf51dff31e0028324fb9a358b2d26c5ae861a71c7dbf9f4dd9bdd399
%global dconf_version 0.26.1
%global glib2_version 2.56.0
%global gtk3_version 3.22.27
%global tarball_version %(echo %{version} | tr '~' '.')
Name:           dconf-editor
Version:        49.0
Release:        1%{?dist}
Summary:        Configuration editor for dconf
License:        GPL-3.0-or-later AND CC0-1.0
URL:            https://wiki.gnome.org/Projects/dconf
Source0:        https://download.gnome.org/sources/%{name}/49/%{name}-%{version}.tar.xz
Source1:        https://raw.githubusercontent.com/flathub/ca.desrt.dconf-editor/master/start-dconf-editor.sh
Requires:       dconf%{?_isa} >= %{dconf_version}
Requires:       glib2%{?_isa} >= %{glib2_version}
Requires:       gtk3%{?_isa} >= %{gtk3_version}
# oreon:deps
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  pkgconfig(dconf)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  vala
# /oreon:deps
%description
Graphical tool for editing the dconf configuration database.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{name}-%{tarball_version}

%build

%meson
%meson_build
%install
%meson_install
%if 0%{?flatpak}
install -m 755 %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/start-dconf-editor
%endif
%find_lang dconf-editor
%oreon_autofiles main

%check

appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_datadir}/metainfo/ca.desrt.dconf-editor.metainfo.xml
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/ca.desrt.dconf-editor.desktop
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 49.0-1
- Prepare for Oreon 11 (RP1)
