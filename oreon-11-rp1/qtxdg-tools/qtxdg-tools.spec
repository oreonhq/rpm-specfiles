%global source0_hash eb86b9b622bf61947a234a4cb701c6531255c4d0144ba783f3f16a5afa53bfbb

Name:    qtxdg-tools
Summary: User tools for libqtxdg
Version: 4.3.0
Release: 2%{?dist}
License: LGPL-2.0-or-later
URL:     https://lxqt-project.org/
Source0: https://github.com/lxqt/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires: cmake
BuildRequires: pkgconfig(Qt6Xdg)
BuildRequires: cmake(lxqt2-build-tools)
BuildRequires: cmake(Qt6Core)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: gcc-c++

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%{_bindir}/qtxdg-mat
%{_datadir}/cmake/qtxdg-tools/

%changelog
%autochangelog
