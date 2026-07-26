%global source0_hash afc7d8c584a5ed0a11033af086e8af226a9c0b206f313e0301f8dd7b6b589602

%global modname semver

Name:           python-%{modname}
Version:        3.0.4
Release:        5%{?dist}
Summary:        Python helper for Semantic Versioning

License:        BSD-3-Clause
URL:            https://github.com/python-semver/python-semver
Source0:        %{pypi_source semver}

BuildArch:      noarch

BuildRequires:  python3-devel
# test requirements
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cov)

%global _description %{expand:
A Python module for semantic versioning. Simplifies comparing versions.}

%description %{_description}

%package -n     python3-%{modname}
Summary:        %{summary}

%description -n python3-%{modname}
%{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{modname}-%{version} -p 1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files 'semver'

%check
%pytest

%files -n python3-%{modname} -f %{pyproject_files}
%license LICENSE.txt
%doc README.rst CHANGELOG.rst
%{_bindir}/pysemver

%changelog
%autochangelog
