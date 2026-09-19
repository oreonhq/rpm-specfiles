%global source0_hash ae661e59fb837173986dd9616aec7895af7b49258b209d3d6a2f13be94641f02

%global srcname pyrpm
%global foldername python-rpm-spec

%global common_description %{expand:
Python-rpm-spec is a Python module for parsing RPM spec files. RPMs are build
from a package's sources along with a spec file. The spec file controls how the
RPM is built. This module allows you to parse spec files and gives you simple
access to various bits of information that is contained in the spec file.}

Name:           python-%{srcname}
Version:        0.16
Release:        %autorelease
Summary:        Python module for parsing RPM spec files

License:        MIT
URL:            https://github.com/bkircher/python-rpm-spec
Source0:        %url/archive/v%{version}/%{foldername}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%description %{common_description}

%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{common_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{foldername}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc AUTHORS CHANGELOG.md README.md examples/

%changelog
%autochangelog
