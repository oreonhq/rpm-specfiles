%global source0_hash 73891b98dabbe836d23a094941e6ec891bc4880e771faea98813f2ff27ede473
%bcond check 0
%global debug_package %{nil}
%global crate readwrite
Name:           rust-readwrite
Version:        0.1.2
Release:        1%{?dist}
Summary:        Combine Read and Write into a single Read+Write object
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/readwrite
Source0:        https://static.crates.io/crates/readwrite/readwrite-%{version}.crate
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

%package     -n %{name}+futures-devel
Summary:        Combine Read and Write into a single Read+Write object
BuildArch:      noarch
%description -n %{name}+futures-devel

This package contains library source intended for building other packages which
use the "futures" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-devel
Summary:        Combine Read and Write into a single Read+Write object
BuildArch:      noarch
%description -n %{name}+tokio-devel

This package contains library source intended for building other packages which
use the "tokio" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-io-devel
Summary:        Combine Read and Write into a single Read+Write object
BuildArch:      noarch
%description -n %{name}+tokio-io-devel

This package contains library source intended for building other packages which
use the "tokio-io" feature of the "%{crate}" crate.

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
%files -n rust-readwrite-devel -f %{oreon_filedir}/rust-readwrite-devel.list

%changelog

%autochangelog
