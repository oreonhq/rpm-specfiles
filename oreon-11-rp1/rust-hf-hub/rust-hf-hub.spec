%global source0_hash e7ccb6bcc85dec15413ef5949879f9a5497ca4568ed702547eb83fac23376e5c
%bcond check 1
%global debug_package %{nil}
%global crate hf-hub
Name:           rust-hf-hub
Version:        1.0.0
Release:        1%{?dist}
Summary:        A limited re-implementation of the huggingface_hub python package in Rust
License:        Apache-2.0
URL:            https://crates.io/crates/hf-hub
Source0:        https://static.crates.io/crates/hf-hub/hf-hub-%{version}.crate
Patch:          hf-hub-fix-metadata-auto.diff
Patch:          hf-hub-fix-metadata.diff
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
Summary:        A limited re-implementation of the huggingface_hub python package in Rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+default-tls-devel
Summary:        A limited re-implementation of the huggingface_hub python package in Rust
BuildArch:      noarch
%description -n %{name}+default-tls-devel

This package contains library source intended for building other packages which
use the "default-tls" feature of the "%{crate}" crate.

%package     -n %{name}+native-tls-devel
Summary:        A limited re-implementation of the huggingface_hub python package in Rust
BuildArch:      noarch
%description -n %{name}+native-tls-devel

This package contains library source intended for building other packages which
use the "native-tls" feature of the "%{crate}" crate.

%package     -n %{name}+rustls-tls-devel
Summary:        A limited re-implementation of the huggingface_hub python package in Rust
BuildArch:      noarch
%description -n %{name}+rustls-tls-devel

This package contains library source intended for building other packages which
use the "rustls-tls" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-devel
Summary:        A limited re-implementation of the huggingface_hub python package in Rust
BuildArch:      noarch
%description -n %{name}+tokio-devel

This package contains library source intended for building other packages which
use the "tokio" feature of the "%{crate}" crate.

%package     -n %{name}+ureq-devel
Summary:        A limited re-implementation of the huggingface_hub python package in Rust
BuildArch:      noarch
%description -n %{name}+ureq-devel

This package contains library source intended for building other packages which
use the "ureq" feature of the "%{crate}" crate.

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

%cargo_test -- --doc -- --skip 34
%{cargo_test -- --lib -- --exact %{shrink:
    --skip api::sync::tests::dataset
    --skip api::sync::tests::detailed_info
    --skip api::sync::tests::info
    --skip api::sync::tests::locking
    --skip api::sync::tests::models
    --skip api::sync::tests::resume
    --skip api::sync::tests::simple
    --skip api::sync::tests::simple_with_retries
    --skip api::tokio::tests::dataset
    --skip api::tokio::tests::info
    --skip api::tokio::tests::info_request
    --skip api::tokio::tests::locking
    --skip api::tokio::tests::models
    --skip api::tokio::tests::repo_info_failed
    --skip api::tokio::tests::resume
    --skip api::tokio::tests::revision
    --skip api::tokio::tests::simple
}}
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-hf-hub-devel -f %{oreon_filedir}/rust-hf-hub-devel.list

%changelog

%autochangelog
