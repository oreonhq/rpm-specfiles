%global source0_hash 392ec2d06d50300dcff1ef269a2a985304e29bce3520002fca29f2edc1d138d1
Name:           phodav
Version:        3.0
Release:        1%{?dist}
Summary:        A WebDAV server using libsoup3
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://wiki.gnome.org/phodav
Source0:        http://download.gnome.org/sources/%{name}/%{version}/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  asciidoc
BuildRequires:  avahi-gobject-devel
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  git-core
BuildRequires:  gtk-doc
BuildRequires:  libsoup3-devel
BuildRequires:  libxml2-devel
BuildRequires:  meson
BuildRequires:  systemd-devel
BuildRequires:  systemd-units
BuildRequires:  xmlto
# /oreon:deps
%description
phởdav is a WebDAV server implementation using libsoup3 (RFC 4918).

%package -n     libphodav
Summary:        A library to serve files with WebDAV
Obsoletes:      libphodav-2.0 <= 0:2.0-3
Obsoletes:      libphodav2 <= 0:2.0-4
Obsoletes:      libphodav-1.0 <= 0:0.4-6
%description -n libphodav
phởdav is a WebDAV server implementation using libsoup3 (RFC 4918).
This package provides the library.

%package -n     libphodav-devel
Summary:        Development files for libphodav
Requires:       libphodav%{?_isa} = %{version}-%{release}
Obsoletes:      libphodav-2.0-devel <= 0:2.0-3
Obsoletes:      libphodav2-devel <= 0:2.0-4
Obsoletes:      libphodav-1.0-devel <= 0:0.4-6
%description -n libphodav-devel
The libphodav-devel package includes the header files for libphodav.

%package -n     chezdav
Summary:        A simple WebDAV server program
%description -n chezdav
The chezdav package contains a simple tool to share a directory
with WebDAV. The service is announced over mDNS for clients to discover.

%package -n     spice-webdavd
Summary:        Spice daemon for the DAV channel
Requires:       avahi
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units
%description -n spice-webdavd
The spice-webdavd package contains a daemon to proxy WebDAV request to
the Spice virtio channel.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson -Dsystemdsystemunitdir=%{_unitdir} -Dudevrulesdir=%{_udevrulesdir} || cat %_vpath_builddir/meson-logs/meson-log.txt
%meson_build
%install
%meson_install
%find_lang phodav-3.0 --with-gnome
%ldconfig_scriptlets -n libphodav
%oreon_autofiles libphodav usr/*/lib*.so.*
%oreon_autofiles libphodav-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles chezdav usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles spice-webdavd usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post -n spice-webdavd

%systemd_post spice-webdavd.service
%preun -n spice-webdavd

%systemd_preun spice-webdavd.service
%postun -n spice-webdavd

%systemd_postun_with_restart spice-webdavd.service
%files -f %{oreon_filedir}/main.list
%files -n libphodav -f %{oreon_filedir}/libphodav.list
%files -n libphodav-devel -f %{oreon_filedir}/libphodav-devel.list
%files -n chezdav -f %{oreon_filedir}/chezdav.list
%files -n spice-webdavd -f %{oreon_filedir}/spice-webdavd.list

%changelog

%autochangelog

