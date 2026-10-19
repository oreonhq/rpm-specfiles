%global source0_hash 67dca2c9c51e58a4791a4b1ed58308b39c64224d349a935ab5039aa360942a48
%bcond check 0
%global debug_package %{nil}
%global crate serde_core
Name:           rust-serde_core
Version:        1.0.229
Release:        1%{?dist}
Summary:        Serde traits
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/serde_core
Source0:        https://static.crates.io/crates/serde_core/serde_core-%{version}.crate
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
Summary:        Serde traits
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Serde traits
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+rc-devel
Summary:        Serde traits
BuildArch:      noarch
%description -n %{name}+rc-devel

This package contains library source intended for building other packages which
use the "rc" feature of the "%{crate}" crate.

%package     -n %{name}+result-devel
Summary:        Serde traits
BuildArch:      noarch
%description -n %{name}+result-devel

This package contains library source intended for building other packages which
use the "result" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Serde traits
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-devel
Summary:        Serde traits
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
%files -n rust-serde_core-devel -f %{oreon_filedir}/rust-serde_core-devel.list

%changelog

%autochangelog
