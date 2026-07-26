%global source0_hash 699c6f3c5942f09da98cef273ffbb7403904ec43f93c0d63f10a367b4479e009

Name:           python-azure-monitor-query
Version:        1.4.0
Release:        %autorelease
Summary:        Microsoft Azure Monitor Query Client Library for Python

License:        MIT
URL:            https://github.com/Azure/azure-sdk-for-python
Source:         %{pypi_source azure-monitor-query %{version}}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
Microsoft Azure Monitor Query Client Library for Python.}

%description %_description

%package -n     python3-azure-monitor-query
Summary:        %{summary}

%description -n python3-azure-monitor-query %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n azure-monitor-query-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files azure

%check
%pyproject_check_import

%files -n python3-azure-monitor-query -f %{pyproject_files}

%changelog
%autochangelog
