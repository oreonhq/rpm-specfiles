%global source0_hash 7741722357dd75f8190766926071fed3bdc211c74dd2d7d4df5404da95930ddb
Name:           python-sphinx
Version:        9.1.0
Release:        1%{?dist}
Summary:        Python documentation generator
License:        BSD-2-Clause
URL:            https://www.sphinx-doc.org/
Source0:        https://files.pythonhosted.org/packages/source/s/sphinx/sphinx-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) >= 3.12
Requires:       python3-sphinx = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-sphinx
Summary:        Python documentation generator
# oreon:reqs
Requires:       python3dist(alabaster) >= 0.7.14
Requires:       python3dist(babel) >= 2.13
Requires:       python3dist(colorama) >= 0.4.6
Requires:       python3dist(docutils) < 0.23
Requires:       python3dist(docutils) >= 0.21
Requires:       python3dist(imagesize) >= 1.3
Requires:       python3dist(jinja2) >= 3.1
Requires:       python3dist(packaging) >= 23.0
Requires:       python3dist(pygments) >= 2.17
Requires:       python3dist(requests) >= 2.30.0
Requires:       python3dist(roman-numerals) >= 1.0.0
Requires:       python3dist(snowballstemmer) >= 2.2
Requires:       python3dist(sphinxcontrib-applehelp) >= 1.0.7
Requires:       python3dist(sphinxcontrib-devhelp) >= 1.0.6
Requires:       python3dist(sphinxcontrib-htmlhelp) >= 2.0.6
Requires:       python3dist(sphinxcontrib-jsmath) >= 1.0.1
Requires:       python3dist(sphinxcontrib-qthelp) >= 1.0.6
Requires:       python3dist(sphinxcontrib-serializinghtml) >= 1.1.9
# /oreon:reqs
%description -n python3-sphinx

%prep
%global oreon_srcdir sphinx-9.1.0
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
ln -s sphinx-build %{buildroot}%{_bindir}/sphinx-build-3
%oreon_autofiles python3-sphinx usr/lib/python3*/site-packages/sphinx* usr/lib64/python3*/site-packages/sphinx* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/sphinx* usr/lib64/python3*/site-packages/sphinx* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-sphinx -f %{oreon_filedir}/python3-sphinx.list

%changelog

%autochangelog
