%global source0_hash 07250741dff8a1ea1f5e38c02f1b9a1ae5e9fa52d013401067338842883a5b9f

Name:           libesedb
Version:        20240420
Release:        7%{?dist}
Summary:        Library to access the Extensible Storage Engine (ESE) Database File (EDB) format
License:        LGPL-3.0-or-later
URL:            https://github.com/libyal/libesedb
VCS:            https://github.com/libyal/libesedb
# Releases      https://github.com/libyal/libesedb/releases

%global         common_description %{expand:
Library and tools to access the Extensible Storage Engine (ESE) Database File
(EDB) format. ESEDB is used in may different applications like Windows Search,
Windows Mail, Exchange, Active Directory, etc.}

%global         gituser         libyal
%global         gitname         libesedb
%global         gitdate         20240420
%global         commit          24ae2ff47365adb5f1dcdce315ac7dd16b972836
%global         shortcommit     %(c=%{commit}; echo ${c:0:7})

# Build with python3 package by default
%bcond_without  python3

# Source0:      %%{url}/archive/%%{commit}/%%{name}-%%{version}-%%{shortcommit}.tar.gz
Source0:        %{url}/releases/download/%{version}/%{gitname}-experimental-%{version}.tar.gz

# Patch build to use the shared system libraries rather than using embedded ones
# Patch0:         %%{name}-libs.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
# autoreconf here needs autopoint from gettext-devel
BuildRequires:  gettext-devel

%if 0%{?with_python3}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
# if with_python3
%endif

Provides: bundled(libbfio)      = 20240420
Provides: bundled(libcdata)     = 20240420
Provides: bundled(libcerror)    = 20240420
Provides: bundled(libcfile)     = 20240420
Provides: bundled(libclocale)   = 20240420
Provides: bundled(libcnotify)   = 20240420
Provides: bundled(libcpath)     = 20240420
Provides: bundled(libcsplit)    = 20240420
Provides: bundled(libcthreads)  = 20240420
Provides: bundled(libfcache)    = 20240420
Provides: bundled(libfdata)     = 20240420
Provides: bundled(libfdatetime) = 20240420
Provides: bundled(libfguid)     = 20240420
Provides: bundled(libfmapi)     = 20240420
Provides: bundled(libfvalue)    = 20240420
Provides: bundled(libfwnt)      = 20240420
Provides: bundled(libmapidb)    = 20240420
Provides: bundled(libuna)       = 20240420

%description
%{common_description}

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.
%{common_description}

%if 0%{?with_python3}
%package -n python%{python3_pkgversion}-pyesedb
Summary:        Python3 binding for the library reading of esedb format
%{?python_provide:%python_provide python%{python3_pkgversion}-pyesedb}

%description -n python%{python3_pkgversion}-pyesedb
Python3 binding for the library reading of esedb format
%{common_description}
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gitname}-%{version}
#./autogen.sh
autoreconf --force --install
aclocal

%build
%configure --disable-static \
%if 0%{?with_python3}
           --enable-python \
%endif
           --enable-wide-character-type \
           --enable-multi-threading-support

make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc COPYING AUTHORS
%{_libdir}/*.so.*
%{_bindir}/esedbexport
%{_bindir}/esedbinfo
%{_mandir}/man1/esedbinfo.1.*
%{_mandir}/man3/libesedb.3.*

%files devel
%doc
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libesedb.pc

%if 0%{?with_python3}
%files -n python%{python3_pkgversion}-pyesedb
%{python3_sitearch}/pyesedb*
%endif

%changelog
%autochangelog
