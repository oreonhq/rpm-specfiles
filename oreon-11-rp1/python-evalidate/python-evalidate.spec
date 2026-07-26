%global source0_hash ba2193af8151c09fb69d2dae948c0680bed9b961ea363bc88b62c1a342c5a957

%global modname evalidate

Name:           python-%{modname}
Version:        2.0.5
Release:        %autorelease
Summary:        Safe and very fast eval()'uating user-supplied python expressions

License:        MIT
URL:            https://github.com/yaroslaff/evalidate
Source:         %{url}/archive/v%{version}/%{modname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
Evalidate is simple python module for safe and very fast eval()'uating user-
supplied (possible malicious) python expressions.}

%description %_description

%package -n python3-%{modname}
Summary:        %{summary}

%description -n python3-%{modname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{modname}-%{version}
# Remove unneded shebang
sed -i -e '/^#!/,1d' evalidate/__init__.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{modname}

%check
%pytest -v

%files -n python3-%{modname} -f %{pyproject_files}
%doc README.*

%changelog
%autochangelog
