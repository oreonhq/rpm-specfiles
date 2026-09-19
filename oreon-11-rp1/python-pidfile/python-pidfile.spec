%global source0_hash 1e1097df41bc75f574599ffef89e8b20eff1bdfc9191d3ed264cc2dae95429d0

%global module_name pidfile
%global pypi_name python-%{module_name}
Name:			%{pypi_name}
Version:		3.0.0
Release:		16%{?dist}
Summary:		Python context manager for managing pid files
License:		MIT
URL:			https://pypi.org/project/python-pidfile
Source0:		%pypi_source
Source1:		https://raw.githubusercontent.com/mosquito/python-pidfile/master/LICENSE
BuildArch:		noarch

%global _description %{expand:
Python context manager for managing pid files.}

%description %_description

%package -n python3-%{module_name}
Summary:		%{summary}

BuildRequires:	python3-devel

%description -n python3-%{module_name} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup %{name}-%{version}
cp -p %{SOURCE1} .

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files %{module_name}

%check
%pyproject_check_import

%files -n python3-pidfile -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
