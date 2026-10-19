%global source0_hash eacaaca27e6477b3b519cdd87495382fc508e66be4945fd255d1e7a26c3ae3c1
Summary:        OpenFabrics Alliance InfiniBand management common library
Name: libibcommon
Version: 1.2.0
Release:        34%{?dist}
License: GPL-2.0-only OR LicenseRef-Callaway-BSD
Source0:        http://www.openfabrics.org/downloads/management/%{name}-%{version}.tar.gz
Url: http://openfabrics.org/
ExcludeArch: s390 s390x
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
libibcommon provides common utility functions for the OFA diagnostic and
management tools. 

%package devel
Summary: Development files for the libibcommon library
Requires: %{name} = %{version}-%{release}
%description devel
Development files for the libibcommon library.

%package static
Summary: Static library files for the libibcommon library
Requires: %{name}-devel = %{version}-%{release}
%description static
Static library files for the libibcommon library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
libtoolize --copy --force
touch NEWS README
autoreconf --install --force

%build

%configure
make %{?_smp_mflags}
%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=${RPM_BUILD_ROOT} install
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libibcommon-devel -f %{oreon_filedir}/libibcommon-devel.list
%files -n libibcommon-static -f %{oreon_filedir}/libibcommon-static.list

%changelog

%autochangelog
