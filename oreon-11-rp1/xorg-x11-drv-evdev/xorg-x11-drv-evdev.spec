%global source0_hash 730022de934cc366bb12439daf202a7bfff52a028cf4573e457642e25a071315

%global tarball xf86-input-evdev
%global moduledir %(pkg-config xorg-server --variable=moduledir )
%global driverdir %{moduledir}/input

#global gitdate 20150807
%global gitversion 66c997886

Summary:    Xorg X11 evdev input driver
Name:       xorg-x11-drv-evdev
Version:    2.11.0
Release:    4%{?gitdate:.%{gitdate}git%{gitversion}}%{?dist}
URL:        http://www.x.org
License:    HPND-sell-variant AND MIT

%if 0%{?gitdate}
Source0:        https://www.x.org/pub/individual/driver/%{tarball}-%{version}.tar.xz
Source1:    make-git-snapshot.sh
Source2:    commitid
%else
Source0:        https://www.x.org/pub/individual/driver/%{tarball}-%{version}.tar.xz
Source30:   xserver-sdk-abi-requires
%endif

BuildRequires: make
BuildRequires: autoconf automake libtool
BuildRequires: xorg-x11-server-devel >= 1.10.99.902
BuildRequires: libudev-devel mtdev-devel libevdev-devel
BuildRequires: xorg-x11-util-macros >= 1.3.0

Requires: Xorg %(sh %{SOURCE30} ansic)
Requires: Xorg %(sh %{SOURCE30} xinput)
Requires:  xkeyboard-config >= 1.4-1
Requires: mtdev

Obsoletes: xorg-x11-drv-mouse < 1.9.0-8
Obsoletes: xorg-x11-drv-keyboard < 1.8.0-6

%description
X.Org X11 evdev input driver.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n %{tarball}-%{?gitdate:%{gitdate}}%{!?gitdate:%{version}}

%build
autoreconf --force -v --install || exit 1
%configure --disable-static --disable-silent-rules
make %{?_smp_mflags}

%install
%make_install

# FIXME: Remove all libtool archives (*.la) from modules directory.  This
# should be fixed in upstream Makefile.am or whatever.
find $RPM_BUILD_ROOT -regex ".*\.la$" | xargs rm -f --


%files
%doc COPYING
%{driverdir}/evdev_drv.so
%{_mandir}/man4/evdev.4*
%{_datadir}/X11/xorg.conf.d/10-evdev.conf

%package devel
Summary:    Xorg X11 evdev input driver development package.
Requires:   pkgconfig
%description devel
X.Org X11 evdev input driver development files.

%files devel
%doc COPYING
%{_libdir}/pkgconfig/xorg-evdev.pc
%dir %{_includedir}/xorg
%{_includedir}/xorg/evdev-properties.h


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.11.0-4
- Import
