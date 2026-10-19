%global source0_hash f98d4cd5464f9610f29e0056d96c0519b52322d0cedaa5e81c9e277ca7cdb8ce
Name:           skyviewer
Version:        1.1.0
Release:        8%{?dist}
Summary:        Program to display HEALPix-based skymaps in FITS files
License:        CFITSIO
URL:            http://lambda.gsfc.nasa.gov/toolbox/tb_skyviewer_ov.cfm
Source0:        http://lambda.gsfc.nasa.gov/toolbox/skyviewer/%{name}-%{version}.tar.gz
Source1:        skyviewer.desktop
# oreon:deps
BuildRequires:  cfitsio-devel
BuildRequires:  chealpix-devel
BuildRequires:  cmake(qt5gui)
BuildRequires:  cmake(qt5opengl)
BuildRequires:  cmake(qt5widgets)
BuildRequires:  cmake(qt5xml)
BuildRequires:  desktop-file-utils
BuildRequires:  libQGLViewer-qt5-devel
BuildRequires:  make
BuildRequires:  mesa-libGLU-devel
# /oreon:deps
%description
SkyViewer is an OpenGL based program to display HEALPix-based skymaps,
saved in FITS format files. The loaded skymaps can be viewed either on a 3D
sphere or as a Mollweide projection. In either case, realtime panning and
zooming are supported, along with rotations for the 3D sphere view,
assuming you have a strong enough graphics card.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%{qmake_qt5} INCLUDE_DIR=%{_includedir} \
        LIB_DIR=%{_libdir} \
        INCPATH=%{_includedir}/cfitsio
make %{?_smp_mflags}
%install
install -d %{buildroot}%{_bindir}
install -pm 0755 skyviewer %{buildroot}%{_bindir}
install -d %{buildroot}%{_datadir}/pixmaps
install -pm 0644 images/spherical.png \
        %{buildroot}%{_datadir}/pixmaps/skyviewer.png
desktop-file-install --vendor='' %{SOURCE1} \
        --dir=%{buildroot}%{_datadir}/applications
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
