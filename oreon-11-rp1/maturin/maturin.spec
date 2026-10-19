%global source0_hash 2c2ae37144811d365509889ed7220b0598487f1278c2441829c3abf56cc6324a
%bcond check 1
Name:           maturin
Version:        1.9.6
Release:        1%{?dist}
Summary:        Build and publish Rust crates as Python packages
SourceLicense:  MIT OR Apache-2.0
%global pypi_version %(echo %{version} | tr -d "~")
License:        %{shrink:
    0BSD AND
    Apache-2.0 AND
    Apache-2.0 WITH LLVM-exception AND
    BSD-3-Clause AND
    MIT AND
    MPL-2.0 AND
    Unicode-3.0 AND
    Unicode-DFS-2016 AND
    (0BSD OR MIT OR Apache-2.0) AND
    (Apache-2.0 OR BSD-2-Clause) AND
    (Apache-2.0 OR BSL-1.0) AND
    (Apache-2.0 OR MIT) AND
    (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
    (BSD-2-Clause OR Apache-2.0 OR MIT) AND
    (MIT OR Zlib OR Apache-2.0) AND
    (MIT-0 OR Apache-2.0) AND
    (Unlicense OR MIT)
}
URL:            https://github.com/PyO3/maturin
Source0:        https://files.pythonhosted.org/packages/source/m/maturin/maturin-1.9.6.tar.gz
Patch:          0001-drop-unavailable-features-and-unused-dev-dependencie.patch
Patch:          0002-drop-incompatible-cargo-flags-from-setuptools_rust.patch
Patch:          0003-remove-shebang-from-non-executable-__init__.py-file.patch
Patch:          0004-Bump-base64-from-0.21-to-0.22-and-itertools-from-0.1.patch
Patch:          0005-revert-to-using-setuptools-for-non-maturin-bootstrap.patch
Patch:          0006-Update-cargo_metadata-to-0.20.0-2864.patch
Requires:       cargo
%py_provides python3-maturin
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77.0.0
BuildRequires:  python3dist(setuptools-rust) >= 1.11.0
BuildRequires:  python3dist(tomli) >= 1.1.0
Requires:       python3-maturin = %{version}-%{release}
# /oreon:deps
%package -n       python3-maturin+zig
Summary:        Metapackage for python3-maturin zig extras
Requires:       python3-maturin = %{version}-%{release}
Requires:       python3dist(ziglang) >= 0.10.0
Requires:       python3dist(ziglang) < 0.13.0
Provides:       python3dist(maturin[zig]) = %{version}-%{release}

%description -n python3-maturin+zig
Metapackage for python3-maturin zig extras.

%package -n       python3-maturin+patchelf
Summary:        Metapackage for python3-maturin patchelf extras
Requires:       python3-maturin = %{version}-%{release}
Provides:       python3dist(maturin[patchelf]) = %{version}-%{release}

%description -n python3-maturin+patchelf
Metapackage for python3-maturin patchelf extras.

%description
Build and publish crates with pyo3, rust-cpython and cffi bindings as
well as rust binaries as python packages.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n maturin-%{pypi_version} -p1

%build

export RUSTFLAGS="%{build_rustflags}"
%pyproject_wheel
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%install
%pyproject_install
target/rpm/maturin completions bash > maturin.bash
target/rpm/maturin completions fish > maturin.fish
target/rpm/maturin completions zsh > _maturin
install -Dpm 0644 maturin.bash -t %{buildroot}/%{bash_completions_dir}
install -Dpm 0644 maturin.fish -t %{buildroot}/%{fish_completions_dir}
install -Dpm 0644 _maturin -t %{buildroot}/%{zsh_completions_dir}
%oreon_autofiles main
%if %{with check}
%check

%{cargo_test -- -- --exact %{shrink:
    --skip build_options::test::test_find_bridge_bin
    --skip build_options::test::test_find_bridge_cffi
    --skip build_options::test::test_find_bridge_pyo3
    --skip build_options::test::test_find_bridge_pyo3_abi3
    --skip build_options::test::test_find_bridge_pyo3_feature
    --skip metadata::test::test_implicit_readme
    --skip metadata::test::test_merge_metadata_from_pyproject_dynamic_license_test
    --skip metadata::test::test_merge_metadata_from_pyproject_toml
    --skip metadata::test::test_merge_metadata_from_pyproject_toml_with_customized_python_source_dir
    --skip metadata::test::test_pep639
    --skip pyproject_toml::tests::test_warn_missing_maturin_version
}}
%endif
%files

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.9.6-1
- Prepare for Oreon 11 (RP1)
