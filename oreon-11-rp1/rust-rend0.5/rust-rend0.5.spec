%global source0_hash 663ba70707f96e871406fe10d68128412e619b06d1d47cb91c3a4c6501176240
%bcond check 0
%global debug_package %{nil}
%global crate rend
Name:           rust-rend0.5
Version:        0.5.4
Release:        1%{?dist}
Summary:        Cross-platform, endian-aware primitives for Rust
License:        MIT
URL:            https://crates.io/crates/rend
Source0:        https://static.crates.io/crates/rend/rend-%{version}.crate
# oreon:deps
BuildRequires:  cargo-rpm-macros
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Cross-platform, endian-aware primitives for Rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+bytecheck-devel
Summary:        Cross-platform, endian-aware primitives for Rust
BuildArch:      noarch
%description -n %{name}+bytecheck-devel

This package contains library source intended for building other packages which
use the "bytecheck" feature of the "%{crate}" crate.

%package     -n %{name}+bytemuck-1-devel
Summary:        Cross-platform, endian-aware primitives for Rust
BuildArch:      noarch
%description -n %{name}+bytemuck-1-devel

This package contains library source intended for building other packages which
use the "bytemuck-1" feature of the "%{crate}" crate.

%package     -n %{name}+zerocopy-0_8-devel
Summary:        Cross-platform, endian-aware primitives for Rust
BuildArch:      noarch
%description -n %{name}+zerocopy-0_8-devel

This package contains library source intended for building other packages which
use the "zerocopy-0_8" feature of the "%{crate}" crate.

%files -f %{oreon_filedir}/main.list
%files -n rust-rend0.5-devel -f %{oreon_filedir}/rust-rend0.5-devel.list
