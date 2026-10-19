%global source0_hash 2d2068fb55115807d3ac77a4ca68fa48803e84ebb0ee2340f858107a36522638
Name:           python-texttable
Version:        1.7.0
Release:        1%{?dist}
Summary:        Python module to create simple ASCII tables
License:        MIT
URL:            https://github.com/foutaise/texttable
Source0:        https://files.pythonhosted.org/packages/source/t/texttable/texttable-%{version}.tar.gz
BuildArch:      noarch
%global common_description %{expand:
Texttable is a module to generate a formatted text table, using ASCII
characters.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-texttable = %{version}-%{release}
# /oreon:deps
%description %{common_description}

%package -n python3-texttable
Summary:        Python module to create simple ASCII tables
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
%description -n python3-texttable %{common_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir texttable-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-texttable usr/lib/python3*/site-packages/texttable* usr/lib64/python3*/site-packages/texttable* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/texttable* usr/lib64/python3*/site-packages/texttable* usr/bin/*

%check

%pytest --verbose tests.py
%files
%files -n python3-texttable -f %{oreon_filedir}/python3-texttable.list

%changelog

%autochangelog
