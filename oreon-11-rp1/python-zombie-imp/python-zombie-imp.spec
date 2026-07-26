%global source0_hash c888321fbd942f1a3205c0923a2f21d3ed6e5ab6c2f6237abf43c147f37df97f

Name:           python-zombie-imp
Version:        0.0.4
Release:        %autorelease
Summary:        A copy of the `imp` module that was removed in Python 3.12

License:        Python-2.0.1
URL:            https://github.com/encukou/zombie-imp
Source:         %{pypi_source zombie_imp}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-test

%global _description %{expand:
A copy of the imp module that was removed in Python 3.12.
This is a compat package to ease transition to Python 3.12.
It shouldn't be used and packages using `imp` module
should use `importlib.metadata` instead.}

%description %_description

%package -n python3-zombie-imp
Summary:        %{summary}

# This package is deprecated, no new packages in Fedora can depend on it
Provides:       deprecated()

%description -n python3-zombie-imp %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n zombie_imp-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files zombie_imp imp

%check
%tox

%files -n python3-zombie-imp -f %{pyproject_files}
%doc README.*

%changelog
%autochangelog
