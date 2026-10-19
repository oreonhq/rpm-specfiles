%global source0_hash 84d2ff8bb979bb85de0fd27bc3e746361eab63e560fac97c826054d94077318c
%global         vimfiles        %{_datadir}/vim/vimfiles
%global         upstream_name   syntastic
%global         appdata_dir %{_datadir}/appdata
%global         python python3
Name:           vim-%{upstream_name}
Version:        3.10.0
Release:        29%{?dist}
Summary:        A vim plugins to check syntax for programming languages
Summary(fr):    Une extension de vim vérifiant la syntaxe pour les langages de programmation
License:        WTFPL
URL:            https://github.com/scrooloose/syntastic
Source0:        https://github.com/scrooloose/%{upstream_name}/archive/%{version}/%{upstream_name}-%{version}.tar.gz
Source1:        vim-syntastic.metainfo.xml
Patch0:         vim-syntastic-3.9.0-python3-shebang.patch
Patch1:         vim-syntastic-3.10.0-5-rvim.patch
Patch2:         vim-syntastic-3.10.0-yamllint-default.patch
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch
Requires:       vim
Provides:       %upstream_name = %version-%release
Obsoletes:      %upstream_name < 3.7.0-6
Obsoletes:      %name-d < %version-%release
Obsoletes:      %name-lisp < %version-%release
Obsoletes:      %name-rnc < %version-%release
Obsoletes:      %name-go < %version-%release
Obsoletes:      %name-coffee < %version-%release
Obsoletes:      %name-scala < %version-%release
# oreon:deps
BuildRequires:  glibc-common
BuildRequires:  libappstream-glib
# /oreon:deps
%description
Syntastic is a syntax checking plugin that runs files through external syntax
checkers and displays any resulting errors to the user. This can be done on
demand, or automatically as files are saved. If syntax errors are detected, the
user is notified and is happy because they didn't have to compile their code or
execute their script to find them.

%description -l fr
Syntastic est une extension vérifiant la syntaxe des fichiers source, un outil
externe de vérification affiche toutes les erreurs trouvées à l'utilisateur.
Ceci peut être fait à la demande ou automatique au moment de la sauvegarde
du fichier. Si une erreur de syntaxe est détecté, les utilisateurs sont
informés et sont heureux de ne pas avoir compiler leur code ou d'avoir
exécuter leur script afin de les trouver.

%define add_subpackage(n:)                                                          \
%package %{-n*}                                                                     \
Summary:        A syntax checker for %{-n*} programming language                    \
Summary(fr):    Un vérificateur de syntaxe pour le langage de programmation %{-n*}  \
Requires:       %{name} =  %{version}-%{release}                                    \
Requires:       %*                                                                  \
Provides:       %upstream_name-%{-n*} = %version-%release                           \
Obsoletes:      %upstream_name-%{-n*} < 3.7.0-6                                     \
%{expand:%%{?%{-n*}_avail_arches:ExclusiveArch: %%%{-n*}_avail_arches}}             \
%description %{-n*}                                                                 \
Allows checking %{-n*} sources files.                                               \
%description -l fr %{-n*}                                                           \
Permet de vérifier les fichiers sources écrit en %{-n*}.                            \
%global files_to_do %{?files_to_do}                                               \\\
%files_for_lang %{-n*}                                                            \\\
%{expand:%%{?additional_files_for_lang_%{-n*}}}

