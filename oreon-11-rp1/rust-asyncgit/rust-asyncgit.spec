%global source0_hash e8d8428ebcb26e0a5fbdc1c2a4a8c30233d0c147798e0f8acc9b77faf6686045
%bcond check 1
%global debug_package %{nil}
%global crate asyncgit
Name:           rust-asyncgit
Version:        0.28.0
Release:        1%{?dist}
Summary:        Allow using git2 in a asynchronous context
License:        MIT
URL:            https://crates.io/crates/asyncgit
Source0:        https://static.crates.io/crates/asyncgit/asyncgit-%{version}.crate
%if %{with check}
%endif
# oreon:deps
BuildRequires:  /usr/bin/git
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
Summary:        Allow using git2 in a asynchronous context
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+trace-libgit-devel
Summary:        Allow using git2 in a asynchronous context
BuildArch:      noarch
%description -n %{name}+trace-libgit-devel

This package contains library source intended for building other packages which
use the "trace-libgit" feature of the "%{crate}" crate.

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

%cargo_test -- -- --skip sync::submodules::tests::test_smoke
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-asyncgit-devel -f %{oreon_filedir}/rust-asyncgit-devel.list

%changelog

%autochangelog
