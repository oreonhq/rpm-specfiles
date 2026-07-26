%global source0_hash 53cefd9d65990f6fe59c0378cad8ea1b9df8f770d2e8bd9d8762edae033be80a

%global pkg_name httpagentparser

Name:           python-%{pkg_name}
Version:        1.9.5
Release:        14%{?dist}
Summary:        Extracts OS Browser etc information from http user agent string

License:        MIT
URL:            https://github.com/shon/httpagentparser
Source0:        %{pypi_source httpagentparser}
BuildArch:      noarch

BuildRequires:  python3-devel

%description
Extracts OS Browser etc information from http user agent string.

%package -n python3-%{pkg_name}
Summary:        Extracts OS Browser etc information from http user agent string

%description -n python3-%{pkg_name}
Extracts OS Browser etc information from http user agent string.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pkg_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files httpagentparser

%check
%py3_check_import httpagentparser

%files -n python3-%{pkg_name}  -f %{pyproject_files}
%license LICENSE.txt
%doc README.rst

%changelog
%autochangelog
