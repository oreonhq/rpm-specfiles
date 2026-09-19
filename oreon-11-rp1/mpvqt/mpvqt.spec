%global source0_hash bdd1ea69338cf3017f628a886218b8c185ca24e8257f03207a3cf1bbb51e3d32

Name:           mpvqt
Version:        1.1.1
Release:        %autorelease
Summary:        QML wrapper for libmpv
License:        LGPL-2.1-only OR LGPL-3.0-only
URL:            https://invent.kde.org/libraries/mpvqt
Source:         https://download.kde.org/%{stable_kf6}/mpvqt/mpvqt-%{version}.tar.xz

BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  pkgconfig(mpv)

%description
MpvQt is a libmpv wrapper for Qt Quick 2/Qml.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Quick)
Requires:       pkgconfig(mpv)
%description devel
Development headers and link library for building packages which use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%files
%license LICENSES/LGPL* LICENSES/LicenseRef-KDE*
%doc README.md
%{_libdir}/libMpvQt.so.{2,%{version}}

%files devel
%{_includedir}/MpvQt/
%{_libdir}/libMpvQt.so
%{_libdir}/cmake/MpvQt/

%changelog
%autochangelog
