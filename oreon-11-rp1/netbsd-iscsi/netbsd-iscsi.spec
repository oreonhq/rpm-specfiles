%global source0_hash b49956379148b9e4facbadcc91f180a9e2869335a044f8de3f1c2f13fde7cb2d
%global _hardened_build 1
Name:           netbsd-iscsi
Version:        20111006
Release:        23%{?dist}
Summary:        User-space implementation of iSCSI target from NetBSD project
License:        LicenseRef-Callaway-BSD
URL:            http://NetBSD.org/
Source0:        http://ftp.netbsd.org/pub/pkgsrc/distfiles/netbsd-iscsi-%{version}.tar.gz
Source1:        netbsd-iscsi.service
Source2:        netbsd-iscsi.sysconfig
Patch0:         netbsd-iscsi-20111006-linux.patch
Patch1:         netbsd-iscsi-20111006-utf8.patch
Patch2:         netbsd-iscsi-20111006-allocate.patch
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
# oreon:deps
BuildRequires:  fuse-devel
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  systemd
# /oreon:deps
%description
NetBSD iSCSI is an iSCSI target following the iSCSI RFC 3720.  It is based
on the BSD-licensed Intel iSCSI reference model.  It has been tried and
tested with the Microsoft iSCSI initiator, version 1.06.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .linux
%patch -P1 -p1 -b .utf8
%patch -P2 -p1 -b .allocate

%build

CFLAGS="%{optflags} -D_FILE_OFFSET_BITS=64"
%configure --enable-shared=no
make %{?_smp_mflags} all
%install
%make_install
install -d %{buildroot}%{_sysconfdir}/sysconfig
install -pm644 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/netbsd-iscsi
install -d %{buildroot}%{_unitdir}
install -pm644 %{SOURCE1} %{buildroot}%{_unitdir}/netbsd-iscsi.service
install -d %{buildroot}%{_sysconfdir}/iscsi
install -pm644 src/etc/targets %{buildroot}%{_sysconfdir}/iscsi
%oreon_autofiles main

%post

%systemd_post netbsd-iscsi.service
%preun

%systemd_preun netbsd-iscsi.service
%postun

%systemd_postun_with_restart netbsd-iscsi.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
