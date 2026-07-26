%global source0_hash 891dcbe54f55397d82d289c459de0ea897e103b86a3f1fad0fdb1895922a75ff

%global pypi_name ollama

Name:           python-%{pypi_name}
Version:        0.4.7
Release:        %autorelease
Summary:        The official Python client for Ollama

License:        MIT
URL:            https://ollama.com
Source:         %{pypi_source ollama}

BuildArch:      noarch
# Ollama only on x86_64
ExclusiveArch:  x86_64

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest-httpserver)
BuildRequires:  python3dist(pytest-asyncio)

%global _description %{expand:
The Ollama Python library provides the easiest way to integrate
Python 3.8+ projects with Ollama.}

%description %_description

%package -n     python3-ollama
Summary:        %{summary}

%description -n python3-ollama %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n ollama-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pyproject_check_import

%files -n python3-ollama -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
