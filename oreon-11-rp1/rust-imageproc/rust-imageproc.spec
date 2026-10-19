%global source0_hash 645329c490783f3ea465d2b6c7c08286fece97f15e714fd533b6c70a3ead2252
%bcond check 0
%global debug_package %{nil}
%global crate imageproc
Name:           rust-imageproc
Version:        0.26.2
Release:        1%{?dist}
Summary:        Image processing operations
License:        MIT
URL:            https://crates.io/crates/imageproc
Source0:        https://static.crates.io/crates/imageproc/imageproc-%{version}.crate
Patch:          imageproc-fix-metadata-auto.diff
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
Summary:        Image processing operations
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+display-window-devel
Summary:        Image processing operations
BuildArch:      noarch
%description -n %{name}+display-window-devel

This package contains library source intended for building other packages which
use the "display-window" feature of the "%{crate}" crate.

%package     -n %{name}+fft-devel
Summary:        Image processing operations
BuildArch:      noarch
%description -n %{name}+fft-devel

This package contains library source intended for building other packages which
use the "fft" feature of the "%{crate}" crate.

%package     -n %{name}+katexit-devel
Summary:        Image processing operations
BuildArch:      noarch
%description -n %{name}+katexit-devel

This package contains library source intended for building other packages which
use the "katexit" feature of the "%{crate}" crate.

%package     -n %{name}+rayon-devel
Summary:        Image processing operations
BuildArch:      noarch
%description -n %{name}+rayon-devel

This package contains library source intended for building other packages which
use the "rayon" feature of the "%{crate}" crate.

%package     -n %{name}+sdl2-devel
Summary:        Image processing operations
BuildArch:      noarch
%description -n %{name}+sdl2-devel

This package contains library source intended for building other packages which
use the "sdl2" feature of the "%{crate}" crate.

%package     -n %{name}+text-devel
Summary:        Image processing operations
BuildArch:      noarch
%description -n %{name}+text-devel

This package contains library source intended for building other packages which
use the "text" feature of the "%{crate}" crate.

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
%files -n rust-imageproc-devel -f %{oreon_filedir}/rust-imageproc-devel.list

%changelog

%autochangelog
