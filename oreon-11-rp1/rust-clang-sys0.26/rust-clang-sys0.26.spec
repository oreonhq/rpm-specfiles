%global source0_hash 6ef0c1bcf2e99c649104bd7a7012d8f8802684400e03db0ec0af48583c6fa0e4
%bcond check 0
%global debug_package %{nil}
%global crate clang-sys
Name:           rust-clang-sys0.26
Version:        0.26.4
Release:        1%{?dist}
Summary:        Rust bindings for libclang.
License:        Apache-2.0
URL:            https://crates.io/crates/clang-sys
Source0:        https://static.crates.io/crates/clang-sys/clang-sys-%{version}.crate
Patch0:         clang-sys-fix-metadata-auto.diff
Patch1:         clang-sys-glob03.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  clang-devel
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       clang-devel >= 3.5
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+clang_3_5-devel
Summary:        Rust bindings for libclang.
BuildArch:      noarch
%description -n %{name}+clang_3_5-devel

This package contains library source intended for building other packages which
use the "clang_3_5" feature of the "%{crate}" crate.

%package     -n %{name}+clang_3_6-devel
Summary:        Rust bindings for libclang.
BuildArch:      noarch
%description -n %{name}+clang_3_6-devel

This package contains library source intended for building other packages which
use the "clang_3_6" feature of the "%{crate}" crate.

%package     -n %{name}+clang_3_7-devel
Summary:        Rust bindings for libclang.
BuildArch:      noarch
%description -n %{name}+clang_3_7-devel

This package contains library source intended for building other packages which
use the "clang_3_7" feature of the "%{crate}" crate.

%package     -n %{name}+clang_3_8-devel
Summary:        Rust bindings for libclang.
BuildArch:      noarch
%description -n %{name}+clang_3_8-devel

This package contains library source intended for building other packages which
use the "clang_3_8" feature of the "%{crate}" crate.

%package     -n %{name}+clang_3_9-devel
Summary:        Rust bindings for libclang.
BuildArch:      noarch
%description -n %{name}+clang_3_9-devel

This package contains library source intended for building other packages which
use the "clang_3_9" feature of the "%{crate}" crate.

%package     -n %{name}+clang_4_0-devel
Summary:        Rust bindings for libclang.
BuildArch:      noarch
%description -n %{name}+clang_4_0-devel

This package contains library source intended for building other packages which
use the "clang_4_0" feature of the "%{crate}" crate.

%package     -n %{name}+clang_5_0-devel
Summary:        Rust bindings for libclang.
BuildArch:      noarch
%description -n %{name}+clang_5_0-devel

This package contains library source intended for building other packages which
use the "clang_5_0" feature of the "%{crate}" crate.

%package     -n %{name}+clang_6_0-devel
Summary:        Rust bindings for libclang.
BuildArch:      noarch
%description -n %{name}+clang_6_0-devel

This package contains library source intended for building other packages which
use the "clang_6_0" feature of the "%{crate}" crate.

%package     -n %{name}+clang_7_0-devel
Summary:        Rust bindings for libclang.
BuildArch:      noarch
%description -n %{name}+clang_7_0-devel

This package contains library source intended for building other packages which
use the "clang_7_0" feature of the "%{crate}" crate.

%package     -n %{name}+gte_clang_3_6-devel
Summary:        Rust bindings for libclang.
BuildArch:      noarch
%description -n %{name}+gte_clang_3_6-devel

This package contains library source intended for building other packages which
use the "gte_clang_3_6" feature of the "%{crate}" crate.

%package     -n %{name}+gte_clang_3_7-devel
Summary:        Rust bindings for libclang.
BuildArch:      noarch
%description -n %{name}+gte_clang_3_7-devel

This package contains library source intended for building other packages which
use the "gte_clang_3_7" feature of the "%{crate}" crate.

%package     -n %{name}+gte_clang_3_8-devel
Summary:        Rust bindings for libclang.
BuildArch:      noarch
%description -n %{name}+gte_clang_3_8-devel

This package contains library source intended for building other packages which
use the "gte_clang_3_8" feature of the "%{crate}" crate.

%package     -n %{name}+gte_clang_3_9-devel
Summary:        Rust bindings for libclang.
BuildArch:      noarch
%description -n %{name}+gte_clang_3_9-devel

This package contains library source intended for building other packages which
use the "gte_clang_3_9" feature of the "%{crate}" crate.

%package     -n %{name}+gte_clang_4_0-devel
Summary:        Rust bindings for libclang.
BuildArch:      noarch
%description -n %{name}+gte_clang_4_0-devel

This package contains library source intended for building other packages which
use the "gte_clang_4_0" feature of the "%{crate}" crate.

%package     -n %{name}+gte_clang_5_0-devel
Summary:        Rust bindings for libclang.
BuildArch:      noarch
%description -n %{name}+gte_clang_5_0-devel

This package contains library source intended for building other packages which
use the "gte_clang_5_0" feature of the "%{crate}" crate.

%package     -n %{name}+gte_clang_6_0-devel
Summary:        Rust bindings for libclang.
BuildArch:      noarch
%description -n %{name}+gte_clang_6_0-devel

This package contains library source intended for building other packages which
use the "gte_clang_6_0" feature of the "%{crate}" crate.

%package     -n %{name}+gte_clang_7_0-devel
Summary:        Rust bindings for libclang.
BuildArch:      noarch
%description -n %{name}+gte_clang_7_0-devel

This package contains library source intended for building other packages which
use the "gte_clang_7_0" feature of the "%{crate}" crate.

%package     -n %{name}+libloading-devel
Summary:        Rust bindings for libclang.
BuildArch:      noarch
%description -n %{name}+libloading-devel

This package contains library source intended for building other packages which
use the "libloading" feature of the "%{crate}" crate.

%package     -n %{name}+runtime-devel
Summary:        Rust bindings for libclang.
BuildArch:      noarch
Requires:       clang-libs
%description -n %{name}+runtime-devel

This package contains library source intended for building other packages which
use the "runtime" feature of the "%{crate}" crate.

%package     -n %{name}+static-devel
Summary:        Rust bindings for libclang.
BuildArch:      noarch
%description -n %{name}+static-devel

This package contains library source intended for building other packages which
use the "static" feature of the "%{crate}" crate.

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
%files -n rust-clang-sys0.26-devel -f %{oreon_filedir}/rust-clang-sys0.26-devel.list

%changelog

%autochangelog
