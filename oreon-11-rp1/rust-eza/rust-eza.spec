%global source0_hash 334199a8059861f81a2d3d888a45f44fa55f82dade2412e752144a404d7ae9af
%bcond check 1
%global crate eza
Name:           rust-eza
Version:        0.23.5
Release:        1%{?dist}
Summary:        Modern replacement for ls
License:        EUPL-1.2
URL:            https://crates.io/crates/eza
Source0:        https://static.crates.io/crates/eza/eza-%{version}.crate
Patch:          eza-fix-metadata-auto.diff
Patch:          eza-fix-metadata.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  pandoc-cli
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Modern replacement for ls
License:        EUPL-1.2
%description -n %{crate}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Modern replacement for ls
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+git-devel
Summary:        Modern replacement for ls
BuildArch:      noarch
%description -n %{name}+git-devel

This package contains library source intended for building other packages which
use the "git" feature of the "%{crate}" crate.

%package     -n %{name}+git2-devel
Summary:        Modern replacement for ls
BuildArch:      noarch
%description -n %{name}+git2-devel

This package contains library source intended for building other packages which
use the "git2" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
for man in eza.1 eza_colors.5 ; do
   pandoc --standalone -f markdown -t man man/$man.md > man/$man
done
%install
%cargo_install
install -Dpm 0644 completions/bash/eza -t %{buildroot}/%{bash_completions_dir}/
install -Dpm 0644 completions/fish/eza.fish -t %{buildroot}/%{fish_completions_dir}/
install -Dpm 0644 completions/zsh/_eza -t %{buildroot}/%{zsh_completions_dir}/
install -Dpm 0644 man/eza.1 -t %{buildroot}/%{_mandir}/man1
install -Dpm 0644 man/eza_colors.5 -t %{buildroot}/%{_mandir}/man5
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n eza -f %{oreon_filedir}/eza.list
%files -n rust-eza-devel -f %{oreon_filedir}/rust-eza-devel.list

%changelog

%autochangelog
