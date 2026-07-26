%global source0_hash 453f7cc20ca90c5214e4d2f3e77cbeaa6d6fb0f69b7bdbf39050cb69a6e09a19

%global glib2_version 2.38.0
%global libsoup_version 3.1.2

# Packagers: This is the API version of libuhttpmock, as it allows
# for parallel installation of different major API versions (e.g. like
# GTK+ 2 and 3).
%global somajor 1
%global apiver %{somajor}.0

Name:           uhttpmock
Version:        0.11.0
Release:        5%{?dist}
Summary:        HTTP web service mocking library

License:        LGPL-2.1-or-later
URL:            https://gitlab.freedesktop.org/pwithnall/uhttpmock
Source:         %{url}/-/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  pkgconfig(glib-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(gio-2.0) >= %{glib2_version}
BuildRequires:  glib-networking
BuildRequires:  pkgconfig(libsoup-3.0) >= %{libsoup_version}
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(gtk-doc)
BuildRequires:  /usr/bin/vapigen

%description
uhttpmock is a project for mocking web service APIs which use HTTP or HTTPS.
It provides a library, libuhttpmock, which implements recording and
playback of HTTP request–response traces.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation files for %{name}
Enhances:       %{name}-devel = %{version}-%{release}
BuildArch:      noarch

%description    doc
The %{name}-doc package contains documentation for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%meson -Dgtk_doc=true -Dintrospection=true -Dvapi=enabled
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license COPYING
%doc README NEWS AUTHORS
%{_libdir}/lib%{name}-%{apiver}.so.%{somajor}{,.*}
%{_libdir}/girepository-1.0/Uhm-%{apiver}.typelib

%files devel
%{_includedir}/lib%{name}-%{apiver}/
%{_libdir}/lib%{name}-%{apiver}.so
%{_libdir}/pkgconfig/lib%{name}-%{apiver}.pc
%{_datadir}/gir-1.0/Uhm-%{apiver}.gir
%{_datadir}/vala/vapi/lib%{name}-%{apiver}.*

%files doc
%license COPYING
%{_datadir}/gtk-doc/html/lib%{name}-%{apiver}/

%changelog
%autochangelog
