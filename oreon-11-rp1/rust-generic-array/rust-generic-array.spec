%global source0_hash 337d46834ee672ab3e48caca2cb0c78cc174fb12b3a68d0d88f99a0519a5e36e
%bcond check 0
%global debug_package %{nil}
%global crate generic-array
Name:           rust-generic-array
Version:        1.4.5
Release:        1%{?dist}
Summary:        Generic types implementing functionality of arrays
License:        MIT
URL:            https://crates.io/crates/generic-array
Source0:        https://static.crates.io/crates/generic-array/generic-array-%{version}.crate
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

%package     -n %{name}+alloc-devel
Summary:        Generic types implementing functionality of arrays
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+as_slice-devel
Summary:        Generic types implementing functionality of arrays
BuildArch:      noarch
%description -n %{name}+as_slice-devel

This package contains library source intended for building other packages which
use the "as_slice" feature of the "%{crate}" crate.

%package     -n %{name}+bitvec-devel
Summary:        Generic types implementing functionality of arrays
BuildArch:      noarch
%description -n %{name}+bitvec-devel

This package contains library source intended for building other packages which
use the "bitvec" feature of the "%{crate}" crate.

%package     -n %{name}+bytecheck-0_8-devel
Summary:        Generic types implementing functionality of arrays
BuildArch:      noarch
%description -n %{name}+bytecheck-0_8-devel

This package contains library source intended for building other packages which
use the "bytecheck-0_8" feature of the "%{crate}" crate.

%package     -n %{name}+compat-0_14-devel
Summary:        Generic types implementing functionality of arrays
BuildArch:      noarch
%description -n %{name}+compat-0_14-devel

This package contains library source intended for building other packages which
use the "compat-0_14" feature of the "%{crate}" crate.

%package     -n %{name}+internals-devel
Summary:        Generic types implementing functionality of arrays
BuildArch:      noarch
%description -n %{name}+internals-devel

This package contains library source intended for building other packages which
use the "internals" feature of the "%{crate}" crate.

%package     -n %{name}+rkyv-0_8-devel
Summary:        Generic types implementing functionality of arrays
BuildArch:      noarch
%description -n %{name}+rkyv-0_8-devel

This package contains library source intended for building other packages which
use the "rkyv-0_8" feature of the "%{crate}" crate.

%package     -n %{name}+rkyv-0_8-full-devel
Summary:        Generic types implementing functionality of arrays
BuildArch:      noarch
%description -n %{name}+rkyv-0_8-full-devel

This package contains library source intended for building other packages which
use the "rkyv-0_8-full" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Generic types implementing functionality of arrays
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

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
%files -n rust-generic-array-devel -f %{oreon_filedir}/rust-generic-array-devel.list

%changelog

%autochangelog
