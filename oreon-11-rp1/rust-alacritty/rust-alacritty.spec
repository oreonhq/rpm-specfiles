%global source0_hash 7071586605718f8b93d55e3057da6d0e863b9237a5fb7face7a72770d3dd02bd
%bcond check 1
%global crate alacritty
Name:           rust-alacritty
Version:        0.17.0
Release:        1%{?dist}
Summary:        Fast, cross-platform, OpenGL terminal emulator
License:        Apache-2.0
URL:            https://crates.io/crates/alacritty
Source0:        https://static.crates.io/crates/alacritty/alacritty-%{version}.crate
Patch:          alacritty-fix-metadata-auto.diff
Patch:          alacritty-fix-metadata.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  rustc
BuildRequires:  scdoc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Fast, cross-platform, OpenGL terminal emulator
License:        %{shrink:
                (0BSD OR MIT OR Apache-2.0)
                AND Apache-2.0
                AND (Apache-2.0 OR BSL-1.0)
                AND (Apache-2.0 OR MIT)
                AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT)
                AND BSD-2-Clause
                AND (BSD-2-Clause OR Apache-2.0 OR MIT)
                AND BSD-3-Clause
                AND CC0-1.0
                AND ISC
                AND MIT
                AND (MIT OR Apache-2.0 OR Zlib)
                AND Unicode-DFS-2016
                AND (Unlicense OR MIT)
                }
Requires:       libwayland-egl
Requires:       libxkbcommon-x11
%description -n %{crate}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
for fname in alacritty-bindings.5 alacritty-msg.1 alacritty.1 alacritty.5; do
    scdoc <extra/man/$fname.scd >extra/man/$fname
done
%install
%cargo_install
desktop-file-install --dir=%{buildroot}%{_datadir}/applications extra/linux/Alacritty.desktop
install -m644 -pvD extra/completions/alacritty.bash %{buildroot}%{bash_completions_dir}/alacritty
install -m644 -pvD extra/completions/_alacritty     %{buildroot}%{zsh_completions_dir}/_alacritty
install -m644 -pvD extra/completions/alacritty.fish %{buildroot}%{fish_completions_dir}/alacritty.fish
install -m644 -pvD extra/logo/alacritty-term.svg    %{buildroot}%{_datadir}/pixmaps/Alacritty.svg
install -m644 -pvD -t %{buildroot}%{_metainfodir}   extra/linux/org.alacritty.Alacritty.appdata.xml
for fname in alacritty-bindings.5 alacritty-msg.1 alacritty.1 alacritty.5; do
    install -m644 -pvD "extra/man/$fname" "%{buildroot}%{_mandir}/man${fname##*.}/$fname"
done
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
%cargo_test -- -- --skip cli::tests::completions
%endif
%files -f %{oreon_filedir}/main.list
%files -n alacritty -f %{oreon_filedir}/alacritty.list

%changelog

%autochangelog
