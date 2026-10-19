%global source0_hash bfbb479c53d0a696ea7402601f4e693c97b0367837c8898bc6471adfca37a6bd
Name:           python-toposort
Version:        1.10
Release:        1%{?dist}
Summary:        Topological sort implementation
License:        Apache-2.0
URL:            https://pypi.org/project/toposort/
Source0:        https://files.pythonhosted.org/packages/69/19/8e955d90985ecbd3b9adb2a759753a6840da2dff3c569d412b2c9217678b/toposort-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 42
Requires:       python3-toposort = %{version}-%{release}
# /oreon:deps
%description
A topological sort for python.

%package -n python3-toposort
Summary:        Topological sort implementation
%description -n python3-toposort
A topological sort for python.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir toposort-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-toposort usr/lib/python3*/site-packages/toposort* usr/lib64/python3*/site-packages/toposort* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/toposort* usr/lib64/python3*/site-packages/toposort* usr/bin/*

%files
%files -n python3-toposort -f %{oreon_filedir}/python3-toposort.list
