%global source0_hash c6341abda6098813f8fa625acd1e925410a17a8a1c7aaabdf975bb7cecb14edf

%global         srcname     azure-functions-devops-build

Name:           python-%{srcname}
Version:        0.0.22
Release:        19%{?dist}
Summary:        Python package for integrating Azure Functions with Azure DevOps
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %pypi_source

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros

%global _description %{expand:
Python package for integrating Azure Functions with Azure DevOps}

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
Obsoletes:      python3-azure-sdk < 5.0.1
%description -n python3-%{srcname} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

# Fix incorrect line endings in the README.
sed -i 's/\r$//' README.md

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files azure_functions_devops_build

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
