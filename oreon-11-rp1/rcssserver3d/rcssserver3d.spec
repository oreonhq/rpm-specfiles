%global source0_hash 114ce3b41802cf1ffc2d9196328781227d201c6e537fa6685ac53df2518b91b5
Name:           rcssserver3d
Version:        0.7.9
Release:        1%{?dist}
Summary:        Robocup 3D Soccer Simulation Server
License:        GPL-2.0-only
URL:            http://sourceforge.net/projects/simspark/
Source0:        http://downloads.sourceforge.net/simspark/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  DevIL-devel
BuildRequires:  ImageMagick
BuildRequires:  SDL-devel
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  freetype-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libGL-devel
BuildRequires:  libGLU-devel
BuildRequires:  make
BuildRequires:  ode-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  simspark-devel
BuildRequires:  tex(latex)
BuildRequires:  tex(subfigure.sty)
BuildRequires:  tex(titlesec.sty)
BuildRequires:  tex(wrapfig.sty)
# /oreon:deps
%description
The RoboCup Soccer Simulator is a research and educational tool for multi-agent
systems and artificial intelligence. It enables for two teams of 11 simulated
autonomous robotic players to play soccer (football).

This package contains the 3D version of the simulator.

%package        devel
Summary:        Header files and libraries for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       boost-devel ode-devel DevIL-devel
Requires:       libGL-devel libGLU-devel simspark-devel
BuildArch:      noarch
%description    devel
This package contains the header files for %{name}. If you like to develop
programs using %{name}, you will need to install %{name}-devel.

%package        doc
Summary:        Users manual for %{name}
BuildArch:      noarch
%description    doc
This package contains the user documentation
for %{name}. If you like to develop agents for %{name},
you will find %{name}-doc package useful.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

mkdir build
cd build
export CXXFLAGS="${CXXFLAGS:-%optflags} -std=gnu++98"
export CFLAGS="${CFLAGS:-%optflags}"
cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} -DLIBDIR:PATH=%{_lib} -DODE_CONFIG_EXEC=ode-double-config ..
make VERBOSE=1 %{?_smp_mflags}
make pdf
cp doc/users/user-manual.pdf ../doc/users/
%install
make -C build install DESTDIR=%{buildroot}
mkdir %{buildroot}/%{_datadir}/pixmaps/
cp -p data/logos/simspark.png %{buildroot}/%{_datadir}/pixmaps/
desktop-file-install \
  --dir=%{buildroot}/%{_datadir}/applications linux/%{name}.desktop
mkdir package_docs
mv %{buildroot}/%{_datadir}/doc/%{name}/* package_docs/
rm -rf %{buildroot}/%{_datadir}/doc
rm -f package_docs/TODO
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n rcssserver3d-devel -f %{oreon_filedir}/rcssserver3d-devel.list
%files -n rcssserver3d-doc -f %{oreon_filedir}/rcssserver3d-doc.list

%changelog

%autochangelog
