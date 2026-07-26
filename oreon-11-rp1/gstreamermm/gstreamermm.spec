%global source0_hash 6b29c0c78a22e3b313d5b1e78488a488605a4d17ba1f69b5476c9bad746dbba0

%bcond mingw %[0%{?fedora} && !0%{?flatpak}]

%global api_ver 1.0
%global branch 1.10
%global mingw32_pkg_name mingw32-%{name}
%global mingw64_pkg_name mingw64-%{name}

Name:           gstreamermm
Version:        1.10.0
Release:        28%{?dist}

Summary:        C++ wrapper for GStreamer library

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://www.gtkmm.org/
Source0:        https://download.gnome.org/sources/gstreamermm/%{branch}/%{name}-%{version}.tar.xz
Patch0:         https://gitlab.gnome.org/GNOME/gstreamermm/-/merge_requests/4.patch
# https://gitlab.gnome.org/GNOME/gstreamermm/-/issues/13
Patch1:         %{name}-tests.patch
# https://gitlab.gnome.org/GNOME/gstreamermm/-/merge_requests/6
Patch2:         %{name}-mingw.patch
# Don't hardcode -std=c++11 or -std=c++0x
Patch3:         %{name}-nostdcxx.patch

BuildRequires:  gcc-c++
BuildRequires: glibmm24-devel >= 2.21.1
# Enable GUI examples build as a test
BuildRequires: gtkmm30-devel >= 3.0
BuildRequires: gstreamer1-devel
BuildRequires: gstreamer1-plugins-base-devel
# Required for building tests
BuildRequires: gtest-devel
BuildRequires: libxml++-devel >= 2.14.0
BuildRequires: doxygen graphviz m4
%if %{with mingw}
BuildRequires: mingw32-filesystem
BuildRequires: mingw64-filesystem
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw32-glibmm24
BuildRequires: mingw64-glibmm24
BuildRequires: mingw32-gtkmm30
BuildRequires: mingw64-gtkmm30
BuildRequires: mingw32-gstreamer1
BuildRequires: mingw64-gstreamer1
BuildRequires: mingw32-gstreamer1-plugins-base
BuildRequires: mingw64-gstreamer1-plugins-base
%endif

%description
GStreamermm is a C++ wrapper library for the multimedia library
GStreamer (http://gstreamer.freedesktop.org).  It is designed to allow
C++ development of applications that work with multi-media.

%package        devel
Summary:        Headers for developing programs that will use %{name}
Requires:       %{name} = %{version}-%{release}

%description devel
This package contains the static libraries and header files needed for
developing gstreamermm applications.

%package          doc
Summary:          Developer's documentation for the gstreamermm library
BuildArch:        noarch
BuildRequires:    doxygen graphviz
BuildRequires: make
Requires:         glibmm24-doc

%description      doc
This package contains developer's documentation for the GStreamermm
library. Gstreamermm is the C++ API for the GStreamer library.

The documentation can be viewed either through the devhelp
documentation browser or through a web browser.

%if %{with mingw}
%package -n mingw32-gstreamermm
Summary: MingwGW Windows C++ wrapper for GStreamer library
BuildArch: noarch

%description -n mingw32-gstreamermm
GStreamermm is a C++ wrapper library for the multimedia library
GStreamer (http://gstreamer.freedesktop.org).  It is designed to allow
C++ development of applications that work with multi-media.

%package -n mingw32-gstreamermm-devel
Summary:        Development files for %{name}
Requires:       mingw32-%{name} = %{version}-%{release}

%description -n mingw32-gstreamermm-devel
The mingw32-%{name}-devel package contains libraries and header files for
developing applications that use mingw32-%{name}.

%package -n mingw64-gstreamermm
Summary: MingwGW Windows C++ wrapper for GStreamer library
BuildArch: noarch

%description -n mingw64-gstreamermm
GStreamermm is a C++ wrapper library for the multimedia library
GStreamer (http://gstreamer.freedesktop.org).  It is designed to allow
C++ development of applications that work with multi-media.

%package -n mingw64-gstreamermm-devel
Summary:        Development files for %{name}
Requires:       mingw64-%{name} = %{version}-%{release}

%description -n mingw64-gstreamermm-devel
The mingw64-%{name}-devel package contains libraries and header files for
developing applications that use mingw64-%{name}.

%{?mingw_debug_package}
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch 0 -p1
%patch 1 -p1 -b .tests
%patch 2 -p1 -b .mingw
%patch 3 -p1 -b .nostdcxx

%build
mkdir %{_target_os}
pushd %{_target_os}
%define _configure ../configure
mkdir -p gstreamer/src
%configure
%make_build
popd

%if %{with mingw}
%mingw_configure
%mingw_make_build
%endif

%install
pushd %{_target_os}
%make_install
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'
popd

%if %{with mingw}
%mingw_make_install
%mingw_debug_install_post

rm -rv %{buildroot}{%{mingw32_docdir},%{mingw64_docdir}}/%{name}-%{api_ver}
%endif

%check
pushd %{_target_os}
%make_build check
popd

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/libgstreamermm-1.0.so.1{,.0.0}

%files devel
%{_includedir}/%{name}-%{api_ver}
%{_libdir}/libgstreamermm-1.0.so
%{_libdir}/pkgconfig/gstreamermm-1.0.pc
%{_libdir}/%{name}-%{api_ver}

%files doc
%license COPYING
%doc %{_docdir}/%{name}-%{api_ver}/
%doc %{_datadir}/devhelp/books/%{name}-%{api_ver}/

%if %{with mingw}
%files -n mingw32-gstreamermm
%doc AUTHORS ChangeLog NEWS README
%{mingw32_bindir}/libgstreamermm-1.0-1.dll

%files -n mingw32-gstreamermm-devel
%{mingw32_libdir}/%{name}-%{api_ver}
%{mingw32_libdir}/libgstreamermm-1.0.dll.a
%{mingw32_libdir}/pkgconfig/gstreamermm-1.0.pc
%{mingw32_includedir}/%{name}-%{api_ver}
%{mingw32_datadir}/devhelp/books/%{name}-%{api_ver}

%files -n mingw64-gstreamermm
%doc AUTHORS ChangeLog NEWS README
%{mingw64_bindir}/libgstreamermm-1.0-1.dll

%files -n mingw64-gstreamermm-devel
%{mingw64_libdir}/%{name}-%{api_ver}
%{mingw64_libdir}/libgstreamermm-1.0.dll.a
%{mingw64_libdir}/pkgconfig/gstreamermm-1.0.pc
%{mingw64_includedir}/%{name}-%{api_ver}
%{mingw64_datadir}/devhelp/books/%{name}-%{api_ver}
%endif

%changelog
%autochangelog
