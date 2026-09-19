%global source0_hash 04424a091e7cb554b2aa62f0e3a6e4778f3dfe580a5f2064681f9d66709be704

Name:          gpsbabel
Version:       1.10.0
Release:       3%{?dist}
Summary:       A tool to convert between various formats used by GPS devices

License:       GPL-2.0-or-later
URL:           http://www.gpsbabel.org
# Upstream's website hides tarball behind some ugly php script
# Original repo is at https://github.com/gpsbabel/gpsbabel
Source0:       gpsbabel-%{version}.tar.gz
Source2:       %{name}.png

# No automatic phone home by default (RHBZ 668865)
Patch1: 0001-No-solicitation.patch
# Upstream patch
Patch2: 0002-add-cmake-option-upgrade-chk-and-stats-reporting.patch

BuildRequires: libusb1-devel
BuildRequires: zlib-devel
BuildRequires: desktop-file-utils
BuildRequires: shapelib-devel
BuildRequires: cmake

BuildRequires: qt6-qtbase-devel
BuildRequires: qt6-qtserialport-devel
## FIXME: Why isn't qt6-linguist enough and qt6-qttools-devel required?
BuildRequires: qt6-qttools-devel
BuildRequires: qt6-qt5compat-devel
%ifarch %{qt6_qtwebengine_arches}
## HACK: Don't build GUI on archs not supported by qtwebengine
%global build_gui 1
BuildRequires: qt6-qtwebchannel-devel
BuildRequires: qt6-qtwebengine-devel
BuildRequires: qt6-qttranslations
%endif

%description
Converts GPS waypoint, route, and track data from one format type
to another.

%if 0%{?build_gui}
%package gui
Summary:        Qt GUI interface for GPSBabel
License:        GPL-2.0-or-later
Requires:       %{name} = %{version}-%{release}
# pull-in qt6 standard translations.
# Otherwise items such as "Close", "Open" won't be translated
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
%endif

%files
%doc README* AUTHORS
%license COPYING
%{_bindir}/gpsbabel

%if 0%{?build_gui}
%files gui
%doc gui/{AUTHORS,README*,TODO}
%license gui/COPYING*
%{_bindir}/gpsbabelfe
%{_datadir}/gpsbabel
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/256x256/apps/*
%endif

%changelog
%autochangelog
