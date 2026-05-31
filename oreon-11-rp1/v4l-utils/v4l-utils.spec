%global source0_hash 6828828a17775526eb93fb258a9294d1d1073d633c344dd71ecd4e7a1ffb7dfc

%bcond qt %[%{undefined rhel} || 0%{?rhel} < 10]

# Currently broken without DVB due to a bunch of random bits
# being built/installed even though they're DVB specific
%define with_dvb 1

Name:           v4l-utils
Version:        1.32.0
Release:        3%{?dist}
Summary:        Utilities for video4linux and DVB devices
# libdvbv5, dvbv5 utils, ir-keytable are GPL-2.0-only
# e.g. utils/cec-follower/cec-follower.cpp is (GPL-2.0-only OR BSD-3-Clause) 
# utils/qvidcap/capture.cpp, paint.cpp are LicenseRef-Fedora-Public-Domain
# utils/v4l2-sysfs-path/v4l2-sysfs-path.c is HPND-sell-variant
License:        GPL-2.0-or-later AND GPL-2.0-only AND (GPL-2.0-only OR BSD-3-Clause) AND LicenseRef-Fedora-Public-Domain AND HPND-sell-variant
URL:            http://www.linuxtv.org/downloads/v4l-utils/

Source0:        http://www.linuxtv.org/downloads/v4l-utils//v4l-utils-1.32.0.tar.xz
# TODO: submit upstream
Patch0:         sbin-location.diff

BuildRequires:  alsa-lib-devel
BuildRequires:  gettext
BuildRequires:  json-c-devel
BuildRequires:  kernel-headers
BuildRequires:  libjpeg-devel
BuildRequires:  meson >= 0.56
BuildRequires:  perl-interpreter
%if %{with qt}
BuildRequires:  desktop-file-utils
%if 0%{?fedora} < 41 || 0%{?rhel}
BuildRequires:  qt5-qtbase-devel
%else
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qt5compat-devel
%endif
%endif
BuildRequires:  systemd-devel
# For /usr/share/pkgconfig/udev.pc
BuildRequires:  systemd
# BPF decoder dependencies
BuildRequires:  clang
BuildRequires:  elfutils-libelf-devel
BuildRequires:  libbpf-devel

# For /lib/udev/rules.d ownership
Requires:       systemd-udev
Requires:       libv4l%{?_isa} = %{version}-%{release}

Provides:       edid-decode = %{version}-%{release}
Obsoletes:      edid-decode < 1

%description
v4l-utils is a collection of various video4linux (V4L), RC core and DVB
utilities. The main v4l-utils package contains cx18-ctl, ivtv-ctl, v4l2-ctl
and v4l2-sysfs-path.


%package -n     libv4l
Summary:        Collection of video4linux support libraries 
# Some of the decompression helpers are GPL-2.0-or-later, the rest is LGPL-2.1-or-later
# lib/libv4lconvert/jidctflt.c and jpeg_memsrcdest.c are IJG-short
# lib/libv4lconvert/helper-funcs.h and libv4lsyscall-priv.h are BSD-2-Clause
License:        LGPL-2.1-or-later AND GPL-2.0-or-later AND IJG-short AND BSD-2-Clause
URL:            http://hansdegoede.livejournal.com/3636.html

%description -n libv4l
libv4l is a collection of libraries which adds a thin abstraction layer on
top of video4linux2 devices. The purpose of this (thin) layer is to make it
easy for application writers to support a wide variety of devices without
having to write separate code for different devices in the same class. libv4l
consists of 3 different libraries: libv4lconvert, libv4l1 and libv4l2.

libv4lconvert offers functions to convert from any (known) pixel-format
to V4l2_PIX_FMT_BGR24 or V4l2_PIX_FMT_YUV420.

libv4l1 offers the (deprecated) v4l1 API on top of v4l2 devices, independent
of the drivers for those devices supporting v4l1 compatibility (which many
v4l2 drivers do not).

libv4l2 offers the v4l2 API on top of v4l2 devices, while adding for the
application transparent libv4lconvert conversion where necessary.


%package -n     libv4l-devel
Summary:        Development files for libv4l
License:        LGPL-2.1-or-later AND GPL-2.0-or-later AND IJG-short AND BSD-2-Clause
URL:            http://hansdegoede.livejournal.com/3636.html
Requires:       libv4l%{?_isa} = %{version}-%{release}

%description -n libv4l-devel
The libv4l-devel package contains libraries and header files for
developing applications that use libv4l.


%package        devel-tools
Summary:        Utilities for v4l2 / DVB driver development and debugging
License:        GPL-2.0-or-later AND GPL-2.0-only
Requires:       libv4l%{?_isa} = %{version}-%{release}

%description    devel-tools
Utilities for v4l2 driver authors: v4l2-compliance and
v4l2-dbg.


%if %{with qt}
%package -n     qv4l2
Summary:        QT v4l2 test control and streaming test application
# utils/qv4l2/qv4l2.svg is CC-BY-SA-3.0
License:        GPL-2.0-or-later AND CC-BY-SA-3.0
Requires:       libv4l%{?_isa} = %{version}-%{release}

%description -n qv4l2
QT v4l2 test control and streaming test application.
%endif


%if %{with dvb}
%package -n     libdvbv5
Summary:        Libraries to control, scan and zap on Digital TV channels
# /lib/include/libdvbv5/dvb-frontend.h is LGPL-2.1-or-later WITH Linux-syscall-note
License:        LGPL-2.1-or-later AND LGPL-2.1-or-later WITH Linux-syscall-note

%description -n libdvbv5
Libraries to control, scan and zap on Digital TV channels


%package -n libdvbv5-gconv
Summary:        Gconv files with the charsets For Digital TV.
License:        LGPL-2.1-or-later

