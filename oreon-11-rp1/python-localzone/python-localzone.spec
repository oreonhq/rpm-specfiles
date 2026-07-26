%global source0_hash 6ef39de76dc59a0c6c13ae85fe85bf3a58323cab568b47cb51b435d42a1d39e6

%global pypi_name  localzone
%global forgeurl   https://github.com/ags-slc/localzone
Version:           0.9.8
%forgemeta

Name:           python-%{pypi_name}
Release:        14%{?dist}
Summary:        A simple library for managing DNS zones

License:        BSD
URL:            %{forgeurl}
# pypi releases don't contain necessary data to run the tests
Source0:        %{forgesource}

# Compatibility with dnspython 2.8.0
Patch:          https://github.com/ags-slc/localzone/pull/6.patch

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
Comprehensive, low-level DNS toolkits can be cumbersome for the more common
zone management tasks–especially those related to making simple changes to
zone records. They can also come with a steep learning curve.
Enter localzone: a simple library for managing DNS zones. While localzone may
be a low-calorie library, it’s stuffed full of everything that a hungry
hostmaster needs.
}

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%tox

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog
