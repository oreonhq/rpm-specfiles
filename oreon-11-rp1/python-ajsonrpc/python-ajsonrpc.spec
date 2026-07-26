%global source0_hash 791bac18f0bf0dee109194644f151cf8b7ff529c4b8d6239ac48104a3251a19f

%global pypi_name ajsonrpc

Name:           python-%{pypi_name}
Version:        1.2.0
Release:        %autorelease
Summary:        Lightweight JSON-RPC 2.0 protocol implementation and asynchronous server

License:        MIT
URL:            https://github.com/pavlov99/ajsonrpc
Source0:        %{pypi_source}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%global _description %{expand:
Lightweight JSON-RPC 2.0 protocol implementation and asynchronous server
powered by asyncio. This library is a successor of json-rpc and written by the
same team.}

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE.txt
%doc README.md
%{_bindir}/async-json-rpc-server

%changelog
%autochangelog
