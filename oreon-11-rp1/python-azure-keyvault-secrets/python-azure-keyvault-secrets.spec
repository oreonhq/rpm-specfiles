%global source0_hash 77ee2534ba651a1f306c85d7b505bc3ccee8fea77450ebafafc26aec16e5445d

%global         srcname     azure-keyvault-secrets

Name:           python-%{srcname}
Version:        4.7.0
Release:        13%{?dist}
Summary:        Microsoft Azure Key Vault Secrets Client Library for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{srcname} %{version} zip}

BuildArch:      noarch

Obsoletes:      python3-azure-sdk < 5.0.1

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros

%global _description %{expand:
Microsoft Azure Key Vault Secrets Client Library for Python}

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
Obsoletes:      python3-azure-sdk < 5.0.1
%description -n python3-%{srcname} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files azure

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
