%global source0_hash 400aa28e1d695a0c0839ab7ebc36899bf0ee4070968e91da4aca3b0cee953e9e
Name:           python-omsdk
Version:        1.2.519
Release:        1%{?dist}
Summary:        Dell EMC OpenManage Python SDK
License:        Apache-2.0
URL:            https://github.com/dell/omsdk
Source0:        https://github.com/dell/omsdk/archive/refs/tags/v%{version}.tar.gz
Patch0:         setup-omsdk.py.patch
Patch1:         00_remove_future.patch 
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-omsdk = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-omsdk
Summary:        Dell EMC OpenManage Python SDK
%py_provides python3-omsdk
%py_provides python3-omdrivers
Requires:       python%{python3_pkgversion}dist(pywinrm)
%description -n python3-omsdk

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n omsdk-%{version}

# Upstream provides seperate setup.py files for omdrivers and omsdk, but we only need one of them
mv setup-omsdk.py setup.py

# ipaddress was merged into Python 3.3, so it does not need to be a dependancy
sed -i '/ipaddress>=0/d' setup.py

# Wheel version is loaded from file
echo "%{version}" > _version.txt

# Upstream has shebangs on non-executable files
find omsdk -type f -exec sed -i '/\/usr\/bin\/env python3/d' {} +
find omdrivers -type f -exec sed -i '/\/usr\/bin\/env python3/d' {} +

# Fix line endings without dos2unix
sed -i 's/\r$//' README.md

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-omsdk usr/lib/python3*/site-packages/omsdk* usr/lib64/python3*/site-packages/omsdk* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/omsdk* usr/lib64/python3*/site-packages/omsdk* usr/bin/*

%check

%pyproject_check_import -e 'omsdk.listener.sdktrapreceiver' -e 'omsdk.sdksnmptrap'
%files
%files -n python3-omsdk -f %{oreon_filedir}/python3-omsdk.list

%changelog

%autochangelog
