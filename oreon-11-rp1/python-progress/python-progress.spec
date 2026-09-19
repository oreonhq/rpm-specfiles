%global source0_hash c9c86e98b5c03fa1fe11e3b67c1feda4788b8d0fe7336c2ff7d5644ccfba34cd

%global pypi_name progress

Name:           python-%{pypi_name}
Version:        1.6
Release:        20%{?dist}
Summary:        Easy to use progress bars

License:        ISC
URL:            http://github.com/verigak/progress/
Source0:        %{pypi_source %{pypi_name}}
BuildArch:      noarch

BuildRequires:  python3-devel
%if %{defined el8}
BuildRequires:  python3-setuptools
%endif

Patch1:         0001-fixup-moving-average-window.patch

%global _description %{expand:
Collection of easy to use progress bars and spinners.}

%description %_description

%package -n     python3-%{pypi_name}
Summary:        Easy to use progress bars

%description -n python3-%{pypi_name} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{version}

%if %{undefined el8}
%generate_buildrequires
%pyproject_buildrequires
%endif

%build
%if %{defined el8}
%py3_build
%else
%pyproject_wheel
%endif

%install
%if %{defined el8}
%py3_install
%else
%pyproject_install
%pyproject_save_files -l %{pypi_name}
%endif

%check
%if %{defined el8}
%py3_check_import %{pypi_name}
%else
%pyproject_check_import
%endif

%files -n python3-%{pypi_name} %{!?el8:-f %{pyproject_files}}
%doc README.rst
%if %{defined el8}
%license LICENSE
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
%endif

%changelog
%autochangelog
