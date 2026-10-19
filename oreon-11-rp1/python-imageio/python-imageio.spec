%global source0_hash e45cbc5e83502047fb138f7f585f7f105a136a57eea5f4b3cfc6ce1b52720bd3
Name:           python-imageio
Version:        2.37.4
Release:        1%{?dist}
Summary:        Read and write images and video across all major formats. Supports scientific and volumetric data.
License:        BSD-2-Clause
URL:            https://github.com/imageio/imageio
Source0:        https://files.pythonhosted.org/packages/source/i/imageio/imageio-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.0
Requires:       python3-imageio = %{version}-%{release}
# /oreon:deps
%package -n       python3-imageio+bsdf
Summary:        Metapackage for python3-imageio bsdf extras
Requires:       python3-imageio = %{version}-%{release}
Provides:       python3dist(imageio[bsdf]) = %{version}-%{release}

%description -n python3-imageio+bsdf
Metapackage for python3-imageio bsdf extras.

%package -n       python3-imageio+dicom
Summary:        Metapackage for python3-imageio dicom extras
Requires:       python3-imageio = %{version}-%{release}
Provides:       python3dist(imageio[dicom]) = %{version}-%{release}

%description -n python3-imageio+dicom
Metapackage for python3-imageio dicom extras.

%package -n       python3-imageio+feisem
Summary:        Metapackage for python3-imageio feisem extras
Requires:       python3-imageio = %{version}-%{release}
Provides:       python3dist(imageio[feisem]) = %{version}-%{release}

%description -n python3-imageio+feisem
Metapackage for python3-imageio feisem extras.

%package -n       python3-imageio+ffmpeg
Summary:        Metapackage for python3-imageio ffmpeg extras
Requires:       python3-imageio = %{version}-%{release}
Provides:       python3dist(imageio[ffmpeg]) = %{version}-%{release}

%description -n python3-imageio+ffmpeg
Metapackage for python3-imageio ffmpeg extras.

%package -n       python3-imageio+freeimage
Summary:        Metapackage for python3-imageio freeimage extras
Requires:       python3-imageio = %{version}-%{release}
Provides:       python3dist(imageio[freeimage]) = %{version}-%{release}

%description -n python3-imageio+freeimage
Metapackage for python3-imageio freeimage extras.

%package -n       python3-imageio+lytro
Summary:        Metapackage for python3-imageio lytro extras
Requires:       python3-imageio = %{version}-%{release}
Provides:       python3dist(imageio[lytro]) = %{version}-%{release}

%description -n python3-imageio+lytro
Metapackage for python3-imageio lytro extras.

%package -n       python3-imageio+numpy
Summary:        Metapackage for python3-imageio numpy extras
Requires:       python3-imageio = %{version}-%{release}
Provides:       python3dist(imageio[numpy]) = %{version}-%{release}

%description -n python3-imageio+numpy
Metapackage for python3-imageio numpy extras.

%package -n       python3-imageio+pillow-heif
Summary:        Metapackage for python3-imageio pillow-heif extras
Requires:       python3-imageio = %{version}-%{release}
Provides:       python3dist(imageio[pillow-heif]) = %{version}-%{release}

%description -n python3-imageio+pillow-heif
Metapackage for python3-imageio pillow-heif extras.

%package -n       python3-imageio+pillow
Summary:        Metapackage for python3-imageio pillow extras
Requires:       python3-imageio = %{version}-%{release}
Provides:       python3dist(imageio[pillow]) = %{version}-%{release}

%description -n python3-imageio+pillow
Metapackage for python3-imageio pillow extras.

%package -n       python3-imageio+simpleitk
Summary:        Metapackage for python3-imageio simpleitk extras
Requires:       python3-imageio = %{version}-%{release}
Provides:       python3dist(imageio[simpleitk]) = %{version}-%{release}

%description -n python3-imageio+simpleitk
Metapackage for python3-imageio simpleitk extras.

%package -n       python3-imageio+spe
Summary:        Metapackage for python3-imageio spe extras
Requires:       python3-imageio = %{version}-%{release}
Provides:       python3dist(imageio[spe]) = %{version}-%{release}

%description -n python3-imageio+spe
Metapackage for python3-imageio spe extras.

%package -n       python3-imageio+swf
Summary:        Metapackage for python3-imageio swf extras
Requires:       python3-imageio = %{version}-%{release}
Provides:       python3dist(imageio[swf]) = %{version}-%{release}

%description -n python3-imageio+swf
Metapackage for python3-imageio swf extras.

%package -n       python3-imageio+tifffile
Summary:        Metapackage for python3-imageio tifffile extras
Requires:       python3-imageio = %{version}-%{release}
Provides:       python3dist(imageio[tifffile]) = %{version}-%{release}

