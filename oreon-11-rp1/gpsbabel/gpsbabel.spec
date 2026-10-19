%global source0_hash 04424a091e7cb554b2aa62f0e3a6e4778f3dfe580a5f2064681f9d66709be704
Name:          gpsbabel
Version:       1.10.0
Release:        1%{?dist}
Summary:        A tool to convert between various formats used by GPS devices
License:       GPL-2.0-or-later
URL:           http://www.gpsbabel.org
Source0:        gpsbabel-%{version}.tar.gz
Source2:       %{name}.png
Patch1: 0001-No-solicitation.patch
Patch2: 0002-add-cmake-option-upgrade-chk-and-stats-reporting.patch
%ifarch %{qt6_qtwebengine_arches}
%global build_gui 1
%endif
# oreon:deps
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  libusb1-devel
BuildRequires:  qt6-qt5compat-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtserialport-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  shapelib-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
Converts GPS waypoint, route, and track data from one format type
to another.

%if 0%{?build_gui}
%package gui
Summary:        Qt GUI interface for GPSBabel
License:        GPL-2.0-or-later
Requires:       %{name} = %{version}-%{release}
Requires:       qt6-qttranslations
%description gui
Qt GUI interface for GPSBabel
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}
%patch -P1 -p1
%patch -P2 -p1

%build

%cmake \
  -DGPSBABEL_UPGRADE_CHECK=false \
  -DGPSBABEL_WITH_LIBUSB=pkgconfig \
  -DGPSBABEL_WITH_ZLIB=pkgconfig \
  -DGPSBABEL_WITH_SHAPELIB=pkgconfig \
  %{?!build_gui:-DGPSBABEL_MAPPREVIEW=OFF} \
  ..
%cmake_build
%install
%cmake_install
install -m 0755 -d %{buildroot}%{_bindir}/
install -m 0755 -p %{_vpath_builddir}/gpsbabel %{buildroot}%{_bindir}/
%if 0%{?build_gui}
install -m 0755 -d %{buildroot}%{_bindir}/
install -m 0755 -p %{_vpath_builddir}/gui/GPSBabelFE/gpsbabelfe %{buildroot}%{_bindir}/
install -m 0755 -d %{buildroot}%{_datadir}/gpsbabel
install -m 0644 -p gui/gmapbase.html %{buildroot}%{_datadir}/gpsbabel
desktop-file-install \
        --dir %{buildroot}/%{_datadir}/applications \
        gui/gpsbabel.desktop
install -m 0755 -d            %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/
install -m 0644 -p %{SOURCE2} %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/
%oreon_autofiles main
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
