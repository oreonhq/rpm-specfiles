%global source0_hash dd5eb614ed4c27c5d706420e4320fbe3216ab31fa1c33cd8246ac36dae4479ba
%bcond check 1
%global debug_package %{nil}
%global crate cargo_metadata
Name:           rust-cargo_metadata0.19
Version:        0.19.2
Release:        1%{?dist}
Summary:        Structured access to the output of cargo metadata
License:        MIT
URL:            https://crates.io/crates/cargo_metadata
Source0:        https://static.crates.io/crates/cargo_metadata/cargo_metadata-%{version}.crate
Patch10:        https://github.com/oli-obk/cargo_metadata/commit/aae754b.patch
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
Summary:        Structured access to the output of cargo metadata
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+builder-devel
Summary:        Structured access to the output of cargo metadata
BuildArch:      noarch
%description -n %{name}+builder-devel

This package contains library source intended for building other packages which
use the "builder" feature of the "%{crate}" crate.

%package     -n %{name}+derive_builder-devel
Summary:        Structured access to the output of cargo metadata
BuildArch:      noarch
%description -n %{name}+derive_builder-devel

This package contains library source intended for building other packages which
use the "derive_builder" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-devel
Summary:        Structured access to the output of cargo metadata
BuildArch:      noarch
%description -n %{name}+unstable-devel

This package contains library source intended for building other packages which
use the "unstable" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build -a
%install
%cargo_install -a
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%{cargo_test -a -- -- %{shrink:
    --skip advanced_feature_configuration
    --skip all_the_fields
    --skip basic_workspace_root_package_exists
    --skip current_dir
}}
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-cargo_metadata0.19-devel -f %{oreon_filedir}/rust-cargo_metadata0.19-devel.list

%changelog

%autochangelog
