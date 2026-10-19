%global source0_hash 0c61b87c9683ab7cb1c6871d261ad5479b6b10ceb52c4352aaca3b5d35a8febe
%bcond check 0
%global debug_package %{nil}
%global crate module-lattice
Name:           rust-module-lattice
Version:        0.2.3
Release:        1%{?dist}
Summary:        Functionality shared between the `ml-kem` and `ml-dsa` crates, includ...
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/module-lattice
Source0:        https://static.crates.io/crates/module-lattice/module-lattice-%{version}.crate
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

%package     -n %{name}+alloc-devel
Summary:        Functionality shared between the `ml-kem` and `ml-dsa` crates, includ...
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+ctutils-devel
Summary:        Functionality shared between the `ml-kem` and `ml-dsa` crates, includ...
BuildArch:      noarch
%description -n %{name}+ctutils-devel

This package contains library source intended for building other packages which
use the "ctutils" feature of the "%{crate}" crate.

%package     -n %{name}+zeroize-devel
Summary:        Functionality shared between the `ml-kem` and `ml-dsa` crates, includ...
BuildArch:      noarch
%description -n %{name}+zeroize-devel

This package contains library source intended for building other packages which
use the "zeroize" feature of the "%{crate}" crate.

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
%files -n rust-module-lattice-devel -f %{oreon_filedir}/rust-module-lattice-devel.list

%changelog

%autochangelog
