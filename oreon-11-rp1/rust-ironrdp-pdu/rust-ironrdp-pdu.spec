%global source0_hash cc69c5d6ad3399965e0d3762886857f5861d4d854efe8d2bfc3462eb2b2b555a
%bcond check 1
%global debug_package %{nil}
%global crate ironrdp-pdu
Name:           rust-ironrdp-pdu
Version:        0.5.0
Release:        1%{?dist}
Summary:        RDP PDU encoding and decoding
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/ironrdp-pdu
Source0:        https://static.crates.io/crates/ironrdp-pdu/ironrdp-pdu-%{version}.crate
Patch:          ironrdp-pdu-fix-metadata.diff
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
Summary:        RDP PDU encoding and decoding
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        RDP PDU encoding and decoding
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        RDP PDU encoding and decoding
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

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
%files -n rust-ironrdp-pdu-devel -f %{oreon_filedir}/rust-ironrdp-pdu-devel.list

%changelog

%autochangelog
