%global source0_hash 3e6811e17f81fe246ef2bc553f76b6ee6ab41a694845df1d37e52a92b7bbd38a
%bcond check 1
%global debug_package %{nil}
%global crate copypasta
Name:           rust-copypasta
Version:        0.10.2
Release:        1%{?dist}
Summary:        Cross-platform library for accessing the OS-level clipboard
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/copypasta
Source0:        https://static.crates.io/crates/copypasta/copypasta-%{version}.crate
Patch:          copypasta-fix-metadata-auto.diff
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
Summary:        Cross-platform library for accessing the OS-level clipboard
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+smithay-clipboard-devel
Summary:        Cross-platform library for accessing the OS-level clipboard
BuildArch:      noarch
%description -n %{name}+smithay-clipboard-devel

This package contains library source intended for building other packages which
use the "smithay-clipboard" feature of the "%{crate}" crate.

%package     -n %{name}+wayland-devel
Summary:        Cross-platform library for accessing the OS-level clipboard
BuildArch:      noarch
%description -n %{name}+wayland-devel

This package contains library source intended for building other packages which
use the "wayland" feature of the "%{crate}" crate.

%package     -n %{name}+wayland-dlopen-devel
Summary:        Cross-platform library for accessing the OS-level clipboard
BuildArch:      noarch
%description -n %{name}+wayland-dlopen-devel

This package contains library source intended for building other packages which
use the "wayland-dlopen" feature of the "%{crate}" crate.

%package     -n %{name}+x11-devel
Summary:        Cross-platform library for accessing the OS-level clipboard
BuildArch:      noarch
%description -n %{name}+x11-devel

This package contains library source intended for building other packages which
use the "x11" feature of the "%{crate}" crate.

%package     -n %{name}+x11-clipboard-devel
Summary:        Cross-platform library for accessing the OS-level clipboard
BuildArch:      noarch
%description -n %{name}+x11-clipboard-devel

This package contains library source intended for building other packages which
use the "x11-clipboard" feature of the "%{crate}" crate.

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
%files -n rust-copypasta-devel -f %{oreon_filedir}/rust-copypasta-devel.list

%changelog

%autochangelog
