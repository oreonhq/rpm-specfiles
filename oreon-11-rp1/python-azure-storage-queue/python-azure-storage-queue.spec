%global source0_hash 4e01dcae5aefd0c463f7bae5c75c8a91f955c893f14ed7590fc0cd447ac4666d

Name:           python-azure-storage-queue
Version:        12.15.0
Release:        %autorelease
Summary:        Azure Storage Queues client library for Python
License:        MIT
URL:            https://pypi.org/project/azure-storage-queue/
Source:         %{pypi_source azure_storage_queue %{version}}

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
Azure Queue storage is a service for storing large numbers of messages that can
be accessed from anywhere in the world via authenticated calls using HTTP or
HTTPS. A single queue message can be up to 64 KiB in size, and a queue can
contain millions of messages, up to the total capacity limit of a storage
account.}

%description %{_description}

%package -n python3-azure-storage-queue
Summary:        %{summary}

%description -n python3-azure-storage-queue %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n azure_storage_queue-%{version}

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

%files -n python3-azure-storage-queue -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
