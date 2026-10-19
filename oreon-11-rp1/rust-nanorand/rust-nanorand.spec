%global source0_hash 6a51313c5820b0b02bd422f4b44776fbf47961755c74ce64afc73bfad10226c3
%bcond check 0
%global debug_package %{nil}
%global crate nanorand
Name:           rust-nanorand
Version:        0.7.0
Release:        1%{?dist}
Summary:        Tiny, fast, zero-dep library for random number generation
License:        Zlib
URL:            https://crates.io/crates/nanorand
Source0:        https://static.crates.io/crates/nanorand/nanorand-%{version}.crate
Patch:          nanorand-fix-metadata.diff
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
Summary:        Tiny, fast, zero-dep library for random number generation
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Tiny, fast, zero-dep library for random number generation
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+chacha-devel
Summary:        Tiny, fast, zero-dep library for random number generation
BuildArch:      noarch
%description -n %{name}+chacha-devel

This package contains library source intended for building other packages which
use the "chacha" feature of the "%{crate}" crate.

%package     -n %{name}+getrandom-devel
Summary:        Tiny, fast, zero-dep library for random number generation
BuildArch:      noarch
%description -n %{name}+getrandom-devel

This package contains library source intended for building other packages which
use the "getrandom" feature of the "%{crate}" crate.

%package     -n %{name}+pcg64-devel
Summary:        Tiny, fast, zero-dep library for random number generation
BuildArch:      noarch
%description -n %{name}+pcg64-devel

This package contains library source intended for building other packages which
use the "pcg64" feature of the "%{crate}" crate.

%package     -n %{name}+rdseed-devel
Summary:        Tiny, fast, zero-dep library for random number generation
BuildArch:      noarch
%description -n %{name}+rdseed-devel

This package contains library source intended for building other packages which
use the "rdseed" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Tiny, fast, zero-dep library for random number generation
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+tls-devel
Summary:        Tiny, fast, zero-dep library for random number generation
BuildArch:      noarch
%description -n %{name}+tls-devel

This package contains library source intended for building other packages which
use the "tls" feature of the "%{crate}" crate.

%package     -n %{name}+wyrand-devel
Summary:        Tiny, fast, zero-dep library for random number generation
BuildArch:      noarch
%description -n %{name}+wyrand-devel

This package contains library source intended for building other packages which
use the "wyrand" feature of the "%{crate}" crate.

%package     -n %{name}+zeroize-devel
Summary:        Tiny, fast, zero-dep library for random number generation
BuildArch:      noarch
%description -n %{name}+zeroize-devel

This package contains library source intended for building other packages which
use the "zeroize" feature of the "%{crate}" crate.

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
%files -n rust-nanorand-devel -f %{oreon_filedir}/rust-nanorand-devel.list

%changelog

%autochangelog
