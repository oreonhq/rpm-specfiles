%global source0_hash d74027f809809a8dfa98baf7719db163416d352665011e1c2cf5e1cf6ad54466

Name:           dtklog
Version:        0.0.2
Release:        %autorelease
Summary:        Simple, convenient and thread safe logger for Qt-based C++ apps
License:        LGPL-2.1-or-later
URL:            https://github.com/linuxdeepin/dtklog
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake

BuildRequires:  cmake(Qt5Core)
BuildRequires:  qt5-qtbase-private-devel
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}
BuildRequires:  cmake(spdlog)
BuildRequires:  pkgconfig(libsystemd)

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains development files for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake \
    -DBUILD_WITH_SYSTEMD=ON \
    -DBUILD_WITH_QT6=OFF \
    -DDLOG_VERSION=%{version} \

%cmake_build

%install
%cmake_install

%files
%license LICENSE.LGPL
%doc README.md
%{_libdir}/libdtklog.so.0*

%files devel
%{_libdir}/libdtklog.so
%{_includedir}/dtk5/DLog/
%{_libdir}/cmake/DtkLog/
%{_libdir}/pkgconfig/dtklog.pc
%{_qt5_archdatadir}/mkspecs/modules/qt_lib_dtklog.pri

%changelog
%autochangelog
