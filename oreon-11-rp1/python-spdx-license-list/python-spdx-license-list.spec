%global source0_hash a5e1f4e8d9bacc7c8829091068b07668194828a82a93420b448d61f2c872eddd

%global pkgname spdx-license-list
%global srcname spdx_license_list

Name:           python-%{pkgname}
Version:        3.27.0
Release:        %autorelease
Summary:        SPDX License List as a Python dictionary
License:        MIT
URL:            https://pypi.org/project/spdx-license-list/
Source:         %{pypi_source %{srcname}}

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
Provides the SPDX License List as a Python dictionary.}

%description %_description

%package -n python3-%{pkgname}
Summary:        %{summary}

%description -n python3-%{pkgname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -L %{srcname}

%check
%pyproject_check_import

%files -n python3-%{pkgname} -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
