%global source0_hash f05cd8797d63865425ff89b5c4a48804f35ba0ce8d125800027ad6017d2b5249
%bcond check 1
%global debug_package %{nil}
%global cargo_install_bin 0
%global crate zopfli
Name:           rust-zopfli
Version:        0.8.3
Release:        1%{?dist}
Summary:        Rust implementation of the Zopfli compression algorithm
License:        Apache-2.0
URL:            https://crates.io/crates/zopfli
Source0:        https://static.crates.io/crates/zopfli/zopfli-%{version}.crate
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
Summary:        Rust implementation of the Zopfli compression algorithm
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+gzip-devel
Summary:        Rust implementation of the Zopfli compression algorithm
BuildArch:      noarch
%description -n %{name}+gzip-devel

This package contains library source intended for building other packages which
use the "gzip" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Rust implementation of the Zopfli compression algorithm
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+zlib-devel
Summary:        Rust implementation of the Zopfli compression algorithm
BuildArch:      noarch
%description -n %{name}+zlib-devel

This package contains library source intended for building other packages which
use the "zlib" feature of the "%{crate}" crate.

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
%files -n rust-zopfli-devel -f %{oreon_filedir}/rust-zopfli-devel.list

%changelog

%autochangelog
