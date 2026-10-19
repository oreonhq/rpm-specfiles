%global source0_hash 1ad10dc8c908255abf125edc3574600c5cfd88fb7a072e2729865049095f3664
%bcond check 1
%global crate lsd
Name:           rust-lsd
Version:        1.2.0
Release:        1%{?dist}
Summary:        Ls command with a lot of pretty colors and some other stuff
License:        Apache-2.0
URL:            https://crates.io/crates/lsd
Source0:        https://static.crates.io/crates/lsd/lsd-%{version}.crate
Patch:          lsd-fix-metadata-auto.diff
Patch:          lsd-fix-metadata.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Ls command with a lot of pretty colors and some other stuff
License:        %{shrink:
  (MIT OR Apache-2.0) AND BSD-3-Clause AND GPL-2.0-only WITH GCC-exception-2.0 AND MIT
  AND Unicode-DFS-2016
  AND Apache-2.0
  AND (Apache-2.0 OR BSL-1.0)
  AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT)
  AND MIT
  AND MPL-2.0
  AND Unicode-3.0
  AND (Unlicense OR MIT)
}
%description -n %{crate}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

mkdir completions
export SHELL_COMPLETIONS_DIR=completions
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%install
%cargo_install
install -Dpm 0644 completions/lsd.bash -t %{buildroot}/%{bash_completions_dir}
install -Dpm 0644 completions/lsd.fish -t %{buildroot}/%{fish_completions_dir}
install -Dpm 0644 completions/_lsd -t %{buildroot}/%{zsh_completions_dir}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%cargo_test -- -- --skip git::tests::test_git_workflow
%endif
%files -f %{oreon_filedir}/main.list
%files -n lsd -f %{oreon_filedir}/lsd.list

%changelog

%autochangelog
