%global source0_hash f88beb3da5b5c38b9890469de67d0cb0f9d494b78b106ca1845f96c10b91c4ac
Name:           python-socksio
Version:        1.0.0
Release:        1%{?dist}
Summary:        Client-side sans-I/O SOCKS proxy implementation
License:        MIT
URL:            https://github.com/sethmlarson/socksio
Source0:        https://files.pythonhosted.org/packages/source/s/socksio/socksio-%{version}.tar.gz
Patch:          0001-Unpin-flit-core-dependency.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 3
BuildRequires:  python3dist(flit-core) >= 2
Requires:       python3-socksio = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-socksio
Summary:        Client-side sans-I/O SOCKS proxy implementation
%description -n python3-socksio

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n socksio-%{version} -p 1
# drop coverage addopts
rm pytest.ini

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-socksio usr/lib/python3*/site-packages/socksio* usr/lib64/python3*/site-packages/socksio* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/socksio* usr/lib64/python3*/site-packages/socksio* usr/bin/*

%check

%pytest
%files
%files -n python3-socksio -f %{oreon_filedir}/python3-socksio.list

%changelog

%autochangelog
