%global source0_hash ba73ea9cf16a25df0c8caa16c51acb937d5712a8429db78a3ee29d5dcacd3a65
%bcond check 0
%global debug_package %{nil}
%global crate valuable
Name:           rust-valuable
Version:        0.1.1
Release:        1%{?dist}
Summary:        Object-safe value inspection, used to pass un-typed structured data a...
License:        MIT
URL:            https://crates.io/crates/valuable
Source0:        https://static.crates.io/crates/valuable/valuable-%{version}.crate
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
Summary:        Object-safe value inspection, used to pass un-typed structured data a...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Object-safe value inspection, used to pass un-typed structured data a...
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+derive-devel
Summary:        Object-safe value inspection, used to pass un-typed structured data a...
BuildArch:      noarch
%description -n %{name}+derive-devel

This package contains library source intended for building other packages which
use the "derive" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Object-safe value inspection, used to pass un-typed structured data a...
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+valuable-derive-devel
Summary:        Object-safe value inspection, used to pass un-typed structured data a...
BuildArch:      noarch
%description -n %{name}+valuable-derive-devel

This package contains library source intended for building other packages which
use the "valuable-derive" feature of the "%{crate}" crate.

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
%files -n rust-valuable-devel -f %{oreon_filedir}/rust-valuable-devel.list

%changelog

%autochangelog
