%global source0_hash af66907df18639dcf4db56ca65490cabc4b27a97dbadd96f2926cca73298f016
%bcond check 1
%global debug_package %{nil}
%global crate quinn-udp
Name:           rust-quinn-udp0.5
Version:        0.5.16
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

%package     -n %{name}+direct-log-devel
Summary:        UDP sockets with ECN information for the QUIC transport protocol
BuildArch:      noarch
%description -n %{name}+direct-log-devel

This package contains library source intended for building other packages which
use the "direct-log" feature of the "%{crate}" crate.

%package     -n %{name}+fast-apple-datapath-devel
Summary:        UDP sockets with ECN information for the QUIC transport protocol
BuildArch:      noarch
%description -n %{name}+fast-apple-datapath-devel

This package contains library source intended for building other packages which
use the "fast-apple-datapath" feature of the "%{crate}" crate.

%package     -n %{name}+log-devel
Summary:        UDP sockets with ECN information for the QUIC transport protocol
BuildArch:      noarch
%description -n %{name}+log-devel

This package contains library source intended for building other packages which
use the "log" feature of the "%{crate}" crate.

%package     -n %{name}+tracing-devel
Summary:        UDP sockets with ECN information for the QUIC transport protocol
BuildArch:      noarch
%description -n %{name}+tracing-devel

This package contains library source intended for building other packages which
use the "tracing" feature of the "%{crate}" crate.

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
%files -n rust-quinn-udp0.5-devel -f %{oreon_filedir}/rust-quinn-udp0.5-devel.list

%changelog

%autochangelog
