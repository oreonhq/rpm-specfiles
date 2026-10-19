%global source0_hash 583f52b0658b321b25fd6b209b6c76cf058f433071297de64e5980c3d9aad937
%bcond check 1
%global debug_package %{nil}
%global crate codespan
Name:           rust-codespan
Version:        0.13.1
Release:        1%{?dist}
Summary:        Data structures for tracking locations in source code
License:        Apache-2.0
URL:            https://crates.io/crates/codespan
Source0:        https://static.crates.io/crates/codespan/codespan-%{version}.crate
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
Summary:        Data structures for tracking locations in source code
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Data structures for tracking locations in source code
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+serialization-devel
Summary:        Data structures for tracking locations in source code
BuildArch:      noarch
%description -n %{name}+serialization-devel

This package contains library source intended for building other packages which
use the "serialization" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Data structures for tracking locations in source code
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+termcolor-devel
Summary:        Data structures for tracking locations in source code
BuildArch:      noarch
%description -n %{name}+termcolor-devel

This package contains library source intended for building other packages which
use the "termcolor" feature of the "%{crate}" crate.

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
%files -n rust-codespan-devel -f %{oreon_filedir}/rust-codespan-devel.list

%changelog

%autochangelog
