%global source0_hash 3c05e05aebcbfcc044d9e8c2d4646cd8359be39a3f0ba8ce4e72a9094bee704f
Name:          libmms
Version:       0.6.4
Release:        30%{?dist}
Summary:        Library for Microsoft Media Server (MMS) streaming protocol
License:       LGPL-2.1-or-later
URL:           https://www.sf.net/projects/libmms
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch1:        0001-Remove-Requires-glib-2.0-since-libmms-no-longer-depe.patch
Patch2:        0002-Add-a-new-testfiledownload.c-example.patch
Patch3:        0003-Fix-build-if-strndup-is-missing.patch
Patch4:        0004-Patch-to-remove-redundant-comparison-in-file-mmsh.c.patch
Patch5:        0005-Avoid-possible-overflow-in-sprintf.patch
Patch6:        0006-Fix-possible-NULL-Pointer-deref-in-mmsh.c.patch
Patch7:        0007-Add-check-for-sys-select.h-and-use-it.patch
Patch8:        0008-C89-fixes-for-Haiku.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
MMS is a streaming protocol used in Microsoft server products, commonly used to
stream WMV data. You can encounter mms:// style URLs all over the net,
especially on news sites and other content-serving sites. Libmms allows you to
download content from such sites, making it easy to add MMS support to your
media applications.

%package devel
Summary:       Development package for %{name}
Requires:      %{name}%{_isa} = %{version}-%{release}
Requires:      pkgconf-pkg-config
%description devel
This package contains development files for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
chmod -x ChangeLog src/mmsh.c

%build

./autogen.sh
%configure --disable-static
%make_build
%install
%make_install
rm %{buildroot}%{_libdir}/%{name}.la
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libmms-devel -f %{oreon_filedir}/libmms-devel.list

%changelog

%autochangelog
