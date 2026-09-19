%global source0_hash 0c26340b5f4c0f7f51c2ea713995609c68c12fa3373cc5c303a4e74f20cd1fbd

%bcond_without  tests
%global pypi_name distroinfo

%global summary Parsing and querying distribution metadata stored in text/YAML files

%global desc\
distroinfo is a python module for parsing, validating and querying\
distribution/packaging metadata stored in human readable and review-able\
text/YAML files.\
\
distroinfo is a generic (re)implementation of rdoinfo parser which proved\
well suited for the task of interfacing with distribution metadata in a human\
friendly way. If you consider code reviews human friendly, that is.\

Name:             python-distroinfo
Version:          0.6.3
Release:          %autorelease
Summary:          %{summary}
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:          Apache-2.0
URL:              https://github.com/softwarefactory-project/distroinfo
Source0:          %pypi_source
BuildArch:        noarch

%description %desc

%package -n python3-distroinfo
Summary:          %{summary}
Requires:         git-core

%description -n python3-distroinfo %{desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires %{?with_tests:-t}

%build
%pyproject_wheel

%if %{with tests}
rm -rf tests/integration
%check
%tox
%endif

%install
%pyproject_install
%pyproject_save_files -l distroinfo

%files -n python3-distroinfo -f %{pyproject_files}
%doc README.rst AUTHORS

%changelog
%autochangelog
