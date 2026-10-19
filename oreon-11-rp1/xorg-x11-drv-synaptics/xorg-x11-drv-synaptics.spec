%global source0_hash 4d0538454c636c763731f601db0ef5164e089fc6eb0988fe6bcd53e4b5d377da
%global tarball xf86-input-synaptics
%global moduledir %(pkg-config xorg-server --variable=moduledir )
%global driverdir %{moduledir}/input
Name:           xorg-x11-drv-synaptics
Summary:        Xorg X11 Synaptics touchpad input driver
Version:        1.10.0
Release:        1%{?dist}
URL:            http://www.x.org
License:        MIT
%if 0%{?gitdate}
Source0:        https://xorg.freedesktop.org/archive/individual/driver/%{tarball}-%{version}.tar.gz
Source1:        make-git-snapshot.sh
Source2:        commitid
%else
%endif
Source3:        70-synaptics.conf
Source4:        70-touchpad-quirks.rules
ExcludeArch:    s390 s390x
Requires:       Xorg %(xserver-sdk-abi-requires ansic)
Requires:       Xorg %(xserver-sdk-abi-requires xinput)
Requires:       libevdev
Requires:       libXi libXtst
Provides:       synaptics = %{version}-%{release}
Obsoletes:      synaptics < 0.15.0
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  git-core
BuildRequires:  libX11-devel
BuildRequires:  libXi-devel
BuildRequires:  libXtst-devel
BuildRequires:  libevdev-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  systemd
BuildRequires:  xorg-x11-server-devel
BuildRequires:  xorg-x11-util-macros
# /oreon:deps
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
find $RPM_BUILD_ROOT -regex ".*\.la$" | xargs rm -f --
rm $RPM_BUILD_ROOT%{_datadir}/X11/xorg.conf.d/70-synaptics.conf
install -d $RPM_BUILD_ROOT%{_datadir}/X11/xorg.conf.d
install -m 0644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/X11/xorg.conf.d/70-synaptics.conf
install -d $RPM_BUILD_ROOT%{_udevrulesdir}
install -m 0644 %{SOURCE4} $RPM_BUILD_ROOT%{_udevrulesdir}/70-touchpad-quirks.rules
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%post

udevadm control --reload-rules || :
%postun

udevadm control --reload-rules || :
%package devel
Summary:        Xorg X11 synaptics input driver
Requires:       pkgconfig
%description devel
Development files for the Synaptics TouchPad for X.Org.

%files -f %{oreon_filedir}/main.list
%files -n xorg-x11-drv-synaptics-legacy -f %{oreon_filedir}/xorg-x11-drv-synaptics-legacy.list
%files -n xorg-x11-drv-synaptics-devel -f %{oreon_filedir}/xorg-x11-drv-synaptics-devel.list

%changelog

%autochangelog
