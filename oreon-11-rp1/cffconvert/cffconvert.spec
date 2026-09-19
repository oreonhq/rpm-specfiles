%global source0_hash 81915a8b1e8ec342af218155c7db2f079a12da8e60c46f5579060b2c3a7109b5

%bcond_without tests

%global pypi_name cffconvert
%global orig_name cff-converter-python

%global _description %{expand:
Implementation of Command-line program to validate and convert
CITATION.cff files in Python.}

Name:           %{pypi_name}
Version:        2.0.0
Release:        21%{?dist}
Summary:        Command line program to validate and convert CITATION.cff files

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/citation-file-format/%{orig_name}
Source0:        %{url}/archive/%{version}/%{orig_name}-%{version}.tar.gz

BuildArch:      noarch

# Allow jsonschema 4.x
# https://github.com/citation-file-format/cff-converter-python/pull/277
Patch:          %{url}/pull/277.patch

BuildRequires:  python3-devel
BuildRequires:  help2man

%if %{with tests}
BuildRequires:  python3dist(pytest)
%endif

%description -n %{pypi_name} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{orig_name}-%{version}

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -r -i 's/--[^[:blank:]]*\bcov\b[^[:blank:]]*//' setup.cfg

%generate_buildrequires
%pyproject_buildrequires -x gcloud

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l cffconvert

# man page
install -d '%{buildroot}%{_mandir}/man1'
    env PATH="${PATH}:%{buildroot}%{_bindir}" \
        PYTHONPATH='%{buildroot}%{python3_sitelib}' \
        help2man --no-info '%{pypi_name}' \
            --output='%{buildroot}%{_mandir}/man1/%{pypi_name}.1'

%check
%if %{with tests}
PYTHONPATH="${PWD}" %pytest -k "${k-}" test/
%endif

%files -n cffconvert -f %{pyproject_files}
%doc docs/ README.md CHANGELOG.md CITATION.cff CONTRIBUTING.md
%{_bindir}/%{pypi_name}
%{_mandir}/man1/%{pypi_name}.1*

%changelog
%autochangelog
