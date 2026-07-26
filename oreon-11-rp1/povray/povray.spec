%global source0_hash none

%global api_vers 3.7

Name:           povray
Version:        3.7.0.10
Release:        20%{?dist}
Summary:        The Persistence of Vision Ray Tracer

# Examples below distribution/ are CC-BY-SA
# The sources are AGPLv3+
License:        AGPL-3.0-or-later
URL:            https://povray.org
Source0:        https://github.com/POV-Ray/povray/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

Patch1:         0001-Fix-encoding.patch
Patch2:         0002-Autotool-massaging.patch
Patch3:         0003-Remove-povuser.patch

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  boost-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libtiff-devel
BuildRequires:  libpng-devel
BuildRequires:  zlib-devel
BuildRequires:  OpenEXR-devel
BuildRequires:  SDL-devel
BuildRequires:  libXpm-devel
BuildRequires:  autoconf automake

# FIXME: packaging bug in libEGL?
# Work-around to running povray issuing
# libEGL warning: MESA-LOADER: failed to open swrast: /usr/lib64/dri/swrast_dri.so: cannot open shared object file
# during "make check"
BuildRequires:  mesa-dri-drivers

%description
POV-Ray is a free, full-featured ray tracer.

%package scenes
Summary:        POV-Ray example scenes
License:        CC-BY-SA
BuildArch:      noarch

%description scenes
POV-Ray example scenes.

%prep
%setup -q -n %{name}-%{version}
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1

# Make sure not to be using bundled libs
rm -rf libraries

cd unix
sed -i \
  -e 's,advanced/biscuit.pov -f +d +p +v +w320 +h240 +a0.3,advanced/biscuit.pov -f +d -p +v +w320 +h240 +a0.3,' \
  prebuild.sh

# Add -p in call to povray to "make check" non-interactive
sed -i \
  -e 's,advanced/biscuit.pov -f +d +p +v +w320 +h240 +a0.3,advanced/biscuit.pov -f +d -p +v +w320 +h240 +a0.3,' \
  prebuild.sh

./prebuild.sh
cd ..

%build
case x"%{?vendor}" in
xFedora\ Project ) # Building under Fedora's builders
  COMPILED_BY="%{vendor} <povray-owner@fedoraproject.org>"
  ;;
*) # elsewhere
  COMPILED_BY="%{?vendor:%vendor}%{!?vendor:$(id -u -n)}"
  ;;
esac

%configure --disable-silent-rules \
  --disable-optimiz --disable-strip \
  --x-includes=%{_includedir} --x-libraries=%{_libdir} \
  --with-boost-libdir=%{_libdir} \
  COMPILED_BY="${COMPILED_BY}"

# Filter out bogus and potentially harmful
# -I%%{_includedir} -L%%{_libdir}
# from Makefiles
find -name Makefile -exec sed -i \
  -e 's,-I%{_includedir}$,,g;s,-I%{_includedir} ,,g;' \
  -e 's,-L%{_libdir}$,,g;s,-L%{_libdir} ,,g' {} \
  -e 's,-R%{_libdir}$,,g;s,-R%{_libdir} ,,g' {} \
  \;

# Adjust bogus paths
sed -i \
  -e '/DEFAULT_DIR=/d' \
  -e 's,SYSCONFDIR=\$DEFAULT_DIR/etc,SYSCONFDIR=%{_sysconfdir},' \
  unix/scripts/{allanim,allscene,portfolio}.sh

%{make_build}

%check
%{__make} check

%install
%{make_install} povdocdir=%{_pkgdocdir}

# Fixup permissions
chmod +x %{buildroot}%{_datadir}/povray-%{api_vers}/scenes/camera/mesh_camera/bake.sh

%files
%doc %{_pkgdocdir}
%{_bindir}/povray
%{_mandir}/man1/povray*
%{_datadir}/povray-%{api_vers}
%exclude %{_datadir}/povray-%{api_vers}/scenes
%dir %{_sysconfdir}/povray
%dir %{_sysconfdir}/povray/%{api_vers}
%config(noreplace) %{_sysconfdir}/povray/%{api_vers}/povray*

%files scenes
%dir %{_datadir}/povray-%{api_vers}
%{_datadir}/povray-%{api_vers}/scenes

%changelog
%autochangelog
