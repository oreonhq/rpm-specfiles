%global source0_hash 33d281d46f6b275c61bbe9ca3b55613c39018586dccbc537456ecaac7bb5377a
%bcond check 1
%global debug_package %{nil}
%global crate timestamped-socket
Name:           rust-timestamped-socket
Version:        0.2.7
Release:        1%{?dist}
Summary:        Implementation of async UDP and raw ethernet sockets with timestamping
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/timestamped-socket
Source0:        https://static.crates.io/crates/timestamped-socket/timestamped-socket-%{version}.crate
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
Summary:        Implementation of async UDP and raw ethernet sockets with timestamping
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Implementation of async UDP and raw ethernet sockets with timestamping
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

%cargo_test -- -- --exact --skip socket::linux::tests::test_software_timestamping
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-timestamped-socket-devel -f %{oreon_filedir}/rust-timestamped-socket-devel.list

%changelog

%autochangelog
