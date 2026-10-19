%global source0_hash 4be19f09d0c923815078f0f01e1313e539c4048d62abe2f42c1e4e81d32e517e
%bcond check 1
%global crate cargo-vendor-filterer
Name:           rust-cargo-vendor-filterer
Version:        0.5.18
Release:        1%{?dist}
Summary:        Cargo vendor, but with filtering for platforms and more
License:        Apache-2.0
URL:            https://crates.io/crates/cargo-vendor-filterer
Source0:        https://static.crates.io/crates/cargo-vendor-filterer/cargo-vendor-filterer-%{version}.crate
Patch:          cargo-vendor-filterer-fix-metadata.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Cargo vendor, but with filtering for platforms and more
License:        %{shrink:
    (0BSD OR MIT OR Apache-2.0) AND
    Apache-2.0 AND
    (Apache-2.0 OR MIT) AND
    (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
    MIT AND
    (MIT OR Zlib OR Apache-2.0)
    (Unlicense OR MIT) AND
    Unicode-3.0
    }
%description -n %{crate}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Cargo vendor, but with filtering for platforms and more
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+openssl-devel
Summary:        Cargo vendor, but with filtering for platforms and more
BuildArch:      noarch
%description -n %{name}+openssl-devel

This package contains library source intended for building other packages which
use the "openssl" feature of the "%{crate}" crate.

%package     -n %{name}+sha-rs-devel
Summary:        Cargo vendor, but with filtering for platforms and more
BuildArch:      noarch
%description -n %{name}+sha-rs-devel

This package contains library source intended for building other packages which
use the "sha-rs" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build -f openssl
%{cargo_license_summary -f openssl}
%{cargo_license -f openssl} > LICENSE.dependencies
%install
%cargo_install -f openssl
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test -f openssl -- -- --skip vendor_filterer::
%endif
%files -f %{oreon_filedir}/main.list
%files -n cargo-vendor-filterer -f %{oreon_filedir}/cargo-vendor-filterer.list
%files -n rust-cargo-vendor-filterer-devel -f %{oreon_filedir}/rust-cargo-vendor-filterer-devel.list

%changelog

%autochangelog
