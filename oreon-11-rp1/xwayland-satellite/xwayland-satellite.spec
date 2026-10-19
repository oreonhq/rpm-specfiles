%global source0_hash cb50bb6948582d5ec3aa511d2d66ad622989bb14bef94e3bb81bae8b64c120b1
%bcond check 1
Name:           xwayland-satellite
Version:        0.8.2
Release:        1%{?dist}
Summary:        Rootless Xwayland integration for Wayland compositors
SourceLicense:  MPL-2.0
License:        %{shrink:
    MPL-2.0 AND
    Apache-2.0 AND
    BSD-2-Clause AND
    BSD-3-Clause AND
    ISC AND
    MIT AND
    Unicode-3.0 AND
    Zlib AND
    (0BSD OR MIT OR Apache-2.0) AND
    (Apache-2.0 OR MIT) AND
    (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
    (BSD-2-Clause OR Apache-2.0 OR MIT) AND
    (BSD-3-Clause OR MIT OR Apache-2.0) AND
    (MIT OR Apache-2.0 OR Zlib) AND
    (Unlicense OR MIT)
}
URL:            https://github.com/Supreeeme/xwayland-satellite
Source0:        https://github.com/Supreeeme/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        xwayland-satellite-%{version}-vendor.tar.xz
Patch:          0001-fix-executable-path-in-systemd-unit.patch
ExcludeArch:    %{ix86}
Requires:       xorg-x11-server-Xwayland
Requires:       font(opensans)
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  clang
BuildRequires:  gcc
BuildRequires:  glibc-devel
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(xcb-cursor)
BuildRequires:  rustc
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
xwayland-satellite grants rootless Xwayland integration to any Wayland
compositor implementing xdg_wm_base and viewporter. This is particularly
useful for compositors that (understandably) do not want to go through
implementing support for rootless Xwayland themselves.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n xwayland-satellite-%{version} -a1 -p1
rm OpenSans-Regular.ttf
%oreon_vendor_cargo
%build

%cargo_build -f systemd,fontconfig
%{cargo_license_summary -f systemd,fontconfig}
%{cargo_license -f systemd,fontconfig} > LICENSE.dependencies
%{cargo_vendor_manifest}
%install
install -Dpm0755 target/rpm/xwayland-satellite -t %{buildroot}%{_bindir}
install -Dpm0644 resources/xwayland-satellite.service -t %{buildroot}%{_userunitdir}
%oreon_autofiles main
%if %{with check}
%check

%cargo_test -f systemd,fontconfig -- --lib
%endif
%post

%systemd_user_post xwayland-satellite.service
%preun

%systemd_user_preun xwayland-satellite.service
%postun

%systemd_user_postun_with_reload xwayland-satellite.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
