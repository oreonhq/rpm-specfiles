%global source0_hash 8916feaa99cb954f963f2cba8dd2dffe57cacf7f284daf00eab071aad6fe2ab3

Summary: A multi-platform helper library for other libraries
Name: gwenhywfar
Version: 5.14.1
Release: 2%{?dist}

URL: https://www.aquamaniac.de/rdm/projects/gwenhywfar
# Download is PHP form at http://www.aquamaniac.de/sites/download/packages.php
Source: https://www.aquamaniac.de/rdm/attachments/download/630/%{name}-%{version}.tar.gz
License: LGPL-2.1-or-later

BuildRequires: cmake gcc gcc-c++
BuildRequires: gnutls-devel gettext libgcrypt-devel openssl-devel
BuildRequires: gtk3-devel >= 3.14.0
BuildRequires: cmake(Qt6Core)

Requires: ca-certificates

%description
This is Gwenhywfar, a multi-platform helper library for networking and
security applications and libraries. It is heavily used by libchipcard
and AqBanking/AqHBCI, the German online banking libraries.

%package devel
Summary: Gwenhywfar core development kit
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
This package contains gwenhywfar-config and header files for writing and
compiling programs using Gwenhywfar.

%package gui-gtk3
Summary: Gwenhywfar GUI framework for GTK3
Obsoletes: %{name}-gui-gtk2 <= %{version}-%{release}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description gui-gtk3
This package contains the gtk3 gwenhywfar GUI backend.

%package gui-gtk3-devel
Summary: Development files for %{name}-gui-gtk3
Obsoletes: %{name}-gui-gtk2-devel <= %{version}-%{release}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description gui-gtk3-devel
%{summary}.

%package gui-cpp
Summary: Gwenhywfar GUI framework for cpp
Requires: %{name}%{?_isa} = %{version}-%{release}
%description gui-cpp
This package contains the cpp gwenhywfar GUI backend.

%package gui-cpp-devel
Summary: Development files for %{name}-gui-cpp
Requires: %{name}-gui-cpp%{?_isa} = %{version}-%{release}
%description gui-cpp-devel
%{summary}.

%package gui-qt6
Summary: Gwenhywfar GUI framework for Qt6
Requires: %{name}-gui-cpp%{?_isa} = %{version}-%{release}
Obsoletes: %{name}-gui-qt5 <= %{version}-%{release}
%description gui-qt6
This package contains the qt6 gwenhywfar GUI backend.

%package gui-qt6-devel
Summary: Development files for %{name}-qt6-cpp
Requires: %{name}-gui-qt6%{?_isa} = %{version}-%{release}
Requires: %{name}-gui-cpp-devel%{?_isa} = %{version}-%{release}
Obsoletes: %{name}-gui-qt5-devel <= %{version}-%{release}
%description gui-qt6-devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version}

%build
export CFLAGS="$CFLAGS -std=gnu17"
export CXXFLAGS="$CXXFLAGS -std=gnu++17"
# avoid detection/use of stuff like x86_64-redhat-linux-gnu-pkg-config -- rdieter
export PKG_CONFIG=/usr/bin/pkg-config
# help configure find qt5 lrelease/lupdate
export QT6_HOST_BINS=$($PKG_CONFIG --variable=host_bins Qt6Core)
export PATH=$PATH:$QT6_HOST_BINS

%configure \
  --disable-static\
  --enable-system-certs \
  --with-guis="gtk3 qt5" \
  --with-openssl-libs=%{_libdir} \
  --with-qt6-qmake=$QT6_HOST_BINS/qmake \
  --with-qt6-moc=$QT6_HOST_BINS/moc \
  --with-qt6-uic=$QT6_HOST_BINS/uic \

# kill rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build

%install
%make_install

# use system ca-certificates
rm -f  %{buildroot}%{_datadir}/%{name}/ca-bundle.crt
ln -sf %{_sysconfdir}/pki/tls/certs/ca-bundle.crt \
       %{buildroot}%{_datadir}/%{name}/ca-bundle.crt
rm -fv %{buildroot}%{_libdir}/lib*.la

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS README ChangeLog
%license COPYING
%{_bindir}/gct-tool
%{_libdir}/libgwenhywfar.so.79*
%{_libdir}/gwenhywfar/
%dir %{_datadir}/gwenhywfar/
%{_datadir}/gwenhywfar/dialogs
# symlink
%{_datadir}/gwenhywfar/ca-bundle.crt

%files devel
%{_bindir}/gsa
%{_bindir}/gwenhywfar-config
%{_bindir}/mklistdoc
%{_bindir}/typemaker*
%{_bindir}/xmlmerge
%{_bindir}/gwbuild
%dir %{_includedir}/gwenhywfar5/
%{_includedir}/gwenhywfar5/gwenhywfar/
%{_libdir}/libgwenhywfar.so
%{_libdir}/cmake/gwenhywfar-*/
%{_datadir}/aclocal/gwenhywfar.m4
%{_datadir}/%{name}/typemaker*
%{_libdir}/pkgconfig/gwenhywfar.pc
%{_datadir}/gwenbuild/templates
%{_datadir}/%{name}/gwenbuild

%files gui-gtk3
%{_libdir}/libgwengui-gtk3.so.79*

%files gui-gtk3-devel
%{_libdir}/libgwengui-gtk3.so
%{_libdir}/pkgconfig/gwengui-gtk3.pc
%{_includedir}/gwenhywfar5/gwen-gui-gtk3/

%files gui-cpp
%{_libdir}/libgwengui-cpp.so.79*
%{_includedir}/gwenhywfar5/gwen-gui-cpp/

%files gui-cpp-devel
%{_libdir}/libgwengui-cpp.so
%{_libdir}/cmake/gwengui-cpp-*/

%files gui-qt6
%{_libdir}/libgwengui-qt6.so.79*

%files gui-qt6-devel
%{_libdir}/libgwengui-qt6.so
%{_libdir}/cmake/gwengui-qt6-*/
%{_libdir}/pkgconfig/gwengui-qt6.pc
%{_includedir}/gwenhywfar5/gwen-gui-qt5/

%changelog
%autochangelog
