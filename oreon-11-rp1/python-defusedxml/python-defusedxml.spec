%global source0_hash 1bb3032db185915b62d7c6209c5a8792be6a32ab2fedacc84e01b52c51aa3e69
Name:           python-defusedxml
Version:        0.7.1
Release:        1%{?dist}
Summary:        XML bomb protection for Python stdlib modules
License:        PSF-2.0
URL:            https://github.com/tiran/defusedxml
Source0:        https://files.pythonhosted.org/packages/source/d/defusedxml/defusedxml-%{version}.tar.gz
Patch:          drop-makeSuite.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-defusedxml = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-defusedxml
Summary:        XML bomb protection for Python stdlib modules
%description -n python3-defusedxml

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir defusedxml-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-defusedxml usr/lib/python3*/site-packages/defusedxml* usr/lib64/python3*/site-packages/defusedxml* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/defusedxml* usr/lib64/python3*/site-packages/defusedxml* usr/bin/*

%check

%{py3_test_envvars} %{python3} tests.py
%files
%files -n python3-defusedxml -f %{oreon_filedir}/python3-defusedxml.list

%changelog

%autochangelog
