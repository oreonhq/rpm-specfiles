%global source0_hash 722038065007226f0fa3de4629127294d2e29bfbbc41042c83a570fa0c455a47

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

Name:		hevea
Version:	2.38
Release:	1%{?dist}
Summary:	LaTeX to HTML translator

# QPL-1.0-INRIA-2004 WITH QPL-1.0-INRIA-2004-exception: the project as a whole
# LPPL-1.3a: hrlang.hva, lstlang*.sty, examples/natbib.sty
# GPL-2.0-or-later: html/mathpartir.hva, examples/mathpartir-test.tex
License:	QPL-1.0-INRIA-2004 WITH QPL-1.0-INRIA-2004-exception AND LPPL-1.3a AND GPL-2.0-or-later
URL:		http://hevea.inria.fr/
VCS:		git:https://github.com/maranget/hevea.git
Source0:	http://hevea.inria.fr/distri/%{name}-%{version}.tar.gz
Source1:	http://hevea.inria.fr/distri/%{name}-%{version}-manual.pdf

BuildRequires:	make
BuildRequires:	ocaml
BuildRequires:	ocaml-ocamlbuild
BuildRequires:	tex(latex)
BuildRequires:	tex(amsfonts.sty)
BuildRequires:	tex(comment.sty)
BuildRequires:	tex(keyval.sty)
BuildRequires:	tex(url.sty)

Requires:	ghostscript
Requires:	netpbm-progs
Requires:	tex(dvips)
Requires:	tex(latex)
Requires:	tex(amsfonts.sty)
Requires:	tex(comment.sty)
Requires:	tex(keyval.sty)
Requires:	tex(url.sty)

%description
HEVEA is a quite complete and fast LATEX to HTML translator.
HEVEA renders symbols by using the so-called HTML "entities", which
modern browsers display correctly most of the time.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
cp -p %{SOURCE1} .

# Fix encoding
iconv -f iso-8859-1 -t utf-8 CHANGES > CHANGES.utf8
touch -r CHANGES CHANGES.utf8
mv -f CHANGES.utf8 CHANGES

%build
# The next line causes ocamlbuild to pass -g everywhere:
echo true: debug >> _tags
ulimit -s unlimited
%make_build \
%ifnarch %{ocaml_native_compiler}
	TARGET=byte \
%endif
	PREFIX=%{_prefix} \
	LIBDIR=%{_datadir}/%{name} \
	LATEXLIBDIR=%{_texmf_main}/tex/latex/hevea

%install
%make_install \
%ifnarch %{ocaml_native_compiler}
	TARGET=byte \
%endif
	PREFIX=%{_prefix} \
	LIBDIR=%{_datadir}/hevea \
	LATEXLIBDIR=%{_texmf_main}/tex/latex/hevea

# Link, rather than copy, identical files
rm %{buildroot}%{_datadir}/hevea/{info,text}/report.hva
ln %{buildroot}%{_datadir}/hevea/html/report.hva \
   %{buildroot}%{_datadir}/hevea/info/report.hva
ln %{buildroot}%{_datadir}/hevea/html/report.hva \
   %{buildroot}%{_datadir}/hevea/text/report.hva

# Fix up the examples for installation
rm examples/.gitignore
rm examples/hevea.sty
ln -s %{_texmf_main}/tex/latex/hevea/hevea.sty examples

%files
%doc README CHANGES examples %{name}-%{version}-manual.pdf
%license LICENSE
%{_bindir}/*
%{_datadir}/hevea
%{_texmf_main}/tex/latex/hevea/

%changelog
%autochangelog
