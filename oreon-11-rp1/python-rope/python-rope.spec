%global source0_hash abd7d50021e847c33c9b36abdea8252f8d9b42701a3af363c8da6ac5f4ac7a7b

Name:           python-rope
Version:        1.14.0
Release:        %autorelease
Summary:        Python Code Refactoring Library

%global forgeurl https://github.com/python-rope/rope
%global tag %{version}
%forgemeta

License:        LGPL-3.0-or-later
URL:            %forgeurl
Source:         %forgesource

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
Rope is the world’s most advanced open source Python refactoring
library (yes, I totally stole that tagline from Postgres).

Most Python syntax up to Python 3.10 is supported. Please file bugs and
contribute patches if you encounter gaps.}

%description %_description

%package -n python3-rope
Summary:        %summary

%description -n python3-rope %_description

%package -n python-rope-doc
Summary:        %summary documentation
Requires:       python3-rope = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n python-rope-doc %{expand:
Documentation for %{summary}.}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

# Remove linter from dev requirements
sed -i '/pytest-cov/d' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires -x dev

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l rope

%check
%pytest -r fEs

%files -n python3-rope -f %{pyproject_files}
%doc docs/README.md *.md

%files -n python-rope-doc
%doc docs/*.rst README.rst

%changelog
%autochangelog
