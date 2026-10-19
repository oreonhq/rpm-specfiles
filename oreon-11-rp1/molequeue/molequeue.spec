%global source0_hash 1b02bba0ca346cce46d6d7dac57115c31cdf95b3d79369594f142afbdcdc0503
%global gitcommit 0a35627edc490a79ac8bb17f1ed5c3d993074b91
%global gitdate 20241024
%global shortcommit %(c=%{gitcommit}; echo ${c:0:7})
Name:    molequeue
Summary:        Desktop integration of high performance computing resources
Version: 0.9.0
Release:        1%{?dist}
License: BSD-3-Clause
URL:     https://github.com/OpenChemistry/%{name}
Source0:        https://github.com/OpenChemistry/%{name}/archive/%{gitcommit}/%{name}-%{gitcommit}.tar.gz
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtscript-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  qt5-qtwebkit-devel
BuildRequires:  qt5-qtxmlpatterns-devel
BuildRequires:  qt5-rpm-macros
# /oreon:deps
%description
MoleQueue is an open-source, cross-platform, system-tray resident desktop
application for abstracting, managing, and coordinating the execution of tasks
both locally and on remote computational resources. Users can set up local and
remote queues that describe where the task will be executed. Each queue can
have programs, with templates to facilitate the execution of the program. Input
files can be staged, and output files collected using a standard interface.
Some highlights:

* Open source distributed under the liberal 3-clause BSD license
* Cross platform with nightly builds on Linux, Mac OS X and Windows
* Intuitive interface designed to be useful to whole community
* Support for local executation and remote schedulers (SGE, PBS, SLURM)
* System tray resident application managing queue of queues and job lifetime
* Simple, lightweight JSON-RPC 2.0 based communication over local sockets
* Qt 5 client library for simple integration in Qt applications

%package libs
Summary: Shared and private libraries of %{name}
%description libs
Shared and private libraries of %{name}.

%package  devel
Summary:  Development files of %{name}
Requires: qt5-qtbase-devel
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%description devel
This package contains libraries and header files for developing
applications that use %{name}.

%package doc
Summary: HTML documentation of %{name}
BuildArch: noarch
%description doc
HTML documentation of %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{gitcommit}

%build

%cmake -Wno-dev \
 -DENABLE_RPATH:BOOL=OFF \
 -DCMAKE_SKIP_INSTALL_RPATH:BOOL=YES \
 -DCMAKE_SKIP_RPATH:BOOL=YES \
 -DENABLE_TESTING:BOOL=OFF \
 -DBUILD_DOCUMENTATION:BOOL=ON \
 -DCMAKE_VERBOSE_MAKEFILE:BOOL=TRUE \
 -DPYTHON_EXECUTABLE:FILEPATH=%{__python3} \
 -DCMAKE_BUILD_TYPE:STRING=Release
%cmake_build
pushd %{__cmake_builddir}/docs
doxygen
popd
%install
%cmake_install
rm -rf %{buildroot}%{_datadir}/doc
cat >%{name}.desktop <<EOF
[Desktop Entry]
Name=MoleQueue
Comment=Manage HPC jobs from the system tray
Exec=%{name}
Terminal=false
Type=Application
Icon=%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
EOF
install -Dpm0644 molequeue/app/icons/%{name}.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
desktop-file-install %{name}.desktop --dir %{buildroot}%{_datadir}/applications
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n molequeue-libs -f %{oreon_filedir}/molequeue-libs.list
%files -n molequeue-devel -f %{oreon_filedir}/molequeue-devel.list
%files -n molequeue-doc -f %{oreon_filedir}/molequeue-doc.list

%changelog

%autochangelog
