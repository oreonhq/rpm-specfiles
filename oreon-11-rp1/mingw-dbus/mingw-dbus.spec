%global source0_hash 0ba2a1a4b16afe7bceb2c07e9ce99a8c2c3508e5dec290dbb643384bd6beb7e2

%{?mingw_package_header}

Name:           mingw-dbus
Version:        1.16.2
Release:        2%{?dist}
Summary:        MinGW Windows port of D-Bus

# The effective license of the majority of the package, including the shared
# library, is "GPL-2+ or AFL-2.1". Certain utilities are "GPL-2+" only.
License: (AFL-2.1 OR GPL-2.0-or-later) AND GPL-2.0-or-later
URL:            http://www.freedesktop.org/wiki/Software/dbus
Source0:        http://dbus.freedesktop.org/releases/dbus/dbus-%{version}.tar.xz

# Restore support for static libs
Patch0:         dbus-static-libs.patch

BuildArch:      noarch

BuildRequires:  cmake

BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-glib2
BuildRequires:  mingw32-expat

BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-glib2
BuildRequires:  mingw64-expat

%description
D-BUS is a system for sending messages between applications. It is
used both for the system wide message bus service, and as a
per-user-login-session messaging facility.

# Win32
%package -n mingw32-dbus
Summary:        MinGW Windows port of D-Bus
Requires:       pkgconfig

%description -n mingw32-dbus
D-BUS is a system for sending messages between applications. It is
used both for the system wide message bus service, and as a
per-user-login-session messaging facility.

%package -n mingw32-dbus-static
Summary:        Static version of MinGW Windows port of DBus library
Requires:       mingw32-dbus = %{version}-%{release}

%description -n mingw32-dbus-static
D-BUS is a system for sending messages between applications. It is
used both for the system wide message bus service, and as a
per-user-login-session messaging facility.

Static version of MinGW Windows port of DBus library

# Win64
%package -n mingw64-dbus
Summary:        MinGW Windows port of D-Bus
Requires:       pkgconfig

%description -n mingw64-dbus
D-BUS is a system for sending messages between applications. It is
used both for the system wide message bus service, and as a
per-user-login-session messaging facility.

%package -n mingw64-dbus-static
Summary:        Static version of MinGW Windows port of DBus library
Requires:       mingw64-dbus = %{version}-%{release}

%description -n mingw64-dbus-static
D-BUS is a system for sending messages between applications. It is
used both for the system wide message bus service, and as a
per-user-login-session messaging facility.

Static version of MinGW Windows port of DBus library

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n dbus-%{version}

%build
MINGW_BUILDDIR_SUFFIX=static %mingw_cmake -DDBUS_ENABLE_DOXYGEN_DOCS=OFF -DENABLE_QT_HELP=OFF -DBUILD_SHARED_LIBS=OFF
MINGW_BUILDDIR_SUFFIX=static %mingw_make_build

MINGW_BUILDDIR_SUFFIX=shared %mingw_cmake -DDBUS_ENABLE_DOXYGEN_DOCS=OFF -DENABLE_QT_HELP=OFF
MINGW_BUILDDIR_SUFFIX=shared %mingw_make_build

%install
MINGW_BUILDDIR_SUFFIX=static %mingw_make_install
MINGW_BUILDDIR_SUFFIX=shared %mingw_make_install

# Remove manpages because they duplicate what's in the
# Fedora native package already.
rm -rf %{buildroot}%{mingw32_datadir}/doc
rm -rf %{buildroot}%{mingw64_datadir}/doc
rm -rf %{buildroot}%{mingw32_datadir}/xml
rm -rf %{buildroot}%{mingw64_datadir}/xml

# Win32
%files -n mingw32-dbus
%license COPYING
%{mingw32_bindir}/dbus-daemon.exe
%{mingw32_bindir}/dbus-env.bat
%{mingw32_bindir}/dbus-launch.exe
%{mingw32_bindir}/dbus-monitor.exe
%{mingw32_bindir}/dbus-run-session.exe
%{mingw32_bindir}/dbus-send.exe
%{mingw32_bindir}/dbus-test-tool.exe
%{mingw32_bindir}/dbus-update-activation-environment.exe
%{mingw32_bindir}/libdbus-1-3.dll
%{mingw32_libdir}/dbus-1.0/
%{mingw32_libdir}/libdbus-1.dll.a
%{mingw32_libdir}/cmake/DBus1/
%{mingw32_libdir}/pkgconfig/dbus-1.pc
%{mingw32_sysconfdir}/dbus-1/
%{mingw32_includedir}/dbus-1.0/
%{mingw32_datadir}/dbus-1/

%files -n mingw32-dbus-static
%{mingw32_libdir}/libdbus-1.a

# Win64
%files -n mingw64-dbus
%license COPYING
%{mingw64_bindir}/dbus-daemon.exe
%{mingw64_bindir}/dbus-env.bat
%{mingw64_bindir}/dbus-launch.exe
%{mingw64_bindir}/dbus-monitor.exe
%{mingw64_bindir}/dbus-run-session.exe
%{mingw64_bindir}/dbus-send.exe
%{mingw64_bindir}/dbus-test-tool.exe
%{mingw64_bindir}/dbus-update-activation-environment.exe
%{mingw64_bindir}/libdbus-1-3.dll
%{mingw64_libdir}/dbus-1.0/
%{mingw64_libdir}/libdbus-1.dll.a
%{mingw64_libdir}/cmake/DBus1/
%{mingw64_libdir}/pkgconfig/dbus-1.pc
%{mingw64_sysconfdir}/dbus-1/
%{mingw64_includedir}/dbus-1.0/
%{mingw64_datadir}/dbus-1/

%files -n mingw64-dbus-static
%{mingw64_libdir}/libdbus-1.a

%changelog
%autochangelog
