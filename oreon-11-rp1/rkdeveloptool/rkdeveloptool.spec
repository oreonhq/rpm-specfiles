%global source0_hash 1832278c986918c38aefb04fad56e2b90a0c984c0df2caefb4070a13d8b51793

Name:          rkdeveloptool
Version:       1.32
Release:       13%{?dist}
Summary:       A simple way to read/write Rock Chips rockusb devices
License:       GPL-2.0-only
URL:           http://opensource.rock-chips.com/wiki_Rkdeveloptool
# Upstream doesn't currently push the release tags, upstream issue filed
# https://github.com/rockchip-linux/rkdeveloptool/issues/36
# git archive --format=tar --prefix=%{name}-%{version}/ 46bb4c0 | xz > ~/%{name}-%{version}.tar.xz
Source0:       %{name}-%{version}.tar.xz
# Source0:       https://github.com/rockchip-linux/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# https://build.opensuse.org/package/view_file/hardware/rkdeveloptool/99-rkdeveloptool.rules
Source1:       99-rkdeveloptool.rules
# https://github.com/rockchip-linux/rkdeveloptool/pull/57
Patch0:        rkdeveloptool-gcc-fixes.patch

BuildRequires: make
BuildRequires: autoconf automake
BuildRequires: gcc-c++
BuildRequires: libusbx-devel
BuildRequires: systemd-devel

%description
A simple way to read/write rockusb devices for flashing firmware to Rock Chips
SoC based devices such as those based on the rk3399/3368/3328/3288 etc.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
NOCONFIGURE=1 autoreconf -vif
%configure

%make_build

%install
%make_install
install -D -m 644 %{SOURCE1} %{buildroot}%{_udevrulesdir}/99-rkdeveloptool.rules

%files
%license license.txt
%doc Readme.txt
%{_bindir}/rkdeveloptool
%{_udevrulesdir}/99-rkdeveloptool.rules

%changelog
%autochangelog
