%global source0_hash eb4c15f0ba298a490b66abac0fefc3a44ff1b8004c38cf140d27c027f1f80784
%bcond check 1
%global debug_package %{nil}
%global cargo_install_bin 0
%global crate uu_cp
Name:           rust-uu_cp
Version:        0.12.0
Release:        1%{?dist}
Summary:        cp ~ (uutils) copy SOURCE to DESTINATION
License:        MIT
URL:            https://crates.io/crates/uu_cp
Source0:        https://static.crates.io/crates/uu_cp/uu_cp-%{version}.crate
Patch:          uu_cp-fix-metadata.diff
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
Summary:        cp ~ (uutils) copy SOURCE to DESTINATION
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+exacl-devel
Summary:        cp ~ (uutils) copy SOURCE to DESTINATION
BuildArch:      noarch
%description -n %{name}+exacl-devel

This package contains library source intended for building other packages which
use the "exacl" feature of the "%{crate}" crate.

%package     -n %{name}+feat_acl-devel
Summary:        cp ~ (uutils) copy SOURCE to DESTINATION
BuildArch:      noarch
%description -n %{name}+feat_acl-devel

This package contains library source intended for building other packages which
use the "feat_acl" feature of the "%{crate}" crate.

%package     -n %{name}+feat_selinux-devel
Summary:        cp ~ (uutils) copy SOURCE to DESTINATION
BuildArch:      noarch
%description -n %{name}+feat_selinux-devel

This package contains library source intended for building other packages which
use the "feat_selinux" feature of the "%{crate}" crate.

%package     -n %{name}+selinux-devel
Summary:        cp ~ (uutils) copy SOURCE to DESTINATION
BuildArch:      noarch
%description -n %{name}+selinux-devel

This package contains library source intended for building other packages which
use the "selinux" feature of the "%{crate}" crate.

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
%files -n rust-uu_cp-devel -f %{oreon_filedir}/rust-uu_cp-devel.list

%changelog

%autochangelog
