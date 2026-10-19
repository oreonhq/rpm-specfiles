%global source0_hash caf600e7036b17782571dd44fa0a5cea3c82f60db5137f774a325a76a0d6852b
%bcond check 1
%global debug_package %{nil}
%global crate tokio-serde
Name:           rust-tokio-serde
Version:        0.9.0
Release:        1%{?dist}
Summary:        Send and receive Serde encodable types over the network using Tokio
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/tokio-serde
Source0:        https://static.crates.io/crates/tokio-serde/tokio-serde-%{version}.crate
Patch:          tokio-serde-fix-metadata.diff
Patch1:         tokio-serde-educe.patch
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
Summary:        Send and receive Serde encodable types over the network using Tokio
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+bincode-devel
Summary:        Send and receive Serde encodable types over the network using Tokio
BuildArch:      noarch
%description -n %{name}+bincode-devel

This package contains library source intended for building other packages which
use the "bincode" feature of the "%{crate}" crate.

%package     -n %{name}+bincode-crate-devel
Summary:        Send and receive Serde encodable types over the network using Tokio
BuildArch:      noarch
%description -n %{name}+bincode-crate-devel

This package contains library source intended for building other packages which
use the "bincode-crate" feature of the "%{crate}" crate.

%package     -n %{name}+cbor-devel
Summary:        Send and receive Serde encodable types over the network using Tokio
BuildArch:      noarch
%description -n %{name}+cbor-devel

This package contains library source intended for building other packages which
use the "cbor" feature of the "%{crate}" crate.

%package     -n %{name}+educe-devel
Summary:        Send and receive Serde encodable types over the network using Tokio
BuildArch:      noarch
%description -n %{name}+educe-devel

This package contains library source intended for building other packages which
use the "educe" feature of the "%{crate}" crate.

%package     -n %{name}+json-devel
Summary:        Send and receive Serde encodable types over the network using Tokio
BuildArch:      noarch
%description -n %{name}+json-devel

This package contains library source intended for building other packages which
use the "json" feature of the "%{crate}" crate.

%package     -n %{name}+messagepack-devel
Summary:        Send and receive Serde encodable types over the network using Tokio
BuildArch:      noarch
%description -n %{name}+messagepack-devel

This package contains library source intended for building other packages which
use the "messagepack" feature of the "%{crate}" crate.

%package     -n %{name}+rmp-serde-devel
Summary:        Send and receive Serde encodable types over the network using Tokio
BuildArch:      noarch
%description -n %{name}+rmp-serde-devel

This package contains library source intended for building other packages which
use the "rmp-serde" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Send and receive Serde encodable types over the network using Tokio
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+serde_cbor-devel
Summary:        Send and receive Serde encodable types over the network using Tokio
BuildArch:      noarch
%description -n %{name}+serde_cbor-devel

This package contains library source intended for building other packages which
use the "serde_cbor" feature of the "%{crate}" crate.

%package     -n %{name}+serde_json-devel
Summary:        Send and receive Serde encodable types over the network using Tokio
BuildArch:      noarch
%description -n %{name}+serde_json-devel

This package contains library source intended for building other packages which
use the "serde_json" feature of the "%{crate}" crate.

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
%files -n rust-tokio-serde-devel -f %{oreon_filedir}/rust-tokio-serde-devel.list

%changelog

%autochangelog