%description -n python3-imageio+tifffile
Metapackage for python3-imageio tifffile extras.

%package -n       python3-imageio+pyav
Summary:        Metapackage for python3-imageio pyav extras
Requires:       python3-imageio = %{version}-%{release}
Provides:       python3dist(imageio[pyav]) = %{version}-%{release}

%description -n python3-imageio+pyav
Metapackage for python3-imageio pyav extras.

%package -n       python3-imageio+fits
Summary:        Metapackage for python3-imageio fits extras
Requires:       python3-imageio = %{version}-%{release}
Provides:       python3dist(imageio[fits]) = %{version}-%{release}

%description -n python3-imageio+fits
Metapackage for python3-imageio fits extras.

%package -n       python3-imageio+rawpy
Summary:        Metapackage for python3-imageio rawpy extras
Requires:       python3-imageio = %{version}-%{release}
Requires:       python3dist(numpy) > 2
Provides:       python3dist(imageio[rawpy]) = %{version}-%{release}

%description -n python3-imageio+rawpy
Metapackage for python3-imageio rawpy extras.

%package -n       python3-imageio+gdal
Summary:        Metapackage for python3-imageio gdal extras
Requires:       python3-imageio = %{version}-%{release}
Provides:       python3dist(imageio[gdal]) = %{version}-%{release}

%description -n python3-imageio+gdal
Metapackage for python3-imageio gdal extras.

%package -n       python3-imageio+itk
Summary:        Metapackage for python3-imageio itk extras
Requires:       python3-imageio = %{version}-%{release}
Provides:       python3dist(imageio[itk]) = %{version}-%{release}

%description -n python3-imageio+itk
Metapackage for python3-imageio itk extras.

%package -n       python3-imageio+linting
Summary:        Metapackage for python3-imageio linting extras
Requires:       python3-imageio = %{version}-%{release}
Provides:       python3dist(imageio[linting]) = %{version}-%{release}

%description -n python3-imageio+linting
Metapackage for python3-imageio linting extras.

%package -n       python3-imageio+test
Summary:        Metapackage for python3-imageio test extras
Requires:       python3-imageio = %{version}-%{release}
Provides:       python3dist(imageio[test]) = %{version}-%{release}

%description -n python3-imageio+test
Metapackage for python3-imageio test extras.

%package -n       python3-imageio+docs
Summary:        Metapackage for python3-imageio docs extras
Requires:       python3-imageio = %{version}-%{release}
Requires:       python3dist(sphinx) < 6
Provides:       python3dist(imageio[docs]) = %{version}-%{release}

%description -n python3-imageio+docs
Metapackage for python3-imageio docs extras.

%package -n       python3-imageio+dev
Summary:        Metapackage for python3-imageio dev extras
Requires:       python3-imageio = %{version}-%{release}
Provides:       python3dist(imageio[dev]) = %{version}-%{release}

%description -n python3-imageio+dev
Metapackage for python3-imageio dev extras.

%package -n       python3-imageio+all-plugins
Summary:        Metapackage for python3-imageio all-plugins extras
Requires:       python3-imageio = %{version}-%{release}
Requires:       python3dist(numpy) > 2
Provides:       python3dist(imageio[all-plugins]) = %{version}-%{release}

%description -n python3-imageio+all-plugins
Metapackage for python3-imageio all-plugins extras.

%package -n       python3-imageio+all-plugins-pypy
Summary:        Metapackage for python3-imageio all-plugins-pypy extras
Requires:       python3-imageio = %{version}-%{release}
Provides:       python3dist(imageio[all-plugins-pypy]) = %{version}-%{release}

%description -n python3-imageio+all-plugins-pypy
Metapackage for python3-imageio all-plugins-pypy extras.

%package -n       python3-imageio+full
Summary:        Metapackage for python3-imageio full extras
Requires:       python3-imageio = %{version}-%{release}
Requires:       python3dist(numpy) > 2
Requires:       python3dist(sphinx) < 6
Provides:       python3dist(imageio[full]) = %{version}-%{release}

%description -n python3-imageio+full
Metapackage for python3-imageio full extras.

%description

%package -n     python3-imageio
Summary:        Read and write images and video across all major formats. Supports scientific and volumetric data.
# oreon:reqs
Requires:       python3dist(pillow) >= 8.3.2
# /oreon:reqs
%description -n python3-imageio

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir imageio-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-imageio usr/lib/python3*/site-packages/imageio* usr/lib64/python3*/site-packages/imageio* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/imageio* usr/lib64/python3*/site-packages/imageio* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-imageio -f %{oreon_filedir}/python3-imageio.list

%changelog

%autochangelog
