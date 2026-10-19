%global source0_hash da14084bca610148224daa7e4d41b71c040599790e7c7b7dd12ddc1f7287af1f
%bcond check 1
%global debug_package %{nil}
%global crate nu-command
Name:           rust-nu-command
Version:        0.99.1
Release:        1%{?dist}
Summary:        Nushell's built-in commands
License:        MIT
URL:            https://crates.io/crates/nu-command
Source0:        https://static.crates.io/crates/nu-command/nu-command-%{version}.crate
Patch:          nu-command-fix-metadata-auto.diff
Patch:          nu-command-fix-metadata.diff
Patch2:         nu-command-fix-for-quick-xml-0_33.diff
Patch3:         https://gist.githubusercontent.com/decathorpe/3a17b07797adeea3858deebfe41d79bf/raw/a4c4e124a2110929eb5f449a6379444d794e4830/nu-command-0.99.1-port-to-uutils-0.7.0.patch
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  dos2unix
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
Summary:        Nushell's built-in commands
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+plugin-devel
Summary:        Nushell's built-in commands
BuildArch:      noarch
%description -n %{name}+plugin-devel

This package contains library source intended for building other packages which
use the "plugin" feature of the "%{crate}" crate.

%package     -n %{name}+rusqlite-devel
Summary:        Nushell's built-in commands
BuildArch:      noarch
%description -n %{name}+rusqlite-devel

This package contains library source intended for building other packages which
use the "rusqlite" feature of the "%{crate}" crate.

%package     -n %{name}+sqlite-devel
Summary:        Nushell's built-in commands
BuildArch:      noarch
%description -n %{name}+sqlite-devel

This package contains library source intended for building other packages which
use the "sqlite" feature of the "%{crate}" crate.

%package     -n %{name}+trash-devel
Summary:        Nushell's built-in commands
BuildArch:      noarch
%description -n %{name}+trash-devel

This package contains library source intended for building other packages which
use the "trash" feature of the "%{crate}" crate.

%package     -n %{name}+trash-support-devel
Summary:        Nushell's built-in commands
BuildArch:      noarch
%description -n %{name}+trash-support-devel

This package contains library source intended for building other packages which
use the "trash-support" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
dos2unix --keepdate src/progress_bar.rs
find . -type f -name '*.rs' -executable -exec chmod -v a-x '{}' '+'
%oreon_vendor_cargo
%build

%cargo_build
%install
%cargo_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%{cargo_test -- -- %{shrink:
    --skip commands::
    --skip debug::timeit::test_time_block
    --skip format_conversions::
    --skip strings::split::words::test::test_incompat_flags
    --skip strings::split::words::test::mixed_letter_number
    --skip strings::str_::stats::test_count_counts_lines
    --skip format_conversions::
    --skip system::run_external::test::test_expand_glob
}}
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-nu-command-devel -f %{oreon_filedir}/rust-nu-command-devel.list

%changelog

%autochangelog
