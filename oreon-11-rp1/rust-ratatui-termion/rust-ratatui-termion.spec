%global source2_hash 50eb43e8d742c9c61a9391e42b2184fce54dbd1893a1bb1c85b8c9ee217ab1f5
%global source0_hash 4cade85a8591fbc911e147951422f0d6fd40f4948b271b6216c7dc01838996f8
%bcond check 1
%global debug_package %{nil}
%global crate ratatui-termion
Name:           rust-ratatui-termion
Version:        0.1.0
Release:        1%{?dist}
Summary:        Termion backend for the Ratatui Terminal UI library
License:        MIT
URL:            https://crates.io/crates/ratatui-termion
Source0:        https://static.crates.io/crates/ratatui-termion/ratatui-termion-%{version}.crate
Source2:        https://github.com/ratatui/ratatui/raw/refs/tags/ratatui-v0.30.0/LICENSE
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
Summary:        Termion backend for the Ratatui Terminal UI library
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+document-features-devel
Summary:        Termion backend for the Ratatui Terminal UI library
BuildArch:      noarch
%description -n %{name}+document-features-devel

This package contains library source intended for building other packages which
use the "document-features" feature of the "%{crate}" crate.

%package     -n %{name}+scrolling-regions-devel
Summary:        Termion backend for the Ratatui Terminal UI library
BuildArch:      noarch
%description -n %{name}+scrolling-regions-devel

This package contains library source intended for building other packages which
use the "scrolling-regions" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Termion backend for the Ratatui Terminal UI library
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-devel
Summary:        Termion backend for the Ratatui Terminal UI library
BuildArch:      noarch
%description -n %{name}+unstable-devel

This package contains library source intended for building other packages which
use the "unstable" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-backend-writer-devel
Summary:        Termion backend for the Ratatui Terminal UI library
BuildArch:      noarch
%description -n %{name}+unstable-backend-writer-devel

This package contains library source intended for building other packages which
use the "unstable-backend-writer" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
cp -pav %{SOURCE2} .
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
%files -n rust-ratatui-termion-devel -f %{oreon_filedir}/rust-ratatui-termion-devel.list

%changelog

%autochangelog
