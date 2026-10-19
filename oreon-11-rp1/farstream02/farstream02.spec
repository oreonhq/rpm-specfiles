%global source0_hash cb7d112433cf7c2e37a8ec918fb24f0ea5cb293cfa1002488e431de26482f47b
%global glib2_ver 2.40
%global gst_ver 1.0.0
%global gst_plugins_base_ver 1.0.0
%global far farstream
Name:           %{far}02
Version:        0.2.9
Release:        1%{?dist}
Summary:        Libraries for videoconferencing
License:        LicenseRef-Callaway-LGPLv2+ AND GPL-2.0-or-later
URL:            https://www.freedesktop.org/wiki/Software/Farstream/
Source0:        https://freedesktop.org/software/%{far}/releases/%{far}/%{far}-%{version}.tar.gz
Patch0:         farstream-0.2.8-configure-add-check-for-glib-mkenums.patch
Patch1:         farstream-0.2.9-build-Adapt-to-backwards-incompatible-change-in-GNU-.patch
Requires:       glib2%{?isa} >= %{glib2_ver}
Requires:       gstreamer1-plugins-good >= 1.0.0
Requires:       gstreamer1-plugins-bad-free >= 1.0.0
Requires:       libnice-gstreamer1
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  gstreamer1-devel
BuildRequires:  gstreamer1-plugins-base-devel
BuildRequires:  gtk-doc
BuildRequires:  gupnp-igd-devel
BuildRequires:  libnice-devel
BuildRequires:  make
# /oreon:deps
%description
%{name} is a collection of GStreamer modules and libraries for
videoconferencing.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gstreamer1-devel  >= %{gst_ver}
Requires:       gstreamer1-plugins-base-devel >= %{gst_plugins_base_ver}
Requires:       pkgconfig
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{far}-%{version}
%patch -P0 -p1
%patch -P1 -p1

%check

%build

autoreconf --force --install
%configure                                                  \
  --with-package-name='Fedora Farstream-0.2 package'        \
  --with-package-origin='http://download.fedoraproject.org' \
  --disable-silent-rules                                    \
  --disable-static
make
%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n farstream02-devel -f %{oreon_filedir}/farstream02-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.2.9-20
- Prepare for Oreon 11 (RP1)
