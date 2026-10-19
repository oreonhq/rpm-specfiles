%global source0_hash c5871835521d015ef2ad1276b1f58340d946c2903466337f3170bac3c58d61f2
Summary:        Gstreamer phonon backend
Name:    phonon-backend-gstreamer
Epoch:   2
Version: 4.10.0
Release:        18%{?dist}
License: LicenseRef-Callaway-LGPLv2+
URL:     https://community.kde.org/Phonon
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        https://download.kde.org/stable/phonon/%{name}/%{version}/%{name}-%{version}.tar.xz
%global phonon_version %(pkg-config --modversion phonon 2>/dev/null || echo 4.11)
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Phonon4Qt5)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf5-rpm-macros
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-app-1.0)
BuildRequires:  pkgconfig(gstreamer-audio-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
# /oreon:deps
%description
%{summary}.

%package -n phonon-qt5-backend-gstreamer
Summary:  Gstreamer phonon-qt5 backend
Provides: phonon-qt5-backend%{?_isa} = %{phonon_version}
Requires: gstreamer1-plugins-good%{?_isa}
%description -n phonon-qt5-backend-gstreamer
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir phonon-backend-gstreamer-%{version}
%oreon_prep
%build

%cmake_kf5 \
  -DCMAKE_BUILD_TYPE:STRING="Release" \
  -DUSE_INSTALL_PLUGIN:BOOL=ON \
  -DPHONON_BUILD_PHONON4QT5:BOOL=ON
%cmake_build
%install
%cmake_install
%find_lang phonon_gstreamer --with-qt
%oreon_autofiles phonon-qt5-backend-gstreamer usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n phonon-qt5-backend-gstreamer -f %{oreon_filedir}/phonon-qt5-backend-gstreamer.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.10.0-18
- Prepare for Oreon 11 (RP1)
