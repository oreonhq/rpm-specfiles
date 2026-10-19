%global source0_hash 808cc0b475acf76adf36f08ca49429b12aad9f678cb56143d5b3cb49b9a1dd08
%bcond check 0
%global debug_package %{nil}
%global crate remove_dir_all
Name:           rust-remove_dir_all
Version:        1.0.0
Release:        1%{?dist}
Summary:        A safe, reliable implementation of remove_dir_all for Windows
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/remove_dir_all
Source0:        https://static.crates.io/crates/remove_dir_all/remove_dir_all-%{version}.crate
Patch:          remove_dir_all-fix-metadata-auto.diff
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
Summary:        A safe, reliable implementation of remove_dir_all for Windows
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+cli-devel
Summary:        A safe, reliable implementation of remove_dir_all for Windows
BuildArch:      noarch
%description -n %{name}+cli-devel

This package contains library source intended for building other packages which
use the "cli" feature of the "%{crate}" crate.

%package     -n %{name}+log-devel
Summary:        A safe, reliable implementation of remove_dir_all for Windows
BuildArch:      noarch
%description -n %{name}+log-devel

This package contains library source intended for building other packages which
use the "log" feature of the "%{crate}" crate.

%package     -n %{name}+parallel-devel
Summary:        A safe, reliable implementation of remove_dir_all for Windows
BuildArch:      noarch
%description -n %{name}+parallel-devel

This package contains library source intended for building other packages which
use the "parallel" feature of the "%{crate}" crate.

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
%files -n rust-remove_dir_all-devel -f %{oreon_filedir}/rust-remove_dir_all-devel.list

%changelog

%autochangelog
