%global source0_hash 046aa45b989642ec2e4717c8e72d677b13edd831a4d3b6cf37d9a3e54912496a
%bcond check 0
%global debug_package %{nil}
%global crate pulp
Name:           rust-pulp
Version:        0.22.3
Release:        1%{?dist}
Summary:        safe generic simd
License:        MIT
URL:            https://crates.io/crates/pulp
Source0:        https://static.crates.io/crates/pulp/pulp-%{version}.crate
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
Summary:        safe generic simd
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+macro-devel
Summary:        safe generic simd
BuildArch:      noarch
%description -n %{name}+macro-devel

This package contains library source intended for building other packages which
use the "macro" feature of the "%{crate}" crate.

%package     -n %{name}+nightly-devel
Summary:        safe generic simd
BuildArch:      noarch
%description -n %{name}+nightly-devel

This package contains library source intended for building other packages which
use the "nightly" feature of the "%{crate}" crate.

%package     -n %{name}+pulp-macro-devel
Summary:        safe generic simd
BuildArch:      noarch
%description -n %{name}+pulp-macro-devel

This package contains library source intended for building other packages which
use the "pulp-macro" feature of the "%{crate}" crate.

%package     -n %{name}+relaxed-simd-devel
Summary:        safe generic simd
BuildArch:      noarch
%description -n %{name}+relaxed-simd-devel

This package contains library source intended for building other packages which
use the "relaxed-simd" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        safe generic simd
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+x86-v3-devel
Summary:        safe generic simd
BuildArch:      noarch
%description -n %{name}+x86-v3-devel

This package contains library source intended for building other packages which
use the "x86-v3" feature of the "%{crate}" crate.

%package     -n %{name}+x86-v4-devel
Summary:        safe generic simd
BuildArch:      noarch
%description -n %{name}+x86-v4-devel

This package contains library source intended for building other packages which
use the "x86-v4" feature of the "%{crate}" crate.

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
%files -n rust-pulp-devel -f %{oreon_filedir}/rust-pulp-devel.list

%changelog

%autochangelog
