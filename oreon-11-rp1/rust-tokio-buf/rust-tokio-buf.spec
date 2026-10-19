%global source0_hash 8fb220f46c53859a4b7ec083e41dec9778ff0b1851c0942b211edb89e0ccdc46
%bcond check 0
%global debug_package %{nil}
%global crate tokio-buf
Name:           rust-tokio-buf
Version:        0.1.1
Release:        1%{?dist}
Summary:        Asynchronous stream of byte buffers
License:        MIT
URL:            https://crates.io/crates/tokio-buf
Source0:        https://static.crates.io/crates/tokio-buf/tokio-buf-%{version}.crate
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
Summary:        Asynchronous stream of byte buffers
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+either-devel
Summary:        Asynchronous stream of byte buffers
BuildArch:      noarch
%description -n %{name}+either-devel

This package contains library source intended for building other packages which
use the "either" feature of the "%{crate}" crate.

%package     -n %{name}+util-devel
Summary:        Asynchronous stream of byte buffers
BuildArch:      noarch
%description -n %{name}+util-devel

This package contains library source intended for building other packages which
use the "util" feature of the "%{crate}" crate.

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
%files -n rust-tokio-buf-devel -f %{oreon_filedir}/rust-tokio-buf-devel.list

%changelog

%autochangelog
