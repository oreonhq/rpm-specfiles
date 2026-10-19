%global source0_hash a5d03435f0ef48bf3d5010e63d9264f2334e7063cba3ecd8d4c0a15616a4f712
Name:           xorgxrdp
Version:        0.10.5
Release:        1%{?dist}
Summary:        Implementation of xrdp backend as Xorg modules
License:        MIT
URL:            https://github.com/neutrinolabs/xorgxrdp
Source0:        https://github.com/neutrinolabs/xorgxrdp/releases/download/v%{version}/%{name}-%{version}.tar.gz
%if 0%{?fedora} >= 35 || 0%{?rhel} >= 8 || 0%{?oreon} >= 11
Conflicts: %{name}-glamor
%endif
Requires:       xrdp >= 1:%{version}
Requires:       Xorg %(xserver-sdk-abi-requires videodrv 2>/dev/null)
Requires:       Xorg %(xserver-sdk-abi-requires xinput 2>/dev/null)
%if 0%{?fedora} >= 35 || 0%{?rhel} >= 8 || 0%{?oreon} >= 11
Requires:       xorg-x11-server-Xorg
%endif
%if 0%{?fedora} >= 35 || 0%{?rhel} >= 8 || 0%{?oreon} >= 11
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libXfont2-devel
BuildRequires:  libdrm-devel
BuildRequires:  libepoxy-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  mesa-libgbm-devel
BuildRequires:  nasm
BuildRequires:  xorg-x11-server-Xorg
BuildRequires:  xorg-x11-server-devel
BuildRequires:  xrdp-devel
# /oreon:deps
%package glamor
Summary:        Implementation of xrdp backend as Xorg modules with glamor
RemovePathPostfixes: .glamor
Conflicts: %{name}
Requires:       xrdp >= 1:%{version}
Requires:       Xorg %(xserver-sdk-abi-requires videodrv 2>/dev/null)
Requires:       Xorg %(xserver-sdk-abi-requires xinput 2>/dev/null)
Requires:       xorg-x11-server-Xorg
%endif
%description
xorgxrdp is a set of X11 modules that make Xorg act as a backend for
xrdp. Xorg with xorgxrdp is the most advanced xrdp backend with support
for screen resizing and multiple monitors.

%if 0%{?fedora} >= 35 || 0%{?rhel} >= 8 || 0%{?oreon} >= 11
%description glamor
xorgxrdp is a set of X11 modules that make Xorg act as a backend for
xrdp. Xorg with xorgxrdp is the most advanced xrdp backend with support
for screen resizing and multiple monitors. Built with glamor support.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf -i
%if 0%{?fedora} >= 35 || 0%{?rhel} >= 8 || 0%{?oreon} >= 11
CFLAGS="$RPM_OPT_FLAGS -I/usr/include/libdrm" \
%configure --enable-glamor
%make_build
%{__mv} xrdpdev/.libs/xrdpdev_drv.so xrdpdev_drv.so.glamor
%{__mv} xrdpkeyb/.libs/xrdpkeyb_drv.so xrdpkeyb_drv.so.glamor
%{__mv} xrdpmouse/.libs/xrdpmouse_drv.so xrdpmouse_drv.so.glamor
%{__mv} module/.libs/libxorgxrdp.so libxorgxrdp.so.glamor
%{__make} clean
%endif
%configure
%make_build
%install
%make_install
%if 0%{?fedora} >= 35 || 0%{?rhel} >= 8 || 0%{?oreon} >= 11
%{__install} -p xrdpdev_drv.so.glamor %{buildroot}%{_libdir}/xorg/modules/drivers
%{__install} -p xrdpkeyb_drv.so.glamor %{buildroot}%{_libdir}/xorg/modules/input
%{__install} -p xrdpmouse_drv.so.glamor %{buildroot}%{_libdir}/xorg/modules/input
%{__install} -p libxorgxrdp.so.glamor %{buildroot}%{_libdir}/xorg/modules
%{__sed} '/^[[:blank:]]*Load "xorgxrdp"/i\    Load "glamoregl"' \
         %{buildroot}%{_sysconfdir}/X11/xrdp/xorg.conf > \
         %{buildroot}%{_sysconfdir}/X11/xrdp/xorg.conf.glamor
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%endif
%files -f %{oreon_filedir}/main.list
%files -n xorgxrdp-glamor -f %{oreon_filedir}/xorgxrdp-glamor.list

%changelog

%autochangelog
