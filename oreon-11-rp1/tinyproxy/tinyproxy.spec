%global source0_hash f05644fdf1211ba13754a354bebed909b5b39371b12cce8563c46929a75bedf6
%global _distro_extra_cflags -DNDEBUG
Name:           tinyproxy
Version:        1.11.3
Release:        1%{?dist}
Summary:        A small, efficient HTTP/SSL proxy daemon
License:        GPL-2.0-or-later
URL:            https://tinyproxy.github.io/
Source0:        https://github.com/tinyproxy/tinyproxy/releases/download/%{version}/tinyproxy-%{version}.tar.xz
Source1:        tinyproxy.service
Patch0:         0001-reqs-fix-integer-overflow-in-port-number-processing.patch
# oreon:deps
BuildRequires:  asciidoc
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
tinyproxy is a small, efficient HTTP/SSL proxy daemon that is very useful in a
small network setting, where a larger proxy like Squid would either be too
resource intensive, or a security risk.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1
sed -e '/^User / s/nobody/tinyproxy/' \
    -e '/^Group / s/nobody/tinyproxy/' \
    -i etc/tinyproxy.conf.in

%build

%configure \
    --enable-reverse \
    --enable-transparent
%make_build
%install
%make_install
install -p -D -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/tinyproxy.service
%oreon_autofiles main

%pre

getent group tinyproxy &> /dev/null || \
groupadd -r tinyproxy &> /dev/null
getent passwd tinyproxy &> /dev/null || \
useradd -r -g tinyproxy -d %{_datadir}/tinyproxy -s /sbin/nologin -c 'tinyproxy user' tinyproxy &> /dev/null
exit 0
%post

%systemd_post tinyproxy.service
%preun

%systemd_preun tinyproxy.service
%postun

%systemd_postun_with_restart tinyproxy.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
