%global source0_hash a7666983ed0dd8d21a6f6576ee00053ca0926fb281a5522577a4dbd0f1b54143
%bcond check 1
%global debug_package %{nil}
%global crate goblin
Name:           rust-goblin0.5
Version:        0.5.4
Release:        1%{?dist}
Summary:        Impish, cross-platform, ELF, Mach-o, and PE binary parsing and loading crate
License:        MIT
URL:            https://crates.io/crates/goblin
Source0:        https://static.crates.io/crates/goblin/goblin-%{version}.crate
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
Summary:        Impish, cross-platform, ELF, Mach-o, and PE binary parsing and loading crate
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Impish, cross-platform, ELF, Mach-o, and PE binary parsing and loading crate
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+archive-devel
Summary:        Impish, cross-platform, ELF, Mach-o, and PE binary parsing and loading crate
BuildArch:      noarch
%description -n %{name}+archive-devel

This package contains library source intended for building other packages which
use the "archive" feature of the "%{crate}" crate.

%package     -n %{name}+elf32-devel
Summary:        Impish, cross-platform, ELF, Mach-o, and PE binary parsing and loading crate
BuildArch:      noarch
%description -n %{name}+elf32-devel

This package contains library source intended for building other packages which
use the "elf32" feature of the "%{crate}" crate.

%package     -n %{name}+elf64-devel
Summary:        Impish, cross-platform, ELF, Mach-o, and PE binary parsing and loading crate
BuildArch:      noarch
%description -n %{name}+elf64-devel

This package contains library source intended for building other packages which
use the "elf64" feature of the "%{crate}" crate.

%package     -n %{name}+endian_fd-devel
Summary:        Impish, cross-platform, ELF, Mach-o, and PE binary parsing and loading crate
BuildArch:      noarch
%description -n %{name}+endian_fd-devel

This package contains library source intended for building other packages which
use the "endian_fd" feature of the "%{crate}" crate.

%package     -n %{name}+log-devel
Summary:        Impish, cross-platform, ELF, Mach-o, and PE binary parsing and loading crate
BuildArch:      noarch
%description -n %{name}+log-devel

This package contains library source intended for building other packages which
use the "log" feature of the "%{crate}" crate.

%package     -n %{name}+mach32-devel
Summary:        Impish, cross-platform, ELF, Mach-o, and PE binary parsing and loading crate
BuildArch:      noarch
%description -n %{name}+mach32-devel

This package contains library source intended for building other packages which
use the "mach32" feature of the "%{crate}" crate.

%package     -n %{name}+mach64-devel
Summary:        Impish, cross-platform, ELF, Mach-o, and PE binary parsing and loading crate
BuildArch:      noarch
%description -n %{name}+mach64-devel

This package contains library source intended for building other packages which
use the "mach64" feature of the "%{crate}" crate.

%package     -n %{name}+pe32-devel
Summary:        Impish, cross-platform, ELF, Mach-o, and PE binary parsing and loading crate
BuildArch:      noarch
%description -n %{name}+pe32-devel

This package contains library source intended for building other packages which
use the "pe32" feature of the "%{crate}" crate.

%package     -n %{name}+pe64-devel
Summary:        Impish, cross-platform, ELF, Mach-o, and PE binary parsing and loading crate
BuildArch:      noarch
%description -n %{name}+pe64-devel

This package contains library source intended for building other packages which
use the "pe64" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Impish, cross-platform, ELF, Mach-o, and PE binary parsing and loading crate
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
%files -n rust-goblin0.5-devel -f %{oreon_filedir}/rust-goblin0.5-devel.list

%changelog

%autochangelog
