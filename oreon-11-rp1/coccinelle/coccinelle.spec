%global source0_hash 85989b37a2b37c37f62ae9576042c0c812908f97dac76ecbbdc9707225aced79
ExcludeArch: %{ix86}
%global forgeurl https://github.com/coccinelle/coccinelle
%global tag 1.3.1
Version:       1.3.3
%forgemeta
%bcond_without doc
%ifnarch %{ocaml_native_compiler}
%global __strip %{_bindir}/true
%global debug_package %{nil}
%endif
Name:           coccinelle
Release:        1%{?dist}
Summary:        Semantic patching for Linux (spatch)
License:        GPL-2.0-only
URL:            https://coccinelle.lip6.fr/
Source0:        %{forgeurl}/archive/%{tag}/%{name}-%{tag}.tar.gz
Source1:        test.c
Source2:        testpy.cocci
%if %{with doc}
%endif
%{lua:
  modules = {
    'Control_flow_c',
    'Cpp_token_c',
    'Danger',
    'Data',
    'Flag_parsing_cocci',
    'Includes',
    'Includes_cache',
    'Lexer_parser',
    'Ograph_extended',
    'Parsing_consistency_c',
    'Parsing_hacks',
    'Parsing_recovery_c',
    'Parsing_stat',
    'Regexp_pcre',
    'Semantic_c',
    'Token_annot',
    'Token_helpers',
    'Token_views_c',
    'Type_annoter_c',
  }
  local arg = "__ocaml_requires_opts"
  for i, m in ipairs(modules) do
    arg = arg .. " -i " .. m .. " -x " .. m
  end
  rpm.define(arg)
}
Requires:       ocaml-findlib
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bash-completion
BuildRequires:  hevea
BuildRequires:  latexmk
BuildRequires:  make
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib-devel
BuildRequires:  ocaml-menhir
BuildRequires:  ocaml-num-devel
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-parmap-devel
BuildRequires:  ocaml-pcre-devel
BuildRequires:  ocaml-pyml-devel
BuildRequires:  ocaml-stdcompat-devel
BuildRequires:  python3-devel
BuildRequires:  texlive-boxedminipage
BuildRequires:  texlive-comment
BuildRequires:  texlive-endnotes
BuildRequires:  texlive-ifsym
BuildRequires:  texlive-latex
BuildRequires:  texlive-listings
BuildRequires:  texlive-moreverb
BuildRequires:  texlive-multirow
BuildRequires:  texlive-preprint
BuildRequires:  texlive-subfigure
BuildRequires:  texlive-wrapfig
BuildRequires:  texlive-xypic
# /oreon:deps
%description
Coccinelle is a tool to utilize semantic patches for manipulating C
code.  It was originally designed to ease maintenance of device
drivers in the Linux kernel.

%package bash-completion
Summary:        Bash tab-completion for %{name}
BuildArch:      noarch
Requires:       bash-completion > 2.0
Requires:       %{name} = %{version}-%{release}
%description bash-completion
Install this package if you want intelligent bash tab-completion
for %{name}.

%if %{with doc}
%package doc
Summary:        Documentation for %{name}
License:        GFDL-1.3-no-invariants-only
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
%description doc
The %{name}-doc package contains documentation for %{name}.
%endif

%package examples
Summary:        Examples for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
%description examples
The %{name}-examples package contains examples for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup

# Replace /usr/bin/env shebang with /usr/bin/python3
sed -i '1s_^#!/usr/bin/env python$_#!%{python3}_' tools/pycocci

# Remove .gitignore files.
find -name .gitignore -delete

# Convert a few files to UTF-8 encoding.
for f in demos/demo_rule9/sym53c8xx.res demos/demo_rule9/sym53c8xx.c; do
  mv $f $f.orig
  iconv -f iso-8859-1 -t utf-8 < $f.orig > $f
  rm $f.orig
done

# replace tabs with spaces
find . -iname '*.py' | xargs -I {} sh -exc 'expand -t8 {} > tempfile && mv tempfile {}'

# Properly rebuild Menhir generated files.
rm -f parsing_cocci/parser_cocci_menhir.ml parsing_cocci/parser_cocci_menhir.mli

%build

autoreconf -i
./autogen
%configure \
    --with-python=%{_bindir}/python3 \
    --with-menhir=%{_bindir}/menhir
%{__sed} -i \
  -e 's,LIBDIR=.*,LIBDIR=%{_libdir},' \
  -e 's,MANDIR=.*,MANDIR=%{_mandir},' \
  -e 's,SHAREDIR=.*,SHAREDIR=%{_libdir}/%{name},' \
  -e 's,DYNLINKDIR=.*,DYNLINKDIR=%{_libdir}/ocaml,' \
  -e 's,BASH_COMPLETION_DIR=.*,BASH_COMPLETION_DIR=%{bash_completions_dir},' \
  Makefile.config
echo '
EXTRA_OCAML_FLAGS = -g
EXTRACFLAGS = $(EXTRA_OCAML_FLAGS)
' > Makefile.local
%ifarch %{ocaml_native_compiler}
target=all-release
%else
target="all-dev docs"
%endif
unset MAKEFLAGS
make $target VERBOSE=yes
%install
mkdir -p $RPM_BUILD_ROOT%{_libdir}/python/coccilib
%make_install
rm -f $RPM_BUILD_ROOT%{_bindir}/spatch.byte
rm -f $RPM_BUILD_ROOT%{_bindir}/spatch.opt
pushd $RPM_BUILD_ROOT%{_libdir}
mkdir coccinelle
mkdir coccinelle/ocaml
for f in standard.h standard.iso spatch spatch.byte spatch.opt ocaml/*; do
  if [ -f $f ]; then
    mv $f coccinelle/$f
  fi
done
popd
mkdir -p $RPM_BUILD_ROOT%{python3_sitelib}
mv $RPM_BUILD_ROOT%{_libdir}/python/coccilib \
  $RPM_BUILD_ROOT%{python3_sitelib}
rmdir $RPM_BUILD_ROOT%{_libdir}/python
mv $RPM_BUILD_ROOT%{_bindir}/spatch $RPM_BUILD_ROOT%{_libdir}/coccinelle
cp -p tools/pycocci $RPM_BUILD_ROOT%{_bindir}/
cp -p scripts/spatch.sh $RPM_BUILD_ROOT%{_bindir}/spatch
chmod a+x $RPM_BUILD_ROOT%{_bindir}/spatch
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export COCCINELLE_HOME=$RPM_BUILD_ROOT%{_libdir}/coccinelle
spatch=$COCCINELLE_HOME/spatch
export LD_LIBRARY_PATH=.
export PYTHONPATH=$RPM_BUILD_ROOT%{python3_sitelib}:$PYTHONPATH
$spatch --help
$spatch -sp_file demos/simple.cocci demos/simple.c
$spatch --sp-file %{SOURCE2} %{SOURCE1}
%files -f %{oreon_filedir}/main.list
%files -n coccinelle-bash-completion -f %{oreon_filedir}/coccinelle-bash-completion.list
%files -n coccinelle-doc -f %{oreon_filedir}/coccinelle-doc.list
%files -n coccinelle-examples -f %{oreon_filedir}/coccinelle-examples.list

%changelog

%autochangelog
