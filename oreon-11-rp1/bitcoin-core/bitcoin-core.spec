%global source2_hash e63028d0bb33d22c847479d73866be8c1142246911765c005efbf611b645e706
%global source1_hash c22e1389b651dfa2f710345e23f3adc52d4e3b3dad8ed7977a7e29d55c55995f
%global source0_hash 50411d5b43c7e4c90099394759eb6c2add6e7c2dbe728840893d638b6fc6afc9
%define _hardened_build 1
%global _compldir %{_datadir}/bash-completion/completions
%global project_name bitcoin
%bcond_with extended_tests
Name:       bitcoin-core
Version:    31.1
Release:        1%{?dist}
Summary:        Peer to Peer Cryptographic Currency
License:    MIT
URL:        https://bitcoincore.org/
Source0:        https://%{project_name}core.org/bin/%{name}-%{version}/%{project_name}-%{version}.tar.gz
Source1:    https://bitcoincore.org/bin/%{name}-%{version}/SHA256SUMS.asc
Source2:    https://bitcoincore.org/bin/%{name}-%{version}/SHA256SUMS
Source3:    %{project_name}-gpg.sh
Source4:    %{project_name}-offline-pubring.gpg
Source5:    %{project_name}-tmpfiles.conf
Source6:    %{project_name}.sysconfig
Source7:    %{project_name}.service.system
Source8:    %{project_name}.service.user
Source9:    %{project_name}-qt.protocol
Source10:   %{project_name}-qt.desktop
Source11:   %{project_name}.sysusers.conf
Source12:   %{project_name}.conf.example
Source13:   README.gui.redhat
Source14:   README.utils.redhat
Source15:   README.server.redhat
Source18:   %{project_name}-qt.metainfo.xml
Patch0:     %{project_name}-verify-offline.patch
Patch1:     %{project_name}-shared.patch
Requires:   %{name}-desktop = %{version}-%{release}
Requires:   %{name}-server = %{version}-%{release}
Requires:   %{name}-utils = %{version}-%{release}
Requires:   lib%{project_name}kernel = %{version}-%{release}
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  capnproto
BuildRequires:  capnproto-devel
BuildRequires:  checkpolicy
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
BuildRequires:  gnupg2
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(libevent)
BuildRequires:  pkgconfig(libevent_pthreads)
BuildRequires:  pkgconfig(libqrencode)
BuildRequires:  pkgconfig(libzmq)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  procps-ng
BuildRequires:  python3
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  systemtap-sdt-devel
# /oreon:deps
%description
Bitcoin is a digital cryptographic currency that uses peer-to-peer technology to
operate with no central authority or banks; managing transactions and the
issuing of bitcoins is carried out collectively by the network.

This package installs the full Bitcoin Core distribution, with utilities, server
and desktop (graphical wallet) components.

%package -n lib%{project_name}kernel
Summary:    Consensus engine and support library
%description -n lib%{project_name}kernel
Bitcoin Core consensus engine. A stateful library that can spawn threads, do
caching, do I/O, and many other things which one may not normally expect from a
library.

%package desktop
Summary:    Peer to Peer Cryptographic Currency
Provides:   bundled(leveldb)
Provides:   bundled(libmultiprocess)
Provides:   bundled(secp256k1)
Provides:   bundled(univalue)
%description desktop
Bitcoin is a digital cryptographic currency that uses peer-to-peer technology to
operate with no central authority or banks; managing transactions and the
issuing of bitcoins is carried out collectively by the network.

This package contains the Qt based graphical client and node. If you are looking
to run a Bitcoin wallet, this is probably the package you want.

%package devel
Summary:    Peer-to-peer digital currency
Requires:   lib%{project_name}kernel = %{version}-%{release}
%description devel
This package contains the bitcoin utility tool.

Most people do not need this package installed.

%package utils
Summary:    Peer-to-peer digital currency
%description utils 
Bitcoin is an experimental new digital currency that enables instant payments to
anyone, anywhere in the world. Bitcoin uses peer-to-peer technology to operate
with no central authority: managing transactions and issuing money are carried
out collectively by the network.

This package provides bitcoin-cli, a utility to communicate with and
control a Bitcoin server via its RPC protocol, and bitcoin-tx, a utility
to create custom Bitcoin transactions.

%package server
Summary:    Peer-to-peer digital currency
Requires:   (%{name}-selinux >= 0.1 if selinux-policy)
Provides:   bundled(leveldb)
Provides:   bundled(libmultiprocess)
Provides:   bundled(secp256k1)
Provides:   bundled(univalue)
%description server
This package provides a stand-alone %{name} daemon. For most users, this
package is only needed if they need a full-node without the graphical client.

