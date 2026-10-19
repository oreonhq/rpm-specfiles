%global source0_hash 25c12d93d53988f3caf9965236ed379f167abde3ea4cc633b134ee6254d87ca1
%bcond scons_quirk 1
%if %{without scons_quirk}
%global scons scons
%else
%global scons scons-3
%endif
Summary:        Free firewire audio driver library
Name:           libffado
Version:        2.5.0
Release:        1%{?dist}
License:        GPL-2.0-only OR GPL-3.0-only
URL:            http://www.ffado.org/
Source0:        http://www.ffado.org/files/%{name}-%{version}.tgz
Source9:        libffado-snapshot.sh
Patch0:         libffado-2.4.4-no-test-apps.patch
Patch1:         libffado-2.4.4-icon-name.patch
Patch2:         libffado-2.4.4-scons-quirk.patch
%if %{without scons_quirk}
%else
%endif
ExcludeArch:    s390 s390x
# oreon:deps
BuildRequires:  alsa-lib-devel
BuildRequires:  dbus-c++-devel
BuildRequires:  dbus-devel
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  glibmm24-devel
BuildRequires:  graphviz
BuildRequires:  libappstream-glib
BuildRequires:  libconfig-devel
BuildRequires:  libiec61883-devel
BuildRequires:  libraw1394-devel
BuildRequires:  libxml++-devel
BuildRequires:  pkgconfig
BuildRequires:  python3-dbus
BuildRequires:  python3-devel
BuildRequires:  python3-qt5-devel
BuildRequires:  python3-rpm-macros
BuildRequires:  python3-scons
BuildRequires:  python3dist(setuptools)
BuildRequires:  rpm_macro(py3_shebang_fix)
# /oreon:deps
%description
The FFADO project aims to provide a generic, open-source solution for the
support of FireWire based audio devices for the Linux platform. It is the
successor of the FreeBoB project.

%package devel
Summary:        Free firewire audio driver library development headers
License:        GPL-2.0-only OR GPL-3.0-only
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
Development files needed to build applications against libffado.

%package -n ffado
Summary:        Free firewire audio driver library applications and utilities
License:        GPL-3.0-only AND GPL-3.0-or-later AND ( GPL-2.0-only OR GPL-3.0-only )
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       dbus
Requires:       python3-dbus
Requires:       python3-qt5
%description -n ffado
Applications and utilities for use with libffado.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -N
%patch -P0 -p1 -b .no-test-apps
%patch -P1 -p1 -b .icon-name
%if %{with scons_quirk}
%patch -P2 -p1 -b .scons-quirk
%endif

# Fix Python shebangs
%py3_shebang_fix \
    admin/*.py doc/SConscript tests/python/*.py tests/*.py \
    support/mixer-qt4/ffado-mixer* support/mixer-qt4/SConscript \
    support/tools/*.py support/tools/SConscript

%build

export CFLAGS="%{optflags} -ffast-math"
export CXXFLAGS="%{optflags} -ffast-math --std=gnu++11"
export LDFLAGS="%{build_ldflags}"
%{scons} %{?_smp_mflags} \
      DETECT_USERSPACE_ENV=False \
      ENABLE_SETBUFFERSIZE_API_VER=True \
      ENABLE_OPTIMIZATIONS=False \
      CUSTOM_ENV=True \
      BUILD_DOC=user \
      PREFIX=%{_prefix} \
      LIBDIR=%{_libdir} \
      MANDIR=%{_mandir} \
      UDEVDIR=%{_prefix}/lib/udev/rules.d/ \
      PYPKGDIR=%{python3_sitelib}/ffado/ \
      PYTHON_INTERPRETER=/usr/bin/python3 \
      BUILD_TESTS=1
%install
export CFLAGS="%{optflags} -ffast-math"
export CXXFLAGS="%{optflags} -ffast-math --std=gnu++11"
export LDFLAGS="%{build_ldflags}"
%{scons} DESTDIR=%{buildroot} PREFIX=%{_prefix}\
      install
install -m 755 tests/ffado-test %{buildroot}%{_bindir}
%ldconfig_scriptlets
%oreon_autofiles ffado usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n libffado-devel -f %{oreon_filedir}/libffado-devel.list
%files -n ffado -f %{oreon_filedir}/ffado.list

%changelog

%autochangelog

