%global source0_hash 89edc6afdd9d60c8020b2b865b61558c86a8928dc6f1773b9f4708b5c28eb873
Name:           FreeSOLID
Version:        2.1.2
Release:        5%{?dist}
Summary:        3D collision detection C++ library
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://sourceforge.net/projects/freesolid/
Source0:        https://sourceforge.net/projects/freesolid/files/%{name}-%{version}.zip
Patch0:         %{name}-%{version}-autotools.patch
Patch1:         %{name}-%{version}-pkgconfig.patch
Patch2:         %{name}-%{version}-Makefile.am-update.patch
# oreon:deps
BuildRequires:  SDL-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  qhull-devel
# /oreon:deps
%description
FreeSOLID is a library for collision detection of three-dimensional
objects undergoing rigid motion and deformation. FreeSOLID is designed
to be used in interactive 3D graphics applications.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig
Requires:       qhull-devel
%description    devel
Libraries and header files for developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n FreeSOLID-%{version}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
mv configure.in configure.ac
autoupdate

# check for libqhull/qhull_a.h instead of qhull/qhull_a.h
sed -i -e 's,qhull/qhull_a.h,libqhull/qhull_a.h,' configure*
sed -i -e 's,VERSION=2.1.1,VERSION=2.1.2,' configure*

mkdir m4
rm acinclude.m4 aclocal.m4
rm ltmain.sh missing depcomp install-sh config.*
chmod 755 configure

%build

autoreconf -fvi
%configure --disable-static
%make_build
%install
make install DESTDIR=%{buildroot}
rm $( find %{buildroot} -name '*.la' ) %{buildroot}%{_infodir}/dir
rm -rf sample/*.o sample/.libs $(find sample -type f -a -executable)
%oreon_autofiles FreeSOLID-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n FreeSOLID-devel -f %{oreon_filedir}/FreeSOLID-devel.list

%changelog

%autochangelog
