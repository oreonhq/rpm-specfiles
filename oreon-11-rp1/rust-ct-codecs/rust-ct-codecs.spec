%global source0_hash 49fb0c6640b4507ebd99ff67677009e381ba5eee1d14df78de4a3d16eb123c39
%bcond check 0
%global debug_package %{nil}
%global crate ct-codecs
Name:           rust-ct-codecs
Version:        1.1.7
Release:        1%{?dist}
Summary:        Constant-time base64, base32, and hex codecs reimplemented in Rust
License:        MIT
URL:            https://crates.io/crates/ct-codecs
Source0:        https://static.crates.io/crates/ct-codecs/ct-codecs-%{version}.crate
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
Summary:        Constant-time base64, base32, and hex codecs reimplemented in Rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Constant-time base64, base32, and hex codecs reimplemented in Rust
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
%files -n rust-ct-codecs-devel -f %{oreon_filedir}/rust-ct-codecs-devel.list

%changelog

%autochangelog
