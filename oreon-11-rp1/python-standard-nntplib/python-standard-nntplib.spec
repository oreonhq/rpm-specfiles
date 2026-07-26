%global source0_hash 27d7f9853bf2f1a67111478d919fba297f9a4fb2b6785fbdea4d9f1cef967680

%bcond tests 1

%if 0%{?fedora} == 42
%bcond old_setuptools 1
%else
%bcond old_setuptools 0
%endif

Name:           python-standard-nntplib
Version:        3.13.0
Release:        %autorelease
Summary:        Standard library nntplib redistribution

License:        PSF-2.0
URL:            https://github.com/youknowone/python-deadlib
Source:         %{pypi_source standard_nntplib}

BuildArch:      noarch
BuildRequires:  python3-devel
%if %{with old_setuptools}
BuildRequires:  sed
%endif
%if %{with tests}
BuildRequires:  python3dist(pytest)
BuildRequires:  python3-test
%endif

%global _description %{expand:
Python is moving forward! Python finally started to remove dead batteries. For
more information, see PEP 594.

If your project depends on nntplib, which has been removed from Python 3.13,
here is the redistribution.}

%description %_description

%package -n     python3-standard-nntplib
Summary:        %{summary}

%description -n python3-standard-nntplib %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n standard_nntplib-%{version}
%if %{with old_setuptools}
sed -i 's:setuptools>=75.0:setuptools>=74.0:' pyproject.toml
%endif

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l nntplib

%check
%pyproject_check_import
%if %{with tests}
# certfile not shipped
%pytest -v \
  --deselect tests/test_nntplib.py::LocalServerTests::test_starttls
%endif

%files -n python3-standard-nntplib -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
