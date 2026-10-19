%global source0_hash 607549934f6cc26b89cfecfdc46fa90f1e5d1536a68349b0c3a4f9d1c0d37959
%bcond check 1
%global debug_package %{nil}
%global crate shared_child
Name:           rust-shared_child
Version:        1.1.2
Release:        1%{?dist}
Summary:        Library for using child processes from multiple threads
License:        MIT
URL:            https://crates.io/crates/shared_child
Source0:        https://static.crates.io/crates/shared_child/shared_child-%{version}.crate
Patch:          shared_child-fix-metadata-auto.diff
%if %{with check}
%endif
# oreon:deps
BuildRequires:  /usr/bin/python
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
Summary:        Library for using child processes from multiple threads
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

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
%files -n rust-shared_child-devel -f %{oreon_filedir}/rust-shared_child-devel.list

%changelog

%autochangelog
