%global source0_hash d465366682af8feb8618283c9789e8b70db6fd17ca8fa950ac6f710102315a81
Name:          mate-sensors-applet
Version:       1.28.0
Release:        1%{?dist}
Summary:        MATE panel applet for hardware sensors
License:       GPL-2.0-or-later
URL:           http://mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/1.28/%{name}-%{version}.tar.xz
Patch1:        mate-sensors-applet_0001-Fix-an-invalid-pointer-crash-with-glib-2.83.2.patch
Requires:      hddtemp
# oreon:deps
BuildRequires:  gtk3-devel
BuildRequires:  libXNVCtrl-devel
BuildRequires:  libnotify-devel
BuildRequires:  lm_sensors-devel
BuildRequires:  make
BuildRequires:  mate-common
BuildRequires:  mate-panel-devel
# /oreon:deps
%description
MATE Sensors Applet is an applet for the MATE Panel to display readings
from hardware sensors, including CPU and system temperatures, fan speeds
and voltage readings under Linux.
Can interface via the Linux kernel i2c modules, or the i8k kernel modules
Includes a simple, yet highly customization display and intuitive 
user-interface.
Alarms can be set for each sensor to notify the user once a certain value
has been reached, and can be configured to execute a given command at given
repeated intervals.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The mate-sensors-applet-devel package contains libraries and header files for
developing applications that use mate-sensors-applet.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure \
    --disable-static \
    --disable-schemas-compile \
    --enable-in-process \
    --enable-libnotify \
    --with-nvidia
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
make %{?_smp_mflags}
%install
%{make_install}
find $RPM_BUILD_ROOT -name "*.la" -exec rm -rf {} ';'
%find_lang %{name} --with-gnome --all-name
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n mate-sensors-applet-devel -f %{oreon_filedir}/mate-sensors-applet-devel.list

%changelog

%autochangelog
