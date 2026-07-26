%global source0_hash b5f03024ccf0fd543fbe0f5abcc74e45b15eccc1c71ab87fc71c63061d9fd63c

Name:           python-azure-ai-projects
Version:        1.0.0
Release:        %autorelease
Summary:        Azure AI Projects client library for Python
License:        MIT
URL:            https://pypi.org/project/azure-ai-projects/
Source:         %{pypi_source azure_ai_projects %{version}}

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
The AI Projects client library is part of the Azure AI Foundry SDK, and
provides easy access to resources in your Azure AI Foundry Project.}

%description %{_description}

%package -n python3-azure-ai-projects
Summary:        %{summary}

%description -n python3-azure-ai-projects %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n azure_ai_projects-%{version}

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

%files -n python3-azure-ai-projects -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
