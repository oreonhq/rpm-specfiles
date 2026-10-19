%global source0_hash ea54e92b8cb06690617a5409577f287e6fb8a7bfc7d6bf390cf7fea4d418ef9e
%global         majorminor      1.0
Name:           gstreamer1-doc
Version:        1.28.7
Release:        1%{?dist}
BuildArch:      noarch
Summary:        GStreamer documentation
License:        (BSD-2-Clause or MIT OR LGPL-2.1-or-later) AND OPUBL-1.0 AND CC-BY-SA-4.0
URL:            http://gstreamer.freedesktop.org/
Source0:        https://gstreamer.freedesktop.org/src/gstreamer-docs/gstreamer-docs-%{version}.tar.xz
# oreon:deps

# /oreon:deps
%description
GStreamer documentation.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n gstreamer-docs-%{version}

%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/gtk-doc/html/
mv devhelp/books/GStreamer $RPM_BUILD_ROOT%{_datadir}/gtk-doc/html/GStreamer-%{majorminor}
rm -rf $RPM_BUILD_ROOT%{_datadir}/gtk-doc/html/GStreamer-%{majorminor}/assets/js/search
mv $RPM_BUILD_ROOT%{_datadir}/gtk-doc/html/GStreamer-%{majorminor}/GStreamer.devhelp2 \
   $RPM_BUILD_ROOT%{_datadir}/gtk-doc/html/GStreamer-%{majorminor}/GStreamer-%{majorminor}.devhelp2
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
