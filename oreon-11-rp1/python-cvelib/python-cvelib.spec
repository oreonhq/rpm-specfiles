%global source0_hash 371984737f29b8e5e433febd07a52eb7d73b4ea9628b79f7b6ce10468feccb3d
Name:           python-cvelib
Version:        1.8.0
Release:        1%{?dist}
Summary:        A library and command line interface for the CVE Project services
License:        MIT
URL:            https://github.com/RedHatProductSecurity/cvelib
Source0:        https://files.pythonhosted.org/packages/source/c/cvelib/cvelib-%{version}.tar.gz
BuildArch:      noarch
Provides: bundled(cve-schema)
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-cvelib = %{version}-%{release}
# /oreon:deps
%package -n       python3-cvelib+test
Summary:        Metapackage for python3-cvelib test extras
Requires:       python3-cvelib = %{version}-%{release}
Provides:       python3dist(cvelib[test]) = %{version}-%{release}

%description -n python3-cvelib+test
Metapackage for python3-cvelib test extras.

%package -n       python3-cvelib+dev
Summary:        Metapackage for python3-cvelib dev extras
Requires:       python3-cvelib = %{version}-%{release}
Provides:       python3dist(cvelib[dev]) = %{version}-%{release}

%description -n python3-cvelib+dev
Metapackage for python3-cvelib dev extras.

%description

%package -n     python3-cvelib
Summary:        A library and command line interface for the CVE Project services
# oreon:reqs
Requires:       python3dist(click) >= 7.1.2
Requires:       python3dist(jsonschema) >= 4.7.2
Requires:       python3dist(requests) >= 2.32.0
# /oreon:reqs
%description -n python3-cvelib

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n cvelib-%{version}
sed -i 's:"collective.checkdocs",::' pyproject.toml

%build

%pyproject_wheel
%install
%pyproject_install
mkdir -p %{buildroot}/%{_mandir}
cp -r --preserve=timestamps man %{buildroot}/%{_mandir}/man1
rm -rf %{buildroot}%{python3_sitelib}/tests
%oreon_autofiles python3-cvelib usr/lib/python3*/site-packages/cvelib* usr/lib64/python3*/site-packages/cvelib* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/cvelib* usr/lib64/python3*/site-packages/cvelib* usr/bin/*

%check

%pyproject_check_import
%files
%files -n python3-cvelib -f %{oreon_filedir}/python3-cvelib.list

%changelog

%autochangelog
