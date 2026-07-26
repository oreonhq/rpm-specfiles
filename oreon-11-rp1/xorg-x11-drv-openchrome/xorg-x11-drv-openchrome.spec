%global source0_hash c307fad3a2157ab36e78fdf098f1d999978436bc3a9e813d3cf1adb30838760e

%global commit0 857d892b668b4737d41ef1b7f58fd45eac84d552
%global date 20230328
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
#global tag %{version}

%define tarball xf86-video-openchrome
%define moduledir %(pkg-config xorg-server --variable=moduledir )
%define driverdir %{moduledir}/drivers

%if 0%{?fedora}
%define with_xvmc 0
%else
%define with_xvmc 1
%endif

%undefine _hardened_build

Summary:        Xorg X11 openchrome video driver
Name:           xorg-x11-drv-openchrome
Version:        0.6.604%{!?tag:^%{date}git%{shortcommit0}}
Release:        4%{?dist}
URL:            http://www.freedesktop.org/wiki/Openchrome/
License:        MIT

%if 0%{?tag:1}
Source0:        http://xorg.freedesktop.org/archive/individual/driver/%{tarball}-%{version}.tar.bz2
%else
Source0:        %{tarball}-%{shortcommit0}.tar.bz2
%endif
Source1:        make-git-snapshot.sh

ExclusiveArch:  %{ix86} x86_64

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  mesa-libGL-devel
BuildRequires:  pkgconfig(libdrm) >= 2.2
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(pciaccess) >= 0.8.0
BuildRequires:  pkgconfig(xorg-server)
%if %{with_xvmc}
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xvmc)
%endif

Requires:       Xorg %(xserver-sdk-abi-requires ansic)
Requires:       Xorg %(xserver-sdk-abi-requires videodrv)
Requires:       xorg-x11-server-wrapper

Obsoletes:      %{name}-devel < %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}

%description
X.Org X11 openchrome video driver.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if 0%{?tag:1}
%autosetup -p1 -n %{tarball}-%{version}
%else
%autosetup -p1 -n %{tarball}-%{commit0}
%endif

%build
autoreconf -vif
%configure --disable-static --enable-viaregtool
%make_build

%install
%make_install
find %{buildroot} -name "*.la" -delete
# Remove unversioned XvMC libraries
rm -f %{buildroot}%{_libdir}/libchromeXvMC*.so

%files
%doc NEWS README
%license COPYING
%{driverdir}/openchrome_drv.so
%if %{with_xvmc}
%{_libdir}/libchromeXvMC.so.1
%{_libdir}/libchromeXvMC.so.1.0.0
%{_libdir}/libchromeXvMCPro.so.1
%{_libdir}/libchromeXvMCPro.so.1.0.0
%endif
%{_mandir}/man4/openchrome.4.gz
%{_sbindir}/via_regs_dump

%changelog
%autochangelog
