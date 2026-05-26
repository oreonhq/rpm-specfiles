%global tarball xf86-video-dummy
%global moduledir %(pkg-config xorg-server --variable=moduledir )
%global driverdir %{moduledir}/drivers

%undefine _hardened_build

Summary:   Xorg X11 dummy video driver
Name:      xorg-x11-drv-dummy
Version:   0.4.1
Release:   8%{?dist}
URL:       http://www.x.org
License:   MIT AND X11

Source0:   https://xorg.freedesktop.org/archive/individual/driver/%{tarball}-%{version}.tar.xz
# oreon url source checksums begin
%global source0_sha256 351920a7fd0f759a3ac972a5999b3ffed46f07fb52a99f319bfb5b6a59d3dfaf
%global source0_file xf86-video-dummy-0.4.1.tar.xz
# oreon url source checksums end

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(xorg-server) >= 1.4.99.901

Requires: Xorg %(xserver-sdk-abi-requires ansic)
Requires: Xorg %(xserver-sdk-abi-requires videodrv)

%description 
X.Org X11 dummy video driver.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/xf86-video-dummy-0.4.1.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "351920a7fd0f759a3ac972a5999b3ffed46f07fb52a99f319bfb5b6a59d3dfaf" || { echo "oreon: Source0 SHA256 mismatch for xf86-video-dummy-0.4.1.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n %{tarball}-%{version}

%build
autoreconf -vif
%configure --disable-static
%make_build

%install
%make_install

find %{buildroot} -name "*.la" -delete

%files
%doc README.md
%{driverdir}/dummy_drv.so

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.4.1-8
- Import
