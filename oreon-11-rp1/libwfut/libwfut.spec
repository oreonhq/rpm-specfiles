%global source0_hash 35d78954b2b20c4bbf45bdbd2ac2624dd3df29aa599018c46883917ad0506b6f
Name:           libwfut
Version:        0.2.3
Release:        1%{?dist}
Summary:        Software updater tool for WorldForge applications
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://www.worldforge.org/
Source0:        http://downloads.sourceforge.net/worldforge/%{name}-%{version}.tar.gz
Patch0:         libwfut-0.2.3-Remove-reference-to-object_slot-h.patch
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  libcurl-devel
BuildRequires:  libsigc++20-devel
BuildRequires:  make
BuildRequires:  swig
BuildRequires:  tinyxml-devel
BuildRequires:  zlib-devel
# /oreon:deps
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
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}
%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_bindir}/wfut
rm -f $RPM_BUILD_ROOT%{_mandir}/man1/wfut.1
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make check
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n libwfut-devel -f %{oreon_filedir}/libwfut-devel.list

%changelog

%autochangelog
