%global source0_hash ab3525d8bad576db911d4ba1b586f303dd988660b3b8980022c1795fd574b165
Name:           hyprland-protocols
Version:        0.4.0
Release:        1%{?dist}
Summary:        Wayland protocol extensions for Hyprland
BuildArch:      noarch
License:        BSD-3-Clause
URL:            https://github.com/hyprwm/hyprland-protocols
Source0:        https://github.com/hyprwm/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  meson
# /oreon:deps
%description
%{summary}.

%package        devel
Summary:        Wayland protocol extensions for Hyprland
%description    devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n hyprland-protocols-devel -f %{oreon_filedir}/hyprland-protocols-devel.list

%changelog

%autochangelog
