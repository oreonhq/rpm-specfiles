%global source0_hash 5d3d67b1244a10cee0e89b045766c05fe1035f7938f0410ac6a3d8222b5df907
%global xfceversion 4.20
%global namespc Libxfce4ui
Name:           libxfce4ui
Version:        4.20.2
Release:        1%{?dist}
Summary:        Commonly used Xfce widgets
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://xfce.org/
Source0:        http://archive.xfce.org/src/xfce/%{name}/%{xfceversion}/%{name}-%{version}.tar.bz2
Patch10:        libxfce4ui-%{xfceversion}-keyboard-shortcuts.patch
Obsoletes:      libxfcegui4 < 4.10.0-9
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  glade-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  gtk3-devel
BuildRequires:  intltool
BuildRequires:  libSM-devel
BuildRequires:  libgtop2-devel
BuildRequires:  make
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(libstartup-notification-1.0)
BuildRequires:  pkgconfig(libxfce4util-1.0)
BuildRequires:  pkgconfig(libxfconf-0)
BuildRequires:  vala
# /oreon:deps
%description
Libxfce4ui is used to share commonly used Xfce widgets among the Xfce
applications.

%package -n     xfce4-about
Summary:        Xfce 4 'About' dialog
%description -n xfce4-about
This package contains the 'About Xfce' dialog with info on the desktop
environment, it's contributors, and it's licensing.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       gtk2-devel
Requires:       libxfce4util-devel
Requires:       glade-devel
Requires:       pkgconfig
Obsoletes:      libxfcegui4-devel < 4.10.0-9
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch 10

%build

%configure --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
export LD_LIBRARY_PATH="`pwd`/libxfce4ui/.libs"
%make_build
%install
%make_install
chmod 755 %{buildroot}%{_libdir}/*.so
find %{buildroot} -name '*.la' -exec rm -f {} ';'
%find_lang %{name}
desktop-file-install \
  --delete-original \
  --remove-category=X-Xfce-Toplevel \
  --add-category=Documentation \
  --add-category=System \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/xfce4-about.desktop
%ldconfig_scriptlets
%oreon_autofiles xfce4-about usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n xfce4-about -f %{oreon_filedir}/xfce4-about.list
%files -n libxfce4ui-devel -f %{oreon_filedir}/libxfce4ui-devel.list

%changelog

%autochangelog
