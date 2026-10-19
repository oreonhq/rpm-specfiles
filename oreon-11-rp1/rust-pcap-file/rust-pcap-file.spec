%global source0_hash 1fc1f139757b058f9f37b76c48501799d12c9aa0aa4c0d4c980b062ee925d1b2
%bcond check 0
%global debug_package %{nil}
%global crate pcap-file
Name:           rust-pcap-file
Version:        2.0.0
Release:        1%{?dist}
Summary:        To parse, read and write Pcap and PcapNg
License:        MIT
URL:            https://crates.io/crates/pcap-file
Source0:        https://static.crates.io/crates/pcap-file/pcap-file-%{version}.crate
Patch:          pcap-file-fix-metadata.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        To parse, read and write Pcap and PcapNg
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build
%install
%cargo_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-pcap-file-devel -f %{oreon_filedir}/rust-pcap-file-devel.list

%changelog

%autochangelog
