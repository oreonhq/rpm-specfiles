%global source0_hash aa77fd90a88b83467cd8d2b39d80e4518ba2903d2e4ca50d32d1b96996685015
%global xfceversion 4.20
Name:           tumbler
Version:        4.20.2
Release:        1%{?dist}
Summary:        D-Bus service for applications to request thumbnails
License:        GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:            http://git.xfce.org/xfce/tumbler/
Source0:        https://archive.xfce.org/src/xfce/%{name}/%{xfceversion}/%{name}-%{version}.tar.bz2
%{?fedora:BuildRequires: libgsf-devel}
%{?fedora:BuildRequires: libopenraw-gnome-devel}
# oreon:deps
BuildRequires:  freetype-devel
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gstreamer1-plugins-base-devel
BuildRequires:  gtk2-devel
BuildRequires:  intltool
BuildRequires:  libgsf-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libopenraw-gnome-devel
BuildRequires:  libpng-devel
BuildRequires:  libxfce4util-devel
BuildRequires:  make
BuildRequires:  poppler-glib-devel
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
Tumbler is a D-Bus service for applications to request thumbnails for various
URI schemes and MIME types. It is an implementation of the thumbnail
management D-Bus specification described on
http://live.gnome.org/ThumbnailerSpec written in an object-oriented fashion

Additional thumbnailers can be found in the tumbler-extras package

%package extras
Summary:       Additional thumbnailers for %{name}
Requires:      %{name}%{?_isa} = %{version}-%{release}
%description extras
This package contains additional thumbnailers for file types, which are not used
very much and require additional libraries to be installed.

%package devel
Summary:       Development files for %{name}
Requires:      %{name}%{?_isa} = %{version}-%{release}
%description devel
This package contains libraries and header files for developing applications 
that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%configure --disable-static
sed --in-place --expression 's! -shared ! -Wl,--as-needed\0!g' libtool
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build
%install
%make_install
chmod 755 $RPM_BUILD_ROOT/%{_libdir}/*.so
find %{buildroot} -type f -name "*.la" -delete
%find_lang %{name}
%ldconfig_scriptlets
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n tumbler-extras -f %{oreon_filedir}/tumbler-extras.list
%files -n tumbler-devel -f %{oreon_filedir}/tumbler-devel.list

%changelog

%autochangelog
