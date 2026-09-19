%global source0_hash afcd4af13897740e34f6ae1f3061bbfbda9c1dd5df3ecc9f57141c985d35d19d

%global forgeurl https://github.com/scottdraves/flam3

Name:           flam3
Version:        3.1.1
Release:        %autorelease
Summary:        Programs to generate and render cosmic recursive fractal flames
%forgemeta
License:        GPL-3.0-only
URL:            http://www.flam3.com/
Source0:        %forgesource

BuildRequires:  gcc
BuildRequires:  chrpath
BuildRequires:  git-core
BuildRequires:  libxml2-devel
BuildRequires:  libpng-devel
BuildRequires:  libjpeg-devel

%description
Flam3, or Fractal Flames, are algorithmically generated images and animations.
This is free software to render fractal flames as described on
http://flam3.com. Flam3-animate makes animations, and flam3-render makes still
images. Flam3-genome creates and manipulates genomes (parameter sets).

%package devel
Summary:        C headers to generate and render cosmic recursive fractal flames
Requires:       pkgconfig
Requires:       libxml2-devel
Requires:       libpng-devel
Requires:       libjpeg-devel
Requires:       flam3 = %{version}-%{release}

%description devel
Flam3, or Fractal Flames, are algorithmically generated images and animations.
This is free software to render fractal flames as described on
http://flam3.com. Flam3-animate makes animations, and flam3-render makes still
images. Flam3-genome creates and manipulates genomes (parameter sets). This
package contains a header file for C, a library, and a pkgconfig file.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%build
%configure --includedir=%{_includedir}/%{name} --enable-shared
make

%install
make install DESTDIR=%{buildroot} INSTALL="install -p"
rm %{buildroot}/%{_libdir}/lib%{name}.la %{buildroot}/%{_libdir}/lib%{name}.a
chrpath --delete %{buildroot}%{_bindir}/flam3-*
%ldconfig_scriptlets

%files
%doc README.txt
%license COPYING
%{_bindir}/flam3-animate
%{_bindir}/flam3-convert
%{_bindir}/flam3-genome
%{_bindir}/flam3-render
%{_datadir}/flam3
%{_libdir}/libflam3.so.*
%{_mandir}/man1/flam3*

%files devel
%{_includedir}/%{name}/
%{_libdir}/libflam3.so
%{_libdir}/pkgconfig/flam3.pc

%changelog
%autochangelog
