%global tarball xf86-video-qxl
%global moduledir %(pkg-config xorg-server --variable=moduledir )
%global driverdir %{moduledir}/drivers

%undefine _hardened_build

# Xspice is x86_64 and ARM only since spice-server is x86_64 / ARM only
%ifarch %{ix86} x86_64 %{arm} aarch64
%define with_xspice 1
%else
%define with_xspice 0
%endif

Summary:    Xorg X11 qxl video driver
Name:       xorg-x11-drv-qxl
Version:    0.1.6
Release:    9%{?dist}
URL:        http://www.x.org
License:    MIT

Source0:    http://xorg.freedesktop.org/releases/individual/driver/%{tarball}-%{version}.tar.xz
Patch1:     0001-worst-hack-of-all-time-to-qxl-driver.patch
# This shebang patch is currently downstream-only
Patch2:     0005-Xspice-Adjust-shebang-to-explicitly-mention-python3.patch
# oreon url source checksums begin
%global source0_sha256 2ad39558db47a8fcc036e290e0b084671e58d43344a57b279abd870c4c67965f
%global source0_file xf86-video-qxl-0.1.6.tar.xz
# oreon url source checksums end

ExcludeArch: s390 s390x

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  libtool
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libdrm) >= 2.4.46
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(xfont2)
BuildRequires:  pkgconfig(xorg-server) >= 1.0.99.901
BuildRequires:  pkgconfig(pciaccess) >= 0.10
BuildRequires:  pkgconfig(spice-protocol) >= 0.12.0
%if %{with_xspice}
BuildRequires:  pkgconfig(libcacard)
BuildRequires:  pkgconfig(libpcsclite)
BuildRequires:  pkgconfig(spice-server) >= 0.6.3
%endif

Requires: Xorg %(xserver-sdk-abi-requires ansic)
Requires: Xorg %(xserver-sdk-abi-requires videodrv)

%description
X.Org X11 qxl video driver.

%if %{with_xspice}
%package -n     xorg-x11-server-Xspice
Summary:        XSpice is an X server that can be accessed by a Spice client
Requires:       Xorg %(xserver-sdk-abi-requires ansic)
Requires:       Xorg %(xserver-sdk-abi-requires videodrv)
Requires:       xorg-x11-server-Xorg
Requires:       pcsc-lite-ccid

%description -n xorg-x11-server-Xspice
XSpice is both an X and a Spice server.
%endif

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/xf86-video-qxl-0.1.6.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "2ad39558db47a8fcc036e290e0b084671e58d43344a57b279abd870c4c67965f" || { echo "oreon: Source0 SHA256 mismatch for xf86-video-qxl-0.1.6.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -S git_am -n %{tarball}-%{version}

%build
autoreconf -vif
%if %{with_xspice}
%define enable_xspice --enable-ccid --enable-xspice
%endif
%configure --disable-static %{?enable_xspice}
%make_build

%install
%make_install

find %{buildroot} -name "*.la" -delete
rm -f %{buildroot}/usr/share/doc/xf86-video-qxl/spiceqxl.xorg.conf.example

%if %{with_xspice}
mkdir -p %{buildroot}%{_sysconfdir}/X11
install -p -m 644 examples/spiceqxl.xorg.conf.example \
    %{buildroot}%{_sysconfdir}/X11/spiceqxl.xorg.conf
%endif


%files
%doc COPYING README.md
%{driverdir}/qxl_drv.so

%if %{with_xspice}
%files -n xorg-x11-server-Xspice
%doc COPYING README.xspice README.md examples/spiceqxl.xorg.conf.example
%config(noreplace) %{_sysconfdir}/X11/spiceqxl.xorg.conf
%{_bindir}/Xspice
%{driverdir}/spiceqxl_drv.so
%{_libdir}/pcsc/drivers/serial/libspiceccid.so*
%endif


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.1.6-9
- Import
