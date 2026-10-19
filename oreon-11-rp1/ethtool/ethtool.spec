%global source2_hash 39d613eeb9498d2944c1e004e9b3a6287fb8ea371aedfd1534089456e7aacdbc
%global source1_hash 89c28ceddb26cad8fbad9295064e73daa5c238f14f1b85a12020f5d434eea436
%global source0_hash 4d78c26edc0255bc92f4b995b5fd66108d75ff966ed4694f6025a6d370bc2496
%global appstream_id org.kernel.software.network.ethtool
Summary:        Settings tool for Ethernet NICs
Name:           ethtool
Epoch:          2
Version:        7.1
Release:        1%{?dist}
License:        GPL-2.0-only AND GPL-2.0-or-later
URL:            https://www.kernel.org/pub/software/network/%{name}/
Source0:        https://www.kernel.org/pub/software/network/%{name}/%{name}-%{version}.tar.xz
Source1:        https://www.kernel.org/pub/software/network/%{name}/%{name}-%{version}.tar.sign
Source2:        https://keys.openpgp.org/vks/v1/by-fingerprint/D2CB120AB45957B721CD9596F4554567B91DE934
Conflicts:      filesystem < 3
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  libappstream-glib
BuildRequires:  libmnl-devel
BuildRequires:  make
BuildRequires:  xz
# /oreon:deps
%description
This utility allows querying and changing settings such as speed,
port, auto-negotiation, PCI locations and checksum offload on many
network devices, especially of Ethernet devices.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
xzcat '%{SOURCE0}' | %{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data=-
%autosetup

%build

%configure
%make_build
%install
%make_install
%oreon_autofiles main

%check

make check
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_metainfodir}/%{appstream_id}.metainfo.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
