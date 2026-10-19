%global source0_hash c51563c6639245219c077420e0a207e99b5e82e2e6bb78fd4898d42028ea7dde
%bcond check 1
%global debug_package %{nil}
%global crate tame-index
Name:           rust-tame-index
Version:        0.26.3
Release:        1%{?dist}
Summary:        Access to local and remote cargo registry indices
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/tame-index
Source0:        https://static.crates.io/crates/tame-index/tame-index-%{version}.crate
Patch:          tame-index-fix-metadata.diff
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
Summary:        Access to local and remote cargo registry indices
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+__git-devel
Summary:        Access to local and remote cargo registry indices
BuildArch:      noarch
%description -n %{name}+__git-devel

This package contains library source intended for building other packages which
use the "__git" feature of the "%{crate}" crate.

%package     -n %{name}+__internal_all-devel
Summary:        Access to local and remote cargo registry indices
BuildArch:      noarch
%description -n %{name}+__internal_all-devel

This package contains library source intended for building other packages which
use the "__internal_all" feature of the "%{crate}" crate.

%package     -n %{name}+git-devel
Summary:        Access to local and remote cargo registry indices
BuildArch:      noarch
%description -n %{name}+git-devel

This package contains library source intended for building other packages which
use the "git" feature of the "%{crate}" crate.

%package     -n %{name}+gix-devel
Summary:        Access to local and remote cargo registry indices
BuildArch:      noarch
%description -n %{name}+gix-devel

This package contains library source intended for building other packages which
use the "gix" feature of the "%{crate}" crate.

%package     -n %{name}+gix-curl-devel
Summary:        Access to local and remote cargo registry indices
BuildArch:      noarch
%description -n %{name}+gix-curl-devel

This package contains library source intended for building other packages which
use the "gix-curl" feature of the "%{crate}" crate.

%package     -n %{name}+gix-reqwest-devel
Summary:        Access to local and remote cargo registry indices
BuildArch:      noarch
%description -n %{name}+gix-reqwest-devel

This package contains library source intended for building other packages which
use the "gix-reqwest" feature of the "%{crate}" crate.

%package     -n %{name}+local-devel
Summary:        Access to local and remote cargo registry indices
BuildArch:      noarch
%description -n %{name}+local-devel

This package contains library source intended for building other packages which
use the "local" feature of the "%{crate}" crate.

%package     -n %{name}+local-builder-devel
Summary:        Access to local and remote cargo registry indices
BuildArch:      noarch
%description -n %{name}+local-builder-devel

This package contains library source intended for building other packages which
use the "local-builder" feature of the "%{crate}" crate.

%package     -n %{name}+native-certs-devel
Summary:        Access to local and remote cargo registry indices
BuildArch:      noarch
%description -n %{name}+native-certs-devel

This package contains library source intended for building other packages which
use the "native-certs" feature of the "%{crate}" crate.

%package     -n %{name}+sparse-devel
Summary:        Access to local and remote cargo registry indices
BuildArch:      noarch
%description -n %{name}+sparse-devel

This package contains library source intended for building other packages which
use the "sparse" feature of the "%{crate}" crate.

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

%{cargo_test -- -- --exact %{shrink:
    --skip serializes_current_cargo_cache
    --skip parses_current_cargo_cache
    --skip can_take_shared_lock
    --skip wait_lock_times_out
    --skip waits_lock
}}
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-tame-index-devel -f %{oreon_filedir}/rust-tame-index-devel.list

%changelog

%autochangelog
