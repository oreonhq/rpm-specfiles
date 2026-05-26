# For bootstrapping sphinxcontrib-websupport
%bcond_without docs

%global mod_name Whoosh

Name:           python-whoosh
Version:        2.7.4
Release:        42%{?dist}
Summary:        Fast, pure-Python full text indexing, search, and spell checking library 

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD 
URL:            http://pythonhosted.org/Whoosh/
Source0:        https://pypi.python.org/packages/source/W/%{mod_name}/%{mod_name}-%{version}.tar.gz
Patch1:         whoosh-fix-sphinx.patch
# oreon url source checksums begin
%global source0_sha256 7ca5633dbfa9e0e0fa400d3151a8a0c4bec53bd2ecedc0a67705b17565c31a83
%global source0_file Whoosh-2.7.4.tar.gz
# oreon url source checksums end

BuildArch:      noarch

%if %{with docs}
BuildRequires:  python%{python3_pkgversion}-sphinx
%endif

BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: python%{python3_pkgversion}-setuptools
BuildRequires: python%{python3_pkgversion}-pytest

%description
Whoosh is a fast, featureful full-text indexing and searching library
implemented in pure Python. Programmers can use it to easily add search
functionality to their applications and websites. Every part of how Whoosh
works can be extended or replaced to meet your needs exactly.

%package -n python%{python3_pkgversion}-whoosh
Summary:    Fast, Python3 full text indexing, search, and spell checking library
%{?python_provide:%python_provide python%{python3_pkgversion}-whoosh}

%description -n python%{python3_pkgversion}-whoosh
Whoosh is a fast, featureful full-text indexing and searching library
implemented in pure Python. Programmers can use it to easily add search
functionality to their applications and websites. Every part of how Whoosh
works can be extended or replaced to meet your needs exactly.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Whoosh-2.7.4.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "7ca5633dbfa9e0e0fa400d3151a8a0c4bec53bd2ecedc0a67705b17565c31a83" || { echo "oreon: Source0 SHA256 mismatch for Whoosh-2.7.4.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n %{mod_name}-%{version}
%patch -p1 -P1
# pytest 4
sed -i 's/\[pytest\]/\[tool:pytest\]/' setup.cfg

%build
%py3_build

%if %{with docs}
sphinx-build docs/source docs/html
rm -f docs/html/.buildinfo
rm -rf docs/html/.doctrees
%endif

%install
%py3_install

%check
# Do not run test over test_automata.py, it fails due to Python 3.13
# Whoosh project is dead, no fixes expected
rm tests/test_automata.py
%pytest

%files -n python%{python3_pkgversion}-whoosh
%license LICENSE.txt
%doc README.txt
%if %{with docs}
%doc docs/html/
%endif
%{python3_sitelib}/whoosh/
%{python3_sitelib}/*.egg-info/

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.7.4-42
- Prepare for Oreon 11 (RP1)
