%global source0_hash 09e5f29531daab93366bb061e76019d5e91691ef0a40328f04c927387d1d364d
%{?python_enable_dependency_generator}
%global pypi_name yamllint
Name:           %{pypi_name}
Version:        1.38.0
Release:        1%{?dist}
Summary:        A linter for YAML files
License:        GPL-3.0-or-later
URL:            https://github.com/adrienverge/yamllint
Source0:        https://pypi.python.org/packages/source/y/%{name}/%{name}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77.0.3
Requires:       python3-yamllint = %{version}-%{release}
# /oreon:deps
%package -n       python3-yamllint+dev
Summary:        Metapackage for python3-yamllint dev extras
Requires:       python3-yamllint = %{version}-%{release}
Provides:       python3dist(yamllint[dev]) = %{version}-%{release}

%description -n python3-yamllint+dev
Metapackage for python3-yamllint dev extras.

%description
A linter for YAML files.

yamllint does not only check for syntax validity, but for weirdnesses like key
repetition and cosmetic problems such as lines length, trailing spaces,
indentation, etc.

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
%pyproject_install
mkdir -p %{buildroot}%{_mandir}/man1/
install -m0644 docs/_build/man/%{pypi_name}.1.gz %{buildroot}%{_mandir}/man1/
%oreon_autofiles main

%check

%{__python3} -m unittest discover
%files

%changelog

%autochangelog
