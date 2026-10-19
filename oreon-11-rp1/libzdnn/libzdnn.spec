%global source0_hash 154acbb56f374e9b88a30d55180d2da776e1742d252ae216d94e9c0b4cef28bd
Name:		libzdnn
Version:	1.0.1
Release:        1%{?dist}
Summary:        Driver library for the IBM Z Neural Network Processing Assist Facility
License:	Apache-2.0
Url:		https://github.com/IBM/zDNN
Source0:        https://github.com/IBM/zDNN/archive/v%{version}/%{name}-%{version}.tar.gz
ExclusiveArch:	s390x
%global soversion 0
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  g++
BuildRequires:  gawk
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
The zDNN library provide a user space API for exploitation of the
Neural Network Processing Assist Facility.  All application which
intend to use that facility on IBM Z are supposed to do this via this
library.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package	static
Summary:	Static library version %{name}
Requires:	%{name}-devel%{?_isa} = %{version}-%{release}
%description    static
The %{name}-static package contains the static library of %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n zDNN-%{version}
autoreconf -i

%build

CFLAGS_INIT="%{build_cflags}"; export CFLAGS_INIT; CFLAGS="%{build_cflags} -march=z14 -mtune=z14" CXXFLAGS="%{build_cxxflags} -march=z14 -mtune=z14" %configure
%make_build build
%install
%make_install
mv $RPM_BUILD_ROOT%{_libdir}/libzdnn.so.%{soversion} $RPM_BUILD_ROOT%{_libdir}/libzdnn.so.%{version}
ln -s -r $RPM_BUILD_ROOT%{_libdir}/libzdnn.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libzdnn.so.%{soversion}
rm -f $RPM_BUILD_ROOT%{_libdir}/libzdnn.so
ln -s -r $RPM_BUILD_ROOT%{_libdir}/libzdnn.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libzdnn.so
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libzdnn-devel -f %{oreon_filedir}/libzdnn-devel.list
%files -n libzdnn-static -f %{oreon_filedir}/libzdnn-static.list

%changelog

%autochangelog
