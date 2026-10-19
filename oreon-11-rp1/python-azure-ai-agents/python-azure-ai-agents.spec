%global source0_hash eb9d7226282d03206c3fab3f3ee0a2fc71e0ad38e52d2f4f19a92c56ed951aea
Name:           python-azure-ai-agents
Version:        1.1.0
Release:        1%{?dist}
Summary:        Azure AI Projects client library for Python
License:        MIT
URL:            https://pypi.org/project/azure-ai-agents/
Source0:        https://files.pythonhosted.org/packages/source/a/azure_ai_agents/azure_ai_agents-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-azure-ai-agents = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-azure-ai-agents
Summary:        Azure AI Projects client library for Python
%description -n python3-azure-ai-agents

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir azure_ai_agents-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-azure-ai-agents usr/lib/python3*/site-packages/azure_ai_agents* usr/lib64/python3*/site-packages/azure_ai_agents* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/azure_ai_agents* usr/lib64/python3*/site-packages/azure_ai_agents* usr/bin/*

%check

%pyproject_check_import -e "azure.ai.agents.telemetry"
%files
%files -n python3-azure-ai-agents -f %{oreon_filedir}/python3-azure-ai-agents.list

%changelog

%autochangelog