# Initialize files_to_do macro here to empty string.  FedoraReview tool, for
# example, runs 'rpm.TransactionSet().parseSpec("syntastic.spec")' _twice_,
# while global macros survive from the first call (we don't want to have all
# %%files sections generated twice).
%global files_to_do %nil
%add_subpackage -n ada gcc-gnat
%add_subpackage -n ansible ansible-lint
%add_subpackage -n asciidoc asciidoc %name-text
%add_subpackage -n asl acpica-tools
%add_subpackage -n asm nasm
%global additional_files_for_lang_c \
%{vimfiles}/autoload/syntastic/c.vim
%add_subpackage -n c gcc
%add_subpackage -n cabal cabal-install
# cofee-script has been retired
#%%add_subpackage -n coffee coffee-script
%add_subpackage -n coq coq
%add_subpackage -n cpp gcc-c++ vim-syntastic-c
%add_subpackage -n cs mono-core
%add_subpackage -n css csslint
%add_subpackage -n cucumber rubygem-cucumber
#https://pagure.io/packaging-committee/issue/312
#%%add_subpackage -n d ldc
%add_subpackage -n docbk /usr/bin/xmllint
%add_subpackage -n elixir elixir
%add_subpackage -n erlang erlang-erts
%add_subpackage -n eruby ruby
%add_subpackage -n fortran gcc-gfortran
%add_subpackage -n glsl mesa-libGLU
%add_subpackage -n go golang-bin
%add_subpackage -n haml rubygem-haml
%add_subpackage -n help proselint
%add_subpackage -n haskell ghc
%add_subpackage -n html sed curl tidy
%add_subpackage -n java java-devel
%add_subpackage -n json %{python}-demjson
%add_subpackage -n julia julia
%add_subpackage -n less nodejs
%add_subpackage -n lex flex
#https://pagure.io/packaging-committee/issue/312
#%%add_subpackage -n lisp clisp
%add_subpackage -n llvm llvm
%add_subpackage -n lua lua
%add_subpackage -n matlab octave
%add_subpackage -n nasm nasm
%add_subpackage -n objc gcc-objc
%add_subpackage -n objcpp gcc-objc++
%add_subpackage -n ocaml ocaml
%add_subpackage -n perl perl-interpreter %name-pod
%add_subpackage -n perl6 rakudo
%add_subpackage -n php php
%add_subpackage -n po gettext
%add_subpackage -n pod perl-interpreter
%add_subpackage -n puppet puppet
%add_subpackage -n python pylint /usr/bin/pyflakes
%add_subpackage -n qml /usr/bin/qmllint
#rnv has been retired
#%%add_subpackage -n rnc rnv
%add_subpackage -n rst %{python}-docutils %name-text %name-xml %name-docbk
%add_subpackage -n ruby ruby
%add_subpackage -n sass rubygem-sass
#Scala has been removed as of F42
#%%add_subpackage -n scala scala
%add_subpackage -n scss rubygem-sass
%add_subpackage -n sh bash
%add_subpackage -n spec rpmlint
%add_subpackage -n tcl tcl
%add_subpackage -n tex texlive-latex
%add_subpackage -n texinfo texinfo
%add_subpackage -n text proselint
%add_subpackage -n trig raptor2
%add_subpackage -n turtle raptor2
%add_subpackage -n vala vala
%add_subpackage -n verilog iverilog
%add_subpackage -n vim vim
%add_subpackage -n xhtml tidy
%add_subpackage -n xml /usr/bin/xmllint
%add_subpackage -n xslt /usr/bin/xmllint
%add_subpackage -n yacc byacc
%add_subpackage -n yaml yamllint perl-YAML-LibYAML
%add_subpackage -n yara yara
%add_subpackage -n z80 z80asm
%add_subpackage -n zsh zsh

# Intentional %%define here, intentionally after %%add_subpackage usage.
%define files_for_lang() \
%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %upstream_name-%version -p1
# Use a free D compiler ldc
sed -i "s/dmd/ldc2/g" syntax_checkers/d/dmd.vim
# Use executable script from bindir
sed -i "s|expand\(.*sfile.*\).*|'%{_bindir}/erlang_check_file.erl'|" syntax_checkers/erlang/escript.vim

# Don't use /bin/env like shebangs.
grep -lr '#!.*/bin/env'  | while read file; do
    sed -i '1 s|#!.*/bin/env \(.*\)|#!/usr/bin/\1|' "$file"
done

