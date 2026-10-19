%global source0_hash 019084058c8bf5aa13353e3eaf7ac5a9e4ac875b5e859c7ca1cf63dc0969db8f
%global source_version %%(echo "%version" | tr '~' '-')
%global commit 46b5b9e4bfb75fbccc5043b07ef5c76a3cc72ce3
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Name:          ibus-unikey
Version:       0.7.0~beta1
Release:        1%{?dist}
Summary:        Vietnamese engine for IBus input platform
License:       GPL-3.0-only
URL:           https://github.com/vn-input/ibus-unikey/
Source0:        https://github.com/vn-input/%{name}/archive/refs/tags/0.7.0-beta1.tar.gz#/%{name}-0.7.0-beta1.tar.gz
Patch1:        %{name}-2267853-super-space.patch
Patch2:        %{name}-2257688-segv-load-config.patch
Patch3:        %{name}-2380650-cmake-4.patch
Requires: ibus
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  gtk3-devel
BuildRequires:  ibus-devel
BuildRequires:  intltool
BuildRequires:  pkgconf-pkg-config
# /oreon:deps
%description
A Vietnamese engine for IBus input platform that uses Unikey.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{source_version}

%build

%cmake
%cmake_build
%install
%cmake_install
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
