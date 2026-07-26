%global source0_hash 90f9b0234e771fda08bf56103c43a4f4ac08bf79334d9dac7bb1b6f37baadd25

Name:           python-azure-storage-file-share
Version:        12.24.0
Release:        %autorelease
Summary:        Azure Storage File Share client library for Python
License:        MIT
URL:            https://pypi.org/project/azure-storage-file-share/
Source:         %{pypi_source azure_storage_file_share %{version}}

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
Azure File Share storage offers fully managed file shares in the cloud that are
accessible via the industry standard Server Message Block (SMB) protocol. Azure
file shares can be mounted concurrently by cloud or on-premises deployments of
Windows, Linux, and macOS. Additionally, Azure file shares can be cached on
Windows Servers with Azure File Sync for fast access near where the data is
being used.}

%description %{_description}

%package -n python3-azure-storage-file-share
Summary:        %{summary}

%description -n python3-azure-storage-file-share %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n azure_storage_file_share-%{version}

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

%files -n python3-azure-storage-file-share -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
