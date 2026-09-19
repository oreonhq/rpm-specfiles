%global source0_hash dd9ffbbd69d09cb07e6e7a8cf80fd28703fdc6d3b9026f8756b49cbe3314676b

%bcond_without tests

%global _description %{expand:
Converts RELAX NG schemata in Compact syntax (rnc)
to the equivalent schema in the XML-based default
RELAX NG syntax.}

Name:           python-rnc2rng
Version:        2.7.0
Release:        9%{?dist}
Summary:        RELAX NG Compact to regular syntax conversion library

License:        MIT
URL:            https://github.com/djc/rnc2rng
Source0:        %{pypi_source rnc2rng}
BuildArch:      noarch

%description %_description

%package -n python3-rnc2rng
Summary:        %{summary}

BuildRequires:  python3-devel

%description -n python3-rnc2rng %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n rnc2rng-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files rnc2rng

%check
%if %{with tests}
%{__python3} test.py
%endif
# additional test
%pyproject_check_import

%files -n python3-rnc2rng -f %{pyproject_files}
%doc README.rst AUTHORS
%{_bindir}/rnc2rng

%changelog
%autochangelog
