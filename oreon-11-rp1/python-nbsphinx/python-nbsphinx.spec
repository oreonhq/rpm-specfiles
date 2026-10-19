%global source0_hash d0765908399a8ee2b57be7ae881cf2ea58d66db3af7bbf33e6eb48f83bea5495
Name:           python-nbsphinx
Version:        0.9.8
Release:        1%{?dist}
Summary:        Jupyter Notebook Tools for Sphinx
License:        MIT
URL:            http://nbsphinx.rtfd.io/
Source0:        https://files.pythonhosted.org/packages/source/n/nbsphinx/nbsphinx-%{version}.tar.gz
Patch0:         allow-errors-in-notebooks-with-external-images.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-nbsphinx = %{version}-%{release}
# /oreon:deps
%description
nbsphinx is a Sphinx extension that provides a source parser for *.ipynb
files. Custom Sphinx directives are used to show Jupyter Notebook code cells
(and of course their results) in both HTML and LaTeX output. Unevaluated
notebooks, i.e. notebooks without stored output cells, will be automatically
executed during the Sphinx build process.

%package -n     python3-nbsphinx
Summary:        Jupyter Notebook Tools for Sphinx
# oreon:reqs
Requires:       python3dist(docutils) >= 0.18.1
Requires:       python3dist(nbconvert) >= 5.3
Requires:       python3dist(sphinx) >= 1.8
Requires:       python3dist(traitlets) >= 5
# /oreon:reqs
%description -n python3-nbsphinx
nbsphinx is a Sphinx extension that provides a source parser for *.ipynb
files. Custom Sphinx directives are used to show Jupyter Notebook code cells
(and of course their results) in both HTML and LaTeX output. Unevaluated
notebooks, i.e. notebooks without stored output cells, will be automatically
executed during the Sphinx build process.

%package -n python-nbsphinx-doc
Summary:        nbsphinx documentation
%description -n python-nbsphinx-doc
Documentation for nbsphinx

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n nbsphinx-%{version} -S git
# Disables custom formatter not available in Fedora.
# The result is that pages:
# https://nbsphinx.readthedocs.io/en/0.8.6/a-markdown-file.html
# https://nbsphinx.readthedocs.io/en/0.8.6/custom-formats.html
# are not available.
# TODO: package jupytext
sed -i "/\['jupytext.reads', {'fmt'/d" doc/conf.py
# Delete the Sphinx extension we don't have packaged in Fedora
# This extension links the code examples to their respective documentation,
# its absence doesn't break the nbsphinx' docs
sed -i "/'sphinx_codeautolink',  # automatic links from code to documentation/d" doc/conf.py

%build

%pyproject_wheel
git tag %{version}
echo "nbsphinx_allow_errors = True" >> doc/conf.py
PYTHONPATH=build/lib sphinx-build-3 doc html
rm -rf html/{.doctrees,.buildinfo,conf.py,_sources}
%install
%pyproject_install
%oreon_autofiles python3-nbsphinx usr/lib/python3*/site-packages/nbsphinx* usr/lib64/python3*/site-packages/nbsphinx* usr/bin/*
%oreon_autofiles python-nbsphinx-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/lib/python3*/site-packages/nbsphinx* usr/lib64/python3*/site-packages/nbsphinx* usr/bin/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%pyproject_check_import
%files
%files -n python3-nbsphinx -f %{oreon_filedir}/python3-nbsphinx.list
%files -n python-nbsphinx-doc -f %{oreon_filedir}/python-nbsphinx-doc.list

%changelog

%autochangelog
