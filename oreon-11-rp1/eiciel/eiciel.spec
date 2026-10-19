%global source0_hash 234280b2cbb83c48c11b6b8e6e9392245bd174f531bdfec5daabad76c24beb71
Name: eiciel
Version: 0.10.1
%global tar_version %{version}
Release:        1%{?dist}
Summary:        Graphical editor for ACLs and xattr
License: GPL-2.0-or-later
URL: http://rofi.roger-ferrer.org/eiciel
Source0:        http://rofi.roger-ferrer.org/%{name}/files/%{name}-%{version}.tar.xz
Patch0: eiciel-0.10.1-rawhide-gcc.patch
Requires: hicolor-icon-theme
%global ext_dir %(eval "pkg-config --variable=extensiondir libnautilus-extension-4")
%global __provides_exclude_from ^%{ext_dir}/.*\\.so$
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  itstool
BuildRequires:  libacl-devel
BuildRequires:  meson
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(gtkmm-4.0)
BuildRequires:  pkgconfig(libnautilus-extension-4)
# /oreon:deps
%description
Graphical editor for access control lists (ACLs) and extended attributes
(xattr), either as an extension within Nautilus, or as a standalone
utility.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{tar_version}

%build

%meson
%meson_build
%install
%meson_install
%find_lang %{name}
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
