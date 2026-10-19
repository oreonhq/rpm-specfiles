%global source0_hash b0be55c14407f586dc10836e8f348b3a002c461a9b47a302071eac0ef85770da
Name:           lrmi
Version:        0.10
Release:        1%{?dist}
Summary:        Library for calling real mode BIOS routines
License:        MIT
URL:            http://sourceforge.net/projects/lrmi/
Source0:        http://download.sourceforge.net/lrmi/%{name}-%{version}.tar.gz
Patch0:         %{name}-0.9-build.patch
Patch1:         lrmi-0.10-newheaders.patch
ExclusiveArch:  %{ix86}
Provides:       lib%{name} = %{version}-%{release}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  kernel-headers
BuildRequires:  make
# /oreon:deps
%description
LRMI is a library for calling real mode BIOS routines.

%package        devel
Summary:        Development files for LRMI
Requires:       %{name} = %{version}-%{release}
Provides:       lib%{name}-devel = %{version}-%{release}
%description    devel
%{summary}.

%package     -n vbetest
Summary:        Utility for listing and testing VESA graphics modes
%description -n vbetest
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0
%patch -P1 -p1 -b .new-headers

%build

make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS" liblrmi.so vbetest
%install
rm -rf $RPM_BUILD_ROOT
make install \
  LIBDIR=$RPM_BUILD_ROOT%{_libdir} INCDIR=$RPM_BUILD_ROOT%{_includedir}
install -Dpm 755 vbetest $RPM_BUILD_ROOT%{_sbindir}/vbetest
%ldconfig_scriptlets
%oreon_autofiles vbetest usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n lrmi-devel -f %{oreon_filedir}/lrmi-devel.list
%files -n vbetest -f %{oreon_filedir}/vbetest.list

%changelog

%autochangelog
