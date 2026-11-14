# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash b2ba6a4dea487a7ebcd53248d3476aca449d30db12a2dde5e0c5ca9624fd77e5
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: python3-imagesize
Version: 2.0.1
Release: 1%{?dist}
Summary: Get image size from headers (BMP/PNG/JPEG/JPEG2000/GIF/TIFF/SVG/Net...
License: MIT
URL: https://pypi.org/project/imagesize/
Source0: https://files.pythonhosted.org/packages/fb/5e/513ff06670c84e7b9887c1fdf61b2d42b4f574a831f2f1d2222023049d8a/imagesize-2.0.1.tar.gz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-setuptools
Requires: python3

%description
Get image size from headers (BMP/PNG/JPEG/JPEG2000/GIF/TIFF/SVG/Net...

%prep
%oreon_sha256
%autosetup -n imagesize-2.0.1

%build
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
%oreon_filelist

%check
python3 -c 'import imagesize'

%files -f %{_builddir}/%{name}.files
