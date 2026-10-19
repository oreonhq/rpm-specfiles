%global source0_hash 77c6ef3f89d8c3ea137a5f4bb0dcd83b261046facbde06eaee223437ad1c732f
%bcond_with    qt6
Name:           chessx
Version:        1.6.10
Release:        1%{?dist}
Summary:        Chess Database and PGN viewer
License:        GPL-2.0-only AND GPL-3.0-only
URL:            https://sourceforge.net/projects/chessx/
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tgz
Patch001:       0001-Work-around-Qt-Wayland-integration-issue.patch
Patch002:       https://github.com/Isarhamster/chessx/pull/61.patch#/0002-Fix-install-path-of-icons-on-Linux.patch
Patch003:       https://github.com/Isarhamster/chessx/pull/63.patch#/0003-Allow-linking-against-system-libraries-via-pkg-confi.patch
%if %{with qt6}
%else
%endif
Provides:       bundled(scid) = 1.0
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Multimedia)
BuildRequires:  pkgconfig(Qt6Svg)
BuildRequires:  pkgconfig(quazip1-qt6)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  qt6-linguist
# /oreon:deps
%description
ChessX is a free and open source chess database application for Linux, Mac OS X
and Windows.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-master

# Fix up lupdate path
sed -i 's| lupdate | $$[QT_INSTALL_BINS]/lupdate |' chessx.pro

# Ensure bundled quazip code is not used
rm -rf src/quazip

# Remove executable bit from regular files (the tarball is buggy)
chmod -R -x+X .

%build

%if %{with qt6}
%qmake_qt6 \
%else
%qmake_qt5 \
%endif
    -r CONFIG+=link_pkgconfig PREFIX=%{_prefix}
%make_build
%install
%make_install INSTALL_ROOT=%{buildroot}
%oreon_autofiles main

%check

appstream-util validate-relax --nonet \
    %{buildroot}%{_metainfodir}/io.sourceforge.ChessX.metainfo.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
