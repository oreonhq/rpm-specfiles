%global source0_hash 3ca5199c7b8398b655a7c38e3ad4191bb053b1486503287f20d30d141bda9d41
Name:           libwebcam
Version:        0.2.5
Release:        1%{?dist}
Summary:        A library for user-space configuration of the uvcvideo driver
License:        LGPL-3.0-or-later
URL:            http://sourceforge.net/p/libwebcam/wiki/Home/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-src-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gengetopt
BuildRequires:  libxml2-devel
# /oreon:deps
%description
Libwebcam provides a user-space library for interaction with the uvcvideo
kernel driver. One could use this library to manipulate settings for one
or many UVC-type webcams found attached on a single computer.

%package devel
Summary:        Development libraries and headers for libwebcam
Requires:       %{name} = %{version}-%{release}
%description devel
Development libraries and headers for libwebcam.

%package -n uvcdynctrl
Summary:        Command line interface to libwebcam
License:        GPL-3.0-only
Requires:       %{name} = %{version}-%{release}
Requires:       uvcdynctrl-data = %{version}-%{release}
%description -n uvcdynctrl
Uvcdynctrl is a command line interface for manipulating settings in
UVC-type webcams. It uses the libwebcam library for webcam access.

%package -n uvcdynctrl-data
Summary:        XML control file for the uvcdynctrl package
License:        GPL-3.0-only
Requires:       uvcdynctrl = %{version}-%{release}
BuildArch:      noarch
%description -n uvcdynctrl-data
XML control file for the uvcdynctrl package.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}
# Remove backup file included in the archive by mistake
# https://sourceforge.net/p/libwebcam/discussion/general/thread/573c86ef22/
rm uvcdynctrl/data/046d/logitech.xml~

%build

%cmake \
  -DCMAKE_POLICY_VERSION_MINIMUM=3.5 \
  -DINCLUDE_INSTALL_DIR:PATH=%{_includedir} \
  -DLIB_INSTALL_DIR:PATH=%{_libdir} \
  -DSYSCONF_INSTALL_DIR:PATH=%{_sysconfdir} \
  -DSHARE_INSTALL_PREFIX:PATH=%{_datadir} \
  %if "%{?_lib}" == "lib64"
    %{?_cmake_lib_suffix64} \
  %endif
%cmake_build
%install
%cmake_install
rm $RPM_BUILD_ROOT%{_libdir}/libwebcam.a
%ldconfig_scriptlets
%oreon_autofiles uvcdynctrl usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles uvcdynctrl-data usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n libwebcam-devel -f %{oreon_filedir}/libwebcam-devel.list
%files -n uvcdynctrl -f %{oreon_filedir}/uvcdynctrl.list
%files -n uvcdynctrl-data -f %{oreon_filedir}/uvcdynctrl-data.list

%changelog

%autochangelog
