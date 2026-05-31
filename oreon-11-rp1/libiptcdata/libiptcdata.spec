%global source0_hash none

%global python_support 1

%if 0%{?rhel} && 0%{?rhel} >= 10 || (0%{?oreon} >= 11)
%global python_support 0
%endif

Name: libiptcdata
Version: 1.0.5
Release: 24%{?dist}
Summary: IPTC tag library

License: LGPL-2.0-only
URL: https://github.com/ianw/%{name}
Source0:        https://github.com/ianw/%{name}/releases/download/release_1_0_5/%{name}-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gettext-devel
BuildRequires:  libtool
BuildRequires:  gtk-doc
%if 0%{?python_support}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%endif


%description
libiptcdata is a library for parsing, editing, and saving IPTC data
stored inside images.  IPTC is a standard for encoding metadata such
as captions, titles, locations, etc. in the headers of an image file.
libiptcdata also includes a command-line utility for modifying the
metadata.

%if 0%{?python_support}
%package -n python3-%{name}
Summary:        Python bindings for libiptcdata
Requires:       %{name}%{?_isa} = %{version}-%{release}
BuildRequires:  python3-devel
BuildRequires: make

%description -n python3-%{name}
The libiptcdata-python package contains a Python module that allows Python
applications to use the libiptcdata API for reading and writing IPTC
metadata in images.
%endif

%package devel
Summary:        Headers and libraries for libiptcdata application development
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description devel
The libiptcdata-devel package contains the libraries and include files
that you can use to develop libiptcdata applications.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup
# fix compatibility with gtk-doc 1.26
gtkdocize
autoreconf -fiv


%build
%if 0%{?python_support}
export PYTHON_VERSION=%python3_version
%configure --enable-gtk-doc --enable-python --disable-static
%else
%configure --enable-gtk-doc --disable-python --disable-static
%endif


%install
%make_install
find %{buildroot} -name "*.la" -exec rm -f {} \;
%find_lang %{name} --all-name


%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README TODO
%license COPYING
%{_bindir}/*
%{_libdir}/lib*.so.*

%if 0%{?python_support}
%files -n python3-%{name}
%doc python/README
%doc python/examples/*
%{python3_sitearch}/*.so
%endif

%files devel
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/libiptcdata
%{_datadir}/gtk-doc/html/libiptcdata


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.5-24
- Import
