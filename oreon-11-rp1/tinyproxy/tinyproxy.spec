%global source0_hash 6a126880706691c987e2957b1c99b522efb1964a75eb767af4b30aac0b88a26a

# must be set to avoid noisy memory debug logging rhbz#1011783
%global _distro_extra_cflags -DNDEBUG

Name:           tinyproxy
Version:        1.11.2
Release:        6%{?dist}
Summary:        A small, efficient HTTP/SSL proxy daemon
License:        GPL-2.0-or-later
URL:            https://tinyproxy.github.io/
Source0:        https://github.com/tinyproxy/tinyproxy/releases/download/%{version}/tinyproxy-%{version}.tar.xz
Source1:        tinyproxy.service
# CVE-2025-63938
# https://github.com/tinyproxy/tinyproxy/commit/3c0fde94981b025271ffa1788ae425257841bf5a
Patch0:         0001-reqs-fix-integer-overflow-in-port-number-processing.patch

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  asciidoc
BuildRequires:  systemd-rpm-macros

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

%files
%license COPYING
%{_pkgdocdir}
%{_bindir}/tinyproxy
%{_mandir}/man8/tinyproxy.8*
%{_mandir}/man5/tinyproxy.conf.5*
%{_unitdir}/tinyproxy.service
%{_datadir}/tinyproxy
%dir %{_sysconfdir}/tinyproxy
%config(noreplace) %{_sysconfdir}/tinyproxy/tinyproxy.conf

%changelog
%autochangelog
