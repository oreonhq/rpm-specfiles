%global source0_hash 8d44fbc9e57f3bac9f761c3b12ce102d47d717f0dd846657fb988e0bb5d1ea33

Name:           dumb
Version:        0.9.3
Release:        46%{?dist}
Summary:        IT, XM, S3M and MOD player library
License:        zlib
URL:            http://dumb.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}-autotools.tar.gz
Source2:        license-clarification.eml
Patch0:         dumb-0.9.3-CVE-2006-3668.patch
Patch1:         dumb-0.9.3-license-clarification.patch
Patch2:         dumb-0.9.3-weak-symbols.patch
Patch3:         dumb-configure-c99.patch
BuildRequires:  make gcc gcc-c++
BuildRequires:  allegro-devel

%description
IT, XM, S3M and MOD player library. Mainly targeted for use with the allegro
game programming library, but it can be used without allegro. Faithful to the
original trackers, especially IT.

%package devel
Summary: Development libraries and headers for dumb
Requires: %{name} = %{version}
Requires: allegro-devel

%description devel
The developmental files that must be installed in order to compile
applications which use dumb.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -b 01
%patch -P0 -p1 -z .cve-2006-3668
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
cp %{SOURCE2} .

%build
%configure
# Remove useless /usr/lib64 rpath on 64bit archs
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags} LIBS=-lm

%install
%make_install
#clean out .la and static libs
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a $RPM_BUILD_ROOT%{_libdir}/*.la

%ldconfig_scriptlets

%files
%doc release.txt readme.txt
%license licence.txt license-clarification.eml
%{_bindir}/dumb*
%{_libdir}/lib*-%{version}.so

%files devel
%doc docs/deprec.txt docs/dumb.txt docs/faq.txt docs/fnptr.txt docs/howto.txt docs/ptr.txt
%{_includedir}/*.h
%{_libdir}/libdumb.so
%{_libdir}/libaldmb.so

%changelog
%autochangelog
