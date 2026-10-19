%global source0_hash 8b37f5c9d43ff8154f749839178f3d03d0dfeb84f4a98241c75c7b19910c5b86
%bcond check 1
%global cargo_install_lib 0
%global crate sequoia-git
Name:           rust-sequoia-git
Version:        0.5.0
Release:        1%{?dist}
Summary:        Tool for managing and enforcing a commit signing policy
License:        LGPL-2.0-or-later
URL:            https://crates.io/crates/sequoia-git
Source0:        https://static.crates.io/crates/sequoia-git/sequoia-git-%{version}.crate
Patch:          sequoia-git-fix-metadata.diff
%if %{with check}
%endif
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  faketime
BuildRequires:  git-core
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Tool for managing and enforcing a commit signing policy
License:        %{shrink:
    LGPL-2.0-or-later
    AND Apache-2.0
    AND BSD-3-Clause
    AND BSL-1.0
    AND GPL-2.0-only WITH GCC-exception-2.0
    AND MIT
    AND MPL-2.0
    AND Unicode-3.0
    AND Unicode-DFS-2016
    AND Zlib
    AND bzip2-1.0.6
    AND (0BSD OR MIT OR Apache-2.0)
    AND (Apache-2.0 OR BSL-1.0)
    AND (Apache-2.0 OR MIT)
    AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT)
    AND (BSD-2-Clause OR Apache-2.0 OR MIT)
    AND (MIT OR Apache-2.0 OR Zlib)
    AND (Unlicense OR MIT)
}
%description -n %{crate}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

export ASSET_OUT_DIR=target/assets
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%install
%cargo_install
mkdir -p %{buildroot}/%{_mandir}/man1
cp -pav target/assets/man-pages/sq-git*.1 %{buildroot}/%{_mandir}/man1/
install -Dpm 0644 target/assets/shell-completions/sq-git.bash \
    %{buildroot}/%{bash_completions_dir}/sq-git.bash
install -Dpm 0644 target/assets/shell-completions/sq-git.fish \
    %{buildroot}/%{fish_completions_dir}/sq-git.fish
install -Dpm 0644 target/assets/shell-completions/_sq-git \
    %{buildroot}/%{zsh_completions_dir}/_sq-git
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n sequoia-git -f %{oreon_filedir}/sequoia-git.list

%changelog

%autochangelog
