%global source0_hash 493d43478ec60838f2e987b3ef8b7077c7ff50747edf5bf82721c9b2de783977

%global srcname colcon-ros-domain-id-coordinator

Name:           python-%{srcname}
Version:        0.2.4
Release:        4%{?dist}
Summary:        Extension for colcon to coordinate different DDS domain IDs

License:        Apache-2.0
URL:            https://github.com/colcon/colcon-ros-domain-id-coordinator
Source0:        https://github.com/colcon/colcon-ros-domain-id-coordinator/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%global _description %{expand:
An extension for colcon-core to coordinate different DDS domain IDs for
concurrently running tasks.}

%description %_description

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel

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
%pyproject_save_files -l colcon_ros_domain_id_coordinator

%check
# The package has no non-linter tests right now
%pyproject_check_import

%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
