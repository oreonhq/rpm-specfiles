%global source0_hash 7f675d0df484a7f6a47e64bd6f311af489d947c0323b0564f36d14f3d7762abb
%bcond check 0
%global debug_package %{nil}
%global crate gix-commitgraph
Name:           rust-gix-commitgraph0.37
Version:        0.37.1
Release:        1%{?dist}
Summary:        Read-only access to the git commitgraph file format
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/gix-commitgraph
Source0:        https://static.crates.io/crates/gix-commitgraph/gix-commitgraph-%{version}.crate
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

%package     -n %{name}+document-features-devel
Summary:        Read-only access to the git commitgraph file format
BuildArch:      noarch
%description -n %{name}+document-features-devel

This package contains library source intended for building other packages which
use the "document-features" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Read-only access to the git commitgraph file format
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+sha1-devel
Summary:        Read-only access to the git commitgraph file format
BuildArch:      noarch
%description -n %{name}+sha1-devel

This package contains library source intended for building other packages which
use the "sha1" feature of the "%{crate}" crate.

%package     -n %{name}+sha256-devel
Summary:        Read-only access to the git commitgraph file format
BuildArch:      noarch
%description -n %{name}+sha256-devel

This package contains library source intended for building other packages which
use the "sha256" feature of the "%{crate}" crate.

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
%files -n rust-gix-commitgraph0.37-devel -f %{oreon_filedir}/rust-gix-commitgraph0.37-devel.list

%changelog

%autochangelog
