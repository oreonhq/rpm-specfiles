%global source0_hash 881647a4172c55a067a7b6687965441cf21176d79d93075b22a373ea9accd8d3

%global __cmake_in_source_build 1
Name:           scantailor
Version:        0.9.11.1
Release:        41%{?dist}
Summary:        An interactive post-processing tool for scanned pages

License:        GPL-3.0-or-later OR LGPL-2.1-only
URL:            http://scantailor.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop
# Don't override CFLAGS and CXXFLAGS: https://github.com/scantailor/scantailor/pull/160
Patch0:         0001-respect-CFLAGS-and-CXXFLAGS.patch
Patch1:         boost1.6.patch
Patch2:         gcc6-build-patch.patch
Patch3:         f30-buildfailures.patch
Patch4:         boost-1.83.0-compat.patch

BuildRequires: make
BuildRequires:  cmake
BuildRequires:  boost-devel
BuildRequires:  libXext-devel
BuildRequires:  qt-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  libjpeg-devel
BuildRequires:  zlib-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  libXrender-devel
BuildRequires:  desktop-file-utils
BuildRequires:  glibc-static

%description
Scan Tailor is an interactive post-processing tool for scanned pages.
It performs operations such as page splitting, deskewing, adding/removing
borders, and others. You give it raw scans, and you get pages ready to be
printed or assembled into a PDF or DJVU file. Scanning, optical character
recognition, and assembling multi-page documents are out of scope of this
project.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1
%patch -P1 -p1 -z .boost
%patch -P2 -p1 -b .gcc6-build
%patch -P3 -p1 -b .f30-buildfaulures
%patch -P4 -p1

%build
%cmake . -DEXTRA_LIBS=Xrender -DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo -DCMAKE_INSTALL_PREFIX="/usr" 
make %{?_smp_mflags}
mv resources/icons/COPYING resources/icons/COPYING-icons

%install
make install DESTDIR=$RPM_BUILD_ROOT
desktop-file-install --dir=${RPM_BUILD_ROOT}%{_datadir}/applications %{SOURCE1}
%{__mkdir_p} ${RPM_BUILD_ROOT}%{_datadir}/icons/hicolor/scalable/apps
cp -p resources/appicon.svg \
        ${RPM_BUILD_ROOT}%{_datadir}/icons/hicolor/scalable/apps/scantailor.svg

%check
make tests
./tests/tests

%files
%doc COPYING resources/icons/COPYING-icons
%{_bindir}/scantailor
%{_bindir}/scantailor-cli
%{_datadir}/scantailor/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/scantailor.svg

%changelog
%autochangelog
