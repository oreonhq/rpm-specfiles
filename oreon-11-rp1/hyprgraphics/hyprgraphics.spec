%global source0_hash 861ecaad872835922dd5745a612d7a4cc7bfc4babb1d06bc92bc63c2ac013b74
%bcond libjxl 1
Name:           hyprgraphics
Version:        0.5.1
Release:        1%{?dist}
Summary:        Graphics library for Hyprland
License:        BSD-3-Clause
URL:            https://github.com/hyprwm/hyprgraphics
Source0:        https://github.com/hyprwm/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
ExcludeArch:    %{ix86}
%if %{with libjxl}
%endif
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(hyprlang)
BuildRequires:  pkgconfig(hyprutils)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libjxl)
BuildRequires:  pkgconfig(libjxl_cms)
BuildRequires:  pkgconfig(libjxl_threads)
BuildRequires:  pkgconfig(libmagic)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(spng)
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

%ifarch s390x
rm tests/resource/images/hyprland.jpg
%endif
%ctest
%files -f %{oreon_filedir}/main.list
%files -n hyprgraphics-devel -f %{oreon_filedir}/hyprgraphics-devel.list

%changelog

%autochangelog
