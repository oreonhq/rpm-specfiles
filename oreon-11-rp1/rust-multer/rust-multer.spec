%global source0_hash 83e87776546dc87511aa5ee218730c92b666d7264ab6ed41f9d215af9cd5224b
%bcond check 0
%global debug_package %{nil}
%global crate multer
Name:           rust-multer
Version:        3.1.0
Release:        1%{?dist}
Summary:        An async parser for `multipart/form-data` content-type in Rust.
License:        MIT
URL:            https://crates.io/crates/multer
Source0:        https://static.crates.io/crates/multer/multer-%{version}.crate
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
Summary:        An async parser for `multipart/form-data` content-type in Rust.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+all-devel
Summary:        An async parser for `multipart/form-data` content-type in Rust.
BuildArch:      noarch
%description -n %{name}+all-devel

This package contains library source intended for building other packages which
use the "all" feature of the "%{crate}" crate.

%package     -n %{name}+json-devel
Summary:        An async parser for `multipart/form-data` content-type in Rust.
BuildArch:      noarch
%description -n %{name}+json-devel

This package contains library source intended for building other packages which
use the "json" feature of the "%{crate}" crate.

%package     -n %{name}+log-devel
Summary:        An async parser for `multipart/form-data` content-type in Rust.
BuildArch:      noarch
%description -n %{name}+log-devel

This package contains library source intended for building other packages which
use the "log" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        An async parser for `multipart/form-data` content-type in Rust.
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+serde_json-devel
Summary:        An async parser for `multipart/form-data` content-type in Rust.
BuildArch:      noarch
%description -n %{name}+serde_json-devel

This package contains library source intended for building other packages which
use the "serde_json" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-devel
Summary:        An async parser for `multipart/form-data` content-type in Rust.
BuildArch:      noarch
%description -n %{name}+tokio-devel

This package contains library source intended for building other packages which
use the "tokio" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-io-devel
Summary:        An async parser for `multipart/form-data` content-type in Rust.
BuildArch:      noarch
%description -n %{name}+tokio-io-devel

This package contains library source intended for building other packages which
use the "tokio-io" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-util-devel
Summary:        An async parser for `multipart/form-data` content-type in Rust.
BuildArch:      noarch
%description -n %{name}+tokio-util-devel

This package contains library source intended for building other packages which
use the "tokio-util" feature of the "%{crate}" crate.

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
%files -n rust-multer-devel -f %{oreon_filedir}/rust-multer-devel.list

%changelog

%autochangelog
