%global source0_hash 4d8e3e471cd3e9a9bd13d5086cdf7c0af1b0c3f3e195e74f5f63318dc40a66d8

Name:           PyX
Version:        0.16
Release:        15%{?dist}
Summary:        Python graphics package

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://pyx-project.org/
Source0:        https://files.pythonhosted.org/packages/source/P/PyX/PyX-%{version}.tar.gz

# Patches from Debian
Patch0:         manual-pythonpath.patch
Patch1:         sphinx-local-mathjax.patch
Patch2:         sphinx-no-eager-only.patch

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  ghostscript
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(setuptools)

#BuildRequires:  texlive-collection-latexextra
BuildRequires:  texlive-lib-devel
BuildRequires:  texlive-collection-latexrecommended
BuildRequires:  latexmk
BuildRequires:  tex(capt-of.sty)
BuildRequires:  tex(fncychap.sty)
BuildRequires:  tex(framed.sty)
BuildRequires:  tex(needspace.sty)
BuildRequires:  tex(upquote.sty)
BuildRequires:  tex(tabulary.sty)
BuildRequires:  tex(tgtermes.sty)
BuildRequires:  tex(wrapfig.sty)

Requires:       tex(latex)
Provides:       python3-pyx = %{version}-%{release}

%description
PyX is a Python package for the creation of PostScript and PDF files. It
combines an abstraction of the PostScript drawing model with a TeX/LaTeX
interface. Complex tasks like 2d and 3d plots in publication-ready quality are
built out of these primitives.

%package doc
Summary: Documentation for %{name}
BuildArch: noarch

%description doc
%{Summary}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
# Set the extensions to be built
%{__sed} -i 's|^build_t1code =.*|build_t1code = 1|' setup.cfg
%{__sed} -i 's|^build_pykpathsea =.*|build_pykpathsea = 1|' setup.cfg

%{py3_build}

# turn on ipc in config file
%{__sed} -i 's|^texipc =.*|texipc = 1|' pyx/data/pyxrc

pushd faq
%{__sed} -i 's|sphinx-build|sphinx-build-3|' Makefile
make
make html
mv _build/html/ faq
mv _build/latex/pyxfaq.pdf ..
popd

pushd manual
%{__sed} -i 's|sphinx-build|sphinx-build-3|' Makefile
make
make html
mv _build/html/ manual
mv _build/latex/manual.pdf ..
popd

%install
rm -rf %{buildroot}
%{py3_install}

%{__mkdir} %{buildroot}%{_sysconfdir}
%{__cp} -a pyx/data/pyxrc %{buildroot}%{_sysconfdir}/pyxrc

# Fix the non-exec with shellbang rpmlint errors
for file in `find %{buildroot}%{python3_sitearch}/pyx -type f -name "*.py"`; do
  [ ! -x ${file} ] && %{__sed} -i 's|^#!|##|' ${file}
done

%files
%license LICENSE
%doc AUTHORS CHANGES PKG-INFO README.md
%config(noreplace) %{_sysconfdir}/pyxrc
%{python3_sitearch}/%{name}*egg-info
%{python3_sitearch}/pyx/

%files doc
%license LICENSE
%doc *.pdf
%doc faq/faq manual/manual
%doc contrib/
%doc examples/

%changelog
%autochangelog
