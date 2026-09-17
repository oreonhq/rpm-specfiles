%global source0_hash 6111555224a277b3698b465c24cef758c2cb7ef101ad22f0308ecd56ccd6c1e7

Name:			maim
Version:		5.8.1
Release:		4%{?dist}
Summary:		Command-line screen capture tool

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:		GPL-3.0-only
URL:			https://github.com/naelstrof/maim
Source0:		https://github.com/naelstrof/maim/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	gcc-c++
BuildRequires:	cmake
BuildRequires:	libX11-devel
BuildRequires:	libXrender-devel
BuildRequires:	libXfixes-devel
BuildRequires:	libXrandr-devel
BuildRequires:	libXcomposite-devel
BuildRequires:	libpng-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libwebp-devel
BuildRequires:	mesa-libGL-devel
BuildRequires:	glm-devel
BuildRequires:	libslopy-devel >= 7.5
BuildRequires:	libicu-devel

%description
maim (make image) is a screenshot utility that provides options for capturing
predetermined or user selected regions of your desktop.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%doc README.md
%{_bindir}/maim
%{_mandir}/man1/maim.1.*

%license COPYING license.txt

%changelog
%autochangelog