rm -r syntax_checkers/actionscript
rm -r syntax_checkers/applescript
rm -r syntax_checkers/apiblueprint
rm -r syntax_checkers/bemhtml
rm -r syntax_checkers/bro
rm -r syntax_checkers/chef
# no cmakelint available in fedora
rm -r syntax_checkers/cmake
rm -r syntax_checkers/co
rm -r syntax_checkers/cobol
# coffee-script has been removed from fedora as of f39
rm -r syntax_checkers/coffee
rm -r syntax_checkers/cuda
# https://pagure.io/packaging-committee/issue/312
rm -r syntax_checkers/d
rm -r syntax_checkers/dart
# dockerfile-lint doesn't seem to be in Fedora yet:
# mock -r fedora-rawhide-x86_64 --install '/*/dockerfile*lint'
rm -r syntax_checkers/dockerfile
rm -r syntax_checkers/dustjs
rm -r syntax_checkers/handlebars
rm -r syntax_checkers/haxe
rm -r syntax_checkers/hss
rm -r syntax_checkers/jade
# rhbz#1912817
rm -r syntax_checkers/javascript
rm -r syntax_checkers/limbo
# https://pagure.io/packaging-committee/issue/312
rm -r syntax_checkers/lisp
rm -r syntax_checkers/markdown
rm -r syntax_checkers/mercury
rm -r syntax_checkers/nix
rm -r syntax_checkers/nroff
# mock -r fedora-rawhide-x86_64 --install '/*/pug*lint'
rm -r syntax_checkers/pug
rm -r syntax_checkers/r
rm -r syntax_checkers/racket
# mock -r fedora-rawhide-x86_64 --install '/*/lintr'
rm -r syntax_checkers/rmd
rm -r syntax_checkers/rnc
# rhbz#2311476
rm -r syntax_checkers/scala
rm -r syntax_checkers/slim
rm -r syntax_checkers/sml
# mock -r fedora-rawhide-x86_64 --install '/*/solc'
rm -r syntax_checkers/solidity
rm -r syntax_checkers/sql
rm -r syntax_checkers/stylus
# removed since nobody needs that, patches welcome!
rm -r syntax_checkers/svg
# Doesn't install binary:
# mock -r fedora-rawhide-x86_64 --install '/*/ttl'
rm -r syntax_checkers/turtle/ttl.vim
rm -r syntax_checkers/twig
rm -r syntax_checkers/typescript
# https://bugzilla.redhat.com/show_bug.cgi?id=1832470
rm -r syntax_checkers/vhdl
# dunno what to do with this
rm -r syntax_checkers/vue
# mock -r fedora-rawhide-x86_64 --install '/*/basex'
rm -r syntax_checkers/xquery
# mock -r fedora-rawhide-x86_64 --install '/*/pyang'
rm -r syntax_checkers/yang
rm -r syntax_checkers/zpt

