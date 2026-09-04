%global source0_hash 4076f1368ea0ed88ff9c19255b5215cf59e92662df040e32698205ab66cc168d

%global srcname colcon-meson

Name:           python-%{srcname}
Version:        0.5.0
Release:        1%{?dist}
Summary:        Extension for colcon to support Meson packages

License:        Apache-2.0
URL:            https://github.com/colcon/colcon-meson
Source0:        https://github.com/colcon/colcon-meson/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%global _description %{expand:
A colcon extension for building Meson packages.}

%description %_description

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest

%description -n python%{python3_pkgversion}-%{srcname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l colcon_meson

%check
%pytest -k 'not linter' test
%pyproject_check_import colcon_meson

%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
