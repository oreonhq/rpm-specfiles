%global source0_hash 28981dcbc72193ace62952431e8963656d708f93b86c43a4bb55f454cdeff860

%global srcname colcon-parallel-executor

Name:           python-%{srcname}
Version:        0.4.0
Release:        4%{?dist}
Summary:        Extension for colcon to process packages in parallel

License:        Apache-2.0
URL:            https://colcon.readthedocs.io
Source0:        https://github.com/colcon/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
An extension for colcon-core to process packages in parallel.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest

%description -n python%{python3_pkgversion}-%{srcname}
An extension for colcon-core to process packages in parallel.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l colcon_parallel_executor

%check
%pytest test -m 'not linter'

%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
