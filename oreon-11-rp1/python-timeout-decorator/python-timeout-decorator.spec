%global source0_hash 6a2f2f58db1c5b24a2cc79de6345760377ad8bdc13813f5265f6c3e63d16b3d7

%bcond_without tests
%global srcname timeout-decorator

Name:           python-%{srcname}
Version:        0.5.0
Release:        %autorelease
Summary:        Timeout decorator for Python

License:        MIT
URL:            https://github.com/pnpnpn/timeout-decorator
Source0:        %{pypi_source}

BuildArch:      noarch

%description
A python module which provides a timeout decorator.

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel

%description -n python3-%{srcname}
A python module which provides a timeout decorator.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files timeout_decorator

%if %{with tests}
%check
%pyproject_check_import timeout_decorator
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
