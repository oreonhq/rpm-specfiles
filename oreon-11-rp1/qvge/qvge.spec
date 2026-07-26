%global source0_hash 034e5ba6cb9a3b67d51815190aae06406fc5ba1ddeb3271fe1c67b7e577657c3

Name:		qvge
Version:	0.6.3
Release:	10%{?dist}
# Automatically converted from old format: MIT and LGPLv3 and BSD - review is highly recommended.
License:	LicenseRef-Callaway-MIT AND LGPL-3.0-only AND LicenseRef-Callaway-BSD
Summary:	Graph editor
URL:		https://arsmasiuk.github.io/qvge/
Source0:	https://github.com/ArsMasiuk/qvge/archive/refs/tags/%{name}-%{version}.tar.gz
# https://github.com/ArsMasiuk/qvge/issues/164
Patch0:		%{name}-%{version}-0.patch
BuildRequires:	make
BuildRequires:	gcc-c++
BuildRequires:	desktop-file-utils
BuildRequires:	libappstream-glib
BuildRequires:	boost-devel
# qt5-qtbase-devel
BuildRequires:	pkgconfig(Qt5Gui)
# qt5-qtx11extras-devel
BuildRequires:	pkgconfig(Qt5X11Extras)
# qt5-qtsvg-devel
BuildRequires:	pkgconfig(Qt5Svg)
# Virtuals
# qpocessinfo (https://github.com/baldurk/qprocessinfo) - BSD
Provides:	bundled(qprocessinfo)
# qsint-widgets (part of https://sourceforge.net/projects/qsint/) - LGLPv3
Provides:	bundled(qsint) = 0.4.0
# qtpropertybrowser (part of https://github.com/qtproject/qt-solutions) - BSD)
Provides:	bundled(qtpropertybrowser) = 2.7
Requires:	shared-mime-info

%description
Multiplatform graph editor written in C++/Qt.
Its main goal is to make possible visually edit two-dimensional graphs in a
simple and intuitive way.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p0

%build
pushd src
%{qmake_qt5} PREFIX=%{_prefix}
%{make_build}
popd

%install
pushd src
%{make_install} INSTALL_ROOT=%{buildroot}
popd
# prepare license files
mv src/3rdParty/qtpropertybrowser/LICENSE src/3rdParty/qprocessinfo/LICENSE.qtpropertybrowser
mv src/3rdParty/qprocessinfo/LICENSE src/3rdParty/qprocessinfo/LICENSE.qprocessinfo
mv src/3rdParty/qsint-widgets/README.txt src/3rdParty/qsint-widgets/README.qsint

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml
# 'make check' not supported with upstream

%files
%license LICENSE src/3rdParty/qprocessinfo/LICENSE.qtpropertybrowser src/3rdParty/qprocessinfo/LICENSE.qprocessinfo src/3rdParty/qsint-widgets/README.qsint
%doc README.md
%{_bindir}/qvgeapp
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/*.xml
%{_datadir}/pixmaps/%{name}.png

%changelog
%autochangelog
