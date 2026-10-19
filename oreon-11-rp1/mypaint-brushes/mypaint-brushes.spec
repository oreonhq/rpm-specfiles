%global source0_hash fef66ffc241b7c5cd29e9c518e933c739618cb51c4ed4d745bf648a1afc3fe70
%global mypaint_data_version 1.0
Name: mypaint-brushes
Epoch: 1
Version: 1.3.1
Release:        1%{?dist}
Summary:        Brushes to be used with the MyPaint library
License: CC0-1.0
URL: https://github.com/mypaint/mypaint-brushes
Source0:        https://github.com/mypaint/mypaint-brushes/releases/download/v%{version}/mypaint-brushes-%{version}.tar.xz
BuildArch: noarch
# oreon:deps
BuildRequires:  make
# /oreon:deps
%package devel
Summary: Files for developing with mypaint-brushes
Requires: pkgconfig
License: GPL-2.0-or-later
%description
This package contains brush files for use with MyPaint and other programs.

%description devel
This package contains a pkgconfig file which makes it easier to develop
programs using these brush files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure
make %{?_smp_mflags}
%install
%make_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n mypaint-brushes-devel -f %{oreon_filedir}/mypaint-brushes-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.3.1-1
- Prepare for Oreon 11 (RP1)
