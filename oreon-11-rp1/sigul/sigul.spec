%global source0_hash 9cb31191ece99d1f351b613b79f1900fbf295c0cc2f67a99a948b2101b065c53
Summary:        A signing server and related software client
Name: sigul
Version: 1.4
Release:        1%{?dist}
License: GPLv2
URL: https://pagure.io/sigul/
Source0:        https://pagure.io/sigul/archive/v%{version}/sigul-v%{version}.tar.gz
Source1: sigul_bridge.service
Source2: sigul_server.service
Source3: sigul.logrotate
Patch0: https://github.com/sigul-project/sigul/commit/2b5cc2054417a3deaea8bc2c4fa7cbcad1a27dc7.patch
Patch1: https://github.com/sigul-project/sigul/commit/ff4f3aa2cad9ce9699c44c9a78a82b09ab40e999.patch
Patch2: https://github.com/sigul-project/sigul/commit/23f65929474dce5ff060ec929ed9aa92174f644b.patch
Requires: python3
Requires: python3-nss >= 0.11
Requires: logrotate
Requires: koji
Requires: coreutils nss-tools
Requires(pre): shadow-utils
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  git
BuildRequires:  gnupg
BuildRequires:  koji
BuildRequires:  make
BuildRequires:  nss-tools
BuildRequires:  ostree
BuildRequires:  ostree-devel
BuildRequires:  python3
BuildRequires:  python3-cryptography
BuildRequires:  python3-fedora
BuildRequires:  python3-gpg
BuildRequires:  python3-nss
BuildRequires:  python3-pexpect
BuildRequires:  python3-pycodestyle
BuildRequires:  python3-sqlalchemy
BuildRequires:  python3-urlgrabber
BuildRequires:  rpm-sign
BuildRequires:  skopeo
BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
A signing server, which lets authorized users sign data without having any
access to the necessary private key, a client for the server, and a "bridge"
that connects the two.

%package server
Summary: Sigul server component
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: gnupg
Requires: python3-cryptography
Requires: python3-gpg
Requires: python3-pexpect
Requires: python3-sqlalchemy >= 0.5
Requires: python3-sqlalchemy
Requires: ostree
Requires: rpm-sign
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
%description server
The server part of sigul that keeps the keys and performs the actual signing.

%package bridge
Summary: Sigul bridge
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: python3-fedora
Requires: python3-urlgrabber
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
%description bridge
The bridge part of sigul that facilitates connection between the client and server.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir sigul-v%{version}
%oreon_prep
%build

autoreconf -i
%configure
make %{?_smp_mflags}
%check

exit 0
%install
make DESTDIR=$RPM_BUILD_ROOT INSTALL='install -p' install
mkdir -p $RPM_BUILD_ROOT%{_unitdir} $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d
install -m 0644 -p %{SOURCE1} $RPM_BUILD_ROOT%{_unitdir}/sigul_bridge.service
install -m 0644 -p %{SOURCE2} $RPM_BUILD_ROOT%{_unitdir}/sigul_server.service
install -m 0644 -p %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/sigul
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%pre

getent group sigul >/dev/null || groupadd -r sigul
getent passwd sigul >/dev/null || \
useradd -r -g sigul -d %{_localstatedir}/lib/sigul -s /sbin/nologin \
        -c "Signing server or bridge" sigul
exit 0
%post bridge

%systemd_post sigul_bridge.service
%post server

%systemd_post sigul_server.service
%preun bridge

%systemd_preun sigul_bridge.service
%preun server

%systemd_preun sigul_server.service
%postun bridge

%systemd_postun_with_restart sigul_bridge.service
%postun server

%systemd_postun_with_restart sigul_server.service
%files -f %{oreon_filedir}/main.list
%files -n sigul-server -f %{oreon_filedir}/sigul-server.list
%files -n sigul-bridge -f %{oreon_filedir}/sigul-bridge.list

%changelog

%autochangelog
