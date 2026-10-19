%global source0_hash 4bb5d8e7814e92297b0e1c773ce43d290bef6c17452dafd9fc49e5edb5beba71
%bcond check 0
%global debug_package %{nil}
%global crate webp
Name:           rust-webp
Version:        0.2.6
Release:        1%{?dist}
Summary:        WebP conversion library.
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/webp
Source0:        https://static.crates.io/crates/webp/webp-%{version}.crate
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
Summary:        WebP conversion library.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+image-devel
Summary:        WebP conversion library.
BuildArch:      noarch
%description -n %{name}+image-devel

This package contains library source intended for building other packages which
use the "image" feature of the "%{crate}" crate.

%package     -n %{name}+img-devel
Summary:        WebP conversion library.
BuildArch:      noarch
%description -n %{name}+img-devel

This package contains library source intended for building other packages which
use the "img" feature of the "%{crate}" crate.

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
%files -n rust-webp-devel -f %{oreon_filedir}/rust-webp-devel.list

%changelog

%autochangelog
