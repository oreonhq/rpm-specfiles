%global source0_hash 37dd54208da7e1cd875388217d5e00ebd4179249f90fb72437e91a35459a0ad3
%global modname dateutil
Name:           python-%{modname}
Version:        2.9.0.post0
Release:        1%{?dist}
Epoch:          1
Summary:        Powerful extensions to the standard datetime module
License:        (Apache-2.0 AND BSD-3-Clause) OR BSD-3-Clause
URL:            https://github.com/dateutil/dateutil
Source0:        https://files.pythonhosted.org/packages/source/p/python-dateutil/python-dateutil-2.9.0.post0.tar.gz
Patch:        relax-setuptools_scm-requires.patch
Patch:        fix-sphinx-import.patch
%bcond tests %{undefined rhel}
BuildArch:      noarch
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) < 40.0
BuildRequires:  python3dist(setuptools-scm) < 8.0
Requires:       python3-dateutil = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-%{modname}
Summary:        %summary
Requires:       tzdata
%description -n python3-%{modname}

%package doc
Summary: API documentation for python-dateutil
%description doc
This package contains %{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{name}-%{version}

iconv --from=ISO-8859-1 --to=UTF-8 NEWS > NEWS.new
mv NEWS.new NEWS

%build

%pyproject_wheel
make -C docs html
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/dateutil* usr/lib64/python3*/site-packages/dateutil* usr/bin/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%pyproject_check_import -e dateutil.tz.win -e dateutil.tzwin
%if %{with tests}
%pytest -W ignore::pytest.PytestUnknownMarkWarning
%endif
%files
%files -n python3-dateutil -f %{oreon_filedir}/python3-dateutil.list
%files -n python-dateutil-doc -f %{oreon_filedir}/python-dateutil-doc.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1:2.9.0.post0-1
- Import
