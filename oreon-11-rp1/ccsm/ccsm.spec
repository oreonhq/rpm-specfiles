%global source0_hash 0dda29684501fee692fa90f3af29503872dd7c9f6b28353f7ba22e4436ce17f8

%global basever 0.8.16

Name:           ccsm
Version:        0.8.18
Release:        24%{?dist}
Epoch:          1
Summary:        Plugin and configuration tool - Compiz Reloaded Project

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://gitlab.com/compiz/%{name}
Source0:        %{url}/-/archive/v%{version}/%{name}-v%{version}.tar.bz2

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  gettext
BuildRequires:  desktop-file-utils
BuildRequires:  intltool

Requires:       compizconfig-python >= %{version}
Requires:       libcompizconfig >= %{basever}
Requires:       compiz >= %{basever}
Requires:       python3-cairo
Requires:       python3-gobject
Requires:       gobject-introspection
Requires:       gdk-pixbuf2
Requires:       pango
Requires:       gtk3
Patch:          ccsm-0.8.18-wheel-fix.patch

%description
The Compiz Project brings 3D desktop visual effects that improve
usability of the X Window System and provide increased productivity
though plugins and themes contributed by the community giving a
rich desktop experience.

This package contains a GUI configuration tool to configure Compiz
plugins and the composite window manager.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-v%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files ccm

mv %{buildroot}%{_datadir}/{metainfo,appdata}/

%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/ccsm.desktop

%files -f %{name}.lang -f %{pyproject_files}
%license COPYING
%doc AUTHORS VERSION
%{_bindir}/ccsm
%{_datadir}/appdata/ccsm.appdata.xml
%{_datadir}/applications/ccsm.desktop
%dir %{_datadir}/ccsm
%{_datadir}/ccsm/*
%{_datadir}/icons/hicolor/*/apps/ccsm.*
%{_datadir}/compiz/icons/hicolor/{22x22/{categories,devices,mimetypes},scalable/{apps,categories}}/*.{png,svg}

%changelog
%autochangelog
