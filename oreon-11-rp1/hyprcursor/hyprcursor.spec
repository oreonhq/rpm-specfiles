%global source0_hash 82af8b2ce27242ffdd6baebaa71b3f6c8665dc25c52bfcfccc16912622896af8
Name:           hyprcursor
Version:        0.1.13
Release:        1%{?dist}
Summary:        The hyprland cursor format, library and utilities
License:        BSD-3-Clause
URL:            https://github.com/hyprwm/hyprcursor
Source0:        https://github.com/hyprwm/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(hyprlang)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libzip)
BuildRequires:  pkgconfig(tomlplusplus)
# /oreon:deps
%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
Development files for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 
mkdir -p $HOME/.icons
mv HyprBibataModernClassicSVG $HOME/.icons

%build

%cmake
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n hyprcursor-devel -f %{oreon_filedir}/hyprcursor-devel.list

%changelog

%autochangelog
