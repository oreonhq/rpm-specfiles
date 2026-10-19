%global source0_hash b4c5cc86750666a3ed20bdaf5ca2a0344f9c67674cae0515bec2da16fbaa47db
%bcond check 0
%global debug_package %{nil}
%global crate petgraph
Name:           rust-petgraph0.6
Version:        0.6.5
Release:        1%{?dist}
Summary:        Graph data structure library. Provides graph types and graph algorithms.
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/petgraph
Source0:        https://static.crates.io/crates/petgraph/petgraph-%{version}.crate
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
Summary:        Graph data structure library. Provides graph types and graph algorithms.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+all-devel
Summary:        Graph data structure library. Provides graph types and graph algorithms.
BuildArch:      noarch
%description -n %{name}+all-devel

This package contains library source intended for building other packages which
use the "all" feature of the "%{crate}" crate.

%package     -n %{name}+generate-devel
Summary:        Graph data structure library. Provides graph types and graph algorithms.
BuildArch:      noarch
%description -n %{name}+generate-devel

This package contains library source intended for building other packages which
use the "generate" feature of the "%{crate}" crate.

%package     -n %{name}+graphmap-devel
Summary:        Graph data structure library. Provides graph types and graph algorithms.
BuildArch:      noarch
%description -n %{name}+graphmap-devel

This package contains library source intended for building other packages which
use the "graphmap" feature of the "%{crate}" crate.

%package     -n %{name}+matrix_graph-devel
Summary:        Graph data structure library. Provides graph types and graph algorithms.
BuildArch:      noarch
%description -n %{name}+matrix_graph-devel

This package contains library source intended for building other packages which
use the "matrix_graph" feature of the "%{crate}" crate.

%package     -n %{name}+quickcheck-devel
Summary:        Graph data structure library. Provides graph types and graph algorithms.
BuildArch:      noarch
%description -n %{name}+quickcheck-devel

This package contains library source intended for building other packages which
use the "quickcheck" feature of the "%{crate}" crate.

%package     -n %{name}+rayon-devel
Summary:        Graph data structure library. Provides graph types and graph algorithms.
BuildArch:      noarch
%description -n %{name}+rayon-devel

This package contains library source intended for building other packages which
use the "rayon" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Graph data structure library. Provides graph types and graph algorithms.
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+serde-1-devel
Summary:        Graph data structure library. Provides graph types and graph algorithms.
BuildArch:      noarch
%description -n %{name}+serde-1-devel

This package contains library source intended for building other packages which
use the "serde-1" feature of the "%{crate}" crate.

%package     -n %{name}+serde_derive-devel
Summary:        Graph data structure library. Provides graph types and graph algorithms.
BuildArch:      noarch
%description -n %{name}+serde_derive-devel

This package contains library source intended for building other packages which
use the "serde_derive" feature of the "%{crate}" crate.

%package     -n %{name}+stable_graph-devel
Summary:        Graph data structure library. Provides graph types and graph algorithms.
BuildArch:      noarch
%description -n %{name}+stable_graph-devel

This package contains library source intended for building other packages which
use the "stable_graph" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-devel
Summary:        Graph data structure library. Provides graph types and graph algorithms.
BuildArch:      noarch
%description -n %{name}+unstable-devel

This package contains library source intended for building other packages which
use the "unstable" feature of the "%{crate}" crate.

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
%files -n rust-petgraph0.6-devel -f %{oreon_filedir}/rust-petgraph0.6-devel.list

%changelog

%autochangelog
