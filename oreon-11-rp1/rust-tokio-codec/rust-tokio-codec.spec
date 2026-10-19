%global source0_hash 25b2998660ba0e70d18684de5d06b70b70a3a747469af9dea7618cc59e75976b
%bcond check 0
%global debug_package %{nil}
%global crate tokio-codec
Name:           rust-tokio-codec
Version:        0.1.2
Release:        1%{?dist}
Summary:        Utilities for encoding and decoding frames.
License:        MIT
URL:            https://crates.io/crates/tokio-codec
Source0:        https://static.crates.io/crates/tokio-codec/tokio-codec-%{version}.crate
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
Summary:        Utilities for encoding and decoding frames.
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
%files -n rust-tokio-codec-devel -f %{oreon_filedir}/rust-tokio-codec-devel.list

%changelog

%autochangelog
