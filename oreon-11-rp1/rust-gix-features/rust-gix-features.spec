%global source0_hash 39c0e59d9d253dcccc38c3a46b91bfb9b46bd63eed54fe1a719e12194884d52a
%bcond check 0
%global debug_package %{nil}
%global crate gix-features
Name:           rust-gix-features
Version:        0.49.1
Release:        2%{?dist}
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
%files -n rust-gix-features-devel -f %{oreon_filedir}/rust-gix-features-devel.list

%changelog

%autochangelog
