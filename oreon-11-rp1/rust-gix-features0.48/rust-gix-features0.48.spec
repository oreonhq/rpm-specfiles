%global source0_hash 1849ae154d38bc403185be14fa871e38e3c93ee606875d94e207fdb9fba52dbc
%bcond check 0
%global debug_package %{nil}
%global crate gix-features
Name:           rust-gix-features0.48
Version:        0.48.1
Release:        1%{?dist}
Summary:        A crate to integrate various capabilities using compile-time feature...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/gix-features
Source0:        https://static.crates.io/crates/gix-features/gix-features-%{version}.crate
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
Summary:        A crate to integrate various capabilities using compile-time feature...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+bytes-devel
Summary:        A crate to integrate various capabilities using compile-time feature...
BuildArch:      noarch
%description -n %{name}+bytes-devel

This package contains library source intended for building other packages which
use the "bytes" feature of the "%{crate}" crate.

%package     -n %{name}+bytesize-devel
Summary:        A crate to integrate various capabilities using compile-time feature...
BuildArch:      noarch
%description -n %{name}+bytesize-devel

This package contains library source intended for building other packages which
use the "bytesize" feature of the "%{crate}" crate.

%package     -n %{name}+cache-efficiency-debug-devel
Summary:        A crate to integrate various capabilities using compile-time feature...
BuildArch:      noarch
%description -n %{name}+cache-efficiency-debug-devel

This package contains library source intended for building other packages which
use the "cache-efficiency-debug" feature of the "%{crate}" crate.

%package     -n %{name}+crc32-devel
Summary:        A crate to integrate various capabilities using compile-time feature...
BuildArch:      noarch
%description -n %{name}+crc32-devel

This package contains library source intended for building other packages which
use the "crc32" feature of the "%{crate}" crate.

%package     -n %{name}+crc32fast-devel
Summary:        A crate to integrate various capabilities using compile-time feature...
BuildArch:      noarch
%description -n %{name}+crc32fast-devel

This package contains library source intended for building other packages which
use the "crc32fast" feature of the "%{crate}" crate.

%package     -n %{name}+crossbeam-channel-devel
Summary:        A crate to integrate various capabilities using compile-time feature...
BuildArch:      noarch
%description -n %{name}+crossbeam-channel-devel

This package contains library source intended for building other packages which
use the "crossbeam-channel" feature of the "%{crate}" crate.

%package     -n %{name}+document-features-devel
Summary:        A crate to integrate various capabilities using compile-time feature...
BuildArch:      noarch
%description -n %{name}+document-features-devel

This package contains library source intended for building other packages which
use the "document-features" feature of the "%{crate}" crate.

%package     -n %{name}+fs-read-dir-devel
Summary:        A crate to integrate various capabilities using compile-time feature...
BuildArch:      noarch
%description -n %{name}+fs-read-dir-devel

This package contains library source intended for building other packages which
use the "fs-read-dir" feature of the "%{crate}" crate.

%package     -n %{name}+gix-path-devel
Summary:        A crate to integrate various capabilities using compile-time feature...
BuildArch:      noarch
%description -n %{name}+gix-path-devel

This package contains library source intended for building other packages which
use the "gix-path" feature of the "%{crate}" crate.

%package     -n %{name}+gix-utils-devel
Summary:        A crate to integrate various capabilities using compile-time feature...
BuildArch:      noarch
%description -n %{name}+gix-utils-devel

This package contains library source intended for building other packages which
use the "gix-utils" feature of the "%{crate}" crate.

%package     -n %{name}+io-pipe-devel
Summary:        A crate to integrate various capabilities using compile-time feature...
BuildArch:      noarch
%description -n %{name}+io-pipe-devel

This package contains library source intended for building other packages which
use the "io-pipe" feature of the "%{crate}" crate.

%package     -n %{name}+once_cell-devel
Summary:        A crate to integrate various capabilities using compile-time feature...
BuildArch:      noarch
%description -n %{name}+once_cell-devel

This package contains library source intended for building other packages which
use the "once_cell" feature of the "%{crate}" crate.

%package     -n %{name}+parallel-devel
Summary:        A crate to integrate various capabilities using compile-time feature...
BuildArch:      noarch
%description -n %{name}+parallel-devel

This package contains library source intended for building other packages which
use the "parallel" feature of the "%{crate}" crate.

%package     -n %{name}+parking_lot-devel
Summary:        A crate to integrate various capabilities using compile-time feature...
BuildArch:      noarch
%description -n %{name}+parking_lot-devel

This package contains library source intended for building other packages which
use the "parking_lot" feature of the "%{crate}" crate.

%package     -n %{name}+prodash-devel
Summary:        A crate to integrate various capabilities using compile-time feature...
BuildArch:      noarch
%description -n %{name}+prodash-devel

This package contains library source intended for building other packages which
use the "prodash" feature of the "%{crate}" crate.

%package     -n %{name}+progress-devel
Summary:        A crate to integrate various capabilities using compile-time feature...
BuildArch:      noarch
%description -n %{name}+progress-devel

This package contains library source intended for building other packages which
use the "progress" feature of the "%{crate}" crate.

%package     -n %{name}+progress-unit-bytes-devel
Summary:        A crate to integrate various capabilities using compile-time feature...
BuildArch:      noarch
%description -n %{name}+progress-unit-bytes-devel

This package contains library source intended for building other packages which
use the "progress-unit-bytes" feature of the "%{crate}" crate.

%package     -n %{name}+progress-unit-human-numbers-devel
Summary:        A crate to integrate various capabilities using compile-time feature...
BuildArch:      noarch
%description -n %{name}+progress-unit-human-numbers-devel

This package contains library source intended for building other packages which
use the "progress-unit-human-numbers" feature of the "%{crate}" crate.

%package     -n %{name}+thiserror-devel
Summary:        A crate to integrate various capabilities using compile-time feature...
BuildArch:      noarch
%description -n %{name}+thiserror-devel

This package contains library source intended for building other packages which
use the "thiserror" feature of the "%{crate}" crate.

%package     -n %{name}+tracing-devel
Summary:        A crate to integrate various capabilities using compile-time feature...
BuildArch:      noarch
%description -n %{name}+tracing-devel

This package contains library source intended for building other packages which
use the "tracing" feature of the "%{crate}" crate.

%package     -n %{name}+tracing-detail-devel
Summary:        A crate to integrate various capabilities using compile-time feature...
BuildArch:      noarch
%description -n %{name}+tracing-detail-devel

This package contains library source intended for building other packages which
use the "tracing-detail" feature of the "%{crate}" crate.

%package     -n %{name}+walkdir-devel
Summary:        A crate to integrate various capabilities using compile-time feature...
BuildArch:      noarch
%description -n %{name}+walkdir-devel

This package contains library source intended for building other packages which
use the "walkdir" feature of the "%{crate}" crate.

%package     -n %{name}+zlib-devel
Summary:        A crate to integrate various capabilities using compile-time feature...
BuildArch:      noarch
%description -n %{name}+zlib-devel

This package contains library source intended for building other packages which
use the "zlib" feature of the "%{crate}" crate.

%package     -n %{name}+zlib-rs-devel
Summary:        A crate to integrate various capabilities using compile-time feature...
BuildArch:      noarch
%description -n %{name}+zlib-rs-devel

This package contains library source intended for building other packages which
use the "zlib-rs" feature of the "%{crate}" crate.

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
%files -n rust-gix-features0.48-devel -f %{oreon_filedir}/rust-gix-features0.48-devel.list

%changelog

%autochangelog
