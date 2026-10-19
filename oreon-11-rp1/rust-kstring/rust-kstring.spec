%global source0_hash b609e7ca5ea38f093c20a4a102335b247221c9643b7a6bc3510f196f99499a9e
%bcond check 0
%global debug_package %{nil}
%global crate kstring
Name:           rust-kstring
Version:        2.0.4
Release:        1%{?dist}
Summary:        Key String: optimized for map keys
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/kstring
Source0:        https://static.crates.io/crates/kstring/kstring-%{version}.crate
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
Summary:        Key String: optimized for map keys
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+arc-devel
Summary:        Key String: optimized for map keys
BuildArch:      noarch
%description -n %{name}+arc-devel

This package contains library source intended for building other packages which
use the "arc" feature of the "%{crate}" crate.

%package     -n %{name}+document-features-devel
Summary:        Key String: optimized for map keys
BuildArch:      noarch
%description -n %{name}+document-features-devel

This package contains library source intended for building other packages which
use the "document-features" feature of the "%{crate}" crate.

%package     -n %{name}+max_inline-devel
Summary:        Key String: optimized for map keys
BuildArch:      noarch
%description -n %{name}+max_inline-devel

This package contains library source intended for building other packages which
use the "max_inline" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Key String: optimized for map keys
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Key String: optimized for map keys
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+unsafe-devel
Summary:        Key String: optimized for map keys
BuildArch:      noarch
%description -n %{name}+unsafe-devel

This package contains library source intended for building other packages which
use the "unsafe" feature of the "%{crate}" crate.

%package     -n %{name}+unstable_bench_subset-devel
Summary:        Key String: optimized for map keys
BuildArch:      noarch
%description -n %{name}+unstable_bench_subset-devel

This package contains library source intended for building other packages which
use the "unstable_bench_subset" feature of the "%{crate}" crate.

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
%files -n rust-kstring-devel -f %{oreon_filedir}/rust-kstring-devel.list

%changelog

%autochangelog
