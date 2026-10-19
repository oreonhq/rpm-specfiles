%global source0_hash c0452a60c1863c1f50b5f77cd295e8d2786849f35883f0b9e18e7e6e1b5691b0
%bcond check 0
%global debug_package %{nil}
%global cargo_install_bin 0
%global crate minicbor
Name:           rust-minicbor
Version:        0.25.1
Release:        1%{?dist}
Summary:        Small CBOR codec suitable for no_std environments
License:        BlueOak-1.0.0
URL:            https://crates.io/crates/minicbor
Source0:        https://static.crates.io/crates/minicbor/minicbor-%{version}.crate
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
Summary:        Small CBOR codec suitable for no_std environments
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Small CBOR codec suitable for no_std environments
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+derive-devel
Summary:        Small CBOR codec suitable for no_std environments
BuildArch:      noarch
%description -n %{name}+derive-devel

This package contains library source intended for building other packages which
use the "derive" feature of the "%{crate}" crate.

%package     -n %{name}+full-devel
Summary:        Small CBOR codec suitable for no_std environments
BuildArch:      noarch
%description -n %{name}+full-devel

This package contains library source intended for building other packages which
use the "full" feature of the "%{crate}" crate.

%package     -n %{name}+half-devel
Summary:        Small CBOR codec suitable for no_std environments
BuildArch:      noarch
%description -n %{name}+half-devel

This package contains library source intended for building other packages which
use the "half" feature of the "%{crate}" crate.

%package     -n %{name}+minicbor-derive-devel
Summary:        Small CBOR codec suitable for no_std environments
BuildArch:      noarch
%description -n %{name}+minicbor-derive-devel

This package contains library source intended for building other packages which
use the "minicbor-derive" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Small CBOR codec suitable for no_std environments
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build -f half,std
%install
%cargo_install -f half,std
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test -f half,std
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-minicbor-devel -f %{oreon_filedir}/rust-minicbor-devel.list

%changelog

%autochangelog
