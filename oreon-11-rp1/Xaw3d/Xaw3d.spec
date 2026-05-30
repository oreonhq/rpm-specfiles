%global source0_hash a41c3e37135ad616b1f28bbde70002afbf3cb59a30df34141f829d32eadc8646

Summary: A version of the MIT Athena widget set for X
Name: Xaw3d
Version: 1.6.6
Release: 6%{?dist}
Source0:        https://xorg.freedesktop.org/archive/individual/lib/libXaw3d-%{version}.tar.xz
Source1:        https://xorg.freedesktop.org/archive/individual/lib/libXaw3d-%{version}.tar.xz.sig
Source2: alan.coopersmith.asc
Patch5: Xaw3d-1.5-debian-fixes.patch
Patch7: Xaw3d-1.6.1-3Dlabel.patch
Patch10: Xaw3d-1.6.5-fontset.patch
Patch11: Xaw3d-1.6.1-hsbar.patch

License: MIT AND X11 AND GPL-3.0-or-later
URL: https://www.x.org/

BuildRequires: gcc
BuildRequires: make
BuildRequires: libXmu-devel
BuildRequires: libXt-devel
BuildRequires: libSM-devel
BuildRequires: libXext-devel
BuildRequires: libX11-devel
BuildRequires: libXpm-devel
BuildRequires: xorg-x11-util-macros
BuildRequires: bison
BuildRequires: flex
BuildRequires: ed
BuildRequires: gnupg2

%description
Xaw3d is an enhanced version of the MIT Athena Widget set for
the X Window System.  Xaw3d adds a three-dimensional look to applications
with minimal or no source code changes.

You should install Xaw3d if you are using applications which incorporate
the MIT Athena widget set and you'd like to incorporate a 3D look into
those applications.

%package devel
Summary: Header files and libraries for development using Xaw3d
Requires: %{name} = %{version}-%{release}
Requires: libXmu-devel
Requires: libXt-devel
Requires: libSM-devel
Requires: libXext-devel
Requires: libX11-devel
Requires: libXpm-devel

%description devel
Xaw3d is an enhanced version of the MIT Athena widget set for
the X Window System.  Xaw3d adds a three-dimensional look to those
applications with minimal or no source code changes. Xaw3d-devel includes
the header files and libraries for developing programs that take full
advantage of Xaw3d's features.

You should install Xaw3d-devel if you are going to develop applications
using the Xaw3d widget set.  You'll also need to install the Xaw3d
package.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -q -n libXaw3d-%{version}
# This doesn't apply cleanly, but has not been applied
#%patch5 -p1 -b .debian
%patch -P 7 -p1 -b .3Dlabel
%patch -P 10 -p1 -b .fontset
%patch -P 11 -p1 -b .hsbar


%build
%configure --disable-static \
  --enable-arrow-scrollbars \
  --enable-gray-stipples \
  --enable-multiplane-bitmaps
%make_build


%install
%make_install
rm $RPM_BUILD_ROOT%{_libdir}/libXaw3d.la
rm -r $RPM_BUILD_ROOT%{_docdir}



%ldconfig_scriptlets


%files
%license COPYING
%doc ChangeLog README.md src/README.XAW3D
%{_libdir}/*.so.*

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/xaw3d.pc
%{_includedir}/X11/Xaw3d

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.6.6-6
- Prepare for Oreon 11 (RP1)
