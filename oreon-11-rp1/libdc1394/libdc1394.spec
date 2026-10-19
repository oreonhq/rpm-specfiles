%global source0_hash 537ceb78dd3cef271a183f4a176191d1cecf85f025520e6bd3758b0e19e6609f
%global sover 26
Name:       libdc1394
Summary:        1394-based digital camera control library
Version:    2.2.7
Release:        1%{?dist}
License:    LGPL-2.0-or-later
URL:        http://sourceforge.net/projects/%{name}/
ExcludeArch:    s390 s390x
Source0:        https://downloads.sourceforge.net/project/%{name}/%{name}-2/%{version}/%{name}-%{version}.tar.gz
Patch0:     %{name}-sdl.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  kernel-headers
BuildRequires:  libX11-devel
BuildRequires:  libXv-devel
BuildRequires:  libraw1394-devel
BuildRequires:  libtool
BuildRequires:  libusb1-devel
BuildRequires:  make
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Libdc1394 is a library that is intended to provide a high level programming
interface for application developers who wish to control IEEE 1394 based cameras
that conform to the 1394-based Digital Camera Specification.

%package devel
Summary:    Header files and libraries for %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}
Requires:   libraw1394-devel
%description devel
This package contains the header files and libraries for %{name}. If you like
to develop programs using %{name}, you will need to install %{name}-devel.

%package docs
Summary:    Development documentation for %{name}
%description docs
This package contains the development documentation for %{name}.

%package tools
Summary:    Tools for use with %{name}
%description tools
This package contains tools that are useful when working and developing with
%{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf -vif
%configure --disable-static --enable-doxygen-html --enable-doxygen-dot
%make_build
%make_build doc
%install
%make_install
for p in grab_color_image grab_gray_image grab_partial_image ladybug grab_partial_pvn; do
    install -p -m 0755 -s examples/.libs/$p %{buildroot}%{_bindir}/dc1394_$p
done
install -p -m 0755 examples/dc1394_multiview %{buildroot}%{_bindir}/dc1394_multiview
for f in grab_color_image grab_gray_image grab_partial_image; do
    mv %{buildroot}%{_mandir}/man1/$f.1 %{buildroot}%{_mandir}/man1/dc1394_$f.1
done
find %{buildroot} -name "*.la" -delete
%{?ldconfig_scriptlets}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libdc1394-devel -f %{oreon_filedir}/libdc1394-devel.list
%files -n libdc1394-docs -f %{oreon_filedir}/libdc1394-docs.list
%files -n libdc1394-tools -f %{oreon_filedir}/libdc1394-tools.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.2.7-1
- Prepare for Oreon 11 (RP1)
