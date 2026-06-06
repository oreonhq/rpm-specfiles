%global source0_hash none

# globals for redhat-lsb-20231006git8d00acdc.tar.gz
%global gitdate 20231006
%global gitversion a25a4fcd73c7

%global snapshot %{gitdate}git%{gitversion}
%global gver .%{gitdate}git%{gitversion}

%global upstreamlsbrelver 2.0
%global lsbrelver 5.0
%global disclaimer This package is not compliance with LSB, because various \
components are missing from Fedora or EPEL, so compliance is not possible. \
Fedora or EPEL explicitly declines add support the missing components from LSB \
5.0 or earlier because these components are very outdated and have been \
removed from the repositories and possibly replaced with new ones. \
This package tries its best to comply with the LSB. Hoping to be helpful and \
continue to support the LSB project and software that uses it

Summary: Partial implementation of Linux Standard Base specification
Name: redhat-lsb
Version: 5.0
Release: 0.18%{gver}%{?dist}
URL: https://wiki.linuxfoundation.org/lsb/start
# https://github.com/LinuxStandardBase/lsb-samples/
Source0:        https://github.com/LinuxStandardBase/lsb-samples/archive/%{gitversion}.tar.gz#/redhat-lsb-%{snapshot}.tar.gz
# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
BuildRequires: make
BuildRequires: help2man
Requires: util-linux

Provides: lsb = %{version}-%{release}
Provides: lsb-noarch = %{version}-%{release}
Obsoletes: redhat-lsb-trialuse < 5
Obsoletes: redhat-lsb-submod-multimedia < 5
Obsoletes: redhat-lsb-submod-security < 5
Obsoletes: redhat-lsb-core <= 5.0-0.12
Obsoletes: redhat-lsb-cxx <= 5.0-0.12
Obsoletes: redhat-lsb-desktop <= 5.0-0.12
Obsoletes: redhat-lsb-languages <= 5.0-0.12
Obsoletes: redhat-lsb-printing <= 5.0-0.12
Obsoletes: redhat-lsb-supplemental <= 5.0-0.12
Conflicts: lsb_release

BuildArch:      noarch

%description
The Linux Standard Base (LSB) is an attempt to develop a set of standards that
will increase compatibility among Linux distributions. It is designed to be
binary-compatible and produce a stable application binary interface (ABI) for
independent software vendors.

%{disclaimer}

The lsb package provides utilities, libraries etc. needed for LSB Compliant
Applications.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n lsb-samples-a25a4fcd73c7
test -d redhat-lsb || ln -s . redhat-lsb

%build
cd lsb_release/src
%make_build

%install
pushd redhat-lsb
%make_install
popd

pushd lsb_release/src
make mandir=%{buildroot}%{_mandir} prefix=%{buildroot}%{_prefix} install
popd

#prepare installation of doc
cp -p lsb_release/src/COPYING .
cp -p lsb_release/src/README README.lsb_release

%files
%doc README.md README.lsb_release
%license COPYING
%{_sysconfdir}/redhat-lsb
%{_mandir}/*/lsb_release*
%{_bindir}/lsb_release
/usr/lib/lsb


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.0-0.18.20231006git8d00acdc
- Import
