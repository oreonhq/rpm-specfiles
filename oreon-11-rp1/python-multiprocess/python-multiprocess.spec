%global source0_hash 098d607e6becc71d74665700ffd3576755098d13216b7f5fe4c344296e436bd5
Name:           python-multiprocess
Version:        0.70.19
Release:        1%{?dist}
Summary:        Better multiprocessing and multithreading in python
License:        BSD-3-Clause AND LicenseRef-Fedora-Public-Domain
URL:            https://github.com/uqfoundation/multiprocess
Source0:        https://github.com/uqfoundation/multiprocess/archive/%{version}/multiprocess-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 42
Requires:       python3-multiprocess = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-multiprocess
Summary:        Better multiprocessing and multithreading in python
License:        BSD-3-Clause
BuildRequires:  python3-devel
BuildRequires:  python3-test
BuildRequires:  python3dist(pox)
%description -n python3-multiprocess

%package doc
Summary:        Documentation for %{name}
%description doc
This package provides documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n multiprocess-%{version} -p1

# Convert line endings
find py%{python3_version}/{doc,examples}/ -type f \
    -exec dos2unix --keepdate '{}' '+'

# Remove shebang
sed -r -i '1{/^#!/d}' py%{python3_version}/multiprocess/tests/__main__.py

# Upstream pretends not to be a pure-Python package to “force python-, abi-,
# and platform-specific naming of bdist_wheel”; this isn’t needed here, and we
# don’t want the RPM package to have to be arched.
sed -r -i 's/^([[:blank:]]*)(distclass=BinaryDistribution,)/\1# \2/' setup.py

# These tests appear to fail because the Python interpreter subprocess called
# through test.support.script_helper.assert_python_ok() does not inherit the
# PYTHONPATH environment variable, so it cannot find the multiprocess package
# in the buildroot.
s='@unittest.skip("Does not respect PYTHONPATH")'
for t in \
    test_spawn_sys_executable_none_allows_import \
    test_global_named_resource_spawn
do
  # The find-then-modify pattern keeps us from discarding mtimes on any sources
  # that do not need modification.
  find . -type f -name '*.py' -exec \
      gawk '/^[[:blank:]]*def '"$t"'\(/ { print FILENAME; nextfile }' '{}' '+' |
    xargs -r -t sed -r -i 's/^([[:blank:]]*)def '"$t"'\(/\1'"$s"'\n&/'
done

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-multiprocess usr/lib/python3*/site-packages/multiprocess* usr/lib64/python3*/site-packages/multiprocess* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/multiprocess* usr/lib64/python3*/site-packages/multiprocess* usr/bin/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%{py3_test_envvars} %{python3} \
    py%{python3_version}/multiprocess/tests/__main__.py
%files
%files -n python3-multiprocess -f %{oreon_filedir}/python3-multiprocess.list
%files -n python-multiprocess-doc -f %{oreon_filedir}/python-multiprocess-doc.list

%changelog

%autochangelog
