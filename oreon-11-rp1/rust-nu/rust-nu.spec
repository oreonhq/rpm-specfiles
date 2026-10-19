%global source0_hash 5f4eb1c96e4041567c169f3d6ce374f6ebc749ff7da4997d6d621fc074110263
%bcond check 1
%global _smp_tasksize_proc 4096
%if %{defined el9}
%global _smp_ncpus_max 64
%endif
%global crate nu
Name:           rust-nu
Version:        0.99.1
Release:        1%{?dist}
Summary:        New type of shell
License:        MIT
URL:            https://crates.io/crates/nu
Source0:        https://static.crates.io/crates/nu/nu-%{version}.crate
Patch:          nu-fix-metadata-auto.diff
Patch:          nu-fix-metadata.diff
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        New type of shell
License:        %{shrink:
    MIT AND
    (Apache-2.0 OR MIT) AND
    BSD-3-Clause AND
    Unicode-DFS-2016 AND
    (0BSD OR MIT OR Apache-2.0) AND
    Apache-2.0 AND
    (Apache-2.0 OR BSL-1.0) AND
    (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
    (BSD-2-Clause OR Apache-2.0 OR MIT) AND
    CC-PDDC AND
    CC0-1.0 AND
    ISC AND
    (MIT OR Apache-2.0 OR Zlib) AND
    (MIT-0 OR Apache-2.0) AND
    MPL-2.0 AND
    Unicode-3.0 AND
    (Unlicense OR MIT) AND
    Zlib
}
%description -n %{crate}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
rm -rv wix/
%oreon_vendor_cargo
%build

%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%install
%cargo_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

export RUST_TEST_THREADS=16
%{cargo_test -- -- %{shrink:
    --skip plugin_persistence::
    --skip repl::test_custom_commands::deprecated_boolean_flag
    --skip repl::test_custom_commands::infinite_mutual_recursion_does_not_panic
    --skip repl::test_custom_commands::infinite_recursion_does_not_panic
    --skip repl::test_custom_commands::override_table_eval_file
    --skip repl::test_env::default_nu_lib_dirs_type
    --skip repl::test_env::default_nu_plugin_dirs_type
    --skip repl::test_parser::assign_backtick_quoted_external_fails
    --skip repl::test_parser::assign_backtick_quoted_external_with_caret
    --skip repl::test_parser::assign_bare_external_fails
    --skip repl::test_parser::assign_bare_external_with_caret
    --skip repl::test_parser::not_panic_with_recursive_call
    --skip repl::test_spread::spread_external_args
    --skip repl::test_spread::spread_non_list_args
    --skip const_::
    --skip eval::
    --skip hooks::
    --skip modules::
    --skip overlays::
    --skip parsing::
    --skip path::
    --skip plugin_persistence::
    --skip plugins::
    --skip scope::
    --skip shell::
}}
%endif
%files -f %{oreon_filedir}/main.list
%files -n nu -f %{oreon_filedir}/nu.list

%changelog

%autochangelog
