%global source0_hash 0348a1c054491f4bfe6ab86a7b6ab1e44e45d899005de92f58b3df180b36ddaf
%bcond check 0
%global debug_package %{nil}
%global crate arboard
Name:           rust-arboard
Version:        3.6.1
Release:        1%{?dist}
Summary:        Image and text handling for the OS clipboard
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/arboard
Source0:        https://static.crates.io/crates/arboard/arboard-%{version}.crate
Patch:          arboard-fix-metadata-auto.diff
Patch:          arboard-fix-metadata.diff
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
Summary:        Image and text handling for the OS clipboard
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+image-devel
Summary:        Image and text handling for the OS clipboard
BuildArch:      noarch
%description -n %{name}+image-devel

This package contains library source intended for building other packages which
use the "image" feature of the "%{crate}" crate.

%package     -n %{name}+image-data-devel
Summary:        Image and text handling for the OS clipboard
BuildArch:      noarch
%description -n %{name}+image-data-devel

This package contains library source intended for building other packages which
use the "image-data" feature of the "%{crate}" crate.

%package     -n %{name}+wayland-data-control-devel
Summary:        Image and text handling for the OS clipboard
BuildArch:      noarch
%description -n %{name}+wayland-data-control-devel

This package contains library source intended for building other packages which
use the "wayland-data-control" feature of the "%{crate}" crate.

%package     -n %{name}+wl-clipboard-rs-devel
Summary:        Image and text handling for the OS clipboard
BuildArch:      noarch
%description -n %{name}+wl-clipboard-rs-devel

This package contains library source intended for building other packages which
use the "wl-clipboard-rs" feature of the "%{crate}" crate.

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
%files -n rust-arboard-devel -f %{oreon_filedir}/rust-arboard-devel.list

%changelog

%autochangelog
