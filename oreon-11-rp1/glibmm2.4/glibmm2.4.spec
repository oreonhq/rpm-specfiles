%global source0_hash e2efa45643f16b9fea2d6299f2f403d672eaeacddf0ff7f8094e1af9b0f5980b
%global apiver 2.4
%define release_version %(echo %{version} | awk -F. '{print $1"."$2}')
%global glib2_version 2.61.2
%global libsigc_version 2.9.1
Name:           glibmm2.4
Version:        2.90.0
Release:        1%{?dist}
Summary:        C++ interface for the GLib library
License:        LGPL-2.1-or-later AND GPL-2.0-or-later
URL:            https://gtkmm.org/
Source0:        https://download.gnome.org/sources/glibmm/%{release_version}/glibmm-%{version}.tar.xz
Patch0:         glibmm24-gcc11.patch
Requires:       glib2%{?_isa} >= %{glib2_version}
Requires:       libsigc++20%{?_isa} >= %{libsigc_version}
Obsoletes:      glibmm24 < %{version}-%{release}
Provides:       glibmm24 = %{version}-%{release}
Provides:       glibmm24%{?_isa} = %{version}-%{release}
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((DocsParser|Enum|Function|FunctionBase|GtkDefs|Object|Output|Property|Util|WrapParser)\\)
# oreon:deps
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  libxslt
BuildRequires:  m4
BuildRequires:  meson
BuildRequires:  mm-common
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(sigc++-2.0)
# /oreon:deps
%description
glibmm is the official C++ interface for the popular cross-platform
library GLib. It provides non-UI API that is not available in standard
C++ and makes it possible for gtkmm to wrap GObject-based APIs.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Obsoletes:      glibmm24-devel < %{version}-%{release}
Provides:       glibmm24-devel = %{version}-%{release}
Provides:       glibmm24-devel%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        API documentation for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       libsigc++20-doc
Obsoletes:      glibmm24-doc < %{version}-%{release}
Provides:       glibmm24-doc = %{version}-%{release}
%description    doc
This package contains the full API documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir glibmm-%{version}
%oreon_prep
%build

%meson -Dbuild-documentation=true
%meson_build
%install
%meson_install
find %{buildroot}%{_includedir}/giomm-2.4 -name '*.h' -exec sed -i '/^using G.*Class = struct _/d' {} +
chmod +x $RPM_BUILD_ROOT%{_libdir}/glibmm-%{apiver}/proc/generate_wrap_init.pl
chmod +x $RPM_BUILD_ROOT%{_libdir}/glibmm-%{apiver}/proc/gmmproc
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n glibmm2.4-devel -f %{oreon_filedir}/glibmm2.4-devel.list
%files -n glibmm2.4-doc -f %{oreon_filedir}/glibmm2.4-doc.list

%changelog

%autochangelog
