%global source0_hash 35d78954b2b20c4bbf45bdbd2ac2624dd3df29aa599018c46883917ad0506b6f

Name:           libwfut
Version:        0.2.3
Release:        34%{?dist}
Summary:        Software updater tool for WorldForge applications

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://www.worldforge.org/
Source0:        http://downloads.sourceforge.net/worldforge/%{name}-%{version}.tar.gz

# libsigc++20-2.6.0 remove object_slot.h and it causes the build failure.
# Backport patch from upstream
Patch0:         libwfut-0.2.3-Remove-reference-to-object_slot-h.patch

BuildRequires:  gcc-c++
BuildRequires:  libsigc++20-devel libcurl-devel zlib-devel tinyxml-devel swig
BuildRequires: make

%description
libwfut is the WorldForge Update Tool (WFUT) client side implementation in C++
for use directly by WorldForge clients.

%package devel
Summary: Development files for libwfut library
Requires: pkgconfig %{name} = %{version}-%{release} libsigc++20-devel libcurl-devel zlib-devel

%description devel
Development libraries and headers for linking against the libwfut library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1

%build
%configure --disable-static
# Don't use rpath!
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

#rm -f $RPM_BUILD_ROOT%{_libdir}/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

# remove wfut binary from package - will return it back when java wfut package will be obsoleted
rm -f $RPM_BUILD_ROOT%{_bindir}/wfut
rm -f $RPM_BUILD_ROOT%{_mandir}/man1/wfut.1

%check
make check

%ldconfig_scriptlets

%files
%doc AUTHORS COPYING ChangeLog NEWS README TODO
#%{_bindir}/wfut
#%{_mandir}/man1/wfut.1.gz
%{_libdir}/libwfut-0.2.so.*

%files devel
%{_includedir}/%{name}-0.2
%{_libdir}/libwfut-0.2.so
%{_libdir}/pkgconfig/*.pc

%changelog
%autochangelog
