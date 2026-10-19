%global source0_hash 0d47946d458e94a1b7bcabbf6521ea7c037062c81f534615abcad76e84d4970d
%bcond check 1
%global debug_package %{nil}
%global crate itertools
Name:           rust-itertools0.7
Version:        0.7.11
Release:        1%{?dist}
Summary:        Extra iterator adaptors, iterator methods, free functions, and macros.
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/itertools
Source0:        https://static.crates.io/crates/itertools/itertools-%{version}.crate
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
Summary:        Extra iterator adaptors, iterator methods, free functions, and macros.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+use_std-devel
Summary:        Extra iterator adaptors, iterator methods, free functions, and macros.
BuildArch:      noarch
%description -n %{name}+use_std-devel

This package contains library source intended for building other packages which
use the "use_std" feature of the "%{crate}" crate.

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
%files -n rust-itertools0.7-devel -f %{oreon_filedir}/rust-itertools0.7-devel.list

%changelog

%autochangelog
