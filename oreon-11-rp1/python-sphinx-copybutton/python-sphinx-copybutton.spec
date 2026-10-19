%global source0_hash 4cf17c82fb9646d1bc9ca92ac280813a3b605d8c421225fd9913154103ee1fbd
Name:           python-sphinx-copybutton
Version:        0.5.2
Release:        1%{?dist}
Summary:        Add a copy button to code cells in Sphinx docs
License:        MIT
URL:            https://sphinx-copybutton.readthedocs.io/en/latest/
Source0:        https://files.pythonhosted.org/packages/source/s/sphinx-copybutton/sphinx-copybutton-%{version}.tar.gz
BuildArch:      noarch
Obsoletes:      %{name}-doc < 0.3.2
Provides:       %{name}-doc = %{version}-%{release}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-sphinx-copybutton = %{version}-%{release}
# /oreon:deps
%description

%package     -n python3-sphinx-copybutton
Summary:        Add a copy button to code cells in Sphinx docs
%description -n python3-sphinx-copybutton

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir sphinx-copybutton-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-sphinx-copybutton usr/lib/python3*/site-packages/sphinx_copybutton* usr/lib64/python3*/site-packages/sphinx_copybutton* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/sphinx_copybutton* usr/lib64/python3*/site-packages/sphinx_copybutton* usr/bin/*

%check

%pyproject_check_import
%files
%files -n python3-sphinx-copybutton -f %{oreon_filedir}/python3-sphinx-copybutton.list

%changelog

%autochangelog
