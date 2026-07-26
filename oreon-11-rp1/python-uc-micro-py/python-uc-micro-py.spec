%global source0_hash 3225a494ec63b39a3542d3e2b88ed2bd85b41aad1e926c3d4453e5fae57efc45

Name:           python-uc-micro-py
Version:        2.0.0
Release:        %autorelease
Summary:        Micro subset of Unicode data files for linkify-it.py projects

License:        MIT
URL:            https://github.com/tsutsu3/uc.micro-py
VCS:            git:%{url}.git
Source:         %{url}/archive/v%{version}/uc.micro-py-%{version}.tar.gz

BuildArch:      noarch
BuildSystem:    pyproject
BuildOption(generate_buildrequires): -x test
BuildOption(install): -l uc_micro

%global _description %{expand:Micro subset of Unicode data files for linkify-it.py projects.  This is a
Python port of uc.micro (https://github.com/markdown-it/uc.micro).}

%description
%_description

%package     -n python3-uc-micro-py
Summary:        Micro subset of Unicode data files for linkify-it.py projects

%description -n python3-uc-micro-py
%_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n uc.micro-py-%{version}

# Do not run coverage tools in RPM builds
sed -i 's/, "coverage", "pytest-cov"//' pyproject.toml

%check
%pytest -v

%files -n python3-uc-micro-py -f %{pyproject_files}
%doc CHANGELOG.md README.md

%changelog
%autochangelog
