%global source0_hash none

Name:           binwalk
Version:        2.3.4
Release:        17%{?dist}
Summary:        Firmware analysis tool
License:        MIT
URL:            https://github.com/ReFirmLabs/binwalk
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        _nose_shim.py
Patch0:         binwalk-2.3.3-tests.patch
Patch1:         %{url}/pull/559/commits/6e7736869d998edb6384728c03a348cd9ab1f9ca.patch
Patch2:         version-oops.patch
# https://github.com/ReFirmLabs/binwalk/issues/507
Patch3:         requires-zombie-imp.patch
Patch4:         0001-Migrate-from-ast.Num-to-ast.Constant.patch
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# https://github.com/ReFirmLabs/binwalk/issues/507
BuildRequires:  (python3-zombie-imp if python3-devel >= 3.12)
# For tests
BuildRequires:  python3-pytest
# Optional, for graphs and visualizations
Suggests:       python3-pyqtgraph
# Optional, for --disasm functionality
Suggests:       capstone
# Optional, for automatic extraction/decompression of files and data
Recommends:     mtd-utils gzip bzip2 tar arj p7zip p7zip-plugins cabextract squashfs-tools lzop srecord
Suggests:       sleuthkit

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

%check
cd testing/tests
%pytest

%files
%doc API.md INSTALL.md README.md
%license LICENSE
%{_bindir}/%{name}
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}-%{version}*.egg-info

%changelog
%autochangelog
