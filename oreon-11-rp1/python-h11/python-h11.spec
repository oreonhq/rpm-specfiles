%global source0_hash 4e35b956cf45792e4caa5885e69fba00bdbc6ffafbfa020300e549b208ee5ff1
Name:           python-h11
Version:        0.16.0
Release:        1%{?dist}
Summary:        A pure-Python, bring-your-own-I/O implementation of HTTP/1.1
License:        MIT
URL:            https://github.com/python-hyper/h11
Source0:        https://files.pythonhosted.org/packages/source/h/h11/h11-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-h11 = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-h11
Summary:        A pure-Python, bring-your-own-I/O implementation of HTTP/1.1
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
%description -n python3-h11

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir h11-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-h11 usr/lib/python3*/site-packages/h11* usr/lib64/python3*/site-packages/h11* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/h11* usr/lib64/python3*/site-packages/h11* usr/bin/*

%check

%pytest h11
%files
%files -n python3-h11 -f %{oreon_filedir}/python3-h11.list

%changelog

%autochangelog
