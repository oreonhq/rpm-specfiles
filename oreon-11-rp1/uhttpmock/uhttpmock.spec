%global source0_hash 453f7cc20ca90c5214e4d2f3e77cbeaa6d6fb0f69b7bdbf39050cb69a6e09a19
%global glib2_version 2.38.0
%global libsoup_version 3.1.2
%global somajor 1
%global apiver %{somajor}.0
Name:           uhttpmock
Version:        0.11.0
Release:        1%{?dist}
Summary:        HTTP web service mocking library
License:        LGPL-2.1-or-later
URL:            https://gitlab.freedesktop.org/pwithnall/uhttpmock
Source0:        https://gitlab.freedesktop.org/pwithnall/%{name}/-/archive/%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  /usr/bin/vapigen
BuildRequires:  gcc
BuildRequires:  glib-networking
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk-doc)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(libxml-2.0)
# /oreon:deps
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
%oreon_prep
%build

%meson -Dgtk_doc=true -Dintrospection=true -Dvapi=enabled
%meson_build
%install
%meson_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%meson_test
%files -f %{oreon_filedir}/main.list
%files -n uhttpmock-devel -f %{oreon_filedir}/uhttpmock-devel.list
%files -n uhttpmock-doc -f %{oreon_filedir}/uhttpmock-doc.list

%changelog

%autochangelog
