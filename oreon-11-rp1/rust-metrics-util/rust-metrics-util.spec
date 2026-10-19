%global source0_hash cdfb1365fea27e6dd9dc1dbc19f570198bc86914533ad639dae939635f096be4
%bcond check 0
%global debug_package %{nil}
%global crate metrics-util
Name:           rust-metrics-util
Version:        0.20.1
Release:        1%{?dist}
Summary:        Helper types/functions used by the metrics ecosystem
License:        MIT
URL:            https://crates.io/crates/metrics-util
Source0:        https://static.crates.io/crates/metrics-util/metrics-util-%{version}.crate
Patch:          metrics-util-fix-metadata.diff
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
Summary:        Helper types/functions used by the metrics ecosystem
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+ahash-devel
Summary:        Helper types/functions used by the metrics ecosystem
BuildArch:      noarch
%description -n %{name}+ahash-devel

This package contains library source intended for building other packages which
use the "ahash" feature of the "%{crate}" crate.

%package     -n %{name}+aho-corasick-devel
Summary:        Helper types/functions used by the metrics ecosystem
BuildArch:      noarch
%description -n %{name}+aho-corasick-devel

This package contains library source intended for building other packages which
use the "aho-corasick" feature of the "%{crate}" crate.

%package     -n %{name}+crossbeam-epoch-devel
Summary:        Helper types/functions used by the metrics ecosystem
BuildArch:      noarch
%description -n %{name}+crossbeam-epoch-devel

This package contains library source intended for building other packages which
use the "crossbeam-epoch" feature of the "%{crate}" crate.

%package     -n %{name}+crossbeam-utils-devel
Summary:        Helper types/functions used by the metrics ecosystem
BuildArch:      noarch
%description -n %{name}+crossbeam-utils-devel

This package contains library source intended for building other packages which
use the "crossbeam-utils" feature of the "%{crate}" crate.

%package     -n %{name}+debugging-devel
Summary:        Helper types/functions used by the metrics ecosystem
BuildArch:      noarch
%description -n %{name}+debugging-devel

This package contains library source intended for building other packages which
use the "debugging" feature of the "%{crate}" crate.

%package     -n %{name}+hashbrown-devel
Summary:        Helper types/functions used by the metrics ecosystem
BuildArch:      noarch
%description -n %{name}+hashbrown-devel

This package contains library source intended for building other packages which
use the "hashbrown" feature of the "%{crate}" crate.

%package     -n %{name}+indexmap-devel
Summary:        Helper types/functions used by the metrics ecosystem
BuildArch:      noarch
%description -n %{name}+indexmap-devel

This package contains library source intended for building other packages which
use the "indexmap" feature of the "%{crate}" crate.

%package     -n %{name}+layer-filter-devel
Summary:        Helper types/functions used by the metrics ecosystem
BuildArch:      noarch
%description -n %{name}+layer-filter-devel

This package contains library source intended for building other packages which
use the "layer-filter" feature of the "%{crate}" crate.

%package     -n %{name}+layer-router-devel
Summary:        Helper types/functions used by the metrics ecosystem
BuildArch:      noarch
%description -n %{name}+layer-router-devel

This package contains library source intended for building other packages which
use the "layer-router" feature of the "%{crate}" crate.

%package     -n %{name}+layers-devel
Summary:        Helper types/functions used by the metrics ecosystem
BuildArch:      noarch
%description -n %{name}+layers-devel

This package contains library source intended for building other packages which
use the "layers" feature of the "%{crate}" crate.

%package     -n %{name}+ordered-float-devel
Summary:        Helper types/functions used by the metrics ecosystem
BuildArch:      noarch
%description -n %{name}+ordered-float-devel

This package contains library source intended for building other packages which
use the "ordered-float" feature of the "%{crate}" crate.

%package     -n %{name}+quanta-devel
Summary:        Helper types/functions used by the metrics ecosystem
BuildArch:      noarch
%description -n %{name}+quanta-devel

This package contains library source intended for building other packages which
use the "quanta" feature of the "%{crate}" crate.

%package     -n %{name}+radix_trie-devel
Summary:        Helper types/functions used by the metrics ecosystem
BuildArch:      noarch
%description -n %{name}+radix_trie-devel

This package contains library source intended for building other packages which
use the "radix_trie" feature of the "%{crate}" crate.

%package     -n %{name}+rand-devel
Summary:        Helper types/functions used by the metrics ecosystem
BuildArch:      noarch
%description -n %{name}+rand-devel

This package contains library source intended for building other packages which
use the "rand" feature of the "%{crate}" crate.

%package     -n %{name}+rand_xoshiro-devel
Summary:        Helper types/functions used by the metrics ecosystem
BuildArch:      noarch
%description -n %{name}+rand_xoshiro-devel

This package contains library source intended for building other packages which
use the "rand_xoshiro" feature of the "%{crate}" crate.

%package     -n %{name}+recency-devel
Summary:        Helper types/functions used by the metrics ecosystem
BuildArch:      noarch
%description -n %{name}+recency-devel

This package contains library source intended for building other packages which
use the "recency" feature of the "%{crate}" crate.

%package     -n %{name}+registry-devel
Summary:        Helper types/functions used by the metrics ecosystem
BuildArch:      noarch
%description -n %{name}+registry-devel

This package contains library source intended for building other packages which
use the "registry" feature of the "%{crate}" crate.

%package     -n %{name}+sketches-ddsketch-devel
Summary:        Helper types/functions used by the metrics ecosystem
BuildArch:      noarch
%description -n %{name}+sketches-ddsketch-devel

This package contains library source intended for building other packages which
use the "sketches-ddsketch" feature of the "%{crate}" crate.

%package     -n %{name}+storage-devel
Summary:        Helper types/functions used by the metrics ecosystem
BuildArch:      noarch
%description -n %{name}+storage-devel

This package contains library source intended for building other packages which
use the "storage" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build -a
%install
%cargo_install -a
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test -a
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-metrics-util-devel -f %{oreon_filedir}/rust-metrics-util-devel.list

%changelog

%autochangelog
