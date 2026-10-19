%global source0_hash b2ed30b30e1e17966b55ddd0b9dd2758fd824f0a6da6875c8abb17e6aba47c28
%bcond check 0
%global debug_package %{nil}
%global crate clang
Name:           rust-clang
Version:        2.1.0
Release:        1%{?dist}
Summary:        A somewhat idiomatic Rust wrapper for libclang.
License:        Apache-2.0
URL:            https://crates.io/crates/clang
Source0:        https://static.crates.io/crates/clang/clang-%{version}.crate
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

%package     -n %{name}+clang_10_0-devel
Summary:        A somewhat idiomatic Rust wrapper for libclang.
BuildArch:      noarch
%description -n %{name}+clang_10_0-devel

This package contains library source intended for building other packages which
use the "clang_10_0" feature of the "%{crate}" crate.

%package     -n %{name}+clang_3_5-devel
Summary:        A somewhat idiomatic Rust wrapper for libclang.
BuildArch:      noarch
%description -n %{name}+clang_3_5-devel

This package contains library source intended for building other packages which
use the "clang_3_5" feature of the "%{crate}" crate.

%package     -n %{name}+clang_3_6-devel
Summary:        A somewhat idiomatic Rust wrapper for libclang.
BuildArch:      noarch
%description -n %{name}+clang_3_6-devel

This package contains library source intended for building other packages which
use the "clang_3_6" feature of the "%{crate}" crate.

%package     -n %{name}+clang_3_7-devel
Summary:        A somewhat idiomatic Rust wrapper for libclang.
BuildArch:      noarch
%description -n %{name}+clang_3_7-devel

This package contains library source intended for building other packages which
use the "clang_3_7" feature of the "%{crate}" crate.

%package     -n %{name}+clang_3_8-devel
Summary:        A somewhat idiomatic Rust wrapper for libclang.
BuildArch:      noarch
%description -n %{name}+clang_3_8-devel

This package contains library source intended for building other packages which
use the "clang_3_8" feature of the "%{crate}" crate.

%package     -n %{name}+clang_3_9-devel
Summary:        A somewhat idiomatic Rust wrapper for libclang.
BuildArch:      noarch
%description -n %{name}+clang_3_9-devel

This package contains library source intended for building other packages which
use the "clang_3_9" feature of the "%{crate}" crate.

%package     -n %{name}+clang_4_0-devel
Summary:        A somewhat idiomatic Rust wrapper for libclang.
BuildArch:      noarch
%description -n %{name}+clang_4_0-devel

This package contains library source intended for building other packages which
use the "clang_4_0" feature of the "%{crate}" crate.

%package     -n %{name}+clang_5_0-devel
Summary:        A somewhat idiomatic Rust wrapper for libclang.
BuildArch:      noarch
%description -n %{name}+clang_5_0-devel

This package contains library source intended for building other packages which
use the "clang_5_0" feature of the "%{crate}" crate.

%package     -n %{name}+clang_6_0-devel
Summary:        A somewhat idiomatic Rust wrapper for libclang.
BuildArch:      noarch
%description -n %{name}+clang_6_0-devel

This package contains library source intended for building other packages which
use the "clang_6_0" feature of the "%{crate}" crate.

%package     -n %{name}+clang_7_0-devel
Summary:        A somewhat idiomatic Rust wrapper for libclang.
BuildArch:      noarch
%description -n %{name}+clang_7_0-devel

This package contains library source intended for building other packages which
use the "clang_7_0" feature of the "%{crate}" crate.

%package     -n %{name}+clang_8_0-devel
Summary:        A somewhat idiomatic Rust wrapper for libclang.
BuildArch:      noarch
%description -n %{name}+clang_8_0-devel

This package contains library source intended for building other packages which
use the "clang_8_0" feature of the "%{crate}" crate.

%package     -n %{name}+clang_9_0-devel
Summary:        A somewhat idiomatic Rust wrapper for libclang.
BuildArch:      noarch
%description -n %{name}+clang_9_0-devel

This package contains library source intended for building other packages which
use the "clang_9_0" feature of the "%{crate}" crate.

%package     -n %{name}+runtime-devel
Summary:        A somewhat idiomatic Rust wrapper for libclang.
BuildArch:      noarch
%description -n %{name}+runtime-devel

This package contains library source intended for building other packages which
use the "runtime" feature of the "%{crate}" crate.

%package     -n %{name}+static-devel
Summary:        A somewhat idiomatic Rust wrapper for libclang.
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
%files -n rust-clang-devel -f %{oreon_filedir}/rust-clang-devel.list

%changelog

%autochangelog
