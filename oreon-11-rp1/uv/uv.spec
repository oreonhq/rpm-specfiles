%global source0_hash 2232ede2d645f347bf6d412563b581e90bdb33b60bd295130cb64e56a65d4640
%bcond check 1
%bcond it %{undefined el10}
Name:           uv
Version:        0.12.15
Release:        1%{?dist}
Summary:        An extremely fast Python package installer and resolver, written in Rust
License:        %{shrink:
                0BSD AND
                (0BSD OR Apache-2.0 OR MIT) AND
                Apache-2.0 AND
                (Apache-2.0 OR BSD-2-Clause) AND
                (Apache-2.0 OR BSD-2-Clause OR MIT) AND
                (Apache-2.0 OR BSL-1.0) AND
                (Apache-2.0 OR ISC OR MIT) AND
                (Apache-2.0 OR MIT) AND
                (Apache-2.0 OR MIT OR Zlib) AND
                (Apache-2.0 OR MIT-0) AND
                (Apache-2.0 WITH LLVM-exception) AND
                (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
                BSD-3-Clause AND
                CC0-1.0 AND
                CDLA-Permissive-2.0 AND
                ISC AND
                (LGPL-3.0-or-later OR MIT) AND
                (LGPL-3.0-or-later OR MPL-2.0) AND
                MIT AND
                MIT-0 AND
                (MIT OR Unlicense) AND
                MPL-2.0 AND
                Unicode-3.0 AND
                Unicode-DFS-2016 AND
                Zlib AND
                bzip2-1.0.6
                }
URL:            https://github.com/astral-sh/uv
Source0:        https://github.com/astral-sh/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        uv.toml
Patch:          0001-Downstream-patch-always-find-the-system-wide-uv-exec.patch
ExcludeArch:    %{ix86}
%global rustflags_debuginfo 1
%global _smp_tasksize_proc 4096
%global _smp_ncpus_max 72
%if %{with check} && %{with it}
%endif
Provides:       bundled(crate(pep440_rs)) = 0.7.0
Provides:       bundled(crate(pep508_rs)) = 0.7.0
Provides:       bundled(crate(ripunzip)) = 0.4.0
Provides:       bundled(crate(rattler_installs_packages)) = 0.9.0
Provides:       bundled(crate(glibc_version)) = 0.1.2^20221117git5e1002d
Provides:       bundled(crate(r-shquote)) = 0.1.1
Provides:       bundled(crate(keyring)) = 4.0.0~rc2
Provides:       bundled(python3dist(virtualenv)) = 20.34
Provides:       bundled(python3dist(packaging)) = 24.1~dev0^20240310gitcc938f9
Provides:       bundled(python3dist(pipreqs)) = 0.5.0
%global common_description %{expand:
An extremely fast Python package and project manager, written in Rust.
Highlights:
  • A single tool to replace pip, pip-tools, pipx, poetry, pyenv, twine,
    virtualenv, and more.
  • 10-100x faster than pip.
  • Provides comprehensive project management, with a universal lockfile.
  • Runs scripts, with support for inline dependency metadata.
  • Installs and manages Python versions.
  • Runs and installs tools published as Python packages.
  • Includes a pip-compatible interface for a performance boost with a familiar
    CLI.
  • Supports Cargo-style workspaces for scalable projects.
  • Disk-space efficient, with a global cache for dependency deduplication.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(maturin) < 2.0
BuildRequires:  python3dist(maturin) >= 1.0
Requires:       python3-uv = %{version}-%{release}
# /oreon:deps
%description %{common_description}

%package -n python3-uv
Summary:        Importable Python module for uv
BuildArch:      noarch
Requires:       uv = %{version}-%{release}
%description -n python3-uv %{common_description}

This package provides an importable Python module for uv.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Collect license files of vendored dependencies in the main source archive
install -t LICENSE.bundled/packaging -D -p -m 0644 \
    crates/uv-python/python/packaging/LICENSE.*
install -t LICENSE.bundled/pep440_rs -D -p -m 0644 crates/uv-pep440/License-*
install -t LICENSE.bundled/pep508_rs -D -p -m 0644 crates/uv-pep508/License-*
install -t LICENSE.bundled/pipreqs -D -p -m 0644 \
    crates/uv-build-frontend/src/pipreqs/LICENSE
install -t LICENSE.bundled/ripunzip -D -p -m 0644 \
    crates/uv-extract/src/vendor/LICENSE
# The original license text from rattler_installs_packages is present in a
# comment, but we want it in a separate file so we can ensure it is present in
# the binary RPM.
install -d LICENSE.bundled/rattler_installs_packages
awk '$2 == "BSD" { out=1 }; $2 == "```" { out=0 }; out' \
    crates/uv-client/src/remote_metadata.rs |
  sed -r 's@^///( |$)@@' |
  tee LICENSE.bundled/rattler_installs_packages/LICENSE
# Similarly for virtualenv. All files in
# crates/uv-virtualenv/src/activator/activate/ have the same license text.
install -d LICENSE.bundled/virtualenv
awk '$1 == "#" { out=1 }; $1 != "#" { out=0; exit }; out' \
    crates/uv-virtualenv/src/activator/activate |
  sed -r 's@^#( |$)@@' |
  tee LICENSE.bundled/virtualenv/LICENSE

# Patch out foreign (e.g. Windows-only) dependencies. Follow symbolic links so
# that we also patch the bundled crates we just finished setting up.
find -L . -type f -name Cargo.toml -print \
    -execdir rust2rpm-helper strip-foreign -o '{}' '{}' ';'

# The uv-trampoline crate (a fork of posy trampolines, from
# https://github.com/njsmith/posy) uses a set of trampoline Windows executables
# for launching Python scripts. These precompiled executables are funished by
# the uv-trampoline-builder crate. We must remove them to prove they are not
# used in the build. Since they are used only on Windows, nothing is lost by
# doing so.
rm -v crates/uv-trampoline-builder/trampolines/*.exe
# Per Cargo.toml, uv-trampoline is excluded from the workspace and not compiled
# because it still requires a nightly compiler. For now, we remove it entirely
# to show that we do not need to document bundling from posy. Note that we
# *cannot* cleanly remove uv-trampoline-builder, only the precompiled
# trampolines themselves.
rm -rv crates/uv-trampoline

# Remove the dependency on embed-manifest, which applies only when (cross-?)
# compiling for Windows.
tomcli set Cargo.toml del workspace.dependencies.embed-manifest
# We may have to do something more sophisticated if this build script ever
# starts to do anything other than just embedding a manifest on Windows.
rm -v crates/uv/build.rs
tomcli set crates/uv/Cargo.toml del build-dependencies.embed-manifest
# The embed-manifest depenency is also used in uv-trampoline, which we removed.

# Do not strip the compiled executable; we need useful debuginfo. Upstream set
# this intentionally, so this change makes sense to keep downstream-only.
tomcli set pyproject.toml false tool.maturin.strip
tomcli set Cargo.toml false profile.release.strip

# Exclude the bench crate from the workspace. We don’t need to build and run
# benchmarks, and it brings in unwanted additional dev dependencies.
tomcli set Cargo.toml append workspace.exclude crates/uv-bench
# The uv-dev crate provides “development utilities for uv,” which should not be
# needed here. It also brings extra dependencies that we would prefer to avoid.
tomcli set Cargo.toml append workspace.exclude crates/uv-dev

# Do not request static linking of anything (particularly, liblzma)
tomcli set Cargo.toml lists delitem \
    workspace.dependencies.xz2.features 'static'
tomcli set crates/uv/Cargo.toml lists delitem \
    features.default 'uv-distribution/static'
tomcli set crates/uv-distribution/Cargo.toml del features.static
tomcli set crates/uv-extract/Cargo.toml del features.static

# Disable several default features that control which tests are compiled and
# executed, and which are not usable in offline builds:
#
# - test-crates-io: Introduces a testing dependency on crates.io.
# - test-git: Introduces a testing dependency on Git. This sounds innocuous –
#   we have git! – but in fact, it controls tests of git dependencies, which
#   implies accessing remote repositories, e.g. on GitHub.
# - test-git-lfs: as for git, but also require Git Large File Storage; again,
#   this implies accessing remote repositories
# - test-pypi: Introduces a testing dependency on PyPI.
# - test-python-managed: Introduces a testing dependency on managed Python
#   installations. (These are pre-compiled Pythons downloaded from the
#   Internet.)
# - test-r2: Introduces a testing dependency on R2.
#
# These are OK:
# - test-python: Introduces a testing dependency on a local Python installation.
# - test-slow: Include "slow" test cases.
# - test-ecosystem: Includes test cases that require ecosystem packages
#
# Note that the python-patch feature, which ”introduces a dependency on a local
# Python installation with specific patch versions,” is already not among the
# default features.
tomcli set crates/uv/Cargo.toml lists delitem features.test-defaults \
    'test-(crates-io|git(-lfs)?|pypi|python-managed|r2)'
# - -test-osv: Introduces a testing dependency on osv.dev.
tomcli set crates/uv-audit/Cargo.toml lists delitem features.default \
    'test-(osv)'

%if %{without it}
# Integration tests (it crate) nearly all require specific Python interpreter
# versions (major.minor, not major.minor.patch, unless the python-patch feature
# is enabled). We might choose to disable this in order to double-check that
# everything else works well with only the primary system Python in the
# environment.
# -p uv --test it:
mods="${mods-}${mods+|}branching_urls"
mods="${mods-}${mods+|}build_backend"
mods="${mods-}${mods+|}pip_(check|list|show|tree|uninstall)"
mods="${mods-}${mods+|}python_(dir|find|install|list|pin)"
mods="${mods-}${mods+|}venv"
mods="${mods-}${mods+|}version"
mods="${mods-}${mods+|}workspace"
comment='Downstream-only: skip, needs specific Python interpreter versions'
sed -r -i "s@mod (${mods});@// ${comment}\n#[cfg(any())]\n&@" \
    crates/uv/tests/it/main.rs
%endif

# For unclear reasons, maturin checks for the presence of optional crate
# dependencies that correspond to features we have not enabled. We need to
# patch out those that are not packaged, an unfortunate but straightforward
# hack. See further commentary in %%generate_buildrequires.
tomcli set crates/uv/Cargo.toml del dependencies.axoupdater
tomcli set crates/uv/Cargo.toml del features.self-update
tomcli set crates/uv/Cargo.toml del features.tracing-durations-export
tomcli set crates/uv/Cargo.toml del dependencies.tracing-durations-export

# We retain the following example even when there are currently no dependencies
# that need to be adjusted.
#
# # foocrate
# #   wanted: 0.2.0
# #   currently packaged: 0.1.2
# #   https://bugzilla.redhat.com/show_bug.cgi?id=1234567
# tomcli set Cargo.toml str workspace.dependencies.foocrate.version 0.1.2

%build

%pyproject_wheel
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%install
%pyproject_install
if [ '%{python3_sitearch}' != '%{python3_sitelib}' ]
then
  install -d %{buildroot}%{python3_sitelib}
  mv %{buildroot}%{python3_sitearch}/uv* %{buildroot}%{python3_sitelib}
  sed -r -i 's@%{python3_sitearch}@%{python3_sitelib}@' %{pyproject_files}
fi
for cmd in uv uvx
do
  target/rpm/${cmd} --generate-shell-completion bash > ${cmd}.bash
  target/rpm/${cmd} --generate-shell-completion fish > ${cmd}.fish
  target/rpm/${cmd} --generate-shell-completion zsh > _${cmd}
  install -Dpm 0644 ${cmd}.bash -t %{buildroot}/%{bash_completions_dir}
  install -Dpm 0644 ${cmd}.fish -t %{buildroot}/%{fish_completions_dir}
  install -Dpm 0644 _${cmd} -t %{buildroot}/%{zsh_completions_dir}
done
install -t '%{buildroot}%{_sysconfdir}/uv' -p -m 0644 -D '%{SOURCE1}'
%oreon_autofiles python3-uv usr/lib/python3*/site-packages/uv* usr/lib64/python3*/site-packages/uv* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/uv* usr/lib64/python3*/site-packages/uv* usr/bin/*

%check

%if %{with check}
skip="${skip-} --skip keyring::tests::fetch_url_no_host"
skip="${skip-} --skip keyring::tests::fetch_url_with_empty_username"
skip="${skip-} --skip keyring::tests::fetch_url_with_no_username"
skip="${skip-} --skip keyring::tests::fetch_url_with_password"
%if %{without it}
skip="${skip-} --skip version::self_version"
skip="${skip-} --skip version::self_version_json"
skip="${skip-} --skip version::self_version_short"
%endif
%ifnarch %{x86_64} %{arm64}
skip="${skip-} --skip python_list::python_list_downloads"
skip="${skip-} --skip python_list::python_list_with_mirrors"
%endif
%ifarch %{power64}
skip="${skip-} --skip python_pin::python_pin_resolve"
%endif
skip="${skip-} --skip registry_client::tests::test_redirect_to_server_with_credentials"
skip="${skip-} --skip remote_metadata::remote_metadata_with_and_without_cache"
skip="${skip-} --skip tests::built_by_uv_building"
skip="${skip-} --skip base_client::tests::retried_status_codes"
%cargo_test -- -- --exact ${skip-}
%endif
%pyproject_check_import
%files
%files -n python3-uv -f %{oreon_filedir}/python3-uv.list

%changelog

%autochangelog
