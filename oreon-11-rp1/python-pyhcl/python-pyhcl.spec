%global source0_hash c47293a51ccdd25e18bb5c8c0ab0ffe355b37c87f8d6f9d3280dc41efd4740bc

%global pypi_name pyhcl

Name:           python-%{pypi_name}
Version:        0.4.5
Release:        12%{?dist}
Summary:        HCL configuration parser for Python

License:        MPL-2.0
URL:            https://github.com/virtuald/pyhcl
Source0:        %{pypi_source}
BuildArch:      noarch

# Fix compatibility with the latest ply commit
# Resolved upstream: https://github.com/virtuald/pyhcl/pull/93
Patch:          fix-ply-compat.patch

%description
Implements a parser for HCL (HashiCorp Configuration Language) in Python.

This implementation aims to be compatible with the original Go version
of the parser.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
# Test requires:
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

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} %python3 -m pytest tests

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{_bindir}/hcltool
%{python3_sitelib}/hcl/
%{python3_sitelib}/pyhcl-*.egg-info/

%changelog
%autochangelog
