%global source200_hash e04167ff997aa3b646e5818e620943d577c4410fd55e364b3cd8c662388a9f7d
%global source0_hash 2d0cf264ac77f8c25386a636e2b3a09a23dec555568cc9a5b2927f84322f544e
%bcond check 0
%global binary_name hx
%global runtime_directory_path %{_libdir}/helix/runtime
Name:           helix
Version:        25.07.1
Release:        1%{?dist}
License:        %{shrink:
                (Apache-2.0 OR MIT) AND
                BSD-3-Clause AND
                Unicode-DFS-2016 AND
                Apache-2.0 AND
                (Apache-2.0 OR BSL-1.0) AND
                (Apache-2.0 OR MIT) AND
                (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
                ISC AND
                MIT AND
                (MIT OR Apache-2.0 OR Zlib) AND
                (CC0-1.0 OR MIT-0 OR Apache-2.0) AND
                MPL-2.0 AND
                MPL-2.0+ AND
                Unicode-3.0 AND
                (Unlicense OR MIT) AND
                Zlib AND
                Unlicense
                }
Summary:        A post-modern modal text editor written in Rust
URL:            https://helix-editor.com/
Source0:        https://github.com/helix-editor/%{name}/releases/download/%{version}/%{name}-%{version}-source.tar.xz
Source200:      https://raw.githubusercontent.com/blinxen/tree-sitter-eex/main/LICENSE#/LICENSE-tree-sitter-eex
Patch:          remove-windows-dependency.patch
Patch:          pr-14673.patch
ExcludeArch: %{ix86}
Requires:       git-core
Requires:       gcc-c++
Recommends:     xsel
Recommends:     wl-clipboard
Provides:       bundled(tree-sitter-sql)
Provides:       bundled(tree-sitter-v)
Provides:       bundled(tree-sitter-pkl)
Provides:       bundled(tree-sitter-elm)
Provides:       bundled(tree-sitter-gren)
Provides:       bundled(tree-sitter-lua)
Provides:       bundled(tree-sitter-latex)
Provides:       bundled(tree-sitter-luau)
Provides:       bundled(tree-sitter-tlaplus)
Provides:       bundled(tree-sitter-ada)
Provides:       bundled(tree-sitter-adl)
Provides:       bundled(tree-sitter-agda)
Provides:       bundled(tree-sitter-alloy)
Provides:       bundled(tree-sitter-amber)
Provides:       bundled(tree-sitter-astro)
Provides:       bundled(tree-sitter-awk)
Provides:       bundled(tree-sitter-bash)
Provides:       bundled(tree-sitter-bass)
Provides:       bundled(tree-sitter-beancount)
Provides:       bundled(tree-sitter-bibtex)
Provides:       bundled(tree-sitter-bicep)
Provides:       bundled(tree-sitter-bitbake)
Provides:       bundled(tree-sitter-blade)
Provides:       bundled(tree-sitter-blueprint)
Provides:       bundled(tree-sitter-c)
Provides:       bundled(tree-sitter-caddyfile)
Provides:       bundled(tree-sitter-cairo)
Provides:       bundled(tree-sitter-capnp)
Provides:       bundled(tree-sitter-cassette)
Provides:       bundled(tree-sitter-cel)
Provides:       bundled(tree-sitter-circom)
Provides:       bundled(tree-sitter-clarity)
Provides:       bundled(tree-sitter-clojure)
Provides:       bundled(tree-sitter-cmake)
Provides:       bundled(tree-sitter-comment)
Provides:       bundled(tree-sitter-cpon)
Provides:       bundled(tree-sitter-cpp)
Provides:       bundled(tree-sitter-crystal)
Provides:       bundled(tree-sitter-c-sharp)
Provides:       bundled(tree-sitter-css)
Provides:       bundled(tree-sitter-cue)
Provides:       bundled(tree-sitter-cylc)
Provides:       bundled(tree-sitter-d)
Provides:       bundled(tree-sitter-dart)
Provides:       bundled(tree-sitter-dbml)
Provides:       bundled(tree-sitter-debian)
Provides:       bundled(tree-sitter-devicetree)
Provides:       bundled(tree-sitter-dhall)
Provides:       bundled(tree-sitter-diff)
Provides:       bundled(tree-sitter-djot)
Provides:       bundled(tree-sitter-dockerfile)
Provides:       bundled(tree-sitter-dot)
Provides:       bundled(tree-sitter-dtd)
Provides:       bundled(tree-sitter-dunstrc)
Provides:       bundled(tree-sitter-earthfile)
Provides:       bundled(tree-sitter-edoc)
Provides:       bundled(tree-sitter-eex)
Provides:       bundled(tree-sitter-elisp)
Provides:       bundled(tree-sitter-elixir)
Provides:       bundled(tree-sitter-elvish)
Provides:       bundled(tree-sitter-embedded-template)
Provides:       bundled(tree-sitter-erlang)
Provides:       bundled(tree-sitter-esdl)
Provides:       bundled(tree-sitter-fennel)
Provides:       bundled(tree-sitter-fga)
Provides:       bundled(tree-sitter-fidl)
Provides:       bundled(tree-sitter-fish)
Provides:       bundled(tree-sitter-forth)
Provides:       bundled(tree-sitter-fortran)
Provides:       bundled(tree-sitter-fsharp)
Provides:       bundled(tree-sitter-gas)
Provides:       bundled(tree-sitter-gdscript)
Provides:       bundled(tree-sitter-gherkin)
Provides:       bundled(tree-sitter-ghostty)
Provides:       bundled(tree-sitter-gitattributes)
Provides:       bundled(tree-sitter-gitcommit)
Provides:       bundled(tree-sitter-git-config)
Provides:       bundled(tree-sitter-gitignore)
Provides:       bundled(tree-sitter-gleam)
Provides:       bundled(tree-sitter-glimmer)
Provides:       bundled(tree-sitter-glsl)
Provides:       bundled(tree-sitter-gn)
Provides:       bundled(tree-sitter-go)
Provides:       bundled(tree-sitter-godot-resource)
Provides:       bundled(tree-sitter-gomod)
Provides:       bundled(tree-sitter-go-template)
Provides:       bundled(tree-sitter-go-work)
Provides:       bundled(tree-sitter-gpr)
Provides:       bundled(tree-sitter-markdown)
Provides:       bundled(tree-sitter-zig)
Provides:       bundled(tree-sitter-graphql)
Provides:       bundled(tree-sitter-groovy)
Provides:       bundled(tree-sitter-hare)
Provides:       bundled(tree-sitter-haskell)
Provides:       bundled(tree-sitter-haskell-persistent)
Provides:       bundled(tree-sitter-hcl)
Provides:       bundled(tree-sitter-heex)
Provides:       bundled(tree-sitter-hocon)
Provides:       bundled(tree-sitter-hoon)
Provides:       bundled(tree-sitter-hosts)
Provides:       bundled(tree-sitter-html)
Provides:       bundled(tree-sitter-htmldjango)
Provides:       bundled(tree-sitter-hurl)
Provides:       bundled(tree-sitter-hyprlang)
Provides:       bundled(tree-sitter-iex)
Provides:       bundled(tree-sitter-ini)
Provides:       bundled(tree-sitter-ink)
Provides:       bundled(tree-sitter-inko)
Provides:       bundled(tree-sitter-janet-simple)
Provides:       bundled(tree-sitter-java)
Provides:       bundled(tree-sitter-javascript)
Provides:       bundled(tree-sitter-jinja2)
Provides:       bundled(tree-sitter-jjdescription)
Provides:       bundled(tree-sitter-jq)
Provides:       bundled(tree-sitter-jsdoc)
Provides:       bundled(tree-sitter-json)
Provides:       bundled(tree-sitter-json5)
Provides:       bundled(tree-sitter-jsonnet)
Provides:       bundled(tree-sitter-julia)
Provides:       bundled(tree-sitter-just)
Provides:       bundled(tree-sitter-kdl)
Provides:       bundled(tree-sitter-koka)
Provides:       bundled(tree-sitter-kotlin)
Provides:       bundled(tree-sitter-koto)
Provides:       bundled(tree-sitter-ld)
Provides:       bundled(tree-sitter-ldif)
Provides:       bundled(tree-sitter-lean)
Provides:       bundled(tree-sitter-ledger)
Provides:       bundled(tree-sitter-llvm)
Provides:       bundled(tree-sitter-llvm-mir)
Provides:       bundled(tree-sitter-log)
Provides:       bundled(tree-sitter-lpf)
Provides:       bundled(tree-sitter-mail)
Provides:       bundled(tree-sitter-make)
Provides:       bundled(tree-sitter-markdoc)
Provides:       bundled(tree-sitter-matlab)
Provides:       bundled(tree-sitter-mermaid)
Provides:       bundled(tree-sitter-meson)
Provides:       bundled(tree-sitter-mojo)
Provides:       bundled(tree-sitter-move)
Provides:       bundled(tree-sitter-nasm)
Provides:       bundled(tree-sitter-nginx)
Provides:       bundled(tree-sitter-nickel)
Provides:       bundled(tree-sitter-nim)
Provides:       bundled(tree-sitter-nix)
Provides:       bundled(tree-sitter-nu)
Provides:       bundled(tree-sitter-ocaml)
Provides:       bundled(tree-sitter-odin)
Provides:       bundled(tree-sitter-ohm)
Provides:       bundled(tree-sitter-opencl)
Provides:       bundled(tree-sitter-openscad)
Provides:       bundled(tree-sitter-org)
Provides:       bundled(tree-sitter-pascal)
Provides:       bundled(tree-sitter-passwd)
Provides:       bundled(tree-sitter-pem)
Provides:       bundled(tree-sitter-perl)
Provides:       bundled(tree-sitter-pest)
Provides:       bundled(tree-sitter-php)
Provides:       bundled(tree-sitter-po)
Provides:       bundled(tree-sitter-pod)
Provides:       bundled(tree-sitter-ponylang)
Provides:       bundled(tree-sitter-powershell)
Provides:       bundled(tree-sitter-prisma)
Provides:       bundled(tree-sitter-prolog)
Provides:       bundled(tree-sitter-properties)
Provides:       bundled(tree-sitter-proto)
Provides:       bundled(tree-sitter-prql)
Provides:       bundled(tree-sitter-pug)
Provides:       bundled(tree-sitter-python)
Provides:       bundled(tree-sitter-ql)
Provides:       bundled(tree-sitter-qmljs)
Provides:       bundled(tree-sitter-query)
Provides:       bundled(tree-sitter-quint)
Provides:       bundled(tree-sitter-r)
Provides:       bundled(tree-sitter-rainbow-csv)
Provides:       bundled(tree-sitter-rebase)
Provides:       bundled(tree-sitter-regex)
Provides:       bundled(tree-sitter-rego)
Provides:       bundled(tree-sitter-rescript)
Provides:       bundled(tree-sitter-robot)
Provides:       bundled(tree-sitter-ron)
Provides:       bundled(tree-sitter-rst)
Provides:       bundled(tree-sitter-ruby)
Provides:       bundled(tree-sitter-rust)
Provides:       bundled(tree-sitter-rust-format-args)
Provides:       bundled(tree-sitter-scala)
Provides:       bundled(tree-sitter-scheme)
Provides:       bundled(tree-sitter-scss)
Provides:       bundled(tree-sitter-slang)
Provides:       bundled(tree-sitter-slint)
Provides:       bundled(tree-sitter-smali)
Provides:       bundled(tree-sitter-smithy)
Provides:       bundled(tree-sitter-sml)
Provides:       bundled(tree-sitter-snakemake)
Provides:       bundled(tree-sitter-solidity)
Provides:       bundled(tree-sitter-sourcepawn)
Provides:       bundled(tree-sitter-spade)
Provides:       bundled(tree-sitter-spicedb)
Provides:       bundled(tree-sitter-ssh-client-config)
Provides:       bundled(tree-sitter-strace)
Provides:       bundled(tree-sitter-supercollider)
Provides:       bundled(tree-sitter-svelte)
Provides:       bundled(tree-sitter-sway)
Provides:       bundled(tree-sitter-swift)
Provides:       bundled(tree-sitter-t32)
Provides:       bundled(tree-sitter-tablegen)
Provides:       bundled(tree-sitter-tact)
Provides:       bundled(tree-sitter-task)
Provides:       bundled(tree-sitter-tcl)
Provides:       bundled(tree-sitter-teal)
Provides:       bundled(tree-sitter-templ)
Provides:       bundled(tree-sitter-tera)
Provides:       bundled(tree-sitter-test)
Provides:       bundled(tree-sitter-textproto)
Provides:       bundled(tree-sitter-thrift)
Provides:       bundled(tree-sitter-todotxt)
Provides:       bundled(tree-sitter-toml)
Provides:       bundled(tree-sitter-twig)
Provides:       bundled(tree-sitter-typescript)
Provides:       bundled(tree-sitter-typespec)
Provides:       bundled(tree-sitter-ungrammar)
Provides:       bundled(tree-sitter-unison)
Provides:       bundled(tree-sitter-uxntal)
Provides:       bundled(tree-sitter-vala)
Provides:       bundled(tree-sitter-vento)
Provides:       bundled(tree-sitter-verilog)
Provides:       bundled(tree-sitter-vhdl)
Provides:       bundled(tree-sitter-vue)
Provides:       bundled(tree-sitter-wasm)
Provides:       bundled(tree-sitter-werk-2)
Provides:       bundled(tree-sitter-wesl)
Provides:       bundled(tree-sitter-wgsl)
Provides:       bundled(tree-sitter-wit)
Provides:       bundled(tree-sitter-xit)
Provides:       bundled(tree-sitter-xml)
Provides:       bundled(tree-sitter-XTC)
Provides:       bundled(tree-sitter-yaml)
Provides:       bundled(tree-sitter-yara)
Provides:       bundled(tree-sitter-yuck)
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  libappstream-glib
BuildRequires:  rustc
BuildRequires:  tomcli
# /oreon:deps
%description
A Kakoune / Neovim inspired editor, written in Rust.

%prep
%autosetup -c -p1
tomcli set helix-vcs/Cargo.toml str dependencies.gix.version 0.75
tomcli set helix-core/Cargo.toml str dependencies.unicode-width 0.1.14
tomcli set helix-stdx/Cargo.toml str dependencies.etcetera '>=0.10.0, <0.12.0'
tomcli set helix-loader/Cargo.toml str dependencies.etcetera '>=0.10.0, <0.12.0'
find runtime/themes/licenses -type f -exec /bin/sh -c 'cp -pav {} LICENSE-themes-$(basename {} .LICENSE)' \;
cp -pav %{SOURCE200} .
find runtime/grammars -name "LICENSE*" -type f -not -path '*/docs/*' -exec /bin/sh -c 'cp -pav {} LICENSE-tree-sitter-$(basename $(dirname {}))' \;
find runtime/grammars -name "LICENCE*" -type f -not -path '*/docs/*' -exec /bin/sh -c 'cp -pav {} LICENSE-tree-sitter-$(basename $(dirname {}))' \;
find runtime/grammars -name "COPYING*" -type f -not -path '*/docs/*' -exec /bin/sh -c 'cp -pav {} LICENSE-tree-sitter-$(basename $(dirname {}))' \;
chmod -x LICENSE-*
%oreon_vendor_cargo
%build

export HELIX_DEFAULT_RUNTIME=%{runtime_directory_path}
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%install
install -Dpm 0755 target/release/%{binary_name} %{buildroot}%{_bindir}/%{binary_name}
sed -i \
    -e "s|Exec=hx %%F|Exec=%{_bindir}/%{binary_name} %%F|g" \
    -e "s|TryExec=hx|TryExec=%{_bindir}/%{binary_name}|g" contrib/Helix.desktop
desktop-file-install --dir=%{buildroot}%{_datadir}/applications contrib/Helix.desktop
install -Dpm 0644 contrib/helix.png %{buildroot}%{_datadir}/pixmaps/helix.png
install -Dpm 0644 contrib/Helix.appdata.xml %{buildroot}%{_metainfodir}/Helix.appdata.xml
install -dm 0755 %{buildroot}%{runtime_directory_path}/
install -dm 0755 %{buildroot}%{runtime_directory_path}/grammars
install -dm 0755 %{buildroot}%{runtime_directory_path}/queries
find runtime/queries/ -type d -exec sh -c 'install -dm 0755 $(basename {}) %{buildroot}%{runtime_directory_path}/queries/$(basename {})' \;
install -dm 0755 %{buildroot}%{runtime_directory_path}/themes
install -Dpm 0644 runtime/tutor %{buildroot}%{runtime_directory_path}/tutor
install -Dpm 0755 runtime/grammars/*.so -t %{buildroot}%{runtime_directory_path}/grammars
find runtime/queries/ -type f -exec sh -c 'install -Dpm 0644 {} %{buildroot}%{runtime_directory_path}/queries/$(basename $(dirname {}))' \;
install -Dpm 0644 runtime/themes/*.toml -t %{buildroot}%{runtime_directory_path}/themes
install -Dpm 0644 contrib/completion/%{binary_name}.bash %{buildroot}/%{bash_completions_dir}/%{binary_name}
install -Dpm 0644 contrib/completion/%{binary_name}.fish %{buildroot}/%{fish_completions_dir}/%{binary_name}.fish
install -Dpm 0644 contrib/completion/%{binary_name}.zsh %{buildroot}/%{zsh_completions_dir}/_%{binary_name}
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/Helix.desktop
%if %{with check}
export HELIX_DISABLE_AUTO_GRAMMAR_BUILD=true
%cargo_test
%{buildroot}%{_bindir}/%{binary_name} --health
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
