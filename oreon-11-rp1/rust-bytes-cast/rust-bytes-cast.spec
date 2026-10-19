%global source0_hash a20de93b91d7703ca0e39e12930e310acec5ff4d715f4166e0ab026babb352e8
%bcond check 0
%global debug_package %{nil}
%global crate bytes-cast
Name:           rust-bytes-cast
Version:        0.3.0
Release:        1%{?dist}
Summary:        Safely re-interpreting &[u8] bytes as custom structs without copying, for efficiently reading structured binary data
License:        Zlib OR Apache-2.0 OR MIT
URL:            https://crates.io/crates/bytes-cast
Source0:        https://static.crates.io/crates/bytes-cast/bytes-cast-%{version}.crate
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
Summary:        Safely re-interpreting &[u8] bytes as custom structs without copying, for efficiently reading structured binary data
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

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
%files -n rust-bytes-cast-devel -f %{oreon_filedir}/rust-bytes-cast-devel.list

%changelog

%autochangelog
