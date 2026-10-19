%global source0_hash 4a700dd472f9afe648e595af69c51a381ecace3412b737f06af4fca2a4be73ef
%bcond check 1
%global debug_package %{nil}
%global cargo_install_bin 0
%global crate uu_id
Name:           rust-uu_id
Version:        0.7.0
Release:        1%{?dist}
Summary:        id ~ (uutils) display user and group information for USER
License:        MIT
URL:            https://crates.io/crates/uu_id
Source0:        https://static.crates.io/crates/uu_id/uu_id-%{version}.crate
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
Summary:        id ~ (uutils) display user and group information for USER
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+feat_selinux-devel
Summary:        id ~ (uutils) display user and group information for USER
BuildArch:      noarch
%description -n %{name}+feat_selinux-devel

This package contains library source intended for building other packages which
use the "feat_selinux" feature of the "%{crate}" crate.

%package     -n %{name}+selinux-devel
Summary:        id ~ (uutils) display user and group information for USER
BuildArch:      noarch
%description -n %{name}+selinux-devel

This package contains library source intended for building other packages which
use the "selinux" feature of the "%{crate}" crate.

%package     -n %{name}+smack-devel
Summary:        id ~ (uutils) display user and group information for USER
BuildArch:      noarch
%description -n %{name}+smack-devel

This package contains library source intended for building other packages which
use the "smack" feature of the "%{crate}" crate.

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
%files -n rust-uu_id-devel -f %{oreon_filedir}/rust-uu_id-devel.list

%changelog

%autochangelog
