%global source0_hash b285c51f8a6ade109ed4566d33ac4fb289fb5d6cf87ed70908a5eaf65e948e34
%bcond check 1
%global debug_package %{nil}
%global crate two-face
Name:           rust-two-face
Version:        0.5.1
Release:        1%{?dist}
Summary:        Extra syntax and theme definitions for syntect
License:        (MIT OR Apache-2.0) AND Apache-2.0 AND BSD-2-Clause AND BSD-2-Clause-Views AND BSD-3-Clause AND MIT AND Unlicense AND WTFPL AND LicenseRef-Fedora-UltraPermissive
URL:            https://crates.io/crates/two-face
Source0:        https://static.crates.io/crates/two-face/two-face-%{version}.crate
Patch:          two-face-fix-metadata.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       bundled(crate(bat)) = 0.24.0~git8676bbf
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
Provides:       bundled(sublime-theme-1337-Scheme)
Provides:       bundled(sublime-theme-Coldark)
Provides:       bundled(sublime-theme-Solarized)
Provides:       bundled(sublime-theme-TwoDark)
Provides:       bundled(sublime-theme-dracula-sublime)
Provides:       bundled(sublime-theme-gruvbox)
Provides:       bundled(sublime-theme-onehalf)
Provides:       bundled(sublime-theme-sublime-monokai-extended)
Provides:       bundled(sublime-theme-zenburn)
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Extra syntax and theme definitions for syntect
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+syntect-default-fancy-devel
Summary:        Extra syntax and theme definitions for syntect
BuildArch:      noarch
%description -n %{name}+syntect-default-fancy-devel

This package contains library source intended for building other packages which
use the "syntect-default-fancy" feature of the "%{crate}" crate.

%package     -n %{name}+syntect-default-onig-devel
Summary:        Extra syntax and theme definitions for syntect
BuildArch:      noarch
%description -n %{name}+syntect-default-onig-devel

This package contains library source intended for building other packages which
use the "syntect-default-onig" feature of the "%{crate}" crate.

%package     -n %{name}+syntect-fancy-devel
Summary:        Extra syntax and theme definitions for syntect
BuildArch:      noarch
%description -n %{name}+syntect-fancy-devel

This package contains library source intended for building other packages which
use the "syntect-fancy" feature of the "%{crate}" crate.

%package     -n %{name}+syntect-onig-devel
Summary:        Extra syntax and theme definitions for syntect
BuildArch:      noarch
%description -n %{name}+syntect-onig-devel

This package contains library source intended for building other packages which
use the "syntect-onig" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build
%install
%cargo_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-two-face-devel -f %{oreon_filedir}/rust-two-face-devel.list

%changelog

%autochangelog
