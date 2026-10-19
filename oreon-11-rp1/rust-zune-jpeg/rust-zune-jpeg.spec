%global source0_hash 27bc9d5b815bc103f142aa054f561d9187d191692ec7c2d1e2b4737f8dbd7296
%bcond check 0
%global debug_package %{nil}
%global crate zune-jpeg
Name:           rust-zune-jpeg
Version:        0.5.15
Release:        1%{?dist}
Summary:        A fast, correct and safe jpeg decoder
License:        MIT OR Apache-2.0 OR Zlib
URL:            https://crates.io/crates/zune-jpeg
Source0:        https://static.crates.io/crates/zune-jpeg/zune-jpeg-%{version}.crate
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
Summary:        A fast, correct and safe jpeg decoder
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+log-devel
Summary:        A fast, correct and safe jpeg decoder
BuildArch:      noarch
%description -n %{name}+log-devel

This package contains library source intended for building other packages which
use the "log" feature of the "%{crate}" crate.

%package     -n %{name}+neon-devel
Summary:        A fast, correct and safe jpeg decoder
BuildArch:      noarch
%description -n %{name}+neon-devel

This package contains library source intended for building other packages which
use the "neon" feature of the "%{crate}" crate.

%package     -n %{name}+portable_simd-devel
Summary:        A fast, correct and safe jpeg decoder
BuildArch:      noarch
%description -n %{name}+portable_simd-devel

This package contains library source intended for building other packages which
use the "portable_simd" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        A fast, correct and safe jpeg decoder
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+x86-devel
Summary:        A fast, correct and safe jpeg decoder
BuildArch:      noarch
%description -n %{name}+x86-devel

This package contains library source intended for building other packages which
use the "x86" feature of the "%{crate}" crate.

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
%files -n rust-zune-jpeg-devel -f %{oreon_filedir}/rust-zune-jpeg-devel.list

%changelog

%autochangelog
