%global source0_hash a5f0266673c59028eab6ceeddd8b862c70abfeb32fb7a5387c16bf46f3269ab2
%global debug_package %{nil}
Name:           inja
Version:        3.5.0
Release:        1%{?dist}
Summary:        Jinja-inspired template engine for modern C++
License:        MIT
URL:            https://pantor.github.io/inja/
Source0:        https://github.com/pantor/inja/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0001:      0001-cmake-Use-GNUInstallDirs-for-install-paths-and-insta.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(nlohmann_json)
BuildRequires:  gcc-c++
# /oreon:deps
%description
Inja is a template engine for modern C++, loosely inspired by jinja for Python.
It has an easy and yet powerful template syntax with all variables, loops, conditions,
includes, callbacks, and comments you need, nested and combined as you like.

%package        devel
Summary:        Development files for %{name}
%description    devel
Inja is a template engine for modern C++, loosely inspired by jinja for Python.
It has an easy and yet powerful template syntax with all variables, loops, conditions,
includes, callbacks, and comments you need, nested and combined as you like.

The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%conf
%cmake -DINJA_USE_EMBEDDED_JSON=OFF

%build

%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n inja-devel -f %{oreon_filedir}/inja-devel.list

%changelog

%autochangelog
