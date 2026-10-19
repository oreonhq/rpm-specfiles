%global source0_hash 510aa6fbe06e5c830064756bc2f554c79378a97f1fec5ed629d044f944c40a36
Name:           nss_nis
Version:        3.4
Release:        1%{?dist}
Summary:        Name Service Switch (NSS) module using NIS
License:        LicenseRef-Callaway-LGPLv2+
Url:            https://github.com/thkukuk/libnss_nis
Source0:        https://github.com/thkukuk/libnss_nis/archive/refs/tags/v%{version}.tar.gz#/nss_nis-%{version}.tar.gz
Source2:        nss_nis.conf
Conflicts:      %{name} < %{version}-%{release}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libnsl2-devel
BuildRequires:  libtirpc-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  systemd
# /oreon:deps
%description
The nss_nis Name Service Switch module uses the Network Information System (NIS)
to obtain user, group, host name, and other data.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n libnss_nis-%{version}

%build

export CFLAGS="%{optflags}"
autoreconf -fiv
%configure --libdir=%{_libdir} --includedir=%{_includedir}
%make_build
%install
%make_install
rm  %{buildroot}/%{_libdir}/libnss_nis.{a,la}
rm  %{buildroot}/%{_libdir}/libnss_nis.so
install -D -m 644 %{SOURCE2} %{buildroot}/%{_unitdir}/systemd-logind.service.d/nss_nis.conf
install -D -m 644 %{SOURCE2} %{buildroot}/%{_unitdir}/systemd-userdbd.service.d/nss_nis.conf
%oreon_autofiles main

%check

make check
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