%build

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{vimfiles}/autoload
cp      -rp       autoload/*                            %{buildroot}%{vimfiles}/autoload/
install -Dpm0644  doc/syntastic.txt                     %{buildroot}%{vimfiles}/doc/syntastic.txt
cp      -rp       plugin/                               %{buildroot}%{vimfiles}/plugin
cp      -rp       syntax_checkers/                      %{buildroot}%{vimfiles}/syntax_checkers
install -Dpm0644 %{SOURCE1} %{buildroot}%{appdata_dir}/vim-syntastic.metainfo.xml
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

appstream-util validate-relax --nonet %{buildroot}%{appdata_dir}/vim-syntastic.metainfo.xml
%files -f %{oreon_filedir}/main.list
%files -n vim-syntastic-ada -f %{oreon_filedir}/vim-syntastic-ada.list
%files -n vim-syntastic-ansible -f %{oreon_filedir}/vim-syntastic-ansible.list
%files -n vim-syntastic-asciidoc -f %{oreon_filedir}/vim-syntastic-asciidoc.list
%files -n vim-syntastic-asl -f %{oreon_filedir}/vim-syntastic-asl.list
%files -n vim-syntastic-asm -f %{oreon_filedir}/vim-syntastic-asm.list
%files -n vim-syntastic-c -f %{oreon_filedir}/vim-syntastic-c.list
%files -n vim-syntastic-cabal -f %{oreon_filedir}/vim-syntastic-cabal.list
%files -n vim-syntastic-coq -f %{oreon_filedir}/vim-syntastic-coq.list
%files -n vim-syntastic-cpp -f %{oreon_filedir}/vim-syntastic-cpp.list
%files -n vim-syntastic-cs -f %{oreon_filedir}/vim-syntastic-cs.list
%files -n vim-syntastic-css -f %{oreon_filedir}/vim-syntastic-css.list
%files -n vim-syntastic-cucumber -f %{oreon_filedir}/vim-syntastic-cucumber.list
%files -n vim-syntastic-docbk -f %{oreon_filedir}/vim-syntastic-docbk.list
%files -n vim-syntastic-elixir -f %{oreon_filedir}/vim-syntastic-elixir.list
%files -n vim-syntastic-erlang -f %{oreon_filedir}/vim-syntastic-erlang.list
%files -n vim-syntastic-eruby -f %{oreon_filedir}/vim-syntastic-eruby.list
%files -n vim-syntastic-fortran -f %{oreon_filedir}/vim-syntastic-fortran.list
%files -n vim-syntastic-glsl -f %{oreon_filedir}/vim-syntastic-glsl.list
%files -n vim-syntastic-go -f %{oreon_filedir}/vim-syntastic-go.list
%files -n vim-syntastic-haml -f %{oreon_filedir}/vim-syntastic-haml.list
%files -n vim-syntastic-help -f %{oreon_filedir}/vim-syntastic-help.list
%files -n vim-syntastic-haskell -f %{oreon_filedir}/vim-syntastic-haskell.list
%files -n vim-syntastic-html -f %{oreon_filedir}/vim-syntastic-html.list
%files -n vim-syntastic-java -f %{oreon_filedir}/vim-syntastic-java.list
%files -n vim-syntastic-json -f %{oreon_filedir}/vim-syntastic-json.list
%files -n vim-syntastic-julia -f %{oreon_filedir}/vim-syntastic-julia.list
%files -n vim-syntastic-less -f %{oreon_filedir}/vim-syntastic-less.list
%files -n vim-syntastic-lex -f %{oreon_filedir}/vim-syntastic-lex.list
%files -n vim-syntastic-llvm -f %{oreon_filedir}/vim-syntastic-llvm.list
%files -n vim-syntastic-lua -f %{oreon_filedir}/vim-syntastic-lua.list
%files -n vim-syntastic-matlab -f %{oreon_filedir}/vim-syntastic-matlab.list
%files -n vim-syntastic-nasm -f %{oreon_filedir}/vim-syntastic-nasm.list
%files -n vim-syntastic-objc -f %{oreon_filedir}/vim-syntastic-objc.list
%files -n vim-syntastic-objcpp -f %{oreon_filedir}/vim-syntastic-objcpp.list
%files -n vim-syntastic-ocaml -f %{oreon_filedir}/vim-syntastic-ocaml.list
%files -n vim-syntastic-perl -f %{oreon_filedir}/vim-syntastic-perl.list
%files -n vim-syntastic-perl6 -f %{oreon_filedir}/vim-syntastic-perl6.list
%files -n vim-syntastic-php -f %{oreon_filedir}/vim-syntastic-php.list
%files -n vim-syntastic-po -f %{oreon_filedir}/vim-syntastic-po.list
%files -n vim-syntastic-pod -f %{oreon_filedir}/vim-syntastic-pod.list
%files -n vim-syntastic-puppet -f %{oreon_filedir}/vim-syntastic-puppet.list
%files -n vim-syntastic-python -f %{oreon_filedir}/vim-syntastic-python.list
%files -n vim-syntastic-qml -f %{oreon_filedir}/vim-syntastic-qml.list
%files -n vim-syntastic-rst -f %{oreon_filedir}/vim-syntastic-rst.list
%files -n vim-syntastic-ruby -f %{oreon_filedir}/vim-syntastic-ruby.list
%files -n vim-syntastic-sass -f %{oreon_filedir}/vim-syntastic-sass.list
%files -n vim-syntastic-scss -f %{oreon_filedir}/vim-syntastic-scss.list
%files -n vim-syntastic-sh -f %{oreon_filedir}/vim-syntastic-sh.list
%files -n vim-syntastic-spec -f %{oreon_filedir}/vim-syntastic-spec.list
%files -n vim-syntastic-tcl -f %{oreon_filedir}/vim-syntastic-tcl.list
%files -n vim-syntastic-tex -f %{oreon_filedir}/vim-syntastic-tex.list
%files -n vim-syntastic-texinfo -f %{oreon_filedir}/vim-syntastic-texinfo.list
%files -n vim-syntastic-text -f %{oreon_filedir}/vim-syntastic-text.list
%files -n vim-syntastic-trig -f %{oreon_filedir}/vim-syntastic-trig.list
%files -n vim-syntastic-turtle -f %{oreon_filedir}/vim-syntastic-turtle.list
%files -n vim-syntastic-vala -f %{oreon_filedir}/vim-syntastic-vala.list
%files -n vim-syntastic-verilog -f %{oreon_filedir}/vim-syntastic-verilog.list
%files -n vim-syntastic-vim -f %{oreon_filedir}/vim-syntastic-vim.list
%files -n vim-syntastic-xhtml -f %{oreon_filedir}/vim-syntastic-xhtml.list
%files -n vim-syntastic-xml -f %{oreon_filedir}/vim-syntastic-xml.list
%files -n vim-syntastic-xslt -f %{oreon_filedir}/vim-syntastic-xslt.list
%files -n vim-syntastic-yacc -f %{oreon_filedir}/vim-syntastic-yacc.list
%files -n vim-syntastic-yaml -f %{oreon_filedir}/vim-syntastic-yaml.list
%files -n vim-syntastic-yara -f %{oreon_filedir}/vim-syntastic-yara.list
%files -n vim-syntastic-z80 -f %{oreon_filedir}/vim-syntastic-z80.list
%files -n vim-syntastic-zsh -f %{oreon_filedir}/vim-syntastic-zsh.list

%changelog

%autochangelog
