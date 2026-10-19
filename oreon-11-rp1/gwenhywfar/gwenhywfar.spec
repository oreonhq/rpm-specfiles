%global source0_hash 8916feaa99cb954f963f2cba8dd2dffe57cacf7f284daf00eab071aad6fe2ab3
Summary:        A multi-platform helper library for other libraries
Name: gwenhywfar
Version: 5.14.1
Release:        1%{?dist}
URL: https://www.aquamaniac.de/rdm/projects/gwenhywfar
Source0:        https://www.aquamaniac.de/rdm/attachments/download/630/%{name}-%{version}.tar.gz
License: LGPL-2.1-or-later
Requires: ca-certificates
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Qt6Core)
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  gnutls-devel
BuildRequires:  gtk3-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  openssl-devel
# /oreon:deps
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
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

export CFLAGS="$CFLAGS -std=gnu17"
export CXXFLAGS="$CXXFLAGS -std=gnu++17"
export PKG_CONFIG=/usr/bin/pkg-config
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
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build
%install
%make_install
rm -f  %{buildroot}%{_datadir}/%{name}/ca-bundle.crt
ln -sf %{_sysconfdir}/pki/tls/certs/ca-bundle.crt \
       %{buildroot}%{_datadir}/%{name}/ca-bundle.crt
rm -fv %{buildroot}%{_libdir}/lib*.la
%find_lang %{name}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n gwenhywfar-devel -f %{oreon_filedir}/gwenhywfar-devel.list
%files -n gwenhywfar-gui-gtk3 -f %{oreon_filedir}/gwenhywfar-gui-gtk3.list
%files -n gwenhywfar-gui-gtk3-devel -f %{oreon_filedir}/gwenhywfar-gui-gtk3-devel.list
%files -n gwenhywfar-gui-cpp -f %{oreon_filedir}/gwenhywfar-gui-cpp.list
%files -n gwenhywfar-gui-cpp-devel -f %{oreon_filedir}/gwenhywfar-gui-cpp-devel.list
%files -n gwenhywfar-gui-qt6 -f %{oreon_filedir}/gwenhywfar-gui-qt6.list
%files -n gwenhywfar-gui-qt6-devel -f %{oreon_filedir}/gwenhywfar-gui-qt6-devel.list

%changelog

%autochangelog
