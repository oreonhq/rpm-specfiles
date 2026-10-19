%global source0_hash 08e645ba5c45109106d56610b3ee60eb13a6f2beb8b74f8dc8186cf261788dda
%bcond check 1
%global debug_package %{nil}
%global crate pipewire
Name:           rust-pipewire0.8
Version:        0.8.0
Release:        1%{?dist}
Summary:        Rust bindings for PipeWire
License:        MIT
URL:            https://crates.io/crates/pipewire
Source0:        https://static.crates.io/crates/pipewire/pipewire-%{version}.crate
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
Summary:        Rust bindings for PipeWire
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+v0_3_32-devel
Summary:        Rust bindings for PipeWire
BuildArch:      noarch
%description -n %{name}+v0_3_32-devel

This package contains library source intended for building other packages which
use the "v0_3_32" feature of the "%{crate}" crate.

%package     -n %{name}+v0_3_33-devel
Summary:        Rust bindings for PipeWire
BuildArch:      noarch
%description -n %{name}+v0_3_33-devel

This package contains library source intended for building other packages which
use the "v0_3_33" feature of the "%{crate}" crate.

%package     -n %{name}+v0_3_34-devel
Summary:        Rust bindings for PipeWire
BuildArch:      noarch
%description -n %{name}+v0_3_34-devel

This package contains library source intended for building other packages which
use the "v0_3_34" feature of the "%{crate}" crate.

%package     -n %{name}+v0_3_39-devel
Summary:        Rust bindings for PipeWire
BuildArch:      noarch
%description -n %{name}+v0_3_39-devel

This package contains library source intended for building other packages which
use the "v0_3_39" feature of the "%{crate}" crate.

%package     -n %{name}+v0_3_40-devel
Summary:        Rust bindings for PipeWire
BuildArch:      noarch
%description -n %{name}+v0_3_40-devel

This package contains library source intended for building other packages which
use the "v0_3_40" feature of the "%{crate}" crate.

%package     -n %{name}+v0_3_41-devel
Summary:        Rust bindings for PipeWire
BuildArch:      noarch
%description -n %{name}+v0_3_41-devel

This package contains library source intended for building other packages which
use the "v0_3_41" feature of the "%{crate}" crate.

%package     -n %{name}+v0_3_43-devel
Summary:        Rust bindings for PipeWire
BuildArch:      noarch
%description -n %{name}+v0_3_43-devel

This package contains library source intended for building other packages which
use the "v0_3_43" feature of the "%{crate}" crate.

%package     -n %{name}+v0_3_44-devel
Summary:        Rust bindings for PipeWire
BuildArch:      noarch
%description -n %{name}+v0_3_44-devel

This package contains library source intended for building other packages which
use the "v0_3_44" feature of the "%{crate}" crate.

%package     -n %{name}+v0_3_45-devel
Summary:        Rust bindings for PipeWire
BuildArch:      noarch
%description -n %{name}+v0_3_45-devel

This package contains library source intended for building other packages which
use the "v0_3_45" feature of the "%{crate}" crate.

%package     -n %{name}+v0_3_49-devel
Summary:        Rust bindings for PipeWire
BuildArch:      noarch
%description -n %{name}+v0_3_49-devel

This package contains library source intended for building other packages which
use the "v0_3_49" feature of the "%{crate}" crate.

%package     -n %{name}+v0_3_53-devel
Summary:        Rust bindings for PipeWire
BuildArch:      noarch
%description -n %{name}+v0_3_53-devel

This package contains library source intended for building other packages which
use the "v0_3_53" feature of the "%{crate}" crate.

%package     -n %{name}+v0_3_57-devel
Summary:        Rust bindings for PipeWire
BuildArch:      noarch
%description -n %{name}+v0_3_57-devel

This package contains library source intended for building other packages which
use the "v0_3_57" feature of the "%{crate}" crate.

%package     -n %{name}+v0_3_64-devel
Summary:        Rust bindings for PipeWire
BuildArch:      noarch
%description -n %{name}+v0_3_64-devel

This package contains library source intended for building other packages which
use the "v0_3_64" feature of the "%{crate}" crate.

%package     -n %{name}+v0_3_65-devel
Summary:        Rust bindings for PipeWire
BuildArch:      noarch
%description -n %{name}+v0_3_65-devel

This package contains library source intended for building other packages which
use the "v0_3_65" feature of the "%{crate}" crate.

%package     -n %{name}+v0_3_77-devel
Summary:        Rust bindings for PipeWire
BuildArch:      noarch
%description -n %{name}+v0_3_77-devel

This package contains library source intended for building other packages which
use the "v0_3_77" feature of the "%{crate}" crate.

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
%files -n rust-pipewire0.8-devel -f %{oreon_filedir}/rust-pipewire0.8-devel.list

%changelog

%autochangelog
