%global source0_hash acc7eb92bd5c554ed577249c6978450a4feda0aa6f01470152b3a7b382a02132

%define		realname PyICU
Name:		pyicu
Version:	2.14
Release:	9%{?dist}
Summary:	Python extension wrapping the ICU C++ libraries

License:	MIT
URL:		https://pypi.org/project/PyICU/
Source0:	https://files.pythonhosted.org/packages/source/P/%{realname}/%{realname}-%{version}.tar.gz

BuildRequires:	gcc-c++
BuildRequires:	libicu-devel
BuildRequires:	python3-devel
%if 0%{?fedora}
BuildRequires:	python3-pytest
%endif
BuildRequires:	python3-setuptools
BuildRequires:	python3-six

%global _description\
PyICU is a python extension implemented in C++ that wraps the C/C++ ICU\
library.

%description %_description

%package -n python3-pyicu
Summary: Python 3 extension wrapping the ICU C++ libraries

%description -n python3-pyicu %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files icu

%if 0%{?fedora}
%check
%pytest
%endif

%files -n python3-pyicu -f %{pyproject_files}
%doc LICENSE

%changelog
%autochangelog
