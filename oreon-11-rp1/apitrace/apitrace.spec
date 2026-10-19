%global source1_hash 201bb83fe8fa09a271c4abc9f0c174effb0c59d0de7c84153847008535d5bedb
%global source0_hash 53469052b28ca56dc0d28153d218dee6c2c128c53b2aa32d6e7f906f7a5c6c7a
%global libbacktrace_commit 8602fda64e78f1f46563220f2ee9f7e70819c51d
%global libbacktrace_shortcommit %(c=%{libbacktrace_commit}; echo ${c:0:7})
Name:           apitrace
Version:        14.0
Release:        1%{?dist}
Summary:        Tools for tracing OpenGL
License:        MIT
URL:            http://apitrace.github.io/
%if 0%{?commit:1}
Source0:        https://github.com/%{name}/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
%else
Source0:        https://github.com/%{name}/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
%endif
Source1:        https://github.com/ianlancetaylor/libbacktrace/archive/%{libbacktrace_commit}/libbacktrace-%{libbacktrace_shortcommit}.tar.gz
Source2:        qapitrace.desktop
Source3:        qapitrace.appdata.xml
Patch0:         apitrace_nosubmodules.patch
Patch1:         apitrace-gcc15.patch
Patch2:         https://github.com/apitrace/apitrace/commit/6f8527625ad5cf636e04a65b035228da96d7e228.patch
Requires:       %{name}-libs%{_isa} = %{version}-%{release}
Requires:       python3-pillow
Provides:       bundled(md5-plumb)
Provides:       bundled(libbacktrace)
Provides:       bundled(crc32c)
# oreon:deps
BuildRequires:  brotli-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gtest-devel
BuildRequires:  libappstream-glib
BuildRequires:  libdwarf-devel
BuildRequires:  libpng-devel
BuildRequires:  python3-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  snappy-devel
# /oreon:deps
%description
apitrace consists of a set of tools to:
 * trace OpenGL and OpenGL ES  APIs calls to a file;
 * replay OpenGL and OpenGL ES calls from a file
 * inspect OpenGL state at any call while retracing
 * visualize and edit trace files

%package libs
Summary:        Libraries used by apitrace
Requires:       %{name} = %{version}-%{release}
%description libs
Libraries used by apitrace

%package gui
Summary:        Graphical frontend for apitrace
Requires:       %{name}%{_isa} = %{version}-%{release}
%description gui
This package contains qapitrace, the Graphical frontend for apitrace.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if 0%{?commit:1}
%autosetup -p1 -n %{name}-%{commit} -a1
%else
%autosetup -p1 -n %{name}-%{version} -a1
%endif

# Remove bundled libraries, except khronos headers
rm -rf `ls -1d thirdparty/* | grep -Ev "(khronos|md5|crc32c|libbacktrace.cmake|support|CMakeLists.txt)"`

# Add bundled libbacktrace
mv libbacktrace-%{libbacktrace_commit} thirdparty/libbacktrace

%build

%cmake -DENABLE_STATIC_SNAPPY=OFF -DENABLE_QT6=ON -DSCRIPTS_INSTALL_DIR=%{_libdir}/%{name}/scripts
%cmake_build
%install
%cmake_install
rm -rf %{buildroot}%{_docdir}/
desktop-file-install --dir=%{buildroot}%{_datadir}/applications/ %{SOURCE2}
install -Dpm 0644 gui/resources/qapitrace.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/qapitrace.png
install -Dpm 0644 %{SOURCE3} %{buildroot}%{_datadir}/appdata/qapitrace.appdata.xml
%{_bindir}/appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/qapitrace.appdata.xml
chmod 0644 %{buildroot}%{_libdir}/%{name}/scripts/highlight.py
%oreon_autofiles apitrace-libs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles apitrace-gui usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n apitrace-libs -f %{oreon_filedir}/apitrace-libs.list
%files -n apitrace-gui -f %{oreon_filedir}/apitrace-gui.list

%changelog

%autochangelog
