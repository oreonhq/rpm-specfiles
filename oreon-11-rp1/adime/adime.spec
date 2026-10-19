%global source0_hash 48268a07f3751e4540cfa6e601f86318a4db9f1fde3630ea11e3ed8539b50fa5
Name:           adime
Version:        2.2.1
Release:        1%{?dist}
Summary:        Allegro Dialogs Made Easy
License:        zlib
URL:            http://adime.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:         adime-2.2.1-so-fixes.patch
# oreon:deps
BuildRequires:  allegro-devel
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  texinfo
# /oreon:deps
%description
Adime is a portable add-on library for Allegro with functions for generating
Allegro dialogs in a very simple way. Its main purpose is to give as easy an
API as possible to people who want dialogs for editing many kinds of input
data.

%package devel
Summary: Development libraries and headers for adime
Requires: %{name} = %{version}-%{release}
Requires: allegro-devel
%description devel
The developmental files that must be installed in order to compile
applications which use adime.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -z .so-fixes
./fix.sh unix
rm docs/txt/tmpfile.txt
mkdir docs/html docs/rtf

%build

make %{?_smp_mflags} lib docs \
  CFLAGS="-fPIC -DPIC $RPM_OPT_FLAGS" \
  CFLAGS_NO_OPTIMIZE="-fPIC -DPIC $RPM_OPT_FLAGS" \
  LFLAGS=-g
%install
make install install-man install-info \
  SYSTEM_DIR=$RPM_BUILD_ROOT/usr \
  SYSTEM_LIB_DIR=$RPM_BUILD_ROOT%{_libdir} \
  SYSTEM_MAN_DIR=$RPM_BUILD_ROOT%{_mandir} \
  SYSTEM_INFO_DIR=$RPM_BUILD_ROOT%{_infodir}
rm $RPM_BUILD_ROOT%{_infodir}/dir
ln -s libadime.so.0 $RPM_BUILD_ROOT%{_libdir}/libadime.so
%ldconfig_scriptlets
%oreon_autofiles adime-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n adime-devel -f %{oreon_filedir}/adime-devel.list

%changelog

%autochangelog
