%global source0_hash 3d291beebbdb48d2b934608bc06195b641da63d2a8f5e0d386f2e9d6d05a0b42

%if "%{?dist}" == ".el8"
    %define fedora 32
%endif

%if 0%{?fedora} > 27 || 0%{?rhel} >= 9 || 0%{?oreon}
%global use_python3 1
%define __python %{__python3}
%endif

%if 0%{?rhel} >= 9 || 0%{?oreon}
%global with_dii 0
%else
%global with_dii 1
%endif
Summary:            Utilities to convert Outlook .pst files to other formats
Name:               libpst
Version:            0.6.76
Release:            28%{?dist}
License:            GPL-2.0-or-later
URL:                http://www.five-ten-sg.com/%{name}/
Source:        http://www.five-ten-sg.com/libpst//packages/libpst-0.6.76.tar.gz
# https://github.com/autoconf-archive/autoconf-archive/pull/235
Patch0:             m4-python310.patch
Patch1:             0002-incompatible-pointer-i686.patch
Patch2:             0003-gcc-c23-changes.patch

BuildRequires:      make
BuildRequires:      libtool gcc-c++
BuildRequires:      gd-devel zlib-devel boost-devel libgsf-devel gettext-devel

%if 0%{with_dii}
BuildRequires:      ImageMagick
%endif

%if 0%{?use_python3}
BuildRequires:      python3 python3-devel boost-python3 boost-python3-devel
Requires:           boost-python3
%else
BuildRequires:      python-devel
%endif

Requires:           %{name}-libs%{?_isa} = %{version}-%{release}

%if 0%{with_dii}
Requires:           ImageMagick%{?_isa}
%endif

%{!?python_sitelib:  %global python_sitelib  %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}


%if 0%{with_dii}
%description
The Libpst utilities include readpst which can convert email messages
to both mbox and MH mailbox formats, pst2ldif which can convert the
contacts to .ldif format for import into ldap databases, and pst2dii
which can convert email messages to the DII load file format used by
Summation.
%else
%description
The Libpst utilities include readpst which can convert email messages
to both mbox and MH mailbox formats, pst2ldif which can convert the
contacts to .ldif format for import into ldap databases.
%endif


%package libs
Summary:            Shared library used by the pst utilities

%description libs
The libpst-libs package contains the shared library used by the pst
utilities.


%if 0%{?use_python3}
%package -n python3-%{name}
Requires:           python3
BuildRequires:      (python3-setuptools if python3 >= 3.12)
Provides:           %{name}-python = %{version}-%{release}
%else
%package python
Requires:           python
%endif
Summary:            Python bindings for libpst
Requires:           %{name}-libs%{?_isa} = %{version}-%{release}

%if 0%{?fedora} >= 20 || 0%{?rhel} >= 9 || 0%{?oreon}
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{python_sitearch}/_.*\.so$
%else
%{?filter_setup:
%filter_provides_in %{python_sitearch}/_.*\.so$
%filter_setup
}
%endif


%if 0%{?use_python3}
%description -n python3-%{name}
%else
%description python
%endif
The libpst-python package allows you to use the libpst shared object
from Python code.


%package devel
Summary:            Library links and header files for libpst application development
Requires:           %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
The libpst-devel package contains the library links and header files
you'll need to develop applications using the libpst shared library.
You do not need to install it if you just want to use the libpst
utilities.


%package devel-doc
Summary:            Documentation for libpst.so for libpst application development
Requires:           %{name}-doc = %{version}-%{release}

%description devel-doc
The libpst-devel-doc package contains the doxygen generated
documentation for the libpst.so shared library.


%package doc
Summary:            Documentation for the pst utilities in html format

%description doc
The libpst-doc package contains the html documentation for the pst
utilities.  You do not need to install it if you just want to use the
libpst utilities.



%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1 -S gendiff


%build
autoreconf -fiv
%configure --enable-libpst-shared \
%if 0%{with_dii}
           --enable-dii \
%else
           --disable-dii \
%endif
           --with-boost-python=boost_python%{python3_version_nodots}
%if 0%{?use_python3}
%make_build
%else
make %{?_smp_mflags}
%endif


%install
%if 0%{?use_python3}
%make_install
%else
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
%endif
#Remove libtool archives.
find %{buildroot} -name '*.la' -or -name '*.a' | xargs rm -f
mv %{buildroot}%{_datadir}/doc/%{name}-%{version} %{buildroot}%{_datadir}/doc/%{name}

# Remove pst2dii man page, when it's not built
%if !0%{with_dii}
rm %{buildroot}%{_mandir}/man1/pst2dii.1*
%endif

%if 0%{?use_python3}
%ldconfig_scriptlets libs
%else
%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig
%endif

%files
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man5/*


%files libs
%{_libdir}/libpst.so.*
%doc COPYING


%if 0%{?use_python3}
%files -n python3-%{name}
%defattr(-,root,root,-)
%{python3_sitearch}/_*.so
%else
%files python
%{python_sitearch}/_*.so
%endif


%files devel
%{_libdir}/libpst.so
%{_includedir}/%{name}-4/
%{_libdir}/pkgconfig/libpst.pc


%files devel-doc
%{_datadir}/doc/%{name}/devel/


%files doc
%dir %{_datadir}/doc/%{name}/
%{_datadir}/doc/%{name}/*.html
%{_datadir}/doc/%{name}/AUTHORS
%{_datadir}/doc/%{name}/COPYING
%{_datadir}/doc/%{name}/ChangeLog
%{_datadir}/doc/%{name}/NEWS
%{_datadir}/doc/%{name}/README


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.6.76-28
- Import
