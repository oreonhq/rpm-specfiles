%global source0_hash 2f1b97e6442c02681ebe01bd84f531028a7caea1af3825000f52345c30285e0f
%bcond_without docs
Name:           python-testpath
Version:        0.6.0
Release:        1%{?dist}
Summary:        Test utilities for code working with files and commands
License:        BSD-3-Clause
URL:            https://github.com/jupyter/testpath
Source0:        https://files.pythonhosted.org/packages/source/t/testpath/testpath-0.6.0.tar.gz
BuildArch:      noarch
%if %{with docs}
%endif
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 4
BuildRequires:  python3dist(flit-core) >= 3.2.0
Requires:       python3-testpath = %{version}-%{release}
# /oreon:deps
%package -n       python3-testpath+test
Summary:        Metapackage for python3-testpath test extras
Requires:       python3-testpath = %{version}-%{release}
Provides:       python3dist(testpath[test]) = %{version}-%{release}

%description -n python3-testpath+test
Metapackage for python3-testpath test extras.

%description

%package -n     python3-testpath
Summary:        %summary
%description -n python3-testpath

%if %{with docs}
%package        doc
Summary:        %{name} documentation
%description doc
Documentation for %{name}.
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n testpath-%{version}

# The exe files are only needed on Microsoft Windows
rm -f testpath/*.exe

%build

%pyproject_wheel
%if %{with docs}
sphinx-build-3 doc html
rm -rf html/.{doctrees,buildinfo}
%endif
%install
%pyproject_install
%oreon_autofiles python3-testpath usr/lib/python3*/site-packages/testpath* usr/lib64/python3*/site-packages/testpath* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/testpath* usr/lib64/python3*/site-packages/testpath* usr/bin/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%pytest
%files
%files -n python3-testpath -f %{oreon_filedir}/python3-testpath.list
%files -n python-testpath-doc -f %{oreon_filedir}/python-testpath-doc.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.6.0-1
- Prepare for Oreon 11 (RP1)
