%global source0_hash e4af381fe79fa195b4909485d99f73a80792331df0625188e707854f0b3383f5
%bcond check 0
%global debug_package %{nil}
%global crate path-absolutize
Name:           rust-path-absolutize
Version:        3.1.1
Release:        1%{?dist}
Summary:        Extend Path and PathBuf for getting an absolute path
License:        MIT
URL:            https://crates.io/crates/path-absolutize
Source0:        https://static.crates.io/crates/path-absolutize/path-absolutize-%{version}.crate
Patch:          path-absolutize-fix-metadata-auto.diff
Patch:          path-absolutize-fix-metadata.diff
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
Summary:        Extend Path and PathBuf for getting an absolute path
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+lazy_static_cache-devel
Summary:        Extend Path and PathBuf for getting an absolute path
BuildArch:      noarch
%description -n %{name}+lazy_static_cache-devel

This package contains library source intended for building other packages which
use the "lazy_static_cache" feature of the "%{crate}" crate.

%package     -n %{name}+once_cell_cache-devel
Summary:        Extend Path and PathBuf for getting an absolute path
BuildArch:      noarch
%description -n %{name}+once_cell_cache-devel

This package contains library source intended for building other packages which
use the "once_cell_cache" feature of the "%{crate}" crate.

%package     -n %{name}+unsafe_cache-devel
Summary:        Extend Path and PathBuf for getting an absolute path
BuildArch:      noarch
%description -n %{name}+unsafe_cache-devel

This package contains library source intended for building other packages which
use the "unsafe_cache" feature of the "%{crate}" crate.

%package     -n %{name}+use_unix_paths_on_wasm-devel
Summary:        Extend Path and PathBuf for getting an absolute path
BuildArch:      noarch
%description -n %{name}+use_unix_paths_on_wasm-devel

This package contains library source intended for building other packages which
use the "use_unix_paths_on_wasm" feature of the "%{crate}" crate.

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
%files -n rust-path-absolutize-devel -f %{oreon_filedir}/rust-path-absolutize-devel.list

%changelog

%autochangelog
