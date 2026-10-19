%global source0_hash 3ca72c3f2792761ab5fa848490694cbc728c7f659669ed4320c4c79c12150966
%bcond check 0
%global debug_package %{nil}
%global crate quinn-udp
Name:           rust-quinn-udp
Version:        0.6.2
Release:        1%{?dist}
Summary:        UDP sockets with ECN information for the QUIC transport protocol
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/quinn-udp
Source0:        https://static.crates.io/crates/quinn-udp/quinn-udp-%{version}.crate
Patch:          quinn-udp-fix-metadata-auto.diff
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
Summary:        UDP sockets with ECN information for the QUIC transport protocol
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+log-devel
Summary:        UDP sockets with ECN information for the QUIC transport protocol
BuildArch:      noarch
%description -n %{name}+log-devel

This package contains library source intended for building other packages which
use the "log" feature of the "%{crate}" crate.

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
%files -n rust-quinn-udp-devel -f %{oreon_filedir}/rust-quinn-udp-devel.list

%changelog

%autochangelog
