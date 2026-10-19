%global source0_hash 3eaf3ede3fee6db1a4c2ee091bf8a8b4dccdc6d17f656fb07896ee72867612f2
%bcond check 1
%global debug_package %{nil}
%global crate libc
Name:           rust-libc
Version:        0.2.189
Release:        1%{?dist}
Summary:        Raw FFI bindings to platform libraries like libc
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/libc
Source0:        https://static.crates.io/crates/libc/libc-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  glibc-devel
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       glibc-devel
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Raw FFI bindings to platform libraries like libc
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+align-devel
Summary:        Raw FFI bindings to platform libraries like libc
BuildArch:      noarch
%description -n %{name}+align-devel

This package contains library source intended for building other packages which
use the "align" feature of the "%{crate}" crate.

%package     -n %{name}+const-extern-fn-devel
Summary:        Raw FFI bindings to platform libraries like libc
BuildArch:      noarch
%description -n %{name}+const-extern-fn-devel

This package contains library source intended for building other packages which
use the "const-extern-fn" feature of the "%{crate}" crate.

%package     -n %{name}+extra_traits-devel
Summary:        Raw FFI bindings to platform libraries like libc
BuildArch:      noarch
%description -n %{name}+extra_traits-devel

This package contains library source intended for building other packages which
use the "extra_traits" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Raw FFI bindings to platform libraries like libc
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+use_std-devel
Summary:        Raw FFI bindings to platform libraries like libc
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
%files -n rust-libc-devel -f %{oreon_filedir}/rust-libc-devel.list

%changelog

%autochangelog
