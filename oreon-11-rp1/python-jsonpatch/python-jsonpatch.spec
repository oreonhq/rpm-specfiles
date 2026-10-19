%global source0_hash 9fcd4009c41e6d12348b4a0ff2563ba56a2923a7dfee731d004e212e1ee5030c
%global pypi_name jsonpatch
Name:           python-%{pypi_name}
Version:        1.33
Release:        12%{?dist}
Summary:        Applying JSON Patches in Python
License:        BSD-3-Clause
URL:            https://github.com/stefankoegl/python-json-patch
Source0:        https://pypi.io/packages/source/j/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Patch0:         0001-Skip-unit-test-in-packaging.patch
Patch1:         https://github.com/stefankoegl/python-json-patch/pull/159.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-jsonpointer
BuildRequires:  python3-setuptools
# /oreon:deps
%description
Library to apply JSON Patches according to RFC 6902 - Python 2 build.

%package -n python3-%{pypi_name}
Summary:        Applying JSON Patches in Python 3
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-jsonpointer
Requires:       python3-jsonpointer
%{?python_provide:%python_provide python3-%{pypi_name}}
%description -n python3-%{pypi_name}
Library to apply JSON Patches according to RFC 6902 - Python 3 build.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -qn %{pypi_name}-%{version}
%patch -P 0 -p1
%patch -P 1 -p1

%build

%py3_build
%install
%py3_install
rm %{buildroot}%{_bindir}/jsondiff
mv %{buildroot}%{_bindir}/jsonpatch %{buildroot}%{_bindir}/jsonpatch-%{python3_version}
ln -s ./jsonpatch-%{python3_version} %{buildroot}%{_bindir}/jsonpatch-3
ln -s ./jsonpatch-%{python3_version} %{buildroot}%{_bindir}/jsonpatch
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%{__python3} tests.py
%files -f %{oreon_filedir}/main.list
%files -n python3-jsonpatch -f %{oreon_filedir}/python3-jsonpatch.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.33-12
- Prepare for Oreon 11 (RP1)
