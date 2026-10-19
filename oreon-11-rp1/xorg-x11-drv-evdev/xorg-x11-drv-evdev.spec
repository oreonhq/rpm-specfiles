%global source0_hash 730022de934cc366bb12439daf202a7bfff52a028cf4573e457642e25a071315
%global tarball xf86-input-evdev
%global moduledir %(pkg-config xorg-server --variable=moduledir )
%global driverdir %{moduledir}/input
%global gitversion 66c997886
Summary:        Xorg X11 evdev input driver
Name:       xorg-x11-drv-evdev
Version:    2.11.0
Release:        1%{?dist}
URL:        http://www.x.org
License:    HPND-sell-variant AND MIT
%if 0%{?gitdate}
Source0:        https://www.x.org/pub/individual/driver/%{tarball}-%{version}.tar.xz
Source1:    make-git-snapshot.sh
Source2:    commitid
%else
Source30:   xserver-sdk-abi-requires
%endif
Requires: Xorg %(sh %{SOURCE30} ansic)
Requires: Xorg %(sh %{SOURCE30} xinput)
Requires:  xkeyboard-config >= 1.4-1
Requires: mtdev
Obsoletes: xorg-x11-drv-mouse < 1.9.0-8
Obsoletes: xorg-x11-drv-keyboard < 1.8.0-6
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libevdev-devel
BuildRequires:  libtool
BuildRequires:  libudev-devel
BuildRequires:  make
BuildRequires:  mtdev-devel
BuildRequires:  xorg-x11-server-devel
BuildRequires:  xorg-x11-util-macros
# /oreon:deps
%description
X.Org X11 evdev input driver.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{tarball}-%{?gitdate:%{gitdate}}%{!?gitdate:%{version}}

%build

autoreconf --force -v --install || exit 1
%configure --disable-static --disable-silent-rules
make %{?_smp_mflags}
%install
%make_install
find $RPM_BUILD_ROOT -regex ".*\.la$" | xargs rm -f --
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%package devel
Summary:    Xorg X11 evdev input driver development package.
Requires:   pkgconfig
%description devel
X.Org X11 evdev input driver development files.

%files -f %{oreon_filedir}/main.list
%files -n xorg-x11-drv-evdev-devel -f %{oreon_filedir}/xorg-x11-drv-evdev-devel.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.11.0-4
- Import
