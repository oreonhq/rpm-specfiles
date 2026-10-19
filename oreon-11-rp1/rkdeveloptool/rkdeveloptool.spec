%global source0_hash 1832278c986918c38aefb04fad56e2b90a0c984c0df2caefb4070a13d8b51793
Name:          rkdeveloptool
Version:       1.32
Release:        1%{?dist}
Summary:        A simple way to read/write Rock Chips rockusb devices
License:       GPL-2.0-only
URL:           http://opensource.rock-chips.com/wiki_Rkdeveloptool
Source0:        %{name}-%{version}.tar.xz
Source1:       99-rkdeveloptool.rules
Patch0:        rkdeveloptool-gcc-fixes.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libusbx-devel
BuildRequires:  make
BuildRequires:  systemd-devel
# /oreon:deps
%description
A simple way to read/write rockusb devices for flashing firmware to Rock Chips
SoC based devices such as those based on the rk3399/3368/3328/3288 etc.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

NOCONFIGURE=1 autoreconf -vif
%configure
%make_build
%install
%make_install
install -D -m 644 %{SOURCE1} %{buildroot}%{_udevrulesdir}/99-rkdeveloptool.rules
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
