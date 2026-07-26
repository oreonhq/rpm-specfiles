%global source0_hash f58e68eb46e1faed27e0f574a55a0455eecd7b8a5b88b85a784519ba3cff047f

%global pypi_name python_json_logger

Name:           python-json-logger
Version:        4.0.0
Release:        2%{?dist}
Summary:        A python library adding a json log formatter

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://github.com/nhairs/python-json-logger
Source:         %{pypi_source %{pypi_name}}
BuildArch:      noarch

%description
A python library adding a json log formatter

%package -n     python3-json-logger
Summary:        A python library adding a json log formatter
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-freezegun

%description -n python3-json-logger
A python library adding a json log formatter

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version} -p1
# Remove bundled egg-info
rm -rf src/%{pypi_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l pythonjsonlogger

%check
%pytest --verbose

%files -n python3-json-logger -f %{pyproject_files}

%changelog
%autochangelog
