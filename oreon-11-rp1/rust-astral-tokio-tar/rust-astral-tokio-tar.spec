%global source0_hash 3c23f3af104b40a3430ccb90ed5f7bd877a8dc5c26fc92fde51a22b40890dcf9
%bcond check 1
%global debug_package %{nil}
%global crate astral-tokio-tar
Name:           rust-astral-tokio-tar
Version:        0.6.0
Release:        1%{?dist}
Summary:        Rust implementation of an async TAR file reader and writer
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/astral-tokio-tar
Source0:        https://static.crates.io/crates/astral-tokio-tar/astral-tokio-tar-%{version}.crate
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
Summary:        Rust implementation of an async TAR file reader and writer
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+xattr-devel
Summary:        Rust implementation of an async TAR file reader and writer
BuildArch:      noarch
%description -n %{name}+xattr-devel

This package contains library source intended for building other packages which
use the "xattr" feature of the "%{crate}" crate.

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
%files -n rust-astral-tokio-tar-devel -f %{oreon_filedir}/rust-astral-tokio-tar-devel.list

%changelog

%autochangelog
