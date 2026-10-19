%global source0_hash efba32610498acde76fa2e147017c91b20c13ec945e05e348cd4183fd1613be1
Summary:        Advanced drum machine for GNU/Linux
Name:         hydrogen
Version:      1.2.6
Release:        1%{?dist}
URL:          http://www.hydrogen-music.org/
Source0:        https://github.com/hydrogen-music/%{name}/archive/refs/tags/%{version}/%{name}-%{version}.tar.gz
License:      GPL-2.0-or-later
Patch0:       %{name}-cxxflags.patch
Requires:      hicolor-icon-theme
# oreon:deps
BuildRequires:  alsa-lib-devel
BuildRequires:  cmake
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  cppunit-devel
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
BuildRequires:  flac-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  ladspa-devel
BuildRequires:  libappstream-glib
BuildRequires:  libarchive-devel
BuildRequires:  liblo-devel
BuildRequires:  libsndfile-devel
BuildRequires:  make
BuildRequires:  pulseaudio-libs-devel
# /oreon:deps
%description
Hydrogen is an advanced drum machine for GNU/Linux. It's main goal is to bring 
professional yet simple and intuitive pattern-based drum programming.

%package devel
Summary:    Hydrogen header files
Requires:   %{name}%{_isa} = %{version}-%{release}
Obsoletes:  devel <= 0.9.7-9
%description devel
Header files for the hydrogen drum machine.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DCMAKE_POSITION_INDEPENDENT_CODE=ON \
  -DCMAKE_SKIP_INSTALL_RPATH=ON \
  -DWANT_DEBUG=OFF \
  -DWANT_QT6=ON
%cmake_build
%install
%cmake_install
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications   \
  --add-category X-Drumming                    \
  --add-category Midi                          \
  --add-category X-Jack                        \
  --add-category AudioVideoEditing             \
  --remove-mime-type text/xml                  \
  --delete-original                            \
  %{buildroot}%{_datadir}/applications/org.hydrogenmusic.Hydrogen.desktop
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
cp %{buildroot}%{_datadir}/%{name}/data/img/gray/*.svg \
   %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
rm -f %{buildroot}%{_datadir}/%{name}/data/doc/{Makefile,README}* \
      %{buildroot}%{_datadir}/%{name}/data/doc/*.{docbook,po,pot}
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.hydrogenmusic.Hydrogen.metainfo.xml
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n hydrogen-devel -f %{oreon_filedir}/hydrogen-devel.list

%changelog

%autochangelog
