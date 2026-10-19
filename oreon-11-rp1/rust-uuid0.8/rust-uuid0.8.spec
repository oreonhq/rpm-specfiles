%global source0_hash bc5cf98d8186244414c848017f0e2676b3fcb46807f6668a97dfe67359a3c4b7
%bcond check 0
%global debug_package %{nil}
%global crate uuid
Name:           rust-uuid0.8
Version:        0.8.2
Release:        1%{?dist}
Summary:        A library to generate and parse UUIDs.
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/uuid
Source0:        https://static.crates.io/crates/uuid/uuid-%{version}.crate
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
Summary:        A library to generate and parse UUIDs.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+getrandom-devel
Summary:        A library to generate and parse UUIDs.
BuildArch:      noarch
%description -n %{name}+getrandom-devel

This package contains library source intended for building other packages which
use the "getrandom" feature of the "%{crate}" crate.

%package     -n %{name}+guid-devel
Summary:        A library to generate and parse UUIDs.
BuildArch:      noarch
%description -n %{name}+guid-devel

This package contains library source intended for building other packages which
use the "guid" feature of the "%{crate}" crate.

%package     -n %{name}+md5-devel
Summary:        A library to generate and parse UUIDs.
BuildArch:      noarch
%description -n %{name}+md5-devel

This package contains library source intended for building other packages which
use the "md5" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        A library to generate and parse UUIDs.
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+sha1-devel
Summary:        A library to generate and parse UUIDs.
BuildArch:      noarch
%description -n %{name}+sha1-devel

This package contains library source intended for building other packages which
use the "sha1" feature of the "%{crate}" crate.

%package     -n %{name}+slog-devel
Summary:        A library to generate and parse UUIDs.
BuildArch:      noarch
%description -n %{name}+slog-devel

This package contains library source intended for building other packages which
use the "slog" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        A library to generate and parse UUIDs.
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+stdweb-devel
Summary:        A library to generate and parse UUIDs.
BuildArch:      noarch
%description -n %{name}+stdweb-devel

This package contains library source intended for building other packages which
use the "stdweb" feature of the "%{crate}" crate.

%package     -n %{name}+v1-devel
Summary:        A library to generate and parse UUIDs.
BuildArch:      noarch
%description -n %{name}+v1-devel

This package contains library source intended for building other packages which
use the "v1" feature of the "%{crate}" crate.

%package     -n %{name}+v3-devel
Summary:        A library to generate and parse UUIDs.
BuildArch:      noarch
%description -n %{name}+v3-devel

This package contains library source intended for building other packages which
use the "v3" feature of the "%{crate}" crate.

%package     -n %{name}+v4-devel
Summary:        A library to generate and parse UUIDs.
BuildArch:      noarch
%description -n %{name}+v4-devel

This package contains library source intended for building other packages which
use the "v4" feature of the "%{crate}" crate.

%package     -n %{name}+v5-devel
Summary:        A library to generate and parse UUIDs.
BuildArch:      noarch
%description -n %{name}+v5-devel

This package contains library source intended for building other packages which
use the "v5" feature of the "%{crate}" crate.

%package     -n %{name}+wasm-bindgen-devel
Summary:        A library to generate and parse UUIDs.
BuildArch:      noarch
%description -n %{name}+wasm-bindgen-devel

This package contains library source intended for building other packages which
use the "wasm-bindgen" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version}
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
%files -n rust-uuid0.8-devel -f %{oreon_filedir}/rust-uuid0.8-devel.list

%changelog

%autochangelog
