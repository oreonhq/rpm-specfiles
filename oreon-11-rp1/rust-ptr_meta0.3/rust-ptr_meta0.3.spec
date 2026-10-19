%global source0_hash 743da816b98c921cdbe8628ef7381b76f25ecf4da599fc80aca90eae7ef70cc0
%bcond check 0
%global debug_package %{nil}
%global crate ptr_meta
Name:           rust-ptr_meta0.3
Version:        0.3.2
Release:        1%{?dist}
Summary:        Radioactive stabilization of the ptr_meta rfc
License:        MIT
URL:            https://crates.io/crates/ptr_meta
Source0:        https://static.crates.io/crates/ptr_meta/ptr_meta-%{version}.crate
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
Summary:        Radioactive stabilization of the ptr_meta rfc
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+derive-devel
Summary:        Radioactive stabilization of the ptr_meta rfc
BuildArch:      noarch
%description -n %{name}+derive-devel

This package contains library source intended for building other packages which
use the "derive" feature of the "%{crate}" crate.

%package     -n %{name}+ptr_meta_derive-devel
Summary:        Radioactive stabilization of the ptr_meta rfc
BuildArch:      noarch
%description -n %{name}+ptr_meta_derive-devel

This package contains library source intended for building other packages which
use the "ptr_meta_derive" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Radioactive stabilization of the ptr_meta rfc
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
%files -n rust-ptr_meta0.3-devel -f %{oreon_filedir}/rust-ptr_meta0.3-devel.list

%changelog

%autochangelog
