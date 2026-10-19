%global source0_hash 1297656b3c221f5251560da47ce530d981345d3dabe822067c18ecb36e67aacb
%bcond check 0
%global debug_package %{nil}
%global crate bytelines
Name:           rust-bytelines
Version:        2.5.0
Release:        1%{?dist}
Summary:        Read input lines as byte slices for high efficiency
License:        MIT
URL:            https://crates.io/crates/bytelines
Source0:        https://static.crates.io/crates/bytelines/bytelines-%{version}.crate
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
Summary:        Read input lines as byte slices for high efficiency
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+futures-util-devel
Summary:        Read input lines as byte slices for high efficiency
BuildArch:      noarch
%description -n %{name}+futures-util-devel

This package contains library source intended for building other packages which
use the "futures-util" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-devel
Summary:        Read input lines as byte slices for high efficiency
BuildArch:      noarch
%description -n %{name}+tokio-devel

This package contains library source intended for building other packages which
use the "tokio" feature of the "%{crate}" crate.

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
%files -n rust-bytelines-devel -f %{oreon_filedir}/rust-bytelines-devel.list

%changelog

%autochangelog
