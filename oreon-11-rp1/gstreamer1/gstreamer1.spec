%global source0_hash 18a5e214114dc501407697dd458514bba62cadd5414c60f793cf70141a4d0bb3

%global         majorminor      1.0

#global gitrel     140
#global gitcommit  a70055b58568f7304ba46bd8742232337013487b
#global shortcommit %%(c=%%{gitcommit}; echo ${c:0:5})

%global         _glib2                  2.32.0
%global         _libxml2                2.4.0
%global         _gobject_introspection  1.31.1
%global 	__python %{__python3}

%if 0%{?fedora}
%bcond_without unwind
%else
%bcond_with unwind
%endif

Name:           gstreamer1
Version:        1.26.7
Release:        2%{?dist}
Summary:        GStreamer streaming media framework runtime

License:        LGPL-2.1-or-later
URL:            http://gstreamer.freedesktop.org/
%if 0%{?gitrel}
# git clone git://anongit.freedesktop.org/gstreamer/gstreamer
# cd gstreamer; git reset --hard %%{gitcommit}; ./autogen.sh; make; make distcheck
Source0:        http://gstreamer.freedesktop.org/src/gstreamer/gstreamer-%{version}.tar.xz
%else
Source0:        http://gstreamer.freedesktop.org/src/gstreamer/gstreamer-%{version}.tar.xz
%endif
## For GStreamer RPM provides
Patch0:         0001-gst-inspect-add-mode-to-output-RPM-requires-format.patch
Source1:        gstreamer1.prov
Source2:        gstreamer1.attr

BuildRequires:  meson >= 0.48.0
BuildRequires:  gcc
BuildRequires:  libatomic
BuildRequires:  glib2-devel >= %{_glib2}
BuildRequires:  libxml2-devel >= %{_libxml2}
BuildRequires:  gobject-introspection-devel >= %{_gobject_introspection}
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  check-devel
BuildRequires:  gettext
BuildRequires:  pkgconfig
BuildRequires:  libcap-devel
%if %{with unwind}
BuildRequires:  libunwind-devel
%endif
BuildRequires:  elfutils-devel
%if 0%{?fedora} >= 41 || 0%{?rhel} >= 11 
BuildRequires:  bash-completion-devel
%else
BuildRequires: bash-completion
%endif
BuildRequires:  rustc

%description
GStreamer is a streaming media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new 
plugins.


%package devel
Summary:        Libraries/include files for GStreamer streaming media framework
Requires:       %{name}%{?isa} = %{version}-%{release}
Requires:       glib2-devel%{?_isa} >= %{_glib2}
Requires:       libxml2-devel%{?_isa} >= %{_libxml2}
Requires:       check-devel
# file /usr/include/gstreamer-1.0/gst/base/gstaggregator.h conflicts between attempted installs of gstreamer1-plugins-bad-free-devel-1.12.4-3.fc28.x86_64 and gstreamer1-devel-1.13.1-1.fc29.x86_64
Conflicts:      gstreamer1-plugins-bad-free-devel < 1.13

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%if 0
%package devel-docs
Summary:         Developer documentation for GStreamer streaming media framework
Requires:        %{name} = %{version}-%{release}
BuildArch:       noarch

%description devel-docs
This %{name}-devel-docs contains developer documentation for the
GStreamer streaming media framework.
%endif


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n gstreamer-%{version}
%patch -P 0 -p3 -b .rpm-provides

%build
%meson	\
  -D package-name='Fedora GStreamer package' \
  -D package-origin='http://download.fedoraproject.org' \
  -D tests=disabled -D examples=disabled \
  -D ptp-helper-permissions=capabilities \
  %{!?with_unwind:-D libunwind=disabled -D libdw=disabled } \
  -D dbghelp=disabled \
  -D doc=disabled
%meson_build

%install
%meson_install

%find_lang gstreamer-%{majorminor}
# Add the provides script
install -m0755 -D %{SOURCE1} $RPM_BUILD_ROOT%{_rpmconfigdir}/gstreamer1.prov
# Add the gstreamer plugin file attribute entry (rpm >= 4.9.0)
install -m0644 -D %{SOURCE2} $RPM_BUILD_ROOT%{_rpmconfigdir}/fileattrs/gstreamer1.attr

%ldconfig_scriptlets

%files -f gstreamer-%{majorminor}.lang
%license COPYING
%doc README.md README.static-linking RELEASE
%{_libdir}/libgstreamer-%{majorminor}.so.*
%{_libdir}/libgstbase-%{majorminor}.so.*
%{_libdir}/libgstcheck-%{majorminor}.so.*
%{_libdir}/libgstcontroller-%{majorminor}.so.*
%{_libdir}/libgstnet-%{majorminor}.so.*

