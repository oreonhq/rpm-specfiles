%global source0_hash 104e3ba4041aa4c2934dfeccaf19decbf79423c9fba566eac65ee801050bd0c1

%{?python_enable_dependency_generator}
%global pypi_name ModulemdTranslationHelpers

Name:           python-%{pypi_name}
Version:        0.6
Release:        28%{?dist}
Summary:        Tools for working with translations of modulemd

License:        MIT
URL:            https://github.com/fedora-modularity/ModulemdTranslationHelpers
Source0:        %{pypi_source}

BuildArch:      noarch

%description
Provides a library and tools for dealing with translatable strings in modulemd
documents.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
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

%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE
%{_bindir}/ModulemdTranslationHelpers
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-*.egg-info/

%changelog
%autochangelog
