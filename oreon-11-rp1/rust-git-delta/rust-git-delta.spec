%global source0_hash 7ff64457ae0530c322df9b6fc1d7fbc017870006cf4bbba334cd93c2f145ad3c
%bcond check 1
%global crate git-delta
Name:           rust-git-delta
Version:        0.19.2
Release:        1%{?dist}
Summary:        Syntax-highlighting pager for git
License:        MIT
URL:            https://crates.io/crates/git-delta
Source0:        https://static.crates.io/crates/git-delta/git-delta-%{version}.crate
Patch:          git-delta-fix-metadata.diff
Patch2:         0001-Update-terminal-colorsaurus-to-version-1.0.3.patch
%if %{with check}
%endif
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  git-core
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Syntax-highlighting pager for git
License:        %{shrink:
                MIT AND
                0BSD AND
                Apache-2.0 AND
                BSD-2-Clause AND
                BSD-2-Clause-Views AND
                BSD-3-Clause AND
                CC-BY-SA-3.0 AND
                GPL-2.0-only WITH GCC-exception-2.0 AND
                LGPL-3.0-or-later AND
                MIT AND
                MPL-2.0 AND
                Unicode-3.0 AND
                Unicode-DFS-2016 AND
                Unlicense AND
                WTFPL AND
                (0BSD OR MIT OR Apache-2.0) AND
                (Apache-2.0 OR BSL-1.0) AND
                (Apache-2.0 OR MIT) AND
                (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
                (MIT OR Zlib OR Apache-2.0) AND
                (Unlicense OR MIT)
                }
%description -n %{crate}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
cp -p src/utils/bat/LICENSE LICENSE-bat
%oreon_vendor_cargo
%build

%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%install
%cargo_install
install -Dpm0644 etc/completion/completion.bash \
    -T %{buildroot}/%{bash_completions_dir}/delta.bash
install -Dpm0644 etc/completion/completion.fish \
    -T %{buildroot}/%{fish_completions_dir}/delta.fish
install -Dpm0644 etc/completion/completion.zsh \
    -T %{buildroot}/%{zsh_completions_dir}/_delta
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n git-delta -f %{oreon_filedir}/git-delta.list

%changelog

%autochangelog
