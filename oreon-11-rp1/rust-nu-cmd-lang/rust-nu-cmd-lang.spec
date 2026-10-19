%global source0_hash 8e2f2d51d6b021064a6c431a22ca71df0882c1290be98753723f80838f388adb
%bcond check 0
%global debug_package %{nil}
%global crate nu-cmd-lang
Name:           rust-nu-cmd-lang
Version:        0.99.1
Release:        1%{?dist}
Summary:        Nushell's core language commands
License:        MIT
URL:            https://crates.io/crates/nu-cmd-lang
Source0:        https://static.crates.io/crates/nu-cmd-lang/nu-cmd-lang-%{version}.crate
Patch:          nu-cmd-lang-fix-metadata.diff
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
Summary:        Nushell's core language commands
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+mimalloc-devel
Summary:        Nushell's core language commands
BuildArch:      noarch
%description -n %{name}+mimalloc-devel

This package contains library source intended for building other packages which
use the "mimalloc" feature of the "%{crate}" crate.

%package     -n %{name}+sqlite-devel
Summary:        Nushell's core language commands
BuildArch:      noarch
%description -n %{name}+sqlite-devel

This package contains library source intended for building other packages which
use the "sqlite" feature of the "%{crate}" crate.

%package     -n %{name}+static-link-openssl-devel
Summary:        Nushell's core language commands
BuildArch:      noarch
%description -n %{name}+static-link-openssl-devel

This package contains library source intended for building other packages which
use the "static-link-openssl" feature of the "%{crate}" crate.

%package     -n %{name}+system-clipboard-devel
Summary:        Nushell's core language commands
BuildArch:      noarch
%description -n %{name}+system-clipboard-devel

This package contains library source intended for building other packages which
use the "system-clipboard" feature of the "%{crate}" crate.

%package     -n %{name}+trash-support-devel
Summary:        Nushell's core language commands
BuildArch:      noarch
%description -n %{name}+trash-support-devel

This package contains library source intended for building other packages which
use the "trash-support" feature of the "%{crate}" crate.

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
%files -n rust-nu-cmd-lang-devel -f %{oreon_filedir}/rust-nu-cmd-lang-devel.list

%changelog

%autochangelog
