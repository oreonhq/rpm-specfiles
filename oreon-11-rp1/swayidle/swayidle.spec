%global source2_hash 42ad6b1bb877e1d8e3dffd101431468573e3678d0a89efff08da8383d6efa16f
%global source0_hash 6c1b769038b60250c88e47380cbb021cfa57a65f872bf4d6c340b5e3057096ac
Name: swayidle
Version: 1.9.0
Release:        1%{?dist}
Summary:        An idle daemon for wayland compositors
License: LicenseRef-Callaway-MIT AND LicenseRef-Callaway-LGPLv2+
URL: https://github.com/swaywm/swayidle
Source0:        https://github.com/swaywm/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1: %{url}/releases/download/%{version}/%{name}-%{version}.tar.gz.sig
Source2: https://emersion.fr/.well-known/openpgpkey/hu/dj3498u4hyyarh35rkjfnghbjxug6b19#/gpgkey-0FDE7BE0E88F5E48.gpg
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  meson
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  scdoc
# /oreon:deps
%description
swayidle is an idle management daemon for Wayland compositors.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build

%meson
%meson_build
%install
%meson_install
%oreon_autofiles main

%check

%meson_test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
