%global source0_hash 2f1e54336ed6cc3dbab5ad5279f2520eae1a90fc80852ab005a8250a5a15d1ac
Name:           hyprwayland-scanner
Version:        0.4.2
Release:        1%{?dist}
Summary:        A Hyprland implementation of wayland-scanner, in and for C++
License:        BSD-3-Clause
URL:            https://github.com/hyprwm/hyprwayland-scanner
Source0:        https://github.com/hyprwm/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(pugixml)
BuildRequires:  gcc-c++
# /oreon:deps
%description
%{summary}.

%package        devel
Summary:        A Hyprland implementation of wayland-scanner, in and for C++
%description    devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n hyprwayland-scanner-devel -f %{oreon_filedir}/hyprwayland-scanner-devel.list

%changelog

%autochangelog
