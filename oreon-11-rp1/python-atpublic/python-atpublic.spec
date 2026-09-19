%global source0_hash 61fa780a1d1e35a0585c795a381ec209d89a260b63fbb516da4bf00905b2889e

%global debug_package %{nil}
%global _description \
This is a very simple decorator and function which populates a  \
module's __all__ and optionally the module globals.  \
This provides both a pure-Python implementation and a C implementation.  \
It is proposed that the C implementation be added to built-ins for  \
Python 3.6.

Name:           python-atpublic
Version:        7.0.0
Release:        2%{?dist}
Summary:        Decorator for populating a Python module's __all__

License:        Apache-2.0
URL:            https://gitlab.com/warsaw/public
Source:         %pypi_source atpublic

BuildRequires:  gcc
BuildRequires:  python3-devel
# for tests
BuildRequires:  python3-pytest
BuildRequires:  python3-sybil

%description %{_description}

%package -n python3-atpublic
Summary:        %{summary}
Requires:       python3-setuptools

%description -n python3-atpublic %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n public-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
export ATPUBLIC_BUILD_EXTENSION=1
%pyproject_wheel

%install
export ATPUBLIC_BUILD_EXTENSION=1
%pyproject_install
%pyproject_save_files public

%check
%pytest

%files -n python3-atpublic -f %{pyproject_files}
%license LICENSE
%doc README.rst docs/

%changelog
%autochangelog
