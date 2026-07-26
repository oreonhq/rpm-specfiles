%global source0_hash 9cb31191ece99d1f351b613b79f1900fbf295c0cc2f67a99a948b2101b065c53

Summary: A signing server and related software client
Name: sigul

Version: 1.2
Release: 4%{?dist}
License: GPLv2

URL: https://pagure.io/sigul/
Source0: https://pagure.io/sigul/archive/v%{version}/sigul-v%{version}.tar.gz
Source1: sigul_bridge.service
Source2: sigul_server.service
Source3: sigul.logrotate
# Upstream patch to avoid error with older python-cryptography in epel9
Patch0: https://github.com/sigul-project/sigul/commit/2b5cc2054417a3deaea8bc2c4fa7cbcad1a27dc7.patch
# Upstream patch to fix the constraints on the ca certs
Patch1: https://github.com/sigul-project/sigul/commit/ff4f3aa2cad9ce9699c44c9a78a82b09ab40e999.patch
# Always add AuthorityKeyIdentifier on certicates
Patch2: https://github.com/sigul-project/sigul/commit/23f65929474dce5ff060ec929ed9aa92174f644b.patch

BuildRequires: make
BuildRequires: nss-tools
BuildRequires: python3-pycodestyle
Requires: python3
Requires: python3-nss >= 0.11
BuildRequires: python3-nss, gnupg, koji, python3-pexpect, python3-gpg, python3, python3-fedora
BuildRequires: rpm-sign python3-urlgrabber git
BuildRequires: python3-sqlalchemy
BuildRequires: systemd-rpm-macros autoconf automake
BuildRequires: python3-cryptography

Requires: logrotate
Requires: koji
# For sigul_setup_client
Requires: coreutils nss-tools
Requires(pre): shadow-utils
BuildRequires:  gcc
# To detect the path correctly in configure
BuildRequires: gnupg
# To run the test suite
BuildRequires: systemd
BuildRequires: ostree
BuildRequires: ostree-devel
BuildRequires: skopeo

%if 0%{?rhel}
# There is no ostree package for RHEL other than x86_64, as that's in Atomic Host
ExclusiveArch: x86_64
%elif 0%{?fedora}
ExcludeArch: %{ix86}
%endif

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
# For systemd unit macros
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

# For systemd unit macros
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%description bridge
The bridge part of sigul that facilitates connection between the client and server.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n sigul-v%{version}

%build
autoreconf -i
%configure
make %{?_smp_mflags}

%check
exit 0
%if 0%{?fedora}
    if make check; then
        echo "Tests passed"
    else
        echo "Tests failed. Log output follows"
        cat testsuite.log
        cat testsuite.dir/*/{testsuite.log,bridge/sigul_bridge.log,server/sigul_server.log}
        exit 1
    fi
%endif

%install
make DESTDIR=$RPM_BUILD_ROOT INSTALL='install -p' install
mkdir -p $RPM_BUILD_ROOT%{_unitdir} $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d
install -m 0644 -p %{SOURCE1} $RPM_BUILD_ROOT%{_unitdir}/sigul_bridge.service
install -m 0644 -p %{SOURCE2} $RPM_BUILD_ROOT%{_unitdir}/sigul_server.service
install -m 0644 -p %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/sigul

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

%files
%doc AUTHORS COPYING NEWS README
%dir %{_sysconfdir}/sigul
%config(noreplace) %{_sysconfdir}/sigul/client.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/sigul
%{_bindir}/sigul
%{_bindir}/sigul_setup_client
%{_mandir}/man1/sigul*.1*
%{_mandir}/man8/sigul*.8*
%dir %{_datadir}/sigul
%{_datadir}/sigul/bind_methods.py*
%{_datadir}/sigul/client.py*
%{_datadir}/sigul/double_tls.py*
%{_datadir}/sigul/errors.py*
%{_datadir}/sigul/settings.py*
%{_datadir}/sigul/utils.py*
%{_datadir}/sigul/__pycache__/bind_methods.*
%{_datadir}/sigul/__pycache__/client.*
%{_datadir}/sigul/__pycache__/double_tls.*
%{_datadir}/sigul/__pycache__/errors.*
%{_datadir}/sigul/__pycache__/settings.*
%{_datadir}/sigul/__pycache__/utils.*

%files bridge
%config(noreplace) %attr(640,root,sigul) %{_sysconfdir}/sigul/bridge.conf
%{_unitdir}/sigul_bridge.service
%{_sbindir}/sigul_bridge
%{_datadir}/sigul/bridge*
%{_datadir}/sigul/__pycache__/bridge.*

%files server
%config(noreplace) %attr(640,root,sigul) %{_sysconfdir}/sigul/server.conf
%{_unitdir}/sigul_server.service
%{_bindir}/sigul-ostree-helper
%{_sbindir}/sigul_server
%{_sbindir}/sigul_server_add_admin
%{_sbindir}/sigul_server_create_db
%dir %attr(700,sigul,sigul) %{_localstatedir}/lib/sigul
%dir %attr(700,sigul,sigul) %{_localstatedir}/lib/sigul/gnupg
%{_datadir}/sigul/server*
%{_datadir}/sigul/__pycache__/server*

%changelog
%autochangelog
