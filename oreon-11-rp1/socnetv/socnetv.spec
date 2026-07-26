%global source0_hash 1f60cb3f14d22b445f80b1106f7e9a9084b7496dd3c979a1421051db25a459a2

%global debug_package %{nil}

Name:		socnetv
Version:	3.2
Release:	4%{?dist}
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:	GPL-3.0-only
Summary:	A Social Networks Analyser and Visualiser
URL:		https://socnetv.org/
Source0:	https://github.com/socnetv/app/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

Patch0:	        socnetv-fix-build-against-qt-6-10.patch

BuildRequires: make
BuildRequires:	gcc-c++
BuildRequires:	gzip
BuildRequires:	qt6-linguist
BuildRequires:	desktop-file-utils
# qt6-qtbase-devel
BuildRequires:	pkgconfig(Qt6)
# qt6-qtsvg-devel
BuildRequires:	pkgconfig(Qt6Svg)
# qt6-qtcharts-devel
BuildRequires:	pkgconfig(Qt6Charts)
# qt6-qt5compat-devel
BuildRequires:	pkgconfig(Qt6Core5Compat)
%if 0%{?fedora} && 0%{?fedora} > 39
ExcludeArch:	i686
%endif

%description
Social Network Visualizer (SocNetV) is a cross-platform, user-friendly
free software application for social network analysis and visualization.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n app-%{version}

%build
lrelease-qt6 socnetv.pro
qmake6
%{make_build}

%install
%{make_install} INSTALL_ROOT=%{buildroot}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%post
/usr/bin/update-desktop-database &> /dev/null || :

%postun
/usr/bin/update-desktop-database &> /dev/null || :

%files
%license COPYING
%doc AUTHORS CHANGELOG.md README.md
%{_bindir}/%{name}
%{_datadir}/%{name}/%{name}_*.qm
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/metainfo/%{name}.appdata.xml
%{_mandir}/man1/%{name}.1.gz

%changelog
%autochangelog
