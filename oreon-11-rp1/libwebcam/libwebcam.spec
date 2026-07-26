%global source0_hash 3ca5199c7b8398b655a7c38e3ad4191bb053b1486503287f20d30d141bda9d41

Name:           libwebcam
Version:        0.2.5
Release:        24%{?dist}
Summary:        A library for user-space configuration of the uvcvideo driver
License:        LGPL-3.0-or-later
URL:            http://sourceforge.net/p/libwebcam/wiki/Home/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-src-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  gengetopt
BuildRequires:  gcc
BuildRequires:  libxml2-devel

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
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
Requires:       %{name} = %{version}-%{release}
Requires:       uvcdynctrl-data = %{version}-%{release}

%description -n uvcdynctrl
Uvcdynctrl is a command line interface for manipulating settings in
UVC-type webcams. It uses the libwebcam library for webcam access.

%package -n uvcdynctrl-data
Summary:        XML control file for the uvcdynctrl package
# Automatically converted from old format: GPLv3 - review is highly recommended.
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
# https://fedoraproject.org/wiki/Changes/CMake4.0
# https://fedoraproject.org/wiki/Changes/CMake_drop_install_vars
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

%files
%doc libwebcam/README libwebcam/COPYING.LESSER
%{_libdir}/libwebcam.so.*

%files devel
%{_includedir}/dynctrl-logitech.h
%{_includedir}/webcam.h
%{_libdir}/libwebcam.so
%{_libdir}/pkgconfig/libwebcam.pc

%files -n uvcdynctrl
%doc uvcdynctrl/README uvcdynctrl/COPYING
%{_bindir}/uvcdynctrl*
/lib/udev/uvcdynctrl
/lib/udev/rules.d/80-uvcdynctrl.rules
%{_mandir}/man1/uvcdynctrl*.1*

%files -n uvcdynctrl-data
%{_datadir}/uvcdynctrl

%changelog
%autochangelog
