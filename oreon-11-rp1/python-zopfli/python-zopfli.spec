%global source0_hash bd6c6febaf8f896a161d4cd3f0d7a20399825e0d6e774bb6ea564dfb0f603408

%global pypi_name zopfli

Name:           python-zopfli
Version:        0.3.0
Release:        2%{?dist}
Summary:        Zopfli module for python
License:        Apache-2.0
URL:            https://pypi.org/project/zopfli/
Source0:        %{pypi_source %{pypi_name}}

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  zopfli-devel

%description
cPython bindings for zopfli.

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
cPython bindings for zopfli.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{version}

# remove vendored zopfli
rm -rf zopfli

%generate_buildrequires
%pyproject_buildrequires -r -x test

%build
export USE_SYSTEM_ZOPFLI=1
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files zopfli

%check
export PYTHONPATH="${PYTHONPATH:-%{buildroot}%{python3_sitearch}}"
%{python3} tests/test_zopfli.py

%files -n  python3-%{pypi_name} -f %{pyproject_files}
%license COPYING
%doc README.rst

%changelog
%autochangelog
