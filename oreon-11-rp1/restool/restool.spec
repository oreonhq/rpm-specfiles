%global source0_hash 00299c57d216ee3138f700fe3539e1bd0e3328bf18cfe891c3538b7408aa52f9

# The labled version is different to the tag and we need specific feature
# branch for the NXP LX2160A functionality
# https://github.com/nxp-qoriq/restool
# git archive --format=tar --prefix=restool-2.4.0/ abd2f5b | xz > restool-%{version}-%{gittag}.tar.xz
%define gittag 443e5fa

Name:      restool
Version:   2.4.0
Release:   14.%{gittag}%{?dist}
Summary:   A tool to create and manage the DPAA2 Management Complex (MC)
# Automatically converted from old format: BSD or GPLv2+ - review is highly recommended.
License:   LicenseRef-Callaway-BSD OR GPL-2.0-or-later
URL:       https://github.com/nxp-qoriq/restool
Source:    %{name}-%{version}-%{gittag}.tar.xz
# udev rule for creating ethX devices
Source1:   fsl_mc_bus.rules

# HW specific to NXP Layerscape arm SoCs with DPAA2
ExclusiveArch: aarch64
BuildRequires: gcc
BuildRequires: make
BuildRequires: pandoc

%description
restool is a user space application providing the ability to dynamically
create and manage DPAA2 containers and objects from Linux.

restool interacts with the DPAA2 Management Complex (MC).  It uses an ioctl to
send MC commands, and thus requires a Linux kernel driver providing the needed
ioctl support.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
# the maybe-uninitialized has been reported to upstream
%{make_build} EXTRA_CFLAGS="%{build_cflags} -Wno-error=maybe-uninitialized" LDFLAGS="%{build_ldflags}"

%install
%{make_install} prefix=%{_usr}
mkdir -p %{buildroot}/etc/udev/rules.d/
install -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/udev/rules.d/

%files
%license LICENSE
%{_bindir}/restool
%{_bindir}/ls-*
%{_datadir}/bash-completion/completions/restool
%{_mandir}/man1/restool*
%{_sysconfdir}/udev/rules.d/fsl_mc_bus.rules

%changelog
%autochangelog