%dir %{_libexecdir}/gstreamer-%{majorminor}/
%{_libexecdir}/gstreamer-%{majorminor}/gst-completion-helper
%{_libexecdir}/gstreamer-%{majorminor}/gst-hotdoc-plugins-scanner
%{_libexecdir}/gstreamer-%{majorminor}/gst-plugins-doc-cache-generator
%{_libexecdir}/gstreamer-%{majorminor}/gst-plugin-scanner
%attr(755,root,root) %caps(cap_net_bind_service,cap_net_admin,cap_sys_nice=ep) %{_libexecdir}/gstreamer-%{majorminor}/gst-ptp-helper
#%%{_libexecdir}/gstreamer-%%{majorminor}/gst-ptp-helper-test

%dir %{_libdir}/gstreamer-%{majorminor}
%{_libdir}/gstreamer-%{majorminor}/libgstcoreelements.so
%{_libdir}/gstreamer-%{majorminor}/libgstcoretracers.so

%{_libdir}/girepository-1.0/Gst-%{majorminor}.typelib
%{_libdir}/girepository-1.0/GstBase-%{majorminor}.typelib
%{_libdir}/girepository-1.0/GstCheck-%{majorminor}.typelib
%{_libdir}/girepository-1.0/GstController-%{majorminor}.typelib
%{_libdir}/girepository-1.0/GstNet-%{majorminor}.typelib

%{_bindir}/gst-inspect-%{majorminor}
%{_bindir}/gst-launch-%{majorminor}
%{_bindir}/gst-stats-%{majorminor}
%{_bindir}/gst-typefind-%{majorminor}

%{_rpmconfigdir}/gstreamer1.prov
%{_rpmconfigdir}/fileattrs/gstreamer1.attr

%doc %{_mandir}/man1/gst-inspect-%{majorminor}.*
%doc %{_mandir}/man1/gst-launch-%{majorminor}.*
%doc %{_mandir}/man1/gst-stats-%{majorminor}.*
%doc %{_mandir}/man1/gst-typefind-%{majorminor}.*

%{_datadir}/bash-completion/completions/gst-inspect-1.0
%{_datadir}/bash-completion/completions/gst-launch-1.0
%{_datadir}/bash-completion/helpers/gst

%files devel
%dir %{_includedir}/gstreamer-%{majorminor}
%dir %{_includedir}/gstreamer-%{majorminor}/gst
%dir %{_includedir}/gstreamer-%{majorminor}/gst/base
%dir %{_includedir}/gstreamer-%{majorminor}/gst/check
%dir %{_includedir}/gstreamer-%{majorminor}/gst/controller
%dir %{_includedir}/gstreamer-%{majorminor}/gst/net
%{_includedir}/gstreamer-%{majorminor}/gst/*.h
%{_includedir}/gstreamer-%{majorminor}/gst/base/*.h
%{_includedir}/gstreamer-%{majorminor}/gst/check/*.h
%{_includedir}/gstreamer-%{majorminor}/gst/controller/*.h
%{_includedir}/gstreamer-%{majorminor}/gst/net/*.h

%{_libdir}/libgstreamer-%{majorminor}.so
%{_libdir}/libgstbase-%{majorminor}.so
%{_libdir}/libgstcheck-%{majorminor}.so
%{_libdir}/libgstcontroller-%{majorminor}.so
%{_libdir}/libgstnet-%{majorminor}.so

%{_datadir}/gir-1.0/Gst-%{majorminor}.gir
%{_datadir}/gir-1.0/GstBase-%{majorminor}.gir
%{_datadir}/gir-1.0/GstCheck-%{majorminor}.gir
%{_datadir}/gir-1.0/GstController-%{majorminor}.gir
%{_datadir}/gir-1.0/GstNet-%{majorminor}.gir

%{_datadir}/aclocal/gst-element-check-%{majorminor}.m4

%dir %{_datadir}/gstreamer-%{majorminor}/gdb
%{_datadir}/gstreamer-%{majorminor}/gdb/
%{_datadir}/gdb/auto-load/

%{_libdir}/pkgconfig/gstreamer-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-base-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-controller-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-check-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-net-%{majorminor}.pc

%{_datadir}/cmake/FindGStreamer.cmake

%if 0
%files devel-docs
%doc %{_datadir}/gtk-doc/html/gstreamer-%{majorminor}
%doc %{_datadir}/gtk-doc/html/gstreamer-libs-%{majorminor}
%doc %{_datadir}/gtk-doc/html/gstreamer-plugins-%{majorminor}
%endif


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.28.1-1
- Prepare for Oreon 11 (RP1)
