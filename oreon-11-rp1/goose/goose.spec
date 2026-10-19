%global source0_hash 87a61407cc0c10642f927d45708278236dc08ac3706973723dc06bd3df0ea262
%bcond check 1
%global _smp_tasksize_proc 4096
Name:           goose
Version:        1.51.0
Release:        1%{?dist}
Summary:        Extensible AI agent client
URL:            https://github.com/block/goose
Source0:        https://github.com/block/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}-%{version}-vendor.tar.xz
Source2:        chart-js.license
Source3:        d3-js.license
Source4:        d3-sankey.license
Source5:        leaflet.license
Source6:        leaflet-markercluster.license
Source7:        mermaid.license
Patch:          0001-Patch-windows-dependencies-across-workspace.patch
Patch1:         0002-Disable-rustls-and-default-features-for-some-librari.patch
Patch2:         0003-Patch-code-to-use-native-tls-instead-of-rustls.patch
Patch4:         0004-Downstream-only-never-use-pre-generated-object-files.patch
ExcludeArch:    %{ix86}
Conflicts: golang-github-pressly-goose
License:        %{shrink:
                (0BSD OR Apache-2.0 OR MIT)
                AND Apache-2.0
                AND (Apache-2.0 OR Apache-2.0 WITH LLVM-exception OR CC0-1.0)
                AND (Apache-2.0 OR Apache-2.0 WITH LLVM-exception OR MIT)
                AND (Apache-2.0 OR BSD-2-Clause OR MIT)
                AND (Apache-2.0 OR BSD-3-Clause)
                AND (Apache-2.0 OR BSD-3-Clause OR MIT)
                AND (Apache-2.0 OR BSL-1.0)
                AND (Apache-2.0 OR CC0-1.0 OR MIT-0)
                AND (Apache-2.0 OR GPL-2.0-only)
                AND (Apache-2.0 OR LGPL-2.1-or-later OR MIT)
                AND (Apache-2.0 OR MIT)
                AND (Apache-2.0 OR MIT OR Zlib)
                AND BSD-2-Clause
                AND BSD-3-Clause
                AND (BSD-3-Clause OR MIT)
                AND BSL-1.0
                AND CC0-1.0
                AND ISC
                AND LGPL-3.0-or-later
                AND MIT
                AND (MIT OR Unlicense)
                AND MIT-0
                AND MPL-2.0
                AND Unicode-3.0
                AND Zlib
                }
Provides:       bundled(sublime-syntax) = 4075~gitfa6b862
Provides:       bundled(sublime-syntax-ASP)
Provides:       bundled(sublime-syntax-ActionScript)
Provides:       bundled(sublime-syntax-AppleScript)
Provides:       bundled(sublime-syntax-BatchFile)
Provides:       bundled(sublime-syntax-CSharp)
Provides:       bundled(sublime-syntax-Cpp)
Provides:       bundled(sublime-syntax-CSS)
Provides:       bundled(sublime-syntax-Clojure)
Provides:       bundled(sublime-syntax-D)
Provides:       bundled(sublime-syntax-Diff)
Provides:       bundled(sublime-syntax-Erlang)
Provides:       bundled(sublime-syntax-Go)
Provides:       bundled(sublime-syntax-Graphviz)
Provides:       bundled(sublime-syntax-Groovy)
Provides:       bundled(sublime-syntax-HTML)
Provides:       bundled(sublime-syntax-Haskell)
Provides:       bundled(sublime-syntax-Java)
Provides:       bundled(sublime-syntax-JavaScript)
Provides:       bundled(sublime-syntax-LaTeX)
Provides:       bundled(sublime-syntax-Lisp)
Provides:       bundled(sublime-syntax-Lua)
Provides:       bundled(sublime-syntax-Makefile)
Provides:       bundled(sublime-syntax-Markdown)
Provides:       bundled(sublime-syntax-Matlab)
Provides:       bundled(sublime-syntax-OCaml)
Provides:       bundled(sublime-syntax-Object-C)
Provides:       bundled(sublime-syntax-PHP)
Provides:       bundled(sublime-syntax-Pascal)
Provides:       bundled(sublime-syntax-Perl)
Provides:       bundled(sublime-syntax-Python)
Provides:       bundled(sublime-syntax-R)
Provides:       bundled(sublime-syntax-Rails)
Provides:       bundled(sublime-syntax-Regular-Expressions)
Provides:       bundled(sublime-syntax-RestructuredText)
Provides:       bundled(sublime-syntax-Ruby)
Provides:       bundled(sublime-syntax-Rust)
Provides:       bundled(sublime-syntax-SQL)
Provides:       bundled(sublime-syntax-Scala)
Provides:       bundled(sublime-syntax-ShellScript)
Provides:       bundled(sublime-syntax-TCL)
Provides:       bundled(sublime-syntax-Textile)
Provides:       bundled(sublime-syntax-XML)
Provides:       bundled(sublime-syntax-YAML)
Provides:       bundled(syntect-theme-InspiredGithub)
Provides:       bundled(syntect-theme-Solarized)
Provides:       bundled(sublime-theme-Spacegray)
Provides:       bundled(chart-min-js) = 4.5.0
Provides:       bundled(d3-min-js) = 7.9.0
Provides:       bundled(d3-sankey-min-js) = 0.12.3
Provides:       bundled(leaflet-min-js) = 1.9.4
Provides:       bundled(leaflet-min-css) = 1.9.4
Provides:       bundled(leaflet-markercluster-min-js) = 1.5.3
Provides:       bundled(mermaid-min-js)
# oreon:deps
BuildRequires:  /usr/bin/perl
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  clang-devel
BuildRequires:  dbus-devel
BuildRequires:  libgit2-devel
BuildRequires:  libxcb-devel
BuildRequires:  libzstd-devel
BuildRequires:  oniguruma-devel
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  rustc
BuildRequires:  tomcli
# /oreon:deps
%description
Goose is your on-machine AI agent, capable of automating complex development
tasks from start to finish. More than just code suggestions, goose can build
entire projects from scratch, write and execute code, debug failures,
orchestrate workflows, and interact with external APIs - autonomously.

