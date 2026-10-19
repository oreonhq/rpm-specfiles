%global source0_hash 104e3ba4041aa4c2934dfeccaf19decbf79423c9fba566eac65ee801050bd0c1
%{?python_enable_dependency_generator}
%global pypi_name ModulemdTranslationHelpers
Name:           python-%{pypi_name}
Version:        0.6
Release:        1%{?dist}
Summary:        Tools for working with translations of modulemd
License:        MIT
URL:            https://github.com/fedora-modularity/ModulemdTranslationHelpers
Source0:        https://files.pythonhosted.org/packages/source/p/python-ModulemdTranslationHelpers/python-ModulemdTranslationHelpers-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
# /oreon:deps
%description
Provides a library and tools for dealing with translatable strings in modulemd
documents.

%package -n     python3-%{pypi_name}
Summary:        Tools for working with translations of modulemd
%{?python_provide:%python_provide python3-%{pypi_name}}
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
Requires:       libmodulemd
Requires:       python%{python3_version}dist(pygobject)
Obsoletes:      python3-mmdzanata < 0.7-3
Obsoletes:      python2-mmdzanata < 0.7-3
%description -n python3-%{pypi_name}
Provides a library and tools for dealing with translatable strings in modulemd
documents.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build

%py3_build
%install
%py3_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python3-ModulemdTranslationHelpers -f %{oreon_filedir}/python3-ModulemdTranslationHelpers.list

%changelog

%autochangelog
