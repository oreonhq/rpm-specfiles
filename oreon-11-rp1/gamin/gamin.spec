%global source0_hash 28085f0ae8be10eab582ff186af4fb0be92cc6c62b5cc19cd09b295c7c2899a1

Name:           gamin
Version:        0.1.10
Release:        1%{?dist}
Summary:        File alteration monitor
License:        LGPL-2.0-or-later
URL:            https://download.gnome.org/sources/gamin/
Source0:        https://download.gnome.org/sources/gamin/0.1/gamin-%{version}.tar.gz
Patch0:         gamin-0.1.10-gcc14.patch
BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  make
BuildRequires:  pkgconfig

%description
Gamin is a file and directory monitoring system. The library is a
drop-in for the old FAM API.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       fam-devel = %{version}-%{release}

%description devel
Headers and the fam library for building software that uses gamin.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1

%build
%configure --disable-static --disable-debug-api --without-python --libexecdir=%{_libexecdir}
%make_build

%install
%make_install
find %{buildroot} -name '*.la' -delete
find %{buildroot} -name '*.a' -delete
ln -s gamin.pc %{buildroot}%{_libdir}/pkgconfig/fam.pc

%files
%license COPYING
%{_libexecdir}/gam_server
%{_libdir}/libfam.so.0
%{_libdir}/libfam.so.0.0.0
%{_libdir}/libgamin-1.so.0
%{_libdir}/libgamin-1.so.0.1.10

%files devel
%{_includedir}/fam.h
%{_libdir}/libfam.so
%{_libdir}/libgamin-1.so
%{_libdir}/pkgconfig/gamin.pc
%{_libdir}/pkgconfig/fam.pc
