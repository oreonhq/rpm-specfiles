%global source0_hash 9548f585513f68629ef0edd894e079efe84d799349fe43f7d3b4f0c932ad855a
%{!?_hardened_build:%global _hardened_build 1}
%if %{?_hardened_build}%{!?_hardened_build:0}
%global cflags_harden -fpie
%global ldflags_harden -pie -z relro -z now
%endif
Summary:        Alternative packet radio system for Linux
Name: uronode
Version: 2.15
Release:        11%{?dist}
License: GPL-2.0-or-later
URL: http://uronode.sourceforge.net
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1: flexd.service
Source2: uronode@.service
Source3: uronode.socket
Source4: uronode.xinetd
Source5: uronode-README.fedora
Patch: uronode-2.7-install-fix.patch
Patch: uronode-2.7-configure-non-interactive.patch
Patch: uronode-2.15-gcc-15-fix.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libax25-devel
BuildRequires:  make
BuildRequires:  systemd
BuildRequires:  zlib-devel
# /oreon:deps
%description
URONode is an alternative packet radio system for Linux. It supports
cross-port digipeating, automatic importing of flexnet routing,
various IP functions, and ANSI colors.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Copy Fedora readme into place
cp -p %{SOURCE5} README.fedora

# Removing bundled libax25, using system one.
rm -rf include

%build

export NON_INTERACTIVE=1
export ETC_DIR=%{_sysconfdir}/ax25
export SBIN_DIR=%{_sbindir}
export BIN_DIR=%{_bindir}
export LIB_DIR=%{_prefix}/lib
export DATA_DIR=%{_datadir}
export MAN_DIR=%{_mandir}
export VAR_DIR=%{_var}
./configure
make %{?_smp_mflags} CFLAGS="%{optflags} %{?cflags_harden}" LDFLAGS="%{?__global_ldflags} %{?ldflags_harden}"
%install
make %{?_smp_mflags} DESTDIR=%{buildroot} install
install -Dpm 644 %{SOURCE1} %{buildroot}%{_unitdir}/flexd.service
install -Dpm 644 %{SOURCE2} %{buildroot}%{_unitdir}/uronode@.service
install -Dpm 644 %{SOURCE3} %{buildroot}%{_unitdir}/uronode.socket
install -Dpm 644 %{SOURCE4} %{buildroot}%{_datadir}/%{name}/xinetd.d/uronode
touch %{buildroot}/%{_var}/lib/flexd/destinations
[ -s %{buildroot}%{_var}/lib/flexd/gateways ] && exit 1
[ -s %{buildroot}%{_var}/log/uronode/lastlog ] && exit 1
[ -s %{buildroot}%{_var}/lib/uronode/loggedin ] && exit 1
%oreon_autofiles main

%post

%systemd_post flexd.service uronode.socket
[ -f %{_var}/lib/uronode/loggedin ] || touch %{_var}/lib/uronode/loggedin
%preun

%systemd_preun flexd.service uronode.socket
%postun

%systemd_postun_with_restart flexd.service uronode.socket
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
