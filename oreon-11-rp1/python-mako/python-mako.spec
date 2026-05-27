%global source0_hash none

Name:    python-mako
Version: 1.2.3
Release: 14%{?dist}
Summary: Mako template library for Python

# Mostly MIT, but _ast_util.py is Python-2.0.1 licensed
# examples/bench/basic.py is BSD-3-Clause
License: MIT AND Python-2.0.1 AND BSD-3-Clause
URL:     https://www.makotemplates.org/
Source0: https://github.com/sqlalchemy/mako/archive/rel_%(echo %{version} | sed "s/\./_/g").tar.gz

BuildArch:     noarch
BuildRequires: python3-devel
BuildRequires: python3-pytest
BuildRequires: python3-setuptools
BuildRequires: python3-markupsafe

%global _description\
Mako is a template library written in Python. It provides a familiar, non-XML\
syntax which compiles into Python modules for maximum performance. Mako's\
syntax and API borrows from the best ideas of many others, including Django\
templates, Cheetah, Myghty, and Genshi. Conceptually, Mako is an embedded\
Python (i.e. Python Server Page) language, which refines the familiar ideas of\
componentized layout and inheritance to produce one of the most straightforward\
and flexible models available, while also maintaining close ties to Python\
calling and scoping semantics.

%description %_description


%package -n python3-mako
Summary: %{summary}

# Beaker is the preferred caching backend, but is not strictly necessary
Recommends: python3-beaker

Obsoletes: python2-mako < 1.1.0-3
Obsoletes: python-mako-doc < 1.1.4-6

%{?python_provide:%python_provide python3-mako}

%description -n python3-mako %_description

This package contains the mako module built for use with python3.



%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1 -n mako-rel_%(echo %{version} | sed "s/\./_/g")

# the package ends up installed as %%{version}.dev0 otherwise:
sed -i '/tag_build = dev/d' setup.cfg


%build
%py3_build


%install
%py3_install

mv %{buildroot}/%{_bindir}/mako-render %{buildroot}/%{_bindir}/mako-render-%{python3_version}
ln -s ./mako-render-%{python3_version} %{buildroot}/%{_bindir}/mako-render-3
ln -s ./mako-render-%{python3_version} %{buildroot}/%{_bindir}/mako-render


%check
pytest-3


%files -n python3-mako
%license LICENSE
%doc CHANGES README.rst examples
%{_bindir}/mako-render
%{_bindir}/mako-render-3
%{_bindir}/mako-render-%{python3_version}
%{python3_sitelib}/mako/
%{python3_sitelib}/Mako-*.egg-info/


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2.3-14
- Prepare for Oreon 11 (RP1)
