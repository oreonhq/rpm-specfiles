%global source0_hash 9737e026353e5cd0736f98eddae28665118eb6f6600902a7f50db585621fecb6
%bcond check 0
%global debug_package %{nil}
%global crate nonempty
Name:           rust-nonempty
Version:        0.12.0
Release:        2%{?dist}
Summary:        Correct by construction non-empty vector
License:        MIT
URL:            https://crates.io/crates/nonempty
Source0:        https://static.crates.io/crates/nonempty/nonempty-%{version}.crate
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
Summary:        Correct by construction non-empty vector
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+arbitrary-devel
Summary:        Correct by construction non-empty vector
BuildArch:      noarch
%description -n %{name}+arbitrary-devel

This package contains library source intended for building other packages which
use the "arbitrary" feature of the "%{crate}" crate.

%package     -n %{name}+bincode-devel
Summary:        Correct by construction non-empty vector
BuildArch:      noarch
%description -n %{name}+bincode-devel

This package contains library source intended for building other packages which
use the "bincode" feature of the "%{crate}" crate.

%package     -n %{name}+serialize-devel
Summary:        Correct by construction non-empty vector
BuildArch:      noarch
%description -n %{name}+serialize-devel

This package contains library source intended for building other packages which
use the "serialize" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Correct by construction non-empty vector
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
%files -n rust-nonempty-devel -f %{oreon_filedir}/rust-nonempty-devel.list

%changelog

%autochangelog
