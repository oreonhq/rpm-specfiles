%global source0_hash 5778cf62fe75dcfc32f096426b9554dadd590061c7fa47c2292fe23b8d35517e
Name:           python-nodeenv
Version:        1.11.0
Release:        1%{?dist}
Summary:        Node.js virtual environment builder
License:        BSD-3-Clause
URL:            https://github.com/ekalinin/nodeenv
Source0:        https://github.com/ekalinin/nodeenv/archive/%{version}/nodeenv-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-nodeenv = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-nodeenv
Summary:        Node.js virtual environment builder
%description -n python3-nodeenv

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n nodeenv-%{version} -p1

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -r -i "s@'coverage', 'run', '-p',@'%{python3}',@" tests/nodeenv_test.py

# Remove unwanted shebangs from files that will not have the executable bit set
sed -r -i '1{/^#!/d}' nodeenv.py

%build

%pyproject_wheel
%install
%pyproject_install
install -d '%{buildroot}%{_mandir}/man1'
PYTHONPATH='%{buildroot}%{python3_sitelib}' \
    help2man --no-info --output='%{buildroot}%{_mandir}/man1/nodeenv.1' \
    '%{buildroot}%{_bindir}/nodeenv'
%oreon_autofiles python3-nodeenv usr/lib/python3*/site-packages/nodeenv* usr/lib64/python3*/site-packages/nodeenv* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/nodeenv* usr/lib64/python3*/site-packages/nodeenv* usr/bin/*

%check

k="${k-}${k+ and }not test_smoke"
%pytest -k "${k-}" -v
%files
%files -n python3-nodeenv -f %{oreon_filedir}/python3-nodeenv.list

%changelog

%autochangelog
