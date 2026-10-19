%global source0_hash 30bd9c329ba465e5b6c5e14ab008260c53fac61e138040b34b19489f3971d7aa
Name:           python-repomd
Version:        0.2.1
Release:        1%{?dist}
Summary:        Library for reading dnf/yum repositories
License:        MIT
URL:            https://github.com/carlwgeorge/repomd
Source0:        https://files.pythonhosted.org/packages/source/r/repomd/repomd-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-repomd = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-repomd
Summary:        Library for reading dnf/yum repositories
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
%description -n python3-repomd

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n repomd-%{version}
rm setup.cfg

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-repomd usr/lib/python3*/site-packages/repomd* usr/lib64/python3*/site-packages/repomd* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/repomd* usr/lib64/python3*/site-packages/repomd* usr/bin/*

%check

%pytest --verbose
%files
%files -n python3-repomd -f %{oreon_filedir}/python3-repomd.list

%changelog

%autochangelog
