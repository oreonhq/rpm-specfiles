%global source0_hash bde5057d6143cc94e861d90f591b9303d6716c6b9602309150bd068853c10899
%bcond check 0
%global debug_package %{nil}
%global crate kasuari
Name:           rust-kasuari
Version:        0.4.12
Release:        1%{?dist}
Summary:        A rust layout solver for GUIs, based on the Cassowary algorithm.
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/kasuari
Source0:        https://static.crates.io/crates/kasuari/kasuari-%{version}.crate
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
Summary:        A rust layout solver for GUIs, based on the Cassowary algorithm.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+document-features-devel
Summary:        A rust layout solver for GUIs, based on the Cassowary algorithm.
BuildArch:      noarch
%description -n %{name}+document-features-devel

This package contains library source intended for building other packages which
use the "document-features" feature of the "%{crate}" crate.

%package     -n %{name}+portable-atomic-devel
Summary:        A rust layout solver for GUIs, based on the Cassowary algorithm.
BuildArch:      noarch
%description -n %{name}+portable-atomic-devel

This package contains library source intended for building other packages which
use the "portable-atomic" feature of the "%{crate}" crate.

%package     -n %{name}+portable-atomic-util-devel
Summary:        A rust layout solver for GUIs, based on the Cassowary algorithm.
BuildArch:      noarch
%description -n %{name}+portable-atomic-util-devel

This package contains library source intended for building other packages which
use the "portable-atomic-util" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        A rust layout solver for GUIs, based on the Cassowary algorithm.
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

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
%files -n rust-kasuari-devel -f %{oreon_filedir}/rust-kasuari-devel.list

%changelog

%autochangelog
