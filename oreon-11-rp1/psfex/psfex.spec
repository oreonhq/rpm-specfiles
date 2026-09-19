%global source0_hash aff89e4bdb9a8392af889f5203279a381532eefcc60a3682824b48c0466dc3d8

Name: psfex
Version: 3.24.1
Release: 8%{?dist}
Summary: Model the Point Spread Function from FITS images

License: GPL-3.0-only
URL: http://astromatic.iap.fr/software/%{name}
Source0: https://github.com/astromatic/psfex/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires: gcc
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool

BuildRequires: fftw-devel
BuildRequires: flexiblas-devel
BuildRequires: plplot-devel

%description
PSFEx (“PSF Extractor”) extracts models of the Point Spread Function (PSF) 
from FITS images processed with SExtractor and measures the quality of images. 
The generated PSF models can be used for model-fitting photometry or 
morphological analyses.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
./autogen.sh
sed -i 's/openblas/flexiblas/g' configure
%configure --enable-plplot=yes --enable-flexiblas=yes \
    --with-flexiblas-incdir=%{_includedir}/flexiblas
%make_build

%install
%make_install

%files
%license LICENSE
%doc AUTHORS HISTORY README.md THANKS 
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_mandir}/manx/%{name}.x*
%{_datadir}/%{name}/

%changelog
%autochangelog
