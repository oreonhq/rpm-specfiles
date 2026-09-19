%global source0_hash 30a11aafacea34f8b160fbdc35254c9029c7e325267874e3c68f6bdbcd6ed2c3

# tests are enabled by default
%bcond_without tests

%global         srcname     applicationinsights

Name:           python-%{srcname}
Version:        0.11.9
Release:        %autorelease
Summary:        Python support for Azure Application Insights API
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{srcname} %{version}}

BuildArch:      noarch

Epoch:          1

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3-test
%endif

%global _description %{expand:
This project extends the Application Insights API surface to support Python}

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
Obsoletes:      python3-azure-sdk < 5.0.1

%description -n python3-%{srcname} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

# Fix incorrect line endings in the README.
sed -i 's/\r$//' README.rst

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files applicationinsights

%if %{with tests}
%check
PYTHONPATH=%{buildroot}/%{python3_sitelib} \
    %{__python3} -m unittest discover ./tests/
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE.txt
%doc README.rst

%changelog
%autochangelog
