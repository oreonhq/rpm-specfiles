%global source0_hash b2ba6a4dea487a7ebcd53248d3476aca449d30db12a2dde5e0c5ca9624fd77e5
Name:           python-imagesize
Version:        2.0.1
Release:        1%{?dist}
Summary:        Get image size from headers _BMP/PNG/JPEG/JPEG2000/GIF/TIFF/SVG/Netpbm/WebP/AVIF/HEIC/HEIF_
License:        MIT
URL:            https://github.com/shibukawa/imagesize_py
Source0:        https://files.pythonhosted.org/packages/source/i/imagesize/imagesize-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-imagesize = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-imagesize
Summary:        Get image size from headers _BMP/PNG/JPEG/JPEG2000/GIF/TIFF/SVG/Netpbm/WebP/AVIF/HEIC/HEIF_
%description -n python3-imagesize

%prep
%global oreon_srcdir imagesize-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-imagesize usr/lib/python3*/site-packages/imagesize* usr/lib64/python3*/site-packages/imagesize* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/imagesize* usr/lib64/python3*/site-packages/imagesize* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-imagesize -f %{oreon_filedir}/python3-imagesize.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.0.0-1
- Prepare for Oreon 11 (RP1)
