%global source0_hash e879da2b9301e82cfc3e60d805630487ac2f7ab17492f4f5ba5aaba94fe56c29
Name:           python-lsprotocol
Version:        2025.0.0
Release:        1%{?dist}
Summary:        Python implementation of the Language Server Protocol
License:        MIT
URL:            https://pypi.org/project/lsprotocol/
Source0:        https://files.pythonhosted.org/packages/source/l/lsprotocol/lsprotocol-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 4
BuildRequires:  python3dist(flit-core) >= 3.2
Requires:       python3-lsprotocol = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-lsprotocol
Summary:        Python implementation of the Language Server Protocol
# oreon:reqs
Requires:       python3dist(attrs) >= 21.3.0
Requires:       python3dist(cattrs)
# /oreon:reqs
%description -n python3-lsprotocol

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir lsprotocol-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-lsprotocol usr/lib/python3*/site-packages/lsprotocol* usr/lib64/python3*/site-packages/lsprotocol* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/lsprotocol* usr/lib64/python3*/site-packages/lsprotocol* usr/bin/*

%check

%pyproject_check_import
%files
%files -n python3-lsprotocol -f %{oreon_filedir}/python3-lsprotocol.list

%changelog

%autochangelog
