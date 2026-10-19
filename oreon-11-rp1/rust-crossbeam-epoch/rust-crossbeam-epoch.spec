%global source0_hash dc74980687109a3b14c72fd458107bf0baa1da1a1a805e178d15501ba9b86d9d
%bcond check 1
%global debug_package %{nil}
%global crate crossbeam-epoch
Name:           rust-crossbeam-epoch
Version:        0.9.21
Release:        1%{?dist}
Summary:        Epoch-based garbage collection
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/crossbeam-epoch
Source0:        https://static.crates.io/crates/crossbeam-epoch/crossbeam-epoch-%{version}.crate
Patch:          crossbeam-epoch-fix-metadata-auto.diff
Patch:          crossbeam-epoch-fix-metadata.diff
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
Summary:        Epoch-based garbage collection
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Epoch-based garbage collection
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+nightly-devel
Summary:        Epoch-based garbage collection
BuildArch:      noarch
%description -n %{name}+nightly-devel

This package contains library source intended for building other packages which
use the "nightly" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Epoch-based garbage collection
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
%files -n rust-crossbeam-epoch-devel -f %{oreon_filedir}/rust-crossbeam-epoch-devel.list

%changelog

%autochangelog
