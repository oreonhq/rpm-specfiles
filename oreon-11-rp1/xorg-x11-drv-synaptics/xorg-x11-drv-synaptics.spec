%global source0_hash 4d0538454c636c763731f601db0ef5164e089fc6eb0988fe6bcd53e4b5d377da

%global tarball xf86-input-synaptics
%global moduledir %(pkg-config xorg-server --variable=moduledir )
%global driverdir %{moduledir}/input

#global gitdate 20160929
#global gitversion 48632211

Name:           xorg-x11-drv-synaptics
Summary:        Xorg X11 Synaptics touchpad input driver
Version:        1.10.0
Release:        4%{?gitdate:.%{gitdate}git%{gitversion}}%{?dist}
URL:            http://www.x.org
# SPDX
License:        MIT

%if 0%{?gitdate}
Source0:        %{tarball}-%{gitdate}.tar.bz2
Source1:        make-git-snapshot.sh
Source2:        commitid
%else
Source0:        https://xorg.freedesktop.org/archive/individual/driver/%{tarball}-%{version}.tar.gz
%endif
Source3:        70-synaptics.conf
Source4:        70-touchpad-quirks.rules

ExcludeArch:    s390 s390x

BuildRequires:  make
BuildRequires:  git-core
BuildRequires:  autoconf automake libtool pkgconfig
BuildRequires:  xorg-x11-server-devel >= 1.10.99.902
BuildRequires:  libX11-devel libXi-devel libXtst-devel
BuildRequires:  xorg-x11-util-macros >= 1.8.0
BuildRequires:  libevdev-devel
BuildRequires:  systemd

Requires:       Xorg %(xserver-sdk-abi-requires ansic)
Requires:       Xorg %(xserver-sdk-abi-requires xinput)
Requires:       libevdev
Requires:       libXi libXtst

Provides:       synaptics = %{version}-%{release}
Obsoletes:      synaptics < 0.15.0

%description
This package is a an empty package. For the legacy X.Org touchpad driver,
please install xorg-x11-drv-synaptics legacy.

%package legacy
Summary:        Xorg X11 synaptics input driver
Requires:       pkgconfig

%description legacy
This is the Synaptics touchpad driver for the X.Org X server. The following
touchpad models are supported:
* Synaptics
* appletouch (Post February 2005 and October 2005 Apple Aluminium Powerbooks)
* Elantech (EeePC)
* bcm5974 (Macbook Air (Jan 2008), Macbook Pro Penryn (Feb 2008), iPhone
  (2007), iPod Touch (2008)

Note that support for appletouch, elantech and bcm5974 requires the respective
kernel module.
A touchpad by default operates in compatibility mode by emulating a standard
mouse. However, by using a dedicated driver, more advanced features of the
touchpad become available.

Features:

    * Movement with adjustable, non-linear acceleration and speed.
    * Button events through short touching of the touchpad ("tapping").
    * Double-Button events through double short touching of the touchpad.
    * Dragging through short touching and holding down the finger on the
      touchpad.
    * Middle and right button events on the upper and lower corner of the
      touchpad.
    * Vertical scrolling (button four and five events) through moving the
      finger on the right side of the touchpad.
    * The up/down button sends button four/five events.
    * Horizontal scrolling (button six and seven events) through moving the
      finger on the lower side of the touchpad.
    * The multi-buttons send button four/five events, and six/seven events for
      horizontal scrolling.
    * Adjustable finger detection.
      Multifinger taps: two finger for middle button and three finger for
      right button events. (Needs hardware support. Not all models implement
      this feature.)
    * Run-time configuration using shared memory. This means you can change
      parameter settings without restarting the X server.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{tarball}-%{?gitdate:%{gitdate}}%{!?gitdate:%{version}}

git init
if [ -z "$GIT_COMMITTER_NAME" ]; then
    git config user.email "x@fedoraproject.org"
    git config user.name "Fedora X Ninjas"
fi
%if !0%{?gitdate}
git add .
git commit -a -q -m "%{version} baseline."
%endif

# Apply all the patches.
git am -p1 %{patches} < /dev/null

%build
autoreconf -v --install --force || exit 1
%configure --disable-static --disable-silent-rules
make %{?_smp_mflags}

%install
%make_install

# FIXME: Remove all libtool archives (*.la) from modules directory.  This
# should be fixed in upstream Makefile.am or whatever.
find $RPM_BUILD_ROOT -regex ".*\.la$" | xargs rm -f --

# Remove upstream synaptics.conf as we've several special fixes in ours
rm $RPM_BUILD_ROOT%{_datadir}/X11/xorg.conf.d/70-synaptics.conf

install -d $RPM_BUILD_ROOT%{_datadir}/X11/xorg.conf.d
install -m 0644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/X11/xorg.conf.d/70-synaptics.conf

install -d $RPM_BUILD_ROOT%{_udevrulesdir}
install -m 0644 %{SOURCE4} $RPM_BUILD_ROOT%{_udevrulesdir}/70-touchpad-quirks.rules

%post
udevadm control --reload-rules || :

%postun
udevadm control --reload-rules || :

# NOTE: xorg-x11-drv-synaptics is obsoleted by xorg-x11-drv-libinput.
# The main package does not have any files anymore and thus does not
# generate an rpm. xorg-x11-drv-libinput can thus easily obsolete < 1.9.0-3,
# the synaptics files are now in xorg-x11-drv-legacy only.
#
# DO NOT CHANGE THIS.
#
%files legacy
%doc README.md
%license COPYING
%{_datadir}/X11/xorg.conf.d/70-synaptics.conf
%{driverdir}/synaptics_drv.so
%{_bindir}/synclient
%{_bindir}/syndaemon
%{_mandir}/man4/synaptics.4*
%{_mandir}/man1/synclient.1*
%{_mandir}/man1/syndaemon.1*
%{_udevrulesdir}/70-touchpad-quirks.rules

%package devel
Summary:        Xorg X11 synaptics input driver
Requires:       pkgconfig

%description devel
Development files for the Synaptics TouchPad for X.Org.

%files devel
%license COPYING
%{_libdir}/pkgconfig/xorg-synaptics.pc
%dir %{_includedir}/xorg
%{_includedir}/xorg/synaptics-properties.h

%changelog
%autochangelog
