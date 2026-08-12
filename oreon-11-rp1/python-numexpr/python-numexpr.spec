%global source0_hash 7cb4c2d5d686f366e1121c287f48c3964ae3ec2ecc559d64a12bb315beebbf9a

Summary:        Fast numerical array expression evaluator for Python and NumPy
Name:           python-numexpr
Version:        2.14.1
Release:        2%{?dist}
URL:            https://github.com/pydata/numexpr
License:        MIT
Source0:        https://github.com/pydata/numexpr/archive/v%{version}/numexpr-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  python3-devel
BuildRequires:  python3-numpy
BuildRequires:  python3-setuptools

%global _description %{expand:
The numexpr package evaluates multiple-operator array expressions many times
faster than NumPy can. It accepts the expression as a string, analyzes it,
rewrites it more efficiently, and compiles it to faster Python code on the
fly.}

%description %_description

%package -n python3-numexpr
Summary:        %{summary}
Requires:       python3-numpy >= 1.6

%description -n python3-numexpr %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n numexpr-%{version} -p1

%build
%py3_build

%install
%py3_install
chmod 0755 %{buildroot}%{python3_sitearch}/numexpr/cpuinfo.py
sed -i "1s|/usr/bin/env python$|%{python3}|" %{buildroot}%{python3_sitearch}/numexpr/cpuinfo.py

%check
pushd build/lib.linux*
%py3_test_envvars %python3 -c 'import numexpr, sys; sys.exit(not numexpr.test().wasSuccessful())'
popd

%files -n python3-numexpr
%license LICENSE.txt
%doc ANNOUNCE.rst RELEASE_NOTES.rst README.rst
%{python3_sitearch}/numexpr/
%{python3_sitearch}/numexpr-%{version}-py*.egg-info

%changelog
%autochangelog