Some third party wallet software will want this package to provide the actual
%{name} node they use to connect to the network.

If you use the graphical %{name} client then you almost certainly do not
need this package.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{project_name}-%{version}

# Bundled script to verify release signatures using offline pubring:
cp %{SOURCE4} .
contrib/verify-binaries/verify.py --min-good-sigs 3 bin %{SOURCE2} %{SOURCE0}

# Check the hash of the tarball, not in the same folder where we are now:
grep -q $(sha256sum %{SOURCE0}) %{SOURCE2}

# Documentation (sources can not be directly reference with doc)
cp -p %{SOURCE12} %{SOURCE13} %{SOURCE14} %{SOURCE15} .

%build

%cmake \
    -DBUILD_CLI=ON \
    -DBUILD_DAEMON=ON \
    -DBUILD_GUI=ON \
    -DBUILD_KERNEL_LIB=ON \
    -DBUILD_TESTS=ON \
    -DBUILD_TX=ON \
    -DBUILD_UTIL=ON \
    -DBUILD_UTIL_CHAINSTATE=ON \
    -DENABLE_IPC=ON \
    -DENABLE_WALLET=ON \
    -DINSTALL_MAN=ON \
    -DWITH_DBUS=ON \
    -DWITH_QRENCODE=ON \
    -DWITH_SQLITE=ON \
    -DWITH_USDT=ON \
    -DWITH_ZMQ=ON
%cmake_build
%install
%cmake_install
find %{buildroot} -name "*.la" -delete
mkdir -p %{buildroot}%{_tmpfilesdir}
install -m 0644 %{SOURCE5} %{buildroot}%{_tmpfilesdir}/%{project_name}.conf
install -D -m600 -p %{SOURCE6} %{buildroot}%{_sysconfdir}/sysconfig/%{project_name}
install -D -m644 -p %{SOURCE7} %{buildroot}%{_unitdir}/%{project_name}.service
install -D -m644 -p %{SOURCE8} %{buildroot}%{_userunitdir}/%{project_name}.service
install -D -m644 -p %{SOURCE9} %{buildroot}%{_datadir}/kde4/services/%{project_name}-qt.protocol
install -d -m750 -p %{buildroot}%{_sharedstatedir}/%{project_name}
install -d -m750 -p %{buildroot}%{_sysconfdir}/%{project_name}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE10}
for size in 16 32 64 128 256; do
    install -p -D -m 644 share/pixmaps/%{project_name}${size}.png \
        %{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps/%{project_name}.png
done
rm -f %{buildroot}%{_datadir}/pixmaps/%{project_name}*
install -D -m644 -p contrib/completions/bash/%{project_name}-cli.bash %{buildroot}%{_compldir}/%{project_name}-cli
install -D -m644 -p contrib/completions/bash/%{project_name}-tx.bash %{buildroot}%{_compldir}/%{project_name}-tx
install -D -m644 -p contrib/completions/bash/%{project_name}d.bash %{buildroot}%{_compldir}/%{project_name}d
mkdir -p %{buildroot}%{_localstatedir}/log/%{project_name}/
install -p -m 644 -D %{SOURCE18} %{buildroot}%{_metainfodir}/%{project_name}-qt.metainfo.xml
rm -f %{buildroot}%{_bindir}/test_*
install -m0644 -D %{SOURCE11} %{buildroot}%{_sysusersdir}/%{name}.conf
%oreon_autofiles libbitcoinkernel usr/*/lib*.so.*
%oreon_autofiles bitcoin-core-desktop usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles bitcoin-core-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles bitcoin-core-utils usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles bitcoin-core-server usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/*/lib*.so.* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/%{project_name}-qt.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{project_name}-qt.metainfo.xml
%ctest
%if %{with extended_tests}
test/functional/test_runner.py --tmpdirprefix `pwd` --extended
%endif
%post server

%systemd_post %{project_name}.service
%preun server

%systemd_preun %{project_name}.service
%postun server

%systemd_postun_with_restart %{project_name}.service
%files -f %{oreon_filedir}/main.list
%files -n libbitcoinkernel -f %{oreon_filedir}/libbitcoinkernel.list
%files -n bitcoin-core-desktop -f %{oreon_filedir}/bitcoin-core-desktop.list
%files -n bitcoin-core-devel -f %{oreon_filedir}/bitcoin-core-devel.list
%files -n bitcoin-core-utils -f %{oreon_filedir}/bitcoin-core-utils.list
%files -n bitcoin-core-server -f %{oreon_filedir}/bitcoin-core-server.list

%changelog

%autochangelog
