%global source0_hash 645efe860a88d34e50a9544a6fd23aa63eb43b4c76b4ac6aed075acf074c39e4
%global debug_package %{nil}
Name:		socnetv
Version:	3.7
Release:        1%{?dist}
License:	GPL-3.0-only
Summary:        A Social Networks Analyser and Visualiser
URL:		https://socnetv.org/
Source0:        https://github.com/socnetv/app/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:	        socnetv-fix-build-against-qt-6-10.patch
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gzip
BuildRequires:  make
BuildRequires:  pkgconfig(Qt6)
BuildRequires:  pkgconfig(Qt6Charts)
BuildRequires:  pkgconfig(Qt6Core5Compat)
BuildRequires:  pkgconfig(Qt6Svg)
BuildRequires:  qt6-linguist
# /oreon:deps
%description
Social Network Visualizer (SocNetV) is a cross-platform, user-friendly
free software application for social network analysis and visualization.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir app-%{version}
%oreon_prep
%build

lrelease-qt6 socnetv.pro
qmake6
%{make_build}
%install
%{make_install} INSTALL_ROOT=%{buildroot}
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
%post

/usr/bin/update-desktop-database &> /dev/null || :
%postun

/usr/bin/update-desktop-database &> /dev/null || :
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
