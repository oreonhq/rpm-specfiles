%global source0_hash 98b0cc327b5bc766e7fda9c9260cc0fa81b43a8e240440422dff70788e3f9ef1
%bcond check 1
%global debug_package %{nil}
%global crate crossbeam-channel
Name:           rust-crossbeam-channel
Version:        0.5.17
Release:        1%{?dist}
Summary:        Multi-producer multi-consumer channels for message passing
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/crossbeam-channel
Source0:        https://static.crates.io/crates/crossbeam-channel/crossbeam-channel-%{version}.crate
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
Summary:        Multi-producer multi-consumer channels for message passing
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Multi-producer multi-consumer channels for message passing
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

%{cargo_test -- -- --exact %{shrink:
    --skip fairness2
    --skip select2::main
}}
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-crossbeam-channel-devel -f %{oreon_filedir}/rust-crossbeam-channel-devel.list

%changelog

%autochangelog
