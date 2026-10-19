%global source0_hash f4da1fb5a89624a1fdac6769c87290572c0c88461f2f8080dcc3710ef44131ee
Name:           python3-lxc
Version:        7.0.0
Release:        1%{?dist}
Summary:        Python binding for LXC
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://linuxcontainers.org/lxc
Source0:        https://linuxcontainers.org/downloads/lxc/%{name}-%{version}.tar.gz
Patch0:         lxc-5.0.0_py3.13.patch
%global desc Linux Resource Containers provide process and resource isolation\
without the overhead of full virtualization.\
\
The python%{python3_pkgversion}-lxc package contains the Python3\
binding for LXC.
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-python3-lxc = %{version}-%{release}
# /oreon:deps
%description
%{desc}

%if 0%{?python3_pkgversion} != 3
%global subpkg -n python%{python3_pkgversion}-lxc
%package %{?subpkg}
Summary: Python binding for LXC
%description %{?subpkg}
%{desc}
%endif

%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}_lxc\\..*\\.so

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
chmod -x examples/*.py
sed -i -e '1 s@^#!.*@#!%{__python3}@' examples/*.py
%oreon_autofiles main

%check

%pyproject_check_import
%py3_check_import lxc _lxc
%files

%changelog

%autochangelog
