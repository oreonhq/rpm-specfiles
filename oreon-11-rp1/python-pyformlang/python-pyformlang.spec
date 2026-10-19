%global source0_hash e292ec8b9cfa64c26b592faf9b7cfc72c4f4b0eb0d533f045a46061e75c5ce99
Name:           python-pyformlang
Version:        1.0.11
Release:        1%{?dist}
Summary:        A python framework for formal grammars
License:        MIT
URL:            https://github.com/Aunsiels/pyformlang
Source0:        https://files.pythonhosted.org/packages/source/p/pyformlang/pyformlang-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pyformlang = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pyformlang
Summary:        A python framework for formal grammars
%description -n python3-pyformlang

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir pyformlang-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pyformlang usr/lib/python3*/site-packages/pyformlang* usr/lib64/python3*/site-packages/pyformlang* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pyformlang* usr/lib64/python3*/site-packages/pyformlang* usr/bin/*

%check

%pyproject_check_import
%pytest
%files
%files -n python3-pyformlang -f %{oreon_filedir}/python3-pyformlang.list

%changelog

%autochangelog
