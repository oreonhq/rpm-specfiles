%global source0_hash 18cc0a45bc22232f4616081190307c0ec5e34c70b09d37f5989ede5a8d20de93

%global         pypi_version 0.3a3

Summary:        Debug plugin for python-llm
Name:           python-llm-echo
Version:        0.5a0
Release:        1%{?dist}
License:        Apache-2.0
URL:            https://github.com/simonw/llm-echo
Source:         https://github.com/simonw/llm-echo/archive/%{pypi_version}/llm-echo-%{pypi_version}.tar.gz
Patch:          python-llm-0.3a3-format-fix.patch
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-asyncio
%global _description \
%{expand:
Debug plugin for LLM. Adds a model which echos its input without hitting
an API or executing a local LLM.
}
%description %_description

%package     -n python3-llm-echo
Summary:        %{summary}
%description -n python3-llm-echo %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n llm-echo-%{pypi_version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files llm_echo

%check
%pyproject_check_import
%pytest

%files -n python3-llm-echo -f %{pyproject_files}

%changelog
%autochangelog
