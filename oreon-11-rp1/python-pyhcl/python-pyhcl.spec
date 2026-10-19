%global source0_hash c47293a51ccdd25e18bb5c8c0ab0ffe355b37c87f8d6f9d3280dc41efd4740bc
%global pypi_name pyhcl
Name:           python-%{pypi_name}
Version:        0.4.5
Release:        1%{?dist}
Summary:        HCL configuration parser for Python
License:        MPL-2.0
URL:            https://github.com/virtuald/pyhcl
Source0:        https://files.pythonhosted.org/packages/source/p/python-pyhcl/python-pyhcl-%{version}.tar.gz
BuildArch:      noarch
Patch:          fix-ply-compat.patch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3dist(ply)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)
# /oreon:deps
%description
Implements a parser for HCL (HashiCorp Configuration Language) in Python.

This implementation aims to be compatible with the original Go version
of the parser.

%package -n     python3-%{pypi_name}
Summary:        HCL configuration parser for Python
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(ply)
%description -n python3-%{pypi_name}
Implements a parser for HCL (HashiCorp Configuration Language) in Python.

This implementation aims to be compatible with the original Go version
of the parser.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version} -p1
# Unbundle ply
rm -vr src/hcl/ply
echo 'ply' >> requirements.txt
sed -i -e "s/,'hcl.ply'//" setup.py
grep -rl '\.ply' | xargs -t sed -i -e 's/\.ply/ply/'

%build

%py3_build
%install
%py3_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

PYTHONPATH=%{buildroot}%{python3_sitelib} %python3 -m pytest tests
%files -f %{oreon_filedir}/main.list
%files -n python3-pyhcl -f %{oreon_filedir}/python3-pyhcl.list

%changelog

%autochangelog
