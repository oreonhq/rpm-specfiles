%global source0_hash 26d142aeadbc4e8c679fc6d93fbe7efe1c021fa7d80629e615915b519e3bc6de
%bcond check 0
%global debug_package %{nil}
%global crate mbox
Name:           rust-mbox
Version:        0.7.1
Release:        1%{?dist}
Summary:        malloc-based box.
License:        MIT
URL:            https://crates.io/crates/mbox
Source0:        https://static.crates.io/crates/mbox/mbox-%{version}.crate
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
Summary:        malloc-based box.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+nightly-devel
Summary:        malloc-based box.
BuildArch:      noarch
%description -n %{name}+nightly-devel

This package contains library source intended for building other packages which
use the "nightly" feature of the "%{crate}" crate.

%package     -n %{name}+stable_deref_trait-devel
Summary:        malloc-based box.
BuildArch:      noarch
%description -n %{name}+stable_deref_trait-devel

This package contains library source intended for building other packages which
use the "stable_deref_trait" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        malloc-based box.
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
%files -n rust-mbox-devel -f %{oreon_filedir}/rust-mbox-devel.list

%changelog

%autochangelog
