%global source0_hash 838bb6a7d096d952178a67417443427feea7cdfe26af7a33ae2384ac235f4d97
%global _smp_build_ncpus 1
ExcludeArch:    %{ix86}
Name:           astrometry
Version:        0.98
Release:        1%{?dist}
Summary:        Blind astrometric calibration of arbitrary astronomical images
License:        BSD-3-Clause and GPL-2.0-or-later and GPL-3.0-or-later
URL:            http://www.astrometry.net
Source0:        %{name}.net-%{version}-clean.tar.xz
Source1:        %{name}-generate-tarball.sh
Source2:        astrometry-data-4107-4119.tar.zst
Source3:        astrometry-data-5206.tar.zst
Source4:        astrometry-data-5205.tar.zst
Source5:        astrometry-get-data.sh
Patch:          Add-SONAME-to-libastrometry.so.patch
Patch:          Dynamically-link-to-libastrometry.so-when-possible.patch
Patch:          Fix-issues-when-using-Debian-libs-instead-of-convienience.patch
Patch:          Fix-shared-lib-flags-so-that-the-package-can-be-built-on-s390x.patch
Patch:          Don-t-copy-demo-files-to-examples.patch
Patch:          Remove-errornous-generation-of-net-client.py.patch
Patch:          Remove-horizons.py-from-Python-package.patch
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       netpbm-progs
Requires:       python3-%{name} = %{version}-%{release}
Recommends:     cfitsio-utils
Recommends:     %{name}-data-4107-4119 = %{version}-%{release}
Provides:       bundled(libkd)
Provides:       bundled(qfits)
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  netpbm-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(cfitsio)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(wcslib)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  python3-astropy
BuildRequires:  python3-devel
BuildRequires:  python3-numpy
BuildRequires:  python3-setuptools
BuildRequires:  swig
BuildRequires:  xorg-x11-proto-devel
# /oreon:deps
%description
The astrometry engine will take any image and return the astrometry
world coordinate system (WCS), a standards-based description of the
transformation between image coordinates and sky coordinates.

Other tools included in the astrometry package can do much more, like
plotting astronomic information over solved images, conversion utilities
or generate statistics from FITS images.

%package data-4107-4119
Summary:        Index files for astrometry (scale 7-19, wide-field)
License:        GPL-2.0-or-later
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Enhances:       %{name}
Obsoletes:      %{name}-data <= %{version}-%{release}
Provides:       %{name}-data = %{version}-%{release}
Obsoletes:      %{name}-data-4207 <= %{version}-%{release}
Provides:       %{name}-data-4207 = %{version}-%{release}
Obsoletes:      %{name}-tycho2 <= 2.0-18
Provides:       %{name}-tycho2 = 2.0-18
%description data-4107-4119
Index files for astrometry built from the Tycho-2 catalog
(scales 7-19, wide-field, from 22 to 2000 arcminutes).

%package data-5206
Summary:        Index files for astrometry (scale 6, 16 to 22 arcmin)
License:        GPL-2.0-or-later
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Enhances:       %{name}
Obsoletes:      %{name}-data-4206 <= %{version}-%{release}
Provides:       %{name}-data-4206 = %{version}-%{release}
%description data-5206
Index files for astrometry built from Tycho-2 + Gaia-DR2 catalogs, light
version (no additional Gaia-DR2 information tagged along).
These indexes are suitable for images from 16 to 22 arcminutes.

%package data-5205
Summary:        Index files for astrometry (scale 5, 11 to 16 arcmin)
License:        GPL-2.0-or-later
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Enhances:       %{name}
Obsoletes:      %{name}-data-4205 <= %{version}-%{release}
Provides:       %{name}-data-4205 = %{version}-%{release}
%description data-5205
Index files for astrometry built from Tycho-2 + Gaia-DR2 catalogs, light
version (no additional Gaia-DR2 information tagged along).
These indexes are suitable for images from 11 to 16 arcminutes.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description devel
%{summary}

%package libs
Summary:        Libraries for %{name}
%description libs
Libraries for %{name}

%package -n python3-%{name}
Summary:        Python modules from %{name}
Requires:       python3-astropy
%description -n python3-%{name}
%{summary}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}.net-%{version}
%setup -T -D -a 2 -n %{name}.net-%{version}
%setup -T -D -a 3 -n %{name}.net-%{version}
%setup -T -D -a 4 -n %{name}.net-%{version}

%build

ln -sf . astrometry
%make_build \
    SYSTEM_GSL=yes \
    NETPBM_INC=-I%{_includedir}/netpbm \
    NETPBM_LIB="-L%{_libdir} -lnetpbm" \
    all py extra
%install
%make_install SYSTEM_GSL=yes \
              INSTALL_DIR=%{buildroot}%{_prefix} \
              PY_BASE_INSTALL_DIR=%{buildroot}%{python3_sitearch}/%{name} \
              INCLUDE_INSTALL_DIR=%{buildroot}%{_includedir}/%{name} \
              LIB_INSTALL_DIR=%{buildroot}%{_libdir} \
              BIN_INSTALL_DIR=%{buildroot}%{_bindir} \
              DATA_INSTALL_DIR=%{buildroot}%{_datadir}/%{name}/data \
              PY_BASE_LINK_DIR=%{python3_sitearch}/%{name} \
              ETC_INSTALL_DIR=%{buildroot}%{_sysconfdir} \
              MAN1_INSTALL_DIR=%{buildroot}%{_mandir}/man1 \
              DOC_INSTALL_DIR=%{buildroot}%{_docdir}/%{name} \
              EXAMPLE_INSTALL_DIR=%{buildroot}%{_datadir}/%{name}/examples
sed -i \
    "s:%{buildroot}%{_prefix}/data:%{_datadir}/%{name}/data:" \
    %{buildroot}/etc/astrometry.cfg
pushd %{buildroot}%{_bindir}
for exec in imarith imstat listhead liststruc modhead tabmerge tablist; do
        mv $exec astrometry-$exec
done
popd
%py3_shebang_fix %{buildroot}%{_bindir}/degtohms \
                 %{buildroot}%{_bindir}/hmstodeg \
                 %{buildroot}%{_bindir}/image2pnm \
                 %{buildroot}%{_bindir}/merge-columns \
                 %{buildroot}%{_bindir}/removelines \
                 %{buildroot}%{_bindir}/text2fits \
                 %{buildroot}%{_bindir}/uniformize \
                 %{buildroot}%{_bindir}/votabletofits
rm -f %{buildroot}%{_docdir}/%{name}/report.txt
rm -f %{buildroot}%{_libdir}/*.a
rm -f %{buildroot}%{_bindir}/plotann.py
install -m0644 astrometry-data*/*.fits %{buildroot}%{_datadir}/%{name}/data
%oreon_autofiles astrometry-data-4107-4119 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles astrometry-data-5206 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles astrometry-data-5205 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles astrometry-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles astrometry-libs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles python3-astrometry usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export PYTHON=%{__python3}
make test ARCH_FLAGS="%{optflags}"
%files -f %{oreon_filedir}/main.list
%files -n astrometry-data-4107-4119 -f %{oreon_filedir}/astrometry-data-4107-4119.list
%files -n astrometry-data-5206 -f %{oreon_filedir}/astrometry-data-5206.list
%files -n astrometry-data-5205 -f %{oreon_filedir}/astrometry-data-5205.list
%files -n astrometry-devel -f %{oreon_filedir}/astrometry-devel.list
%files -n astrometry-libs -f %{oreon_filedir}/astrometry-libs.list
%files -n python3-astrometry -f %{oreon_filedir}/python3-astrometry.list

%changelog

%autochangelog
