%global source0_hash 6db2cd1b5ab7ff52c6fe8df473d5518b29fe5f0e5ec267fc731272a71e46a5ea
Name:           python-comm
Version:        0.2.3
Release:        1%{?dist}
Summary:        Jupyter Python Comm implementation, for usage in ipykernel, xeus-python etc.
License:        BSD-3-Clause
URL:            https://github.com/ipython/comm
Source0:        https://github.com/ipython/comm/archive/v%{version}/comm-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(hatchling) >= 1.10
Requires:       python3-comm = %{version}-%{release}
# /oreon:deps
%package -n       python3-comm+test
Summary:        Metapackage for python3-comm test extras
Requires:       python3-comm = %{version}-%{release}
Provides:       python3dist(comm[test]) = %{version}-%{release}

%description -n python3-comm+test
Metapackage for python3-comm test extras.

%description

%package -n     python3-comm
Summary:        Jupyter Python Comm implementation, for usage in ipykernel, xeus-python etc.
%description -n python3-comm

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir comm-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-comm usr/lib/python3*/site-packages/comm* usr/lib64/python3*/site-packages/comm* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/comm* usr/lib64/python3*/site-packages/comm* usr/bin/*

%check

%pytest
%files
%files -n python3-comm -f %{oreon_filedir}/python3-comm.list

%changelog

%autochangelog
