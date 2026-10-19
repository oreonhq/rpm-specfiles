%global source0_hash f1bddf1187be692e79c5ffeab891132dfb0f236ed36a43c7ed39f1165ee20191
%bcond check 0
%global debug_package %{nil}
%global crate vec_map
Name:           rust-vec_map
Version:        0.8.2
Release:        1%{?dist}
Summary:        A simple map based on a vector for small integer keys
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/vec_map
Source0:        https://static.crates.io/crates/vec_map/vec_map-%{version}.crate
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
Summary:        A simple map based on a vector for small integer keys
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+eders-devel
Summary:        A simple map based on a vector for small integer keys
BuildArch:      noarch
%description -n %{name}+eders-devel

This package contains library source intended for building other packages which
use the "eders" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        A simple map based on a vector for small integer keys
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
%files -n rust-vec_map-devel -f %{oreon_filedir}/rust-vec_map-devel.list

%changelog

%autochangelog
