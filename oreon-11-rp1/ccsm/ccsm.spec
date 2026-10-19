%global source0_hash 0dda29684501fee692fa90f3af29503872dd7c9f6b28353f7ba22e4436ce17f8
%global basever 0.8.16
Name:           ccsm
Version:        0.8.18
Release:        24%{?dist}
Epoch:          1
Summary:        Plugin and configuration tool - Compiz Reloaded Project
License:        GPL-2.0-or-later
URL:            https://gitlab.com/compiz/%{name}
Source0:        https://gitlab.com/compiz/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.bz2
BuildArch:      noarch
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
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-ccsm = %{version}-%{release}
# /oreon:deps
%description
The Compiz Project brings 3D desktop visual effects that improve
usability of the X Window System and provide increased productivity
though plugins and themes contributed by the community giving a
rich desktop experience.

This package contains a GUI configuration tool to configure Compiz
plugins and the composite window manager.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-v%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
mv %{buildroot}%{_datadir}/{metainfo,appdata}/
%find_lang %{name}
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/ccsm.desktop
%files

%changelog

%autochangelog