%description -n libdvbv5-gconv
Some digital TV standards define their own charsets. Add library
support for them: EN 300 468 and ARIB STD-B24


%package -n     libdvbv5-devel
Summary:        Development files for libdvbv5
License:        LGPL-2.1-or-later AND LGPL-2.1-or-later WITH Linux-syscall-note
Requires:       libdvbv5%{?_isa} = %{version}-%{release}

%description -n libdvbv5-devel
The libdvbv5-devel package contains libraries and header
files for developing applications that use libdvbv5.


%package        -n dvb-tools
Summary:        Utilities for DVB driver
License:        GPL-2.0-or-later AND GPL-2.0-only
Requires:       libdvbv5%{?_isa} = %{version}-%{release}
Requires:       libv4l%{?_isa} = %{version}-%{release}
Requires:       v4l-utils%{?_isa} = %{version}-%{release}

%description    -n dvb-tools
Utilities and tools for DVB receivers.
%endif

%package	-n rc-tools
Summary:	Utilities for RC core
License:        GPL-2.0-or-later AND GPL-2.0-only
Requires:       v4l-utils%{?_isa} = %{version}-%{release}

%description	-n rc-tools
Utilities for Infrared receivers and transmitters using RC core.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1

%build
%meson -Dbpf=auto \
  -Ddoxygen-doc=disabled -Ddoxygen-man=false -Ddoxygen-html=false \
  %{!?with_dvb:-Dlibdvbv5=disabled} \
  %{!?with_qt:-Dqv4l2=disabled -Dqvidcap=disabled}

%meson_build

%install
%meson_install

find $RPM_BUILD_ROOT -name '*.la' -delete
# Driver removed from upstream
rm -f $RPM_BUILD_ROOT%{_bindir}/decode_tm6000
rm -f $RPM_BUILD_ROOT%{_libdir}/{v4l1compat.so,v4l2convert.so}
mkdir $RPM_BUILD_ROOT%{_libdir}/gconv/gconv-modules.d
mv $RPM_BUILD_ROOT%{_libdir}/gconv/gconv-modules $RPM_BUILD_ROOT%{_libdir}/gconv/gconv-modules.d/libdvbv5.conf

%if %{with qt}
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/qv4l2.desktop
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/qvidcap.desktop
%endif

%find_lang %{name}
%find_lang libdvbv5


%ldconfig_scriptlets -n libv4l

%ldconfig_scriptlets -n libdvbv5

%files -f %{name}.lang
%doc README.md
%{_bindir}/cec-ctl
%{_bindir}/cec-follower
%{_bindir}/edid-decode
%{_bindir}/media-ctl
%{_bindir}/rds-ctl
%{_bindir}/v4l2-ctl
%{_bindir}/v4l2-sysfs-path
%{_bindir}/v4l2-tracer
%{_mandir}/man1/cec-ctl*.1*
%{_mandir}/man1/cec-follower*.1*
%{_mandir}/man1/edid-decode*.1*
%{_mandir}/man1/v4l*.1*
%exclude %{_mandir}/man1/v4l2-compliance.1*

%files devel-tools
%doc README.md
%{_bindir}/cec-compliance
%{_bindir}/v4l2-compliance
%{_mandir}/man1/cec-compliance.1*
%{_mandir}/man1/v4l2-compliance.1*
%{_sbindir}/v4l2-dbg

%files -n libv4l
%license COPYING.libv4l COPYING
%doc README.libv4l
%dir %{_libdir}/libv4l
%{_libdir}/libv4l/v4l*
%{_libdir}/libv4l/plugins
%{_libdir}/libv4l*.so.*

%files -n libv4l-devel
%doc README.lib-multi-threading ChangeLog TODO
%{_includedir}/libv4l*.h
%{_libdir}/libv4l*.so
%{_libdir}/libv4l/ov*
%{_libdir}/libv4l/libv4l2tracer.so
%{_libdir}/pkgconfig/libv4l*.pc

%if %{with qt}
%files -n qv4l2
%doc README.md
%{_bindir}/qv4l2
%{_bindir}/qvidcap
%{_datadir}/applications/qv4l2.desktop
%{_datadir}/applications/qvidcap.desktop
%{_datadir}/icons/hicolor/*/apps/qv4l2.*
%{_datadir}/icons/hicolor/*/apps/qvidcap.*
%{_mandir}/man1/qv4l2.1*
%{_mandir}/man1/qvidcap.1*
%endif

%if %{with dvb}
%files -n libdvbv5 -f libdvbv5.lang
%license COPYING.libdvbv5 COPYING
%doc lib/libdvbv5/README
%{_libdir}/libdvbv5*.so.*

%files -n libdvbv5-gconv
%{_libdir}/gconv/*.so
%{_libdir}/gconv/gconv-modules.d/libdvbv5.conf

%files -n libdvbv5-devel
%{_includedir}/libdvbv5/*.h
%{_libdir}/libdvbv5*.so
%{_libdir}/pkgconfig/libdvbv5*.pc

%files -n dvb-tools
%{_bindir}/cx18-ctl
%{_bindir}/dvb*
%{_bindir}/ivtv-ctl
%{_mandir}/man1/dvb*.1*

%files -n rc-tools
%dir %{_sysconfdir}/rc_keymaps
%config(noreplace) %{_sysconfdir}/rc_maps.cfg
%{_udevrulesdir}/70-infrared.rules
%{_udevrulesdir}/../rc_keymaps/*
%{_bindir}/ir-ctl
%{_bindir}/ir-keytable
%{_mandir}/man1/ir*.1*
%{_mandir}/man5/rc_keymap*.5*

%endif


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.32.0-3
- Prepare for Oreon 11 (RP1)
