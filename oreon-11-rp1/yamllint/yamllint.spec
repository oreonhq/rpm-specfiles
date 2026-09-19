%global source0_hash 09e5f29531daab93366bb061e76019d5e91691ef0a40328f04c927387d1d364d

%{?python_enable_dependency_generator}
# Based on spec created by pyp2rpm-2.0.0
%global pypi_name yamllint

Name:           %{pypi_name}
Version:        1.38.0
Release:        1%{?dist}
Summary:        A linter for YAML files

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/adrienverge/yamllint
Source0:        https://pypi.python.org/packages/source/y/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires: make
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pathspec
BuildRequires:  python3-PyYAML
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme

%description
A linter for YAML files.

yamllint does not only check for syntax validity, but for weirdnesses like key
repetition and cosmetic problems such as lines length, trailing spaces,
indentation, etc.

%generate_buildrequires
%pyproject_buildrequires

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%pyproject_wheel

%{__make} SPHINXBUILD=/usr/bin/sphinx-build-3 -C docs man
gzip docs/_build/man/%{pypi_name}.1

%install
# Must do the subpackages' install first because the scripts in /usr/bin are
# overwritten with every setup.py install.
%pyproject_install

mkdir -p %{buildroot}%{_mandir}/man1/
install -m0644 docs/_build/man/%{pypi_name}.1.gz %{buildroot}%{_mandir}/man1/

%check
%{__python3} -m unittest discover

%files
%doc README.rst
%license LICENSE
%{_bindir}/%{pypi_name}
%{_mandir}/man1/%{pypi_name}.1.gz
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-*
%exclude %{python3_sitelib}/tests

%changelog
%autochangelog
