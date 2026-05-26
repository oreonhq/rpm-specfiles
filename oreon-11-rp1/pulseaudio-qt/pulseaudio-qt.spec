# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 79619c55b94808aa7d307fb234ad39a1096d088f21f806be0e788be79a76b3c9
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

Name:    pulseaudio-qt
Summary: Qt bindings for PulseAudio
Version: 1.8.1
Release: 1%{?dist}

License: CC0-1.0 AND LGPL-2.1-only AND LGPL-3.0-only
URL:     https://invent.kde.org/libraries/pulseaudio-qt
Source:  https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  kf5-rpm-macros
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6DBus)

%description
Pulseaudio-Qt is a library providing Qt bindings to PulseAudio.

%package qt6
Summary: Qt6 bindings for PulseAudio
%description qt6
%{summary}.

%package qt6-devel
Summary: Development files for %{name} (Qt6)
Requires: %{name}-qt6%{?_isa} = %{version}-%{release}
%description qt6-devel
%{summary}.

%package qt6-doc
Summary: Developer Documentation files for %{name}
%description qt6-doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.


%prep
%oreon_verify_sources
%autosetup -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
rm %{buildroot}%{_kf6_includedir}/pulseaudioqt_version.h

%files qt6
%license LICENSES/*.txt
%doc README.md
%{_kf6_libdir}/libKF6PulseAudioQt.so.5
%{_kf6_libdir}/libKF6PulseAudioQt.so.%{version}

%files qt6-devel
%{_kf6_includedir}/KF6PulseAudioQt/
%{_kf6_libdir}/libKF6PulseAudioQt.so
%{_kf6_libdir}/cmake/KF6PulseAudioQt/
%{_kf6_libdir}/pkgconfig/KF6PulseAudioQt.pc
%{_qt6_docdir}/*.tags

%files qt6-doc
%{_qt6_docdir}/*.qch

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.8.1-1
- Import
