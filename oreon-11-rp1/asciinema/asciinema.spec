%global source0_hash e7e49a09c664a76afc5bc25ca09871eb090bfbe68a2ddbc72750d3cb215d36f1
Name:           asciinema
Version:        3.2.1
Release:        1%{?dist}
Summary:        Terminal session recorder, streamer and player
SourceLicense:  GPL-3.0-or-later
License:        %{shrink:
    GPL-3.0-or-later AND
    Apache-2.0 AND
    BSD-3-Clause AND
    ISC AND
    MIT AND
    Unicode-3.0 AND
    Unicode-DFS-2016 AND
    (0BSD OR MIT OR Apache-2.0) AND
    (Apache-2.0 OR BSL-1.0) AND
    (Apache-2.0 OR ISC OR MIT) AND
    (Apache-2.0 OR MIT) AND
    (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
    (BSD-2-Clause OR Apache-2.0 OR MIT) AND
    (MIT OR Zlib OR Apache-2.0) AND
    (Unlicense OR MIT)
}
URL:            https://asciinema.org
Source0:        https://github.com/asciinema/asciinema/archive/v%{version}/asciinema-%{version}.tar.gz
Patch:          0001-Update-tokio-tungstenite-from-0.26-to-0.28.patch
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description
asciinema (aka asciinema CLI or asciinema recorder) is a command-line
tool for recording and live streaming terminal sessions.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n asciinema-%{version} -p1
%oreon_vendor_cargo
%build

export ASCIINEMA_GEN_DIR=assets
%cargo_build
%cargo_license_summary
%{cargo_license} > LICENSE.dependencies
%install
install -Dpm 0755 target/rpm/asciinema -t %{buildroot}/%{_bindir}/
install -Dpm 0644 assets/man/*.1 -t %{buildroot}/%{_mandir}/man1/
install -Dpm 0644 assets/completion/asciinema.bash -t %{buildroot}/%{bash_completions_dir}/
install -Dpm 0644 assets/completion/asciinema.fish -t %{buildroot}/%{fish_completions_dir}/
install -Dpm 0644 assets/completion/_asciinema -t %{buildroot}/%{zsh_completions_dir}
%oreon_autofiles main

%check

%cargo_test -- -- --test-threads 1
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
