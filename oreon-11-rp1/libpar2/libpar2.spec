%global source0_hash 074fbf840f73b1e13e0405fce261078c81c8c0a4859e30a7bba10510f9199908

Name:           libpar2
Version:        0.2       
Release:        46%{?dist}
Summary:        Library for performing comman tasks related to PAR recovery sets
     
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later        
URL:            http://parchive.sourceforge.net/           
Source0:        http://prdownloads.sourceforge.net/sourceforge/parchive/%{name}-%{version}.tar.gz   
Patch0:         libpar2-0.2-cancel.patch
Patch1:         libpar2-0.2-bugfixes.patch
  
BuildRequires:  gcc-c++
BuildRequires:  libsigc++20-devel libtool
BuildRequires:  sed
BuildRequires: make

%description
LibPar2 allows for the generation, modification, verification,
and repair of PAR v1.0 and PAR v2.0(PAR2) recovery sets.
It contains the basic functions needed for working with these
sets and is the basis for GUI applications such as GPar2.

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}-%{release}
Requires: libsigc++20-devel

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p2
%patch -P1 -p2
#fix source files
chmod -x *.cpp *.h ChangeLog
touch tmpfile -r README 
sed -i 's/\r//' README
touch -r tmpfile README
touch tmpfile -r ROADMAP 
sed -i 's/\r//' ROADMAP
touch -r tmpfile ROADMAP
touch tmpfile -r AUTHORS
sed -i 's/\r//' AUTHORS
touch -r tmpfile AUTHORS

%build
#fix aarch64 build
libtoolize
autoreconf -i

%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%ldconfig_scriptlets

%files
%{_libdir}/*.so.*
%doc COPYING README ChangeLog AUTHORS ROADMAP

%files devel
%{_includedir}/*
%{_libdir}/*.so
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/include/

%changelog
%autochangelog
