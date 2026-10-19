%global source0_hash adc1976c0106919e9338db20102b91009256dcfec924a66928d7297026f72477
Name:           pycmd
Version:        1.2
Release:        1%{?dist}
Summary:        Tools for managing/searching Python related files
License:        MIT
URL:            https://pypi.python.org/pypi/pycmd
Source0:        https://pypi.python.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pycmd = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-pycmd
Summary:        Tools for managing/searching Python related files
Requires:       python3-setuptools
Requires:       python3-py >= 1.4.0
%description -n python3-pycmd

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
find %{buildroot}%{python3_sitelib} -name '*.py' \
     -exec sed -i -e '1{/^#!/d}' {} \;
%oreon_autofiles python3-pycmd usr/lib/python3*/site-packages/pycmd* usr/lib64/python3*/site-packages/pycmd* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pycmd* usr/lib64/python3*/site-packages/pycmd* usr/bin/*

%files
%files -n python3-pycmd -f %{oreon_filedir}/python3-pycmd.list

%changelog

%autochangelog
