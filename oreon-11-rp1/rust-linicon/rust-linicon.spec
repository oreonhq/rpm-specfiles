%global source0_hash 4ee8c5653188a809616c97296180a0547a61dba205bcdcbdd261dbd022a25fd9
%bcond check 1
%global debug_package %{nil}
%global crate linicon
Name:           rust-linicon
Version:        2.3.0
Release:        1%{?dist}
Summary:        Look up icons and icon theme info on Linux
License:        MPL-2.0
URL:            https://crates.io/crates/linicon
Source0:        https://static.crates.io/crates/linicon/linicon-%{version}.crate
Patch:          linicon-fix-metadata.diff
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
Summary:        Look up icons and icon theme info on Linux
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+expand-paths-devel
Summary:        Look up icons and icon theme info on Linux
BuildArch:      noarch
%description -n %{name}+expand-paths-devel

This package contains library source intended for building other packages which
use the "expand-paths" feature of the "%{crate}" crate.

%package     -n %{name}+linicon-theme-devel
Summary:        Look up icons and icon theme info on Linux
BuildArch:      noarch
%description -n %{name}+linicon-theme-devel

This package contains library source intended for building other packages which
use the "linicon-theme" feature of the "%{crate}" crate.

%package     -n %{name}+shellexpand-devel
Summary:        Look up icons and icon theme info on Linux
BuildArch:      noarch
%description -n %{name}+shellexpand-devel

This package contains library source intended for building other packages which
use the "shellexpand" feature of the "%{crate}" crate.

%package     -n %{name}+system-theme-devel
Summary:        Look up icons and icon theme info on Linux
BuildArch:      noarch
%description -n %{name}+system-theme-devel

This package contains library source intended for building other packages which
use the "system-theme" feature of the "%{crate}" crate.

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
    --skip tests::do_lookup
    --skip tests::do_lookup_no_scale
    --skip tests::do_lookup_no_size
    --skip tests::do_lookup_no_size_scale
    --skip tests::get_themes
    --skip tests::move_iter
    --skip tests::move_threads
}}
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-linicon-devel -f %{oreon_filedir}/rust-linicon-devel.list

%changelog

%autochangelog
