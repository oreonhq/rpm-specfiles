%global source0_hash 2c7e611d49285d4c4b2e1727b72cf05353558885cc5252f93707b845dfcaf3d3
%bcond check 1
%global debug_package %{nil}
%global crate font-kit
Name:           rust-font-kit
Version:        0.14.3
Release:        1%{?dist}
Summary:        Cross-platform font loading library
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/font-kit
Source0:        https://static.crates.io/crates/font-kit/font-kit-%{version}.crate
Patch:          font-kit-fix-metadata-auto.diff
Patch:          font-kit-fix-metadata.diff
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
Summary:        Cross-platform font loading library
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+freetype-devel
Summary:        Cross-platform font loading library
BuildArch:      noarch
%description -n %{name}+freetype-devel

This package contains library source intended for building other packages which
use the "freetype" feature of the "%{crate}" crate.

%package     -n %{name}+loader-freetype-devel
Summary:        Cross-platform font loading library
BuildArch:      noarch
%description -n %{name}+loader-freetype-devel

This package contains library source intended for building other packages which
use the "loader-freetype" feature of the "%{crate}" crate.

%package     -n %{name}+loader-freetype-default-devel
Summary:        Cross-platform font loading library
BuildArch:      noarch
%description -n %{name}+loader-freetype-default-devel

This package contains library source intended for building other packages which
use the "loader-freetype-default" feature of the "%{crate}" crate.

%package     -n %{name}+source-devel
Summary:        Cross-platform font loading library
BuildArch:      noarch
%description -n %{name}+source-devel

This package contains library source intended for building other packages which
use the "source" feature of the "%{crate}" crate.

%package     -n %{name}+source-fontconfig-devel
Summary:        Cross-platform font loading library
BuildArch:      noarch
%description -n %{name}+source-fontconfig-devel

This package contains library source intended for building other packages which
use the "source-fontconfig" feature of the "%{crate}" crate.

%package     -n %{name}+source-fontconfig-default-devel
Summary:        Cross-platform font loading library
BuildArch:      noarch
%description -n %{name}+source-fontconfig-default-devel

This package contains library source intended for building other packages which
use the "source-fontconfig-default" feature of the "%{crate}" crate.

%package     -n %{name}+source-fontconfig-dlopen-devel
Summary:        Cross-platform font loading library
BuildArch:      noarch
%description -n %{name}+source-fontconfig-dlopen-devel

This package contains library source intended for building other packages which
use the "source-fontconfig-dlopen" feature of the "%{crate}" crate.

%package     -n %{name}+yeslogic-fontconfig-sys-devel
Summary:        Cross-platform font loading library
BuildArch:      noarch
%description -n %{name}+yeslogic-fontconfig-sys-devel

This package contains library source intended for building other packages which
use the "yeslogic-fontconfig-sys" feature of the "%{crate}" crate.

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
%files -n rust-font-kit-devel -f %{oreon_filedir}/rust-font-kit-devel.list

%changelog

%autochangelog
