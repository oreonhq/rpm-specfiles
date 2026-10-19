%global source0_hash bf3923a6f5c4c6382e0b653c4117f48d631ea17f38ed86e2a828e6f7412f5239
%bcond check 0
%global debug_package %{nil}
%global crate uuid
Name:           rust-uuid
Version:        1.24.0
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

%package     -n %{name}+arbitrary-devel
Summary:        A library to generate and parse UUIDs.
BuildArch:      noarch
%description -n %{name}+arbitrary-devel

This package contains library source intended for building other packages which
use the "arbitrary" feature of the "%{crate}" crate.

%package     -n %{name}+atomic-devel
Summary:        A library to generate and parse UUIDs.
BuildArch:      noarch
%description -n %{name}+atomic-devel

This package contains library source intended for building other packages which
use the "atomic" feature of the "%{crate}" crate.

%package     -n %{name}+borsh-devel
Summary:        A library to generate and parse UUIDs.
BuildArch:      noarch
%description -n %{name}+borsh-devel

This package contains library source intended for building other packages which
use the "borsh" feature of the "%{crate}" crate.

%package     -n %{name}+bytemuck-devel
Summary:        A library to generate and parse UUIDs.
BuildArch:      noarch
%description -n %{name}+bytemuck-devel

This package contains library source intended for building other packages which
use the "bytemuck" feature of the "%{crate}" crate.

%package     -n %{name}+fast-rng-devel
Summary:        A library to generate and parse UUIDs.
BuildArch:      noarch
%description -n %{name}+fast-rng-devel

This package contains library source intended for building other packages which
use the "fast-rng" feature of the "%{crate}" crate.

%package     -n %{name}+js-devel
Summary:        A library to generate and parse UUIDs.
BuildArch:      noarch
%description -n %{name}+js-devel

This package contains library source intended for building other packages which
use the "js" feature of the "%{crate}" crate.

%package     -n %{name}+macro-diagnostics-devel
Summary:        A library to generate and parse UUIDs.
BuildArch:      noarch
%description -n %{name}+macro-diagnostics-devel

This package contains library source intended for building other packages which
use the "macro-diagnostics" feature of the "%{crate}" crate.

%package     -n %{name}+md5-devel
Summary:        A library to generate and parse UUIDs.
BuildArch:      noarch
%description -n %{name}+md5-devel

This package contains library source intended for building other packages which
use the "md5" feature of the "%{crate}" crate.

%package     -n %{name}+rng-devel
Summary:        A library to generate and parse UUIDs.
BuildArch:      noarch
%description -n %{name}+rng-devel

This package contains library source intended for building other packages which
use the "rng" feature of the "%{crate}" crate.

%package     -n %{name}+rng-getrandom-devel
Summary:        A library to generate and parse UUIDs.
BuildArch:      noarch
%description -n %{name}+rng-getrandom-devel

This package contains library source intended for building other packages which
use the "rng-getrandom" feature of the "%{crate}" crate.

%package     -n %{name}+rng-rand-devel
Summary:        A library to generate and parse UUIDs.
BuildArch:      noarch
%description -n %{name}+rng-rand-devel

This package contains library source intended for building other packages which
use the "rng-rand" feature of the "%{crate}" crate.

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

%package     -n %{name}+v6-devel
Summary:        A library to generate and parse UUIDs.
BuildArch:      noarch
%description -n %{name}+v6-devel

This package contains library source intended for building other packages which
use the "v6" feature of the "%{crate}" crate.

%package     -n %{name}+v7-devel
Summary:        A library to generate and parse UUIDs.
BuildArch:      noarch
%description -n %{name}+v7-devel

This package contains library source intended for building other packages which
use the "v7" feature of the "%{crate}" crate.

%package     -n %{name}+v8-devel
Summary:        A library to generate and parse UUIDs.
BuildArch:      noarch
%description -n %{name}+v8-devel

This package contains library source intended for building other packages which
use the "v8" feature of the "%{crate}" crate.

%package     -n %{name}+zerocopy-devel
Summary:        A library to generate and parse UUIDs.
BuildArch:      noarch
%description -n %{name}+zerocopy-devel

This package contains library source intended for building other packages which
use the "zerocopy" feature of the "%{crate}" crate.

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
%files -n rust-uuid-devel -f %{oreon_filedir}/rust-uuid-devel.list

%changelog

%autochangelog
