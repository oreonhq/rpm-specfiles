%global source0_hash eb2c55a318a87600ea870ff8c2012148b44bf18b74fad48d0f835c38c7d07c5f
%bcond check 0
%global debug_package %{nil}
%global crate logos
Name:           rust-logos
Version:        0.16.1
Release:        1%{?dist}
Summary:        Create ridiculously fast Lexers
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/logos
Source0:        https://static.crates.io/crates/logos/logos-%{version}.crate
Patch:          logos-fix-metadata.diff
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
Summary:        Create ridiculously fast Lexers
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+debug-devel
Summary:        Create ridiculously fast Lexers
BuildArch:      noarch
%description -n %{name}+debug-devel

This package contains library source intended for building other packages which
use the "debug" feature of the "%{crate}" crate.

%package     -n %{name}+export_derive-devel
Summary:        Create ridiculously fast Lexers
BuildArch:      noarch
%description -n %{name}+export_derive-devel

This package contains library source intended for building other packages which
use the "export_derive" feature of the "%{crate}" crate.

%package     -n %{name}+forbid_unsafe-devel
Summary:        Create ridiculously fast Lexers
BuildArch:      noarch
%description -n %{name}+forbid_unsafe-devel

This package contains library source intended for building other packages which
use the "forbid_unsafe" feature of the "%{crate}" crate.

%package     -n %{name}+logos-derive-devel
Summary:        Create ridiculously fast Lexers
BuildArch:      noarch
%description -n %{name}+logos-derive-devel

This package contains library source intended for building other packages which
use the "logos-derive" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Create ridiculously fast Lexers
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

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
%files -n rust-logos-devel -f %{oreon_filedir}/rust-logos-devel.list

%changelog

%autochangelog
