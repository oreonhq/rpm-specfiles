%global source0_hash 94ce1a209e726bce3a54266822901fa190d2029c89b52be6f5e78d7e5fb1092f

Name:           python-azure-storage-file-datalake
Version:        12.23.0
Release:        %autorelease
Summary:        Azure DataLake service client library for Python
License:        MIT
URL:            https://pypi.org/project/azure-storage-file-datalake/
Source:         %{pypi_source azure_storage_file_datalake %{version}}

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
Azure DataLake service client library for Python.}

%description %{_description}

%package -n python3-azure-storage-file-datalake
Summary:        %{summary}

%description -n python3-azure-storage-file-datalake %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n azure_storage_file_datalake-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l azure

# Like other Azure SDK packages, the tests expect Azure to be available
%check
%pyproject_check_import

%files -n python3-azure-storage-file-datalake -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
