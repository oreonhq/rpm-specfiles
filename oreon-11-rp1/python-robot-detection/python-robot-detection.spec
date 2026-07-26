%global source0_hash 9fa0423a890fd5856e5494076ba6e67abd2f4173d91c8b292819dfaa815b5060

%global srcname robot-detection

Name:           python-%{srcname}
Version:        0.4
%global gh_ver %{version}.0
Release:        %autorelease
Summary:        Library for detecting bot HTTP UA headers
License:        GPL-3.0-or-later
URL:            https://github.com/amandasaurus/robot-detection
# PyPI source does not have tests and license text
# Source0:        %%{pypi_source %%{srcname}}
Source0:        %{url}/archive/v%{gh_ver}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python3dist(pytest)

%global _description %{expand:
robot_detection is a python module to detect if a given HTTP User Agent is a web
crawler. It uses the list of registered robots from http://www.robotstxt.org:
[Robots Database](http://www.robotstxt.org/db.html).}

%description %{_description}

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}

%description -n python%{python3_pkgversion}-%{srcname} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{gh_ver}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files robot_detection

%check
%pytest -v tests.py

%files -n  python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%license LICENCE
%doc README.md

%changelog
%autochangelog
