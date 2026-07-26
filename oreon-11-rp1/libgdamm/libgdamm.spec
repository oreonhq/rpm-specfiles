%global source0_hash e9820070a1b258fbdfa9b6583d97dfdb1340c90bb353c5f5e21522375609d0bb

%global api_ver 5.0

%global glibmm_version 2.46.1

Name:           libgdamm
Version:        4.99.11
Release:        24%{?dist}
Summary:        C++ wrappers for libgda
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://www.gtkmm.org/
Source0:        http://ftp.gnome.org/pub/GNOME/sources/libgdamm/4.99/%{name}-%{version}.tar.xz
BuildRequires:  gcc-c++
BuildRequires:  glibmm24-devel >= %{glibmm_version}
BuildRequires:  libgda5-devel
BuildRequires:  libgda5-bdb

Requires:       glibmm24%{?_isa} >= %{glibmm_version}

%description
C++ wrappers for libgda. libgdamm is part of a set of powerful
C++ bindings for the GNOME libraries, which provide additional
functionality above GTK+/gtkmm.

%package devel
Summary:        Headers/Libraries for developing programs that use libgdamm
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains headers and libraries that programmers will need 
to develop applications which use libgdamm.

%package        doc
Summary:        API documentation for %{name}
BuildArch:      noarch
BuildRequires:  doxygen graphviz
BuildRequires: make
Requires:       glibmm24-doc

%description    doc
This package contains the full API documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%ldconfig_scriptlets

%files
%license COPYING
%doc AUTHORS NEWS
%{_libdir}/*.so.*

%files devel
%{_includedir}/libgdamm-%{api_ver}
%{_libdir}/*.so
%{_libdir}/libgdamm-%{api_ver}
%{_libdir}/pkgconfig/*.pc

%files doc
%license COPYING
%doc %{_datadir}/devhelp/books/%{name}-%{api_ver}
%doc %{_docdir}/%{name}-%{api_ver}

%changelog
%autochangelog
