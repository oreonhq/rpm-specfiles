%global source0_hash 9cf5aab32853c8c31af572e4fecdc09c997e2b8be5a07daf2a389e270e85b213
%global _docdir_fmt %{name}
%global giturl  https://github.com/sphinx-doc/sphinx-autobuild
Name:           python-sphinx-autobuild
Version:        2025.8.25
Release:        1%{?dist}
Summary:        Autobuild a Sphinx directory when a change is detected
License:        MIT
URL:            https://sphinx-autobuild.readthedocs.io/
VCS:            git:%{giturl}.git
Source0:        https://files.pythonhosted.org/packages/source/s/sphinx-autobuild/sphinx_autobuild-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) >= 3.7
Requires:       python3-sphinx-autobuild = %{version}-%{release}
# /oreon:deps
%package -n       python3-sphinx-autobuild+docs
Summary:        Metapackage for python3-sphinx-autobuild docs extras
Requires:       python3-sphinx-autobuild = %{version}-%{release}
Provides:       python3dist(sphinx-autobuild[docs]) = %{version}-%{release}

%description -n python3-sphinx-autobuild+docs
Metapackage for python3-sphinx-autobuild docs extras.

%package -n       python3-sphinx-autobuild+test
Summary:        Metapackage for python3-sphinx-autobuild test extras
Requires:       python3-sphinx-autobuild = %{version}-%{release}
Requires:       python3dist(pytest) >= 6
Provides:       python3dist(sphinx-autobuild[test]) = %{version}-%{release}

%description -n python3-sphinx-autobuild+test
Metapackage for python3-sphinx-autobuild test extras.

%description
Rebuild Sphinx documentation on changes, with live-reload in the browser.

%package     -n python3-sphinx-autobuild
Summary:        Autobuild a Sphinx directory when a change is detected
# oreon:reqs
Requires:       python3dist(colorama) >= 0.4.6
Requires:       python3dist(starlette) >= 0.35
Requires:       python3dist(uvicorn) >= 0.25
Requires:       python3dist(watchfiles) >= 0.20
Requires:       python3dist(websockets) >= 11
# /oreon:reqs
%description -n python3-sphinx-autobuild
Rebuild Sphinx documentation on changes, with live-reload in the browser.

%package        doc
License:        MIT AND BSD-2-Clause AND BSD-3-Clause
Summary:        Documentation for sphinx-autobuild
%description    doc
Documentation for sphinx-autobuild.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir sphinx_autobuild-%{version}
%oreon_prep
%build

%pyproject_wheel
rst2html --no-datestamp NEWS.rst NEWS.html
rst2html --no-datestamp README.rst README.html
mkdir html
sphinx-build -b html docs html
rm -rf html/{.buildinfo,.doctrees}
%install
%pyproject_install
mkdir -p %{buildroot}%{_mandir}/man1
%{py3_test_envvars} help2man -N %{buildroot}%{_bindir}/sphinx-autobuild \
  -n 'Autobuild a Sphinx directory when a change is detected' \
  > %{buildroot}%{_mandir}/man1/sphinx-autobuild.1
%oreon_autofiles python3-sphinx-autobuild usr/lib/python3*/site-packages/sphinx_autobuild* usr/lib64/python3*/site-packages/sphinx_autobuild* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/sphinx_autobuild* usr/lib64/python3*/site-packages/sphinx_autobuild* usr/bin/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%pytest -v
%files
%files -n python3-sphinx-autobuild -f %{oreon_filedir}/python3-sphinx-autobuild.list
%files -n python-sphinx-autobuild-doc -f %{oreon_filedir}/python-sphinx-autobuild-doc.list

%changelog

%autochangelog
