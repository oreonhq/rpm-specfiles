%global source0_hash 2252c95c7eeebdee190c0a8cae3adeb1bb9c70858aef807060669fd02180204c
Name:			maim
Version:		5.8.2
Release:        1%{?dist}
Summary:        Command-line screen capture tool
License:		GPL-3.0-only
URL:			https://github.com/naelstrof/maim
Source0:        https://github.com/naelstrof/maim/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  glm-devel
BuildRequires:  libX11-devel
BuildRequires:  libXcomposite-devel
BuildRequires:  libXfixes-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXrender-devel
BuildRequires:  libicu-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libslopy-devel
BuildRequires:  libwebp-devel
BuildRequires:  mesa-libGL-devel
# /oreon:deps
%description
maim (make image) is a screenshot utility that provides options for capturing
predetermined or user selected regions of your desktop.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%check

%ctest
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
