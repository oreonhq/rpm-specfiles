%global source0_hash 5a3d6b383ca5afc235b171118e90f5ff6aa27e9fea3303065231a6d403f0183a

Name:           libxslt
Summary:        Library providing the Gnome XSLT engine
Version:        1.1.43
Release:        6%{?dist}

License:        MIT
URL:            https://gitlab.gnome.org/GNOME/libxslt
Source0:        https://download.gnome.org/sources/%{name}/1.1/%{name}-%{version}.tar.xz

Provides: xsltproc = %{version}-%{release}

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  pkgconfig(libxml-2.0) >= 2.6.27
BuildRequires:  python3-devel

# Fedora specific patches
Patch0:         multilib.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1467435
Patch1:         multilib2.patch

%description
This C library allows to transform XML files into other XML files
(or HTML, text, ...) using the standard XSLT stylesheet transformation
mechanism. To use it you need to have a version of libxml2 >= 2.6.27
installed. The xsltproc command is a command line interface to the XSLT engine

%package devel
Summary:        Development libraries and header files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libgpg-error-devel%{?_isa}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%if 0%{?fedora}
# Upstream package has not been ported to Python 3.  I have
# converted this section so it could be used to compile the
# Python 3 bindings one day once that has happened, but
# commented it out.  - RWMJ 2019-09-10
%package -n python3-libxslt
Summary:        Python 3 bindings for %{name}
BuildRequires:  python3-libxml2
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       python3-libxml2
%{?python_provide:%python_provide python3-%{name}}

%description -n python3-libxslt
The libxslt-python package contains a module that permits applications
written in the Python programming language to use the interface
supplied by the libxslt library to apply XSLT transformations.

This library allows to parse sytlesheets, uses the libxml2-python
to load and save XML and HTML files. Direct access to XPath and
the XSLT transformation context are possible to extend the XSLT language
with XPath functions written in Python.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1
chmod 644 python/tests/*

%build
autoreconf -vfi
#export PYTHON=%%{__python3}
#%configure --disable-static --disable-silent-rules --with-python
%configure \
  --disable-static \
  --disable-silent-rules \
  --with-plugins \
%if 0%{?fedora}
  --with-python=yes \
%else
  --with-python=no \
%endif
  --with-crypto=no
%make_build

%install
%make_install
find %{buildroot} -name '*.la' -print -delete
# multiarch crazyness on timestamp differences
touch -m --reference=%{buildroot}%{_includedir}/libxslt/xslt.h %{buildroot}%{_bindir}/xslt-config
rm -vrf %{buildroot}%{_docdir}

%check
%make_build tests

%ldconfig_scriptlets

%files
%license Copyright
%doc AUTHORS NEWS README.md FEATURES
%{_bindir}/xsltproc
%{_libdir}/libxslt.so.*
%{_libdir}/libexslt.so.*
%{_libdir}/libxslt-plugins/
%{_mandir}/man1/xsltproc.1*

%files devel
%doc doc/libxslt-api.xml
%doc doc/EXSLT/libexslt-api.xml
%doc %{_mandir}/man3/libxslt.3*
%doc %{_mandir}/man3/libexslt.3*
%doc doc/tutorial
%doc doc/tutorial2
%{_datadir}/gtk-doc/
%{_libdir}/cmake/libxslt/
%{_libdir}/libxslt.so
%{_libdir}/libexslt.so
%{_libdir}/xsltConf.sh
%{_includedir}/libxslt/
%{_includedir}/libexslt/
%{_libdir}/pkgconfig/libxslt.pc
%{_libdir}/pkgconfig/libexslt.pc
%{_bindir}/xslt-config

%if 0%{?fedora}
%files -n python3-libxslt
%{python3_sitelib}/libxslt.py*
%{python3_sitearch}/libxsltmod.so
%{python3_sitelib}/__pycache__/libxslt*
%doc python/libxsltclass.txt
%doc python/tests/*.py
%doc python/tests/*.xml
%doc python/tests/*.xsl
%endif

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1.43-6
- Prepare for Oreon 11 (RP1)
