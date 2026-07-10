%global source0_hash 0680a53b7bf90b4e4bf444d1d89e6df41c777e0bacc96e9c09fc4dd2f5fe6b72
%global tarname gtkmm
%global api_ver 2.4

Name:           gtkmm2.4
Version:        2.24.5
Release:        24%{?dist}

Summary:        C++ interface for GTK2 (a GUI library for X)

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://www.gtkmm.org/
Source0:        https://download.gnome.org/sources/gtkmm/2.24/gtkmm-%{version}.tar.xz

BuildRequires:  atkmm-devel
BuildRequires:  cairomm-devel
BuildRequires:  gcc-c++
BuildRequires:  glibmm2.4-devel
BuildRequires:  gtk2-devel
BuildRequires:  make
BuildRequires:  pangomm-devel

# Renamed in F37
Obsoletes:      gtkmm24 < %{version}-%{release}
Provides:       gtkmm24 = %{version}-%{release}
Provides:       gtkmm24%{?_isa} = %{version}-%{release}

%description
gtkmm provides a C++ interface to the GTK+ GUI library. gtkmm2 wraps GTK+ 2.
Highlights include typesafe callbacks, widgets extensible via inheritance
and a comprehensive set of widget classes that can be freely combined to
quickly create complex user interfaces.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{_isa} = %{version}-%{release}
# Renamed in F37
Obsoletes:      gtkmm24-devel < %{version}-%{release}
Provides:       gtkmm24-devel = %{version}-%{release}
Provides:       gtkmm24-devel%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        doc
Summary:        API documentation for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       glibmm2.4-doc
# Renamed in F37
Obsoletes:      gtkmm24-docs < %{version}-%{release}
Provides:       gtkmm24-docs = %{version}-%{release}

%description    doc
This package contains the full API documentation for %{name}.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n gtkmm-%{version}


%build
%configure --enable-shared
# removing rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build


%install
%make_install
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'


%files
%license COPYING
%doc AUTHORS NEWS README
%{_libdir}/*.so.*

%files devel
%doc PORTING demos/gtk-demo/
%{_includedir}/gtkmm-2.4/
%{_includedir}/gdkmm-2.4/
%{_libdir}/*.so
%{_libdir}/gtkmm-2.4/
%{_libdir}/gdkmm-2.4/
%{_libdir}/pkgconfig/*.pc

%files doc
%doc %{_docdir}/%{tarname}-%{api_ver}
%doc %{_datadir}/devhelp/


%changelog
%autochangelog