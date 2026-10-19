%global source0_hash cf66d0164db6827afe1694b8d4939f36a5507b7186f8d3cc529c66baf03b0d09
%bcond check 1
%global crate bat
Name:           rust-bat
Version:        0.26.1
Release:        1%{?dist}
Summary:        Cat(1) clone with wings
License:        (MIT OR Apache-2.0) AND Apache-2.0 AND BSD-2-Clause AND BSD-2-Clause-Views AND BSD-3-Clause AND CC-BY-SA-3.0 AND MIT AND Unlicense AND WTFPL AND LicenseRef-Fedora-UltraPermissive
URL:            https://crates.io/crates/bat
Source0:        https://static.crates.io/crates/bat/bat-%{version}.crate
Patch:          bat-fix-metadata-auto.diff
Patch:          bat-fix-metadata.diff
Patch10:        0001-port-from-path_abs-to-path-absolutize.patch
%global _bundled_deps %{expand:
Provides:       bundled(sublime-syntax) = 4075~git759d6ee
Provides:       bundled(sublime-syntax-AWK)
Provides:       bundled(sublime-syntax-Ada)
Provides:       bundled(sublime-syntax-Apache)
Provides:       bundled(sublime-syntax-AsciiDoc)
Provides:       bundled(sublime-syntax-CMake)
Provides:       bundled(sublime-syntax-CoffeeScript)
Provides:       bundled(sublime-syntax-Crontab)
Provides:       bundled(sublime-syntax-Crontab-cron_descriptor)
Provides:       bundled(sublime-syntax-Crystal)
Provides:       bundled(sublime-syntax-Dart)
Provides:       bundled(sublime-syntax-Docker)
Provides:       bundled(sublime-syntax-DotENV)
Provides:       bundled(sublime-syntax-Elixir)
Provides:       bundled(sublime-syntax-Elm)
Provides:       bundled(sublime-syntax-Email)
Provides:       bundled(sublime-syntax-Fish)
Provides:       bundled(sublime-syntax-GLSL)
Provides:       bundled(sublime-syntax-GraphQL)
Provides:       bundled(sublime-syntax-Groff)
Provides:       bundled(sublime-syntax-HTML-Twig)
Provides:       bundled(sublime-syntax-JavaScript-Babel)
Provides:       bundled(sublime-syntax-Jsonnet)
Provides:       bundled(sublime-syntax-Julia)
Provides:       bundled(sublime-syntax-Kotlin)
Provides:       bundled(sublime-syntax-LLVM)
Provides:       bundled(sublime-syntax-Lean)
Provides:       bundled(sublime-syntax-LiveScript)
Provides:       bundled(sublime-syntax-MediaWiki)
Provides:       bundled(sublime-syntax-NSIS)
Provides:       bundled(sublime-syntax-Nginx)
Provides:       bundled(sublime-syntax-Ninja)
Provides:       bundled(sublime-syntax-Nix)
Provides:       bundled(sublime-syntax-Org-mode)
Provides:       bundled(sublime-syntax-PowerShell)
Provides:       bundled(sublime-syntax-Protobuf)
Provides:       bundled(sublime-syntax-Puppet)
Provides:       bundled(sublime-syntax-PureScript)
Provides:       bundled(sublime-syntax-QML)
Provides:       bundled(sublime-syntax-Robot)
Provides:       bundled(sublime-syntax-SCSS_Sass)
Provides:       bundled(sublime-syntax-SLS)
Provides:       bundled(sublime-syntax-Slim)
Provides:       bundled(sublime-syntax-Stylus)
Provides:       bundled(sublime-syntax-SublimeEthereum)
Provides:       bundled(sublime-syntax-Svelte)
Provides:       bundled(sublime-syntax-Swift)
Provides:       bundled(sublime-syntax-SystemVerilog)
Provides:       bundled(sublime-syntax-TOML)
Provides:       bundled(sublime-syntax-Terraform)
Provides:       bundled(sublime-syntax-TypeScript)
Provides:       bundled(sublime-syntax-VimL)
Provides:       bundled(sublime-syntax-Vue)
Provides:       bundled(sublime-syntax-Zig)
Provides:       bundled(sublime-syntax-cmd-help)
Provides:       bundled(sublime-syntax-gnuplot)
Provides:       bundled(sublime-syntax-hosts)
Provides:       bundled(sublime-syntax-http-request-response)
Provides:       bundled(sublime-syntax-varlink)
Provides:       bundled(sublime-syntax-vscode-wgsl)
Provides:       bundled(sublime-theme-1337-Scheme)
Provides:       bundled(sublime-theme-Coldark)
Provides:       bundled(sublime-theme-DarkNeon)
Provides:       bundled(sublime-theme-Nord-sublime)
Provides:       bundled(sublime-theme-Solarized)
Provides:       bundled(sublime-theme-TwoDark)
Provides:       bundled(sublime-theme-dracula-sublime)
Provides:       bundled(sublime-theme-github-sublime-theme)
Provides:       bundled(sublime-theme-gruvbox)
Provides:       bundled(sublime-theme-onehalf)
Provides:       bundled(sublime-theme-sublime-monokai-extended)
Provides:       bundled(sublime-theme-sublime-snazzy)
Provides:       bundled(sublime-theme-visual-studio-dark-plus)
Provides:       bundled(sublime-theme-zenburn)
}
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Cat(1) clone with wings
%{_bundled_deps}
License:        Apache-2.0 AND BSD-2-Clause AND BSD-2-Clause-Views AND BSD-3-Clause AND CC-BY-SA-3.0 AND LGPL-3.0-or-later AND GPL-2.0-only WITH GCC-exception-2.0 AND MIT AND Unicode-3.0 AND Unicode-DFS-2016 AND Unlicense AND WTFPL AND (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (MIT OR Apache-2.0 OR Zlib) AND (Unlicense OR MIT)
%description -n %{crate}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%{_bundled_deps}
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Cat(1) clone with wings
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+application-devel
Summary:        Cat(1) clone with wings
BuildArch:      noarch
%description -n %{name}+application-devel

This package contains library source intended for building other packages which
use the "application" feature of the "%{crate}" crate.

%package     -n %{name}+bugreport-devel
Summary:        Cat(1) clone with wings
BuildArch:      noarch
%description -n %{name}+bugreport-devel

This package contains library source intended for building other packages which
use the "bugreport" feature of the "%{crate}" crate.

%package     -n %{name}+build-assets-devel
Summary:        Cat(1) clone with wings
BuildArch:      noarch
%description -n %{name}+build-assets-devel

This package contains library source intended for building other packages which
use the "build-assets" feature of the "%{crate}" crate.

%package     -n %{name}+clap-devel
Summary:        Cat(1) clone with wings
BuildArch:      noarch
%description -n %{name}+clap-devel

This package contains library source intended for building other packages which
use the "clap" feature of the "%{crate}" crate.

%package     -n %{name}+etcetera-devel
Summary:        Cat(1) clone with wings
BuildArch:      noarch
%description -n %{name}+etcetera-devel

This package contains library source intended for building other packages which
use the "etcetera" feature of the "%{crate}" crate.

%package     -n %{name}+git-devel
Summary:        Cat(1) clone with wings
BuildArch:      noarch
%description -n %{name}+git-devel

This package contains library source intended for building other packages which
use the "git" feature of the "%{crate}" crate.

%package     -n %{name}+git2-devel
Summary:        Cat(1) clone with wings
BuildArch:      noarch
%description -n %{name}+git2-devel

This package contains library source intended for building other packages which
use the "git2" feature of the "%{crate}" crate.

%package     -n %{name}+grep-cli-devel
Summary:        Cat(1) clone with wings
BuildArch:      noarch
%description -n %{name}+grep-cli-devel

This package contains library source intended for building other packages which
use the "grep-cli" feature of the "%{crate}" crate.

%package     -n %{name}+minimal-application-devel
Summary:        Cat(1) clone with wings
BuildArch:      noarch
%description -n %{name}+minimal-application-devel

This package contains library source intended for building other packages which
use the "minimal-application" feature of the "%{crate}" crate.

%package     -n %{name}+minus-devel
Summary:        Cat(1) clone with wings
BuildArch:      noarch
%description -n %{name}+minus-devel

This package contains library source intended for building other packages which
use the "minus" feature of the "%{crate}" crate.

%package     -n %{name}+paging-devel
Summary:        Cat(1) clone with wings
BuildArch:      noarch
%description -n %{name}+paging-devel

This package contains library source intended for building other packages which
use the "paging" feature of the "%{crate}" crate.

%package     -n %{name}+regex-devel
Summary:        Cat(1) clone with wings
BuildArch:      noarch
%description -n %{name}+regex-devel

This package contains library source intended for building other packages which
use the "regex" feature of the "%{crate}" crate.

%package     -n %{name}+regex-fancy-devel
Summary:        Cat(1) clone with wings
BuildArch:      noarch
%description -n %{name}+regex-fancy-devel

This package contains library source intended for building other packages which
use the "regex-fancy" feature of the "%{crate}" crate.

%package     -n %{name}+regex-onig-devel
Summary:        Cat(1) clone with wings
BuildArch:      noarch
%description -n %{name}+regex-onig-devel

This package contains library source intended for building other packages which
use the "regex-onig" feature of the "%{crate}" crate.

%package     -n %{name}+shell-words-devel
Summary:        Cat(1) clone with wings
BuildArch:      noarch
%description -n %{name}+shell-words-devel

This package contains library source intended for building other packages which
use the "shell-words" feature of the "%{crate}" crate.

%package     -n %{name}+walkdir-devel
Summary:        Cat(1) clone with wings
BuildArch:      noarch
%description -n %{name}+walkdir-devel

This package contains library source intended for building other packages which
use the "walkdir" feature of the "%{crate}" crate.

%package     -n %{name}+wild-devel
Summary:        Cat(1) clone with wings
BuildArch:      noarch
%description -n %{name}+wild-devel

This package contains library source intended for building other packages which
use the "wild" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%install
%cargo_install
install -Dpm0644 target/release/build/%{crate}-*/out/assets/manual/bat.1 \
    -t %{buildroot}%{_mandir}/man1/
install -Dpm0644 target/release/build/%{crate}-*/out/assets/completions/bat.bash \
    %{buildroot}/%{bash_completions_dir}/bat.bash
install -Dpm0644 target/release/build/%{crate}-*/out/assets/completions/bat.fish \
    %{buildroot}/%{fish_completions_dir}/bat.fish
install -Dpm0644 target/release/build/%{crate}-*/out/assets/completions/bat.zsh \
    %{buildroot}/%{zsh_completions_dir}/_bat
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n bat -f %{oreon_filedir}/bat.list
%files -n rust-bat-devel -f %{oreon_filedir}/rust-bat-devel.list

%changelog

%autochangelog
