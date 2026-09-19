%global source0_hash 77a214c2200b537521bb7b102d4cebc2764946d52ae50d822bd46c43ba2ca9d3

%global srcname flake8-deprecated

Name:           python-%{srcname}
Version:        2.3.0
Release:        2%{?dist}
Summary:        Flake8 plugin that warns about deprecated method calls

License:        GPL-2.0-only
URL:            https://github.com/gforcada/flake8-deprecated
Source0:        https://github.com/gforcada/flake8-deprecated/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%global _description %{expand:
No language, library or framework ever get everything right from the very
beginning. The project evolves, new features are added/changed/removed.

This means that projects relying on them must keep an eye on what's currently
best practices.

This flake8 plugin helps you keeping up with method deprecations and giving
hints about what they should be replaced with.}

%description %_description

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel

%description -n python%{python3_pkgversion}-%{srcname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -x test

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l flake8_deprecated

%check
%pytest run_tests.py

%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%doc CHANGES.rst README.rst

%changelog
%autochangelog
