%global source0_hash cd7395eaeb1eee90ebeba9c1330a7635709dd0900ebbe349a7aa5702ba4d613f
Name:           hyprlang
Version:        0.6.4
Release:        1%{?dist}
Summary:        The official implementation library for the hypr config language
License:        LGPL-3.0-only
URL:            https://github.com/hyprwm/hyprlang
Source0:        https://github.com/hyprwm/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(hyprutils)
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
%oreon_prep
%build

%cmake
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n hyprlang-devel -f %{oreon_filedir}/hyprlang-devel.list

%changelog

%autochangelog
