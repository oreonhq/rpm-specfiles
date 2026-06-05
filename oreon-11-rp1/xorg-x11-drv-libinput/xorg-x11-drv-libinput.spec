%global source0_hash 2524c35f196554ea11aef3bba1cf324759454e1d49f98ac026ace2f6003580e6

%global tarball xf86-input-libinput
%global moduledir %(pkg-config xorg-server --variable=moduledir )
%global driverdir %{moduledir}/input

#define gitdate 20160929
%global gitversion 66c997886

Summary:    Xorg X11 libinput input driver
Name:       xorg-x11-drv-libinput
Version:    1.5.0
Release:    4%{?gitdate:.%{gitdate}git%{gitversion}}%{?dist}
URL:        http://www.x.org
# SPDX
License:    MIT

%if 0%{?gitdate}
Source0:        xf86-input-libinput-1.5.0.tar.xz
%else
Source0:        xf86-input-libinput-1.5.0.tar.xz
%endif
Source1:        71-libinput-overrides-wacom.conf
Source30:        xserver-sdk-abi-requires

# Fedora-only hack for hidpi screens
# https://bugzilla.redhat.com/show_bug.cgi?id=1413306
Patch01:    0001-Add-a-DPIScaleFactor-option-as-temporary-solution-to.patch

BuildRequires: make
BuildRequires: autoconf automake libtool
BuildRequires: xorg-x11-server-devel >= 1.14.0
BuildRequires: libudev-devel libevdev-devel libinput-devel >= 0.6.0-3
BuildRequires: xorg-x11-util-macros

Requires: Xorg %(sh %{SOURCE30} ansic)
Requires: Xorg %(sh %{SOURCE30} xinput)
Requires: xkeyboard-config
Requires: libinput >= 0.21.0

Provides: xorg-x11-drv-synaptics = 1.9.0-3
Obsoletes: xorg-x11-drv-synaptics < 1.9.0-3

%description
A generic input driver for the X.Org X11 X server based on libinput,
supporting all devices.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p 1 -n %{tarball}-%{?gitdate:%{gitdate}}%{!?gitdate:%{version}}

%build
autoreconf --force -v --install || exit 1
%configure --disable-static --disable-silent-rules
make %{?_smp_mflags}

%install
%make_install

# FIXME: Remove all libtool archives (*.la) from modules directory.  This
# should be fixed in upstream Makefile.am or whatever.
find $RPM_BUILD_ROOT -regex ".*\.la$" | xargs rm -f --

cp %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/X11/xorg.conf.d/

%files
%doc COPYING
%{driverdir}/libinput_drv.so
%{_datadir}/X11/xorg.conf.d/40-libinput.conf
%{_datadir}/X11/xorg.conf.d/71-libinput-overrides-wacom.conf
%{_mandir}/man4/libinput.4*

%package devel
Summary:        Xorg X11 libinput input driver development package.
Requires:       pkgconfig
%description devel
Xorg X11 libinput input driver development files.

%files devel
%doc COPYING
%{_libdir}/pkgconfig/xorg-libinput.pc
%dir %{_includedir}/xorg/
%{_includedir}/xorg/libinput-properties.h


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.5.0-4
- Import