Whether you're prototyping an idea, refining existing code, or managing
intricate engineering pipelines, goose adapts to your workflow and executes
tasks with precision.

Designed for maximum flexibility, goose works with any LLM and supports
multi-model configuration to optimize performance and cost, seamlessly
integrates with MCP servers, and is available as both a desktop app as well as
CLI - making it the ultimate AI assistant for developers who want to move
faster and focus on innovation.

%prep
%autosetup -p1 -a1
cp -pav %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6} %{SOURCE7} .
find documentation \
-depth \( -type f ! -path "documentation/static/img/logo_dark.png" ! -path "documentation/static/img/logo_light.png" -delete \) \
-o \( -type d -empty -delete \)
rm -rf ui
rm -rf bin
rm -rf services
rm crates/goose-cli/src/scenario_tests/test_data/test_image.jpg
prune_vendor() {
local crate_pattern="$1"
local path_to_remove="$2"
rm -rf ${crate_pattern}/${path_to_remove}
find . -path "*/${crate_pattern}/.cargo-checksum.json" \
-exec sed -i.uncheck -e 's/"files":{[^}]*}/"files":{ }/' '{}' '+'
}
pushd vendor
prune_vendor "bzip2-sys-*" "bzip-*"
prune_vendor "libdbus-sys-*" "vendor"
prune_vendor "libsqlite3-sys-*" "{sqlite3,sqlcipher}"
prune_vendor "onig_sys-*" "oniguruma"
prune_vendor "ring-*" "pregenerated"
find . -maxdepth 1 -path "*/zstd-*" \
-exec tomcli set "{}/Cargo.toml" append features.default pkg-config \; \
-exec sed -i.uncheck -e 's/"files":{[^}]*}/"files":{ }/' "{}/.cargo-checksum.json" \;
prune_vendor "zstd-sys-*" "zstd"
find . -maxdepth 1 -path "*/posthog-rs-*" \
-exec tomcli set "{}/Cargo.toml" str dependencies.reqwest.version "0.12.28" \; \
-exec tomcli set "{}/Cargo.toml" arrays delitem dependencies.reqwest.features "rustls-tls" \; \
-exec tomcli set "{}/Cargo.toml" append dependencies.reqwest.features "native-tls" \; \
-exec sed -i.uncheck -e 's/"files":{[^}]*}/"files":{ }/' "{}/.cargo-checksum.json" \;
popd
find -name '*.rs' -type f -perm /111 -exec chmod -v -x '{}' '+'
%oreon_vendor_cargo
%build

export RUSTONIG_SYSTEM_LIBONIG=1
%cargo_build
%cargo_vendor_manifest
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%install
install -Dpm 0755 target/rpm/goose -t %{buildroot}%{_bindir}
install -Dpm 0755 target/rpm/goosed -t %{buildroot}%{_bindir}
%oreon_autofiles main
%if %{with check}
%check

export RUSTONIG_SYSTEM_LIBONIG=1
skip="${skip-} --skip providers::gcpauth::tests::test_token_refresh_race_condition"
skip="${skip-} --skip routes::audio::tests::test_transcribe_endpoint_requires_auth"
skip="${skip-} --skip tunnel::lapstone_test::test_tunnel_end_to_end"
skip="${skip-} --skip tunnel::lapstone_test::test_tunnel_post_request"
skip="${skip-} --skip scenario_tests::scenarios::tests::test_image_analysis"
%cargo_test -- -- ${skip-}
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
