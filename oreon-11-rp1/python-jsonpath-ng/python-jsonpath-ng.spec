%global source0_hash 54252968134b5e549ea5b872f1df1168bd7defe1a52fed5a358c194e1943ddc3

%global pypi_name jsonpath-ng

Name:           python-%{pypi_name}
Version:        1.8.0
Release:        %autorelease
Summary:        Implementation of JSONPath for Python

# Main library: ASL 2.0
# jsonpath_ng/bin/jsonpath.py: WTFPL
License:        Apache-2.0 AND WTFPL
URL:            https://github.com/h2non/jsonpath-ng
Source0:        %{pypi_source jsonpath_ng}
BuildArch:      noarch

BuildRequires:  python3-devel
# Test dependencies
BuildRequires:  python3-hypothesis
BuildRequires:  python3-pytest

%global _description %{expand:
Implementation of JSONPath for Python that aims to be standard compliant,
including arithmetic and binary comparison operators, as defined in the
original JSONPath proposal.}

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n jsonpath_ng-%{version}
sed -i -e '/^#!\//, 1d' jsonpath_ng/bin/jsonpath.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files jsonpath_ng

%check
%{pytest} -v

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%{_bindir}/jsonpath_ng

%changelog
%autochangelog
