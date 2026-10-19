%global source0_hash 597cfddf9c2d7993e9b0b86bca1b73839567ee9116ee33f6d750a449b5033d91
Name:           ncview
Version:        2.1.11
Release:        1%{?dist}
Summary:        A visual browser for netCDF format files
License:        GPL-3.0-only
URL:            https://cirrus.ucsd.edu/ncview/
Source0:        https://cirrus.ucsd.edu/~pierce/ncview/ncview-%{version}.tar.gz
Patch0:         ncview-rpath.patch
Patch1:         ncview-fixes.patch
# oreon:deps
BuildRequires:  chrpath
BuildRequires:  expat-devel
BuildRequires:  libICE-devel
BuildRequires:  libSM-devel
BuildRequires:  libX11-devel
BuildRequires:  libXaw-devel
BuildRequires:  libXext-devel
BuildRequires:  libXmu-devel
BuildRequires:  libXt-devel
BuildRequires:  libpng-devel
BuildRequires:  make
BuildRequires:  netcdf-devel
BuildRequires:  udunits2-devel
BuildRequires:  xorg-x11-proto-devel
# /oreon:deps
%description
Ncview is a visual browser for netCDF format files.  Typically you
would use ncview to get a quick and easy, push-button look at your
netCDF files.  You can view simple movies of the data, view along
various dimensions, take a look at the actual data values, change
color maps, invert the data, etc.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure X_CFLAGS="%{optflags}" --with-udunits2_incdir=%{_includedir}/udunits2 \
 --x-libraries=%{_libdir}  --datadir=%{_datadir}/ncview
make
sed s=NCVIEW_LIB_DIR=%{_datadir}/ncview= < data/ncview.1.sed > data/ncview.1
%install
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/X11/app-defaults
cp -p Ncview-appdefaults ${RPM_BUILD_ROOT}%{_datadir}/X11/app-defaults/Ncview
%makeinstall NCVIEW_LIB_DIR=${RPM_BUILD_ROOT}%{_datadir}/ncview BINDIR=${RPM_BUILD_ROOT}%{_bindir} MANDIR=${RPM_BUILD_ROOT}%{_mandir}/man1
mkdir ${RPM_BUILD_ROOT}%{_datadir}/ncview/
install -m0644 -p *.ncmap ${RPM_BUILD_ROOT}%{_datadir}/ncview/
chmod 644 ${RPM_BUILD_ROOT}%{_datadir}/X11/app-defaults/Ncview
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man1/
install -m0644 -p data/ncview.1 ${RPM_BUILD_ROOT}%{_mandir}/man1/
chrpath -l -d %{buildroot}%{_bindir}/ncview
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
