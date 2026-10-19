%global source10_hash ff03eff2e3a826290ab6ed790c953a3280749da2a4f1332f5e525268c81232e0
%global source0_hash 961d16382652bfdd8c6f68b223b26a8c93e0d475c672f414411db31c6c5c900e
%bcond check 0
%global debug_package %{nil}
%global crate jiff
Name:           rust-jiff
Version:        0.2.32
Release:        2%{?dist}
Summary:        Date-time library that encourages you to jump into the pit of success
License:        Unlicense OR MIT
URL:            https://crates.io/crates/jiff
Source0:        https://static.crates.io/crates/jiff/jiff-%{version}.crate
Source10:       https://github.com/BurntSushi/jiff/archive/%{version}/jiff-%{version}.tar.gz
Patch:          jiff-fix-metadata-auto.diff
Patch:          jiff-fix-metadata.diff
Patch10:        0001-Downstream-only-Omit-doctests-that-require-hifitime.patch
Patch11:        0002-Downstream-only-Omit-doctests-that-require-jiff-stat.patch
Patch12:        0003-Downstream-only-Omit-doctest-that-requires-time-tz.patch
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
BuildRequires:  tomcli
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Date-time library that encourages you to jump into the pit of success
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Date-time library that encourages you to jump into the pit of success
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+logging-devel
Summary:        Date-time library that encourages you to jump into the pit of success
BuildArch:      noarch
%description -n %{name}+logging-devel

This package contains library source intended for building other packages which
use the "logging" feature of the "%{crate}" crate.

%package     -n %{name}+perf-inline-devel
Summary:        Date-time library that encourages you to jump into the pit of success
BuildArch:      noarch
%description -n %{name}+perf-inline-devel

This package contains library source intended for building other packages which
use the "perf-inline" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Date-time library that encourages you to jump into the pit of success
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Date-time library that encourages you to jump into the pit of success
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+tz-fat-devel
Summary:        Date-time library that encourages you to jump into the pit of success
BuildArch:      noarch
%description -n %{name}+tz-fat-devel

This package contains library source intended for building other packages which
use the "tz-fat" feature of the "%{crate}" crate.

%package     -n %{name}+tz-system-devel
Summary:        Date-time library that encourages you to jump into the pit of success
BuildArch:      noarch
%description -n %{name}+tz-system-devel

This package contains library source intended for building other packages which
use the "tz-system" feature of the "%{crate}" crate.

%package     -n %{name}+tzdb-bundle-platform-devel
Summary:        Date-time library that encourages you to jump into the pit of success
BuildArch:      noarch
%description -n %{name}+tzdb-bundle-platform-devel

This package contains library source intended for building other packages which
use the "tzdb-bundle-platform" feature of the "%{crate}" crate.

%package     -n %{name}+tzdb-concatenated-devel
Summary:        Date-time library that encourages you to jump into the pit of success
BuildArch:      noarch
%description -n %{name}+tzdb-concatenated-devel

This package contains library source intended for building other packages which
use the "tzdb-concatenated" feature of the "%{crate}" crate.

%package     -n %{name}+tzdb-zoneinfo-devel
Summary:        Date-time library that encourages you to jump into the pit of success
BuildArch:      noarch
%description -n %{name}+tzdb-zoneinfo-devel

This package contains library source intended for building other packages which
use the "tzdb-zoneinfo" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
tomcli set Cargo.toml del \
"target.'cfg(not(target_family = \"wasm\"))'.dev-dependencies.hifitime"
tomcli set Cargo.toml del dev-dependencies.time-tz
tomcli set Cargo.toml del 'target."cfg(any())".dependencies.jiff-static'
%oreon_vendor_cargo
%build

%cargo_build -f serde
%install
%cargo_install -f serde
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

tar -xzvf '%{SOURCE10}' --strip-components=1 \
    jiff-%{version}/src/tz/snapshots \
    jiff-%{version}/src/tz/testdata \
    jiff-%{version}/tests
rm -rv tests/procmacro/
sed -r -i 's@^mod procmacro;@// &@' tests/lib.rs
%cargo_test -f serde
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-jiff-devel -f %{oreon_filedir}/rust-jiff-devel.list

%changelog

%autochangelog
