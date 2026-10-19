%global source0_hash 3f6221d9a6003c78398e3b239969f352578258df48c8eb051caadae0015bc840
%bcond check 0
%global debug_package %{nil}
%global crate tar
Name:           rust-tar
Version:        0.4.46
Release:        1%{?dist}
Summary:        A Rust implementation of a TAR file reader and writer. This library d...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/tar
Source0:        https://static.crates.io/crates/tar/tar-%{version}.crate
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
Summary:        A Rust implementation of a TAR file reader and writer. This library d...
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
%files -n rust-tar-devel -f %{oreon_filedir}/rust-tar-devel.list

%changelog

%autochangelog
