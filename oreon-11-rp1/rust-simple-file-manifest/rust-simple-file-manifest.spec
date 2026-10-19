%global source0_hash 5dd19be0257552dd56d1bb6946f89f193c6e5b9f13cc9327c4bc84a357507c74
%bcond check 0
%global debug_package %{nil}
%global crate simple-file-manifest
Name:           rust-simple-file-manifest
Version:        0.11.0
Release:        1%{?dist}
Summary:        Interact with lists of files through a storage-agnostic interface
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/simple-file-manifest
Source0:        https://static.crates.io/crates/simple-file-manifest/simple-file-manifest-%{version}.crate
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
Summary:        Interact with lists of files through a storage-agnostic interface
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
%files -n rust-simple-file-manifest-devel -f %{oreon_filedir}/rust-simple-file-manifest-devel.list

%changelog

%autochangelog
