%global source0_hash d830528f36c340f1488ff259dbf64ff19dc5db43253517e8c724313858e71c6b

Name:           python-django-health-check
Version:        3.20.8
Release:        1%{?dist}
Summary:        Monitor the health of your Django app and its connected services

License:        MIT
URL:            https://github.com/codingjoe/django-health-check
Source:         %{url}/archive/%{version}/django-health-check-%{version}.tar.gz

# Downstream-only: patch out coverage-analysis (pytest-cov) options for pytest
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
Patch:          django-health-check-3.20.8-pytest-no-coverage.patch

BuildArch:      noarch

BuildRequires:  tomcli

%global _description %{expand:
Pluggable health checks for Django applications. This project checks for
various conditions and provides reports when anomalous behavior is detected.}

%description %_description

%package -n python3-django-health-check
Summary:        %summary

# The -doc subpackage previously contained only the README and license file.
# Now we ship the Markdown sources because they are useful on their own. (We
# could build them with mkdocs, but there are missing extensions, and the
# resulting HTML would have license and bundling difficulties similar to those
# numerous, we don’t need to split them out into a -doc subpackage.
Provides:       python-django-health-check-doc = %{version}-%{release}
Obsoletes:      python-django-health-check-doc < 3.20.8

%description -n python3-django-health-check %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n django-health-check-%{version}
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
tomcli set pyproject.toml lists delitem dependency-groups.test 'pytest-cov\b.*'

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%pyproject_buildrequires -g test

%build
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l health_check

%check
PYTHONPATH="${PWD}" %pytest

%files -n python3-django-health-check -f %{pyproject_files}
%doc README.md
# Markdown sources and associated images
%doc docs/

%changelog
%autochangelog
