%global source0_hash d010acf9ed312cbc737e5f9064c375a7093975b0c25568337f0c24148f46540d
%bcond check 1
%global debug_package %{nil}
%global crate reedline
Name:           rust-reedline
Version:        0.51.0
Release:        1%{?dist}
Summary:        Readline-like crate for CLI text input
License:        MIT
URL:            https://crates.io/crates/reedline
Source0:        https://static.crates.io/crates/reedline/reedline-%{version}.crate
Patch:          reedline-fix-metadata.diff
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
Summary:        Readline-like crate for CLI text input
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+arboard-devel
Summary:        Readline-like crate for CLI text input
BuildArch:      noarch
%description -n %{name}+arboard-devel

This package contains library source intended for building other packages which
use the "arboard" feature of the "%{crate}" crate.

%package     -n %{name}+bashisms-devel
Summary:        Readline-like crate for CLI text input
BuildArch:      noarch
%description -n %{name}+bashisms-devel

This package contains library source intended for building other packages which
use the "bashisms" feature of the "%{crate}" crate.

%package     -n %{name}+crossbeam-devel
Summary:        Readline-like crate for CLI text input
BuildArch:      noarch
%description -n %{name}+crossbeam-devel

This package contains library source intended for building other packages which
use the "crossbeam" feature of the "%{crate}" crate.

%package     -n %{name}+external_printer-devel
Summary:        Readline-like crate for CLI text input
BuildArch:      noarch
%description -n %{name}+external_printer-devel

This package contains library source intended for building other packages which
use the "external_printer" feature of the "%{crate}" crate.

%package     -n %{name}+rusqlite-devel
Summary:        Readline-like crate for CLI text input
BuildArch:      noarch
%description -n %{name}+rusqlite-devel

This package contains library source intended for building other packages which
use the "rusqlite" feature of the "%{crate}" crate.

%package     -n %{name}+serde_json-devel
Summary:        Readline-like crate for CLI text input
BuildArch:      noarch
%description -n %{name}+serde_json-devel

This package contains library source intended for building other packages which
use the "serde_json" feature of the "%{crate}" crate.

%package     -n %{name}+sqlite-devel
Summary:        Readline-like crate for CLI text input
BuildArch:      noarch
%description -n %{name}+sqlite-devel

This package contains library source intended for building other packages which
use the "sqlite" feature of the "%{crate}" crate.

%package     -n %{name}+sqlite-dynlib-devel
Summary:        Readline-like crate for CLI text input
BuildArch:      noarch
%description -n %{name}+sqlite-dynlib-devel

This package contains library source intended for building other packages which
use the "sqlite-dynlib" feature of the "%{crate}" crate.

%package     -n %{name}+system_clipboard-devel
Summary:        Readline-like crate for CLI text input
BuildArch:      noarch
%description -n %{name}+system_clipboard-devel

This package contains library source intended for building other packages which
use the "system_clipboard" feature of the "%{crate}" crate.

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
%files -n rust-reedline-devel -f %{oreon_filedir}/rust-reedline-devel.list

%changelog

%autochangelog
