%global source0_hash 5f5ed7ac0ff3d75b38fc615e8d88885121e7346a498d2b48c4313b7997703723
%bcond check 1
Name:           ty
Version:        0.0.82
Release:        1%{?dist}
Summary:        Extremely fast Python type checker and language server
SourceLicense:  %{shrink:
    MIT AND
    Apache-2.0 AND
    (Apache-2.0 OR MIT)
    }
License:        %{shrink:
    MIT AND
    Apache-2.0 AND
    (Apache-2.0 OR BSD-2-Clause) AND
    (Apache-2.0 OR BSL-1.0) AND
    (Apache-2.0 OR MIT) AND
    (Apache-2.0 OR MIT OR Zlib) AND
    (Apache-2.0 OR MIT-0) AND
    (Apache-2.0 OR Apache-2.0 WITH LLVM-exception OR MIT) AND
    BSD-3-Clause AND
    (BSD-3-Clause OR MIT) AND
    CC0-1.0 AND
    ISC AND
    (MIT OR Unlicense) AND
    MPL-2.0 AND
    PSF-2.0 AND
    Unicode-3.0 AND
    Unicode-DFS-2016 AND
    WTFPL AND
    Zlib
    }
URL:            https://github.com/astral-sh/ty
Source0:        https://github.com/astral-sh/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
%global ruff_git https://github.com/astral-sh/ruff
%global ruff_rev 34998be22ec3a77d398bbd55234ef8740f768329
%global ruff_baseversion 0.15.7
%global ruff_snapdate 20260326
Source100:        %{ruff_git}/archive/%{ruff_rev}/ruff-%{ruff_rev}.tar.gz
%global lsp_types_git https://github.com/astral-sh/lsp-types
%global lsp_types_rev e15db0593f0ecbbd80599c3f5880e4bf5da1ca0c
%global lsp_types_baseversion 0.95.1
%global lsp_types_snapdate 20260220
Source200:      %{lsp_types_git}/archive/%{lsp_types_rev}/lsp-types-%{lsp_types_rev}.tar.gz
%global salsa_git https://github.com/salsa-rs/salsa
%global salsa_rev 2f687a17ceea8ec7aaa605561ccbde938ccef086
%global salsa_baseversion 0.26.1
%global salsa_snapdate 20260320
Source300:      %{salsa_git}/archive/%{salsa_rev}/salsa-%{salsa_rev}.tar.gz
%global typeshed_rev f8f0794d0fe249c06dc9f31a004d85be6cca6ced
%global typeshed_baseversion 0
%global typeshed_snapdate 20260314
Patch:          0001-Downstream-patch-always-find-the-system-wide-ty-exec.patch
Patch102:          0002-drop-unavailable-features-from-uuid-dependency.patch
Patch103:          0003-ignore-vendored-annotate-snippets-tests-that-hang-in.patch
ExcludeArch:    %{ix86}
%global _smp_tasksize_proc 16384
%global ruff_snapinfo %{ruff_snapdate}git%{sub %{ruff_rev} 1 7}
%global ruff_version %{ruff_baseversion}^%{ruff_snapinfo}
Provides:       bundled(ruff) = %{ruff_version}
%global lsp_types_snapinfo %{lsp_types_snapdate}git%{sub %{lsp_types_rev} 1 7}
%global lsp_types_version %{lsp_types_baseversion}^%{lsp_types_snapinfo}
Provides:       bundled(crate(lsp-types)) = %{lsp_types_version}
%global salsa_snapinfo %{salsa_snapdate}git%{sub %{salsa_rev} 1 7}
%global salsa_version %{salsa_baseversion}^%{salsa_snapinfo}
Provides:       bundled(crate(salsa)) = %{salsa_version}
Provides:       bundled(crate(salsa-macros)) = %{salsa_version}
Provides:       bundled(crate(salsa-macro-rules)) = %{salsa_version}
%global typeshed_snapinfo %{typeshed_snapdate}git%{sub %{typeshed_rev} 1 7}
%global typeshed_version %{typeshed_baseversion}^%{typeshed_snapinfo}
Provides:       bundled(typeshed) = %{typeshed_version}
Provides:       bundled(crate(annotate-snippets)) = 0.11.5
Provides:       bundled(crate(lsp-types)) = 0.95.1
%global common_description %{expand:
An extremely fast Python type checker and language server, written in Rust.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(maturin) < 2.0
BuildRequires:  python3dist(maturin) >= 1.0
Requires:       python3-ty = %{version}-%{release}
# /oreon:deps
%description %{common_description}

%package -n python3-ty
Summary:        Importable Python module for ty
BuildArch:      noarch
Requires:       ty = %{version}-%{release}
%description -n python3-ty %{common_description}

This package provides an importable Python module for ty.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -N
%autopatch -p1 -M99

# See comments above Source100:
%setup -q -T -D -b 100 -n ty-%{version}
# Replace the empty directory corresponding to a git submodule with the
# extracted ruff source tree.
rmdir ruff
mv ../ruff-%{ruff_rev} ruff
pushd ruff
%autopatch -p1 -m100 -M199
# We have to adjust this both in the top-level pyproject.toml and in the ruff
# pyproject.toml. (TODO: Is this really true?)
tomcli set pyproject.toml false tool.maturin.strip
popd

# Usage: git2path SELECTOR PATH
# Replace a git dependency with a path dependency in Cargo.toml
git2path() {
  tomcli set Cargo.toml del "${1}.git"
  tomcli set Cargo.toml del "${1}.rev"
  tomcli set Cargo.toml str "${1}.path" "${2}"
}

# See comments above Source200:
%setup -q -T -D -b 200 -n ty-%{version}
# Adding the crate to the workspace (in this case implicitly, by linking it
# under crates/) means %%cargo_generate_buildrequires can handle it correctly.
mv ../lsp-types-%{lsp_types_rev} ruff/crates/lsp-types
pushd ruff
git2path workspace.dependencies.lsp-types crates/lsp-types
pushd crates/lsp-types
%autopatch -p1 -m200 -M299
popd
popd
install -t LICENSE.bundled/lsp-types -D -p -m 0644 ruff/crates/lsp-types/LICENSE

# See comments above Source300:
%setup -q -T -D -b 300 -n ty-%{version}
mv ../salsa-%{salsa_rev} ruff/crates/salsa
mv ruff/crates/salsa/components/salsa-macro-rules ruff/crates/salsa-macro-rules
mv ruff/crates/salsa/components/salsa-macros ruff/crates/salsa-macros
pushd ruff
git2path workspace.dependencies.salsa crates/salsa
pushd crates/salsa
%autopatch -p1 -m300 -M399
popd
# These were taken from salsa’s workspace, but we have added the salsa crates
# to ruff’s workspace, and we cannot have more than one workspace.
tomcli set crates/salsa/Cargo.toml del 'workspace.package.authors'
tomcli set crates/salsa/Cargo.toml list package.authors 'Salsa developers'
for field in edition license repository rust-version
do
  value="$(tomcli get crates/salsa/Cargo.toml "workspace.package.${field}")"
  tomcli set crates/salsa/Cargo.toml del "workspace.package.${field}"
  tomcli set crates/salsa/Cargo.toml str "package.${field}" "${value}"
done
# Now remove salsa’s workspace entirely.
tomcli set crates/salsa/Cargo.toml del workspace
# Fix up paths to ancillary salsa crates since we have moved them into the
# workspace.
tomcli set crates/salsa/Cargo.toml str dependencies.salsa-macro-rules.path \
    '../salsa-macro-rules'
tomcli set crates/salsa/Cargo.toml str dependencies.salsa-macros.path \
    '../salsa-macros'
tomcli set crates/salsa/Cargo.toml str \
    "target.'cfg(any())'.dependencies.salsa-macros.path" \
    '../salsa-macros'
# Remove examples, and omit dev-dependencies that are only for examples:
rm -rv crates/salsa/examples/
tomcli set crates/salsa/Cargo.toml del example
for crate in crossbeam-channel eyre notify-debouncer-mini ordered-float
do
  tomcli set crates/salsa/Cargo.toml del "dev-dependencies.${crate}"
done
# Remove benchmark-only dev-dependencies
for crate in annotate-snippets codspeed-criterion-compat
do
  tomcli set crates/salsa/Cargo.toml del "dev-dependencies.${crate}"
done
# Remove the shuttle feature since rust-shuttle is not packaged
tomcli set crates/salsa/Cargo.toml del features.shuttle
tomcli set crates/salsa/Cargo.toml del dependencies.shuttle
# Remove bundled, pre-compiled mermaid JavaScript to prove it is not used.
rm crates/salsa/book/mermaid.min.js
popd
install -t LICENSE.bundled/salsa -D -p -m 0644 ruff/crates/salsa/LICENSE-*

# Loosen some version bounds. We retain this comment and the following example
# even when there are currently no dependencies that need to be adjusted.
#
# # foocrate
# #   wanted: 0.2.0
# #   currently packaged: 0.1.2
# #   https://bugzilla.redhat.com/show_bug.cgi?id=1234567
# tomcli set Cargo.toml str workspace.dependencies.foocrate.version 0.1.2

# Collect license files of vendored dependencies in the main source archive
install -t LICENSE.bundled/typeshed -D -p -m 0644 \
    ruff/crates/ty_vendored/vendor/typeshed/LICENSE
install -t LICENSE.bundled/annotate_snippets -D -p -m 0644 \
    ruff/crates/ruff_annotate_snippets/LICENSE-*

# Patch out foreign (e.g. Windows-only) dependencies. Follow symbolic links so
# that we also patch the bundled crates we just finished setting up.
find -L . -type f -name Cargo.toml -print \
    -execdir rust2rpm-helper strip-foreign -o '{}' '{}' ';'

# Drop unused subproject crates.
# binary crate for running micro-benchmarks.
rm -rv ruff/crates/ruff_benchmark
# binary crate containing utilities used in the development of Ruff itself
rm -rv ruff/crates/ruff_dev
# library crate for exposing Ruff as a WebAssembly module. Powers the
# [Ruff Playground](https://play.ruff.rs/).
rm -rv ruff/crates/ruff_wasm ruff/crates/ty_wasm

# Verify we have the correct snapshot hash for typeshed
typeshed_rev_file='ruff/crates/ty_vendored/vendor/typeshed/source_commit.txt'
typeshed_rev_in_source="$(cat "${typeshed_rev_file}")"
if [[ '%{typeshed_rev}' != "${typeshed_rev_in_source}" ]]
then
  cat 1>&2 <<EOF
Mismatch between %%{typeshed_rev}:
  %{typeshed_rev}
and ${typeshed_rev_file}:
  ${typeshed_rev_in_source}
Please update %%{typeshed_rev} in the spec file!
EOF
  exit 1
fi

# Verify we have the correct base version for salsa
salsa_version_in_source="$(tomcli get ruff/crates/salsa/Cargo.toml package.version)"
if [[ '%{salsa_baseversion}' != "${salsa_version_in_source}" ]]
then
  cat 1>&2 <<EOF
Mismatch between %%{salsa_baseversion}:
  %{salsa_baseversion}
and version in ruff/crates/salsa/Cargo.toml:
  ${salsa_version_in_source}
Please update %%{salsa_baseversion} in the spec file!
EOF
  exit 1
fi

%build

export RUSTFLAGS='%{build_rustflags}'
%pyproject_wheel
LDEPS="${PWD}/LICENSE.dependencies"
pushd ruff
%{cargo_license_summary}
%{cargo_license} > "${LDEPS}"
popd
%install
%pyproject_install
if [ '%{python3_sitearch}' != '%{python3_sitelib}' ]
then
  install -d %{buildroot}%{python3_sitelib}
  mv %{buildroot}%{python3_sitearch}/ty* %{buildroot}%{python3_sitelib}
  sed -r -i 's@%{python3_sitearch}@%{python3_sitelib}@' %{pyproject_files}
fi
ruff/target/rpm/ty generate-shell-completion bash > ty.bash
ruff/target/rpm/ty generate-shell-completion fish > ty.fish
ruff/target/rpm/ty generate-shell-completion zsh > _ty
install -Dpm 0644 ty.bash -t %{buildroot}/%{bash_completions_dir}
install -Dpm 0644 ty.fish -t %{buildroot}/%{fish_completions_dir}
install -Dpm 0644 _ty -t %{buildroot}/%{zsh_completions_dir}
%oreon_autofiles python3-ty usr/lib/python3*/site-packages/ty* usr/lib64/python3*/site-packages/ty* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/ty* usr/lib64/python3*/site-packages/ty* usr/bin/*

%check

%if %{with check}
skip="${skip-} --skip backtrace_works"
skip="${skip-} --skip color/"
skip="${skip-} --skip compile_fail"
skip="${skip-} --skip python_environment::ty_environment_and_active_environment"
skip="${skip-} --skip python_environment::ty_environment_and_discovered_venv"
skip="${skip-} --skip python_environment::ty_environment_is_only_environment"
skip="${skip-} --skip python_environment::ty_environment_is_system_not_virtual"
%ifarch s390x
skip="${skip-} --skip mdtest__generics_specialize_constrained"
%if %{defined fc42}
skip="${skip-} --skip cycle_nested_deep_panic"
%endif
%endif
pushd ruff
export RUST_TEST_THREADS=1
%cargo_test -- -- ${skip-}
popd
%endif
%pyproject_check_import
%files
%files -n python3-ty -f %{oreon_filedir}/python3-ty.list

%changelog

%autochangelog
