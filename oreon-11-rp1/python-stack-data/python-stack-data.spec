%global source0_hash 836a778de4fec4dcd1dcd89ed8abff8a221f58308462e1c4aa2a3cf30148f0b9
Name:           python-stack-data
Version:        0.6.3
Release:        1%{?dist}
Summary:        Extract data from python stack frames and tracebacks for informative displays
License:        MIT
URL:            http://github.com/alexmojaki/stack_data
Source0:        https://files.pythonhosted.org/packages/source/s/stack_data/stack_data-%{version}.tar.gz
Patch:          no-typeguard.patch
Patch:          https://github.com/alexmojaki/stack_data/pull/58.patch
Patch:          fix-pygments2.patch
Patch:          fix-pygments3.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 44
BuildRequires:  python3dist(setuptools-scm[toml]) >= 3.4.3
Requires:       python3-stack-data = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-stack-data
Summary:        Extract data from python stack frames and tracebacks for informative displays
%description -n python3-stack-data

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir stack_data-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-stack-data usr/lib/python3*/site-packages/stack_data* usr/lib64/python3*/site-packages/stack_data* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/stack_data* usr/lib64/python3*/site-packages/stack_data* usr/bin/*

%check

export FIX_STACK_DATA_TESTS=1
%tox
%files
%files -n python3-stack-data -f %{oreon_filedir}/python3-stack-data.list

%changelog

%autochangelog
