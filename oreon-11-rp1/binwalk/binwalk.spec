%global source0_hash 06f595719417b70a592580258ed980237892eadc198e02363201abe6ca59e49a
Name:           binwalk
Version:        3.1.0
Release:        1%{?dist}
Summary:        Firmware analysis tool
License:        MIT
URL:            https://github.com/ReFirmLabs/binwalk
Source0:        https://github.com/ReFirmLabs/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        _nose_shim.py
Patch0:         binwalk-2.3.3-tests.patch
Patch1:         %{url}/pull/559/commits/6e7736869d998edb6384728c03a348cd9ab1f9ca.patch
Patch2:         version-oops.patch
Patch3:         requires-zombie-imp.patch
Patch4:         0001-Migrate-from-ast.Num-to-ast.Constant.patch
BuildArch:      noarch
Suggests:       python3-pyqtgraph
Suggests:       capstone
Recommends:     mtd-utils gzip bzip2 tar arj p7zip p7zip-plugins cabextract squashfs-tools lzop srecord
Suggests:       sleuthkit
# oreon:deps
BuildRequires:  (python3-zombie-imp if python3-devel >= 3.12)
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
# /oreon:deps
%description
Binwalk is a tool for searching a given binary image for embedded files and
executable code. Specifically, it is designed for identifying files and code
embedded inside of firmware images. Binwalk uses the python-magic library, so 
it is compatible with magic signatures created for the Unix file utility. 

%prep

%autosetup -p1
# replace nose with minimal compatibility shim
# upsteram has moved away from Python in version 3+
cp -a %{SOURCE1} testing/tests/_nose_shim.py
sed -i 's/from nose.tools import/from _nose_shim import/' testing/tests/*.py

%build

%py3_build
%install
%py3_install
%oreon_autofiles main

%check

cd testing/tests
%pytest
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
