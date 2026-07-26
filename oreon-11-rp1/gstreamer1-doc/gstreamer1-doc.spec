%global source0_hash none

%global         majorminor      1.0

Name:           gstreamer1-doc
Version:        1.28.1
Release:        1%{?dist}
BuildArch:      noarch
Summary:        GStreamer documentation

# All tutorial code is licensed under any of the following licenses (your choice):
#  BSD-2-Clause license ("simplified BSD license") (LICENSE.BSD)
#  MIT license (LICENSE.MIT)
#  LGPL-2.1-or-later (LICENSE.LGPL-2.1)
# Application Developer Manual and Plugin Writer's Guide
#  OPUBL-1.0 (LICENSE.OPL), for historical reasons.
#  this is not-allowed license with an exception, see https://gitlab.com/fedora/legal/fedora-license-data/-/merge_requests/827
# Documentation
#  CC-BY-SA-4.0, but some parts of the documentation
#  may still be licensed differently (e.g. LGPLv2.1) for historical reasons.
License:        (BSD-2-Clause or MIT OR LGPL-2.1-or-later) AND OPUBL-1.0 AND CC-BY-SA-4.0
URL:            http://gstreamer.freedesktop.org/
Source0:        https://gstreamer.freedesktop.org/src/gstreamer-docs/gstreamer-docs-%{version}.tar.xz

%description
GStreamer documentation.

%prep
%setup -q -n gstreamer-docs-%{version}

%install

# move devhelp into the right directory
mkdir -p $RPM_BUILD_ROOT%{_datadir}/gtk-doc/html/
mv devhelp/books/GStreamer $RPM_BUILD_ROOT%{_datadir}/gtk-doc/html/GStreamer-%{majorminor}
# Remove the search assets, we use devhelp search
rm -rf $RPM_BUILD_ROOT%{_datadir}/gtk-doc/html/GStreamer-%{majorminor}/assets/js/search
# Rename the devhelp docs to include the version
mv $RPM_BUILD_ROOT%{_datadir}/gtk-doc/html/GStreamer-%{majorminor}/GStreamer.devhelp2 \
   $RPM_BUILD_ROOT%{_datadir}/gtk-doc/html/GStreamer-%{majorminor}/GStreamer-%{majorminor}.devhelp2

%files
%doc README.md html
%{_datadir}/gtk-doc/html/GStreamer-%{majorminor}/

%changelog
%autochangelog
