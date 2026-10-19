%global source0_hash 9c26be8ced271f658751bfb6bdabbaf67f6f40eb895f37ad685e455599944db2
%bcond check 1
%global debug_package %{nil}
%global cargo_install_bin 0
%global crate uu_mknod
Name:           rust-uu_mknod
Version:        0.7.0
Release:        1%{?dist}
Summary:        mknod ~ (uutils) create special file NAME of TYPE
License:        MIT
URL:            https://crates.io/crates/uu_mknod
Source0:        https://static.crates.io/crates/uu_mknod/uu_mknod-%{version}.crate
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
Summary:        mknod ~ (uutils) create special file NAME of TYPE
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+selinux-devel
Summary:        mknod ~ (uutils) create special file NAME of TYPE
BuildArch:      noarch
%description -n %{name}+selinux-devel

This package contains library source intended for building other packages which
use the "selinux" feature of the "%{crate}" crate.

%package     -n %{name}+smack-devel
Summary:        mknod ~ (uutils) create special file NAME of TYPE
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
%files -n rust-uu_mknod-devel -f %{oreon_filedir}/rust-uu_mknod-devel.list

%changelog

%autochangelog
