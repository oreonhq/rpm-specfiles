%global source0_hash b0f7e269b48f0a7dd0146680fa24b50cc67fc0373f086a5b2f99bd084639b482
%bcond check 0
%global debug_package %{nil}
%global crate thin-vec
Name:           rust-thin-vec
Version:        0.2.18
Release:        1%{?dist}
Summary:        A Vec that takes up less space on the stack.
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/thin-vec
Source0:        https://static.crates.io/crates/thin-vec/thin-vec-%{version}.crate
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
Summary:        A Vec that takes up less space on the stack.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+const_new-devel
Summary:        A Vec that takes up less space on the stack.
BuildArch:      noarch
%description -n %{name}+const_new-devel

This package contains library source intended for building other packages which
use the "const_new" feature of the "%{crate}" crate.

%package     -n %{name}+gecko-ffi-devel
Summary:        A Vec that takes up less space on the stack.
BuildArch:      noarch
%description -n %{name}+gecko-ffi-devel

This package contains library source intended for building other packages which
use the "gecko-ffi" feature of the "%{crate}" crate.

%package     -n %{name}+malloc_size_of-devel
Summary:        A Vec that takes up less space on the stack.
BuildArch:      noarch
%description -n %{name}+malloc_size_of-devel

This package contains library source intended for building other packages which
use the "malloc_size_of" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        A Vec that takes up less space on the stack.
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        A Vec that takes up less space on the stack.
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-devel
Summary:        A Vec that takes up less space on the stack.
BuildArch:      noarch
%description -n %{name}+unstable-devel

This package contains library source intended for building other packages which
use the "unstable" feature of the "%{crate}" crate.

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
%files -n rust-thin-vec-devel -f %{oreon_filedir}/rust-thin-vec-devel.list

%changelog

%autochangelog
