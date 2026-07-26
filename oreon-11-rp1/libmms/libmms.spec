%global source0_hash 3c05e05aebcbfcc044d9e8c2d4646cd8359be39a3f0ba8ce4e72a9094bee704f

Name:          libmms
Version:       0.6.4
Release:       30%{?dist}
Summary:       Library for Microsoft Media Server (MMS) streaming protocol
License:       LGPL-2.1-or-later
URL:           https://www.sf.net/projects/libmms
Source0:       https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# https://sourceforge.net/p/libmms/code/ci/b9bbe17c08e5dcbe3ce841e6bed52ce8d8b10f9e/
Patch1:        0001-Remove-Requires-glib-2.0-since-libmms-no-longer-depe.patch
# https://sourceforge.net/p/libmms/code/ci/34060b0c0cb13eed323577becf72a13b43654c00/
Patch2:        0002-Add-a-new-testfiledownload.c-example.patch
# https://sourceforge.net/p/libmms/code/ci/67d54003b8075b8ea8102bc4a808df4543ab113a/
Patch3:        0003-Fix-build-if-strndup-is-missing.patch
# https://sourceforge.net/p/libmms/code/ci/5cface3df0e0213d8bc593d82a9a7c1e648dd71a/
Patch4:        0004-Patch-to-remove-redundant-comparison-in-file-mmsh.c.patch
# https://sourceforge.net/p/libmms/code/ci/8b5e303fc1f01521c727e351270dd68c4f15190b/
Patch5:        0005-Avoid-possible-overflow-in-sprintf.patch
# https://sourceforge.net/p/libmms/code/ci/5cface3df0e0213d8bc593d82a9a7c1e648dd71a/
Patch6:        0006-Fix-possible-NULL-Pointer-deref-in-mmsh.c.patch
# https://sourceforge.net/p/libmms/code/ci/5d39f692d55c04839be78e470820f49d53e40bcb/
Patch7:        0007-Add-check-for-sys-select.h-and-use-it.patch
# https://sourceforge.net/p/libmms/code/ci/a9f692323e597324e6f01263c12b6f4290d5b56f/
Patch8:        0008-C89-fixes-for-Haiku.patch

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gcc
BuildRequires: libtool
BuildRequires: make

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

%files
%doc AUTHORS ChangeLog README*
%license COPYING.LIB
%{_libdir}/%{name}.so.0{,.*}

%files devel
%{_includedir}/%{name}
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
