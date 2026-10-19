%global source0_hash ff70335d468e7eb6ec65b95b99d3a2836546063f63acc5171de367e834932a81
%bcond_without tests
Name:           python-six
Version:        1.17.0
Release:        1%{?dist}
Summary:        Python 2 and 3 compatibility utilities
License:        MIT
URL:            https://github.com/benjaminp/six
Source0:        https://files.pythonhosted.org/packages/source/s/six/six-1.17.0.tar.gz
BuildArch:      noarch
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-six = %{version}-%{release}
# /oreon:deps
%description

%package -n python%{python3_pkgversion}-six
Summary:        Python 2 and 3 compatibility utilities
%description -n python%{python3_pkgversion}-six

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir six-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/six* usr/lib64/python3*/site-packages/six* usr/bin/*

%check

%pyproject_check_import
%if %{with tests}
%pytest
%endif
%files
%files -n python3-six -f %{oreon_filedir}/python3-six.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.17.0-1
- Import
