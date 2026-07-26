%global source0_hash b10abf0b7717b804bdd7a860956b51aa750c64b93b860816056c08cd2e8893d2

%global ini_name 39-mapserver.ini
%global project_owner MapServer
%global project_name MapServer

%global python_mapscript 1
%global srcname mapscript

%ifarch %{java_arches}
%bcond_without java
%else
%bcond_with java
%endif

%if 0%{?fedora} >= 41
%ifarch %{ix86}
%bcond_with    php
%else
%bcond_without php
%endif
%else
%bcond_without php
%endif

Name:           mapserver
Version:        8.6.0
Release:        3%{?dist}
Summary:        Platform for publishing spatial data and interactive mapping applications to the web
%global dashver %(echo %version | sed 's|\\.|-|g')

License:        MIT
URL:            https://mapserver.org

Source0:        https://github.com/%{project_owner}/%{project_name}/archive/rel-%{dashver}/%{project_name}-%{version}.tar.gz

Requires:       httpd
Requires:       dejavu-sans-fonts

BuildRequires:  autoconf
BuildRequires:  gcc-c++
BuildRequires:  cairo-devel
BuildRequires:  cmake
BuildRequires:  curl-devel
BuildRequires:  fcgi-devel
BuildRequires:  freetype-devel
BuildRequires:  fribidi-devel
BuildRequires:  gd-devel >= 2.0.16
BuildRequires:  gdal-devel
BuildRequires:  geos-devel >= 3.7.1
BuildRequires:  giflib-devel
BuildRequires:  httpd-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  libxml2-devel
BuildRequires:  libXpm-devel
BuildRequires:  libxslt-devel
BuildRequires:  mariadb-connector-c-devel
BuildRequires:  openssl-devel
BuildRequires:  harfbuzz-devel
BuildRequires:  pam-devel
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  protobuf-c-devel
BuildRequires:  libpq-devel
BuildRequires:  proj-devel => 5.2.0
BuildRequires:  readline-devel
BuildRequires:  swig
BuildRequires:  zlib-devel
#Get
#/usr/share/fonts/dejavu-sans-fonts/DejaVuSans.ttf
#/usr/share/fonts/dejavu-sans-fonts/DejaVuSans-Bold.ttf
# See %%prep below
BuildRequires:  dejavu-sans-fonts

%description
MapServer is an Open Source platform for publishing spatial data and
interactive mapping applications to the web.

%package  libs
Summary:  %{summary}

%description libs
This package contains the libs for mapserver.

%package  devel
Summary:        Development files for mapserver
Requires:       %{name} = %{version}

%description devel
This package contains development files for mapserver.

%if %{with php}
%package -n php-%{name}
Summary:        PHP/Mapscript map making extensions to PHP
BuildRequires:  php-devel
Requires:       php-gd%{?_isa}
Requires:       php(zend-abi) = %{php_zend_api}
Requires:       php(api) = %{php_core_api}

%description -n php-%{name}
The PHP/Mapscript extension provides full map customization capabilities within
the PHP scripting language.
%endif

%package perl
Summary:        Perl/Mapscript map making extensions to Perl
Requires:       %{name} = %{version}-%{release}

%description perl
The Perl/Mapscript extension provides full map customization capabilities
within the Perl programming language.

%if 0%{python_mapscript}
%package -n python3-mapserver
%{?python_provide:%python_provide python3-mapserver}
# Remove before F30
Provides: %{name}-python = %{version}-%{release}
Provides: %{name}-python%{?_isa} = %{version}-%{release}
Obsoletes: %{name}-python < %{version}-%{release}
Summary:        Python/Mapscript map making extensions to Python
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       %{name} = %{version}-%{release}
Requires:       python3

%description -n python3-mapserver
The Python/Mapscript extension provides full map customization capabilities
within the Python programming language.
%endif

%if %{with java}
%package java
Summary:        Java/Mapscript map making extensions to Java
BuildRequires:  java-devel
Requires:       %{name} = %{version}-%{release}
Requires:       java-headless

%description java
The Java/Mapscript extension provides full map customization capabilities
within the Java programming language.
%endif

%package ruby
Summary:       Ruby/Mapscript map making extensions to Ruby
BuildRequires: ruby-devel
Requires:      %{name} = %{version}-%{release}

%description ruby
The Ruby/Mapscript extension provides full map customization capabilities within
the ruby programming language.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{project_owner}-rel-%{dashver}

# replace fonts for tests with symlinks
ln -sf /usr/share/fonts/dejavu-sans-fonts/DejaVuSans.ttf tests/vera/Vera.ttf
ln -sf /usr/share/fonts/dejavu-sans-fonts/DejaVuSans-Bold.ttf tests/vera/VeraBd.ttf

# Force swig to regenerate the wrapper
rm -rf mapscript/perl/mapscript_wrap.c

%build
export CFLAGS="${CFLAGS} -ldl -fPIC -fno-strict-aliasing"
export CXXFLAGS="%{optflags} -fno-strict-aliasing"

%cmake -DINSTALL_LIB_DIR=%{_libdir} \
      -DCMAKE_SKIP_RPATH=ON \
      -DCMAKE_SKIP_INSTALL_RPATH=ON \
      -DWITH_CAIRO=TRUE \
      -DWITH_CLIENT_WFS=TRUE \
      -DWITH_CLIENT_WMS=TRUE \
      -DWITH_CURL=TRUE \
      -DWITH_FCGI=TRUE \
      -DWITH_FRIBIDI=TRUE \
      -DWITH_GD=TRUE \
      -DWITH_GDAL=TRUE \
      -DWITH_GEOS=TRUE \
      -DWITH_GIF=TRUE \
      -DWITH_ICONV=TRUE \
%if %{with java}
      -DWITH_JAVA=TRUE \
%else
      -DWITH_JAVA=FALSE \
%endif
      -DWITH_KML=TRUE \
      -DWITH_LIBXML2=TRUE \
      -DWITH_OGR=TRUE \
      -DWITH_MYSQL=TRUE \
      -DWITH_PERL=TRUE \
      -DCUSTOM_PERL_SITE_ARCH_DIR="%{perl_vendorarch}" \
%if %{with php}
      -DWITH_PHPNG=TRUE \
%endif
      -DWITH_POSTGIS=TRUE \
      -DWITH_PROJ=TRUE \
%if 0%{python_mapscript}
      -DWITH_PYTHON=TRUE \
%endif
      -DWITH_RUBY=TRUE \
      -DWITH_V8=FALSE \
      -DWITH_SOS=TRUE \
      -DWITH_THREAD_SAFETY=TRUE \
      -DWITH_WCS=TRUE \
      -DWITH_WMS=TRUE \
      -DWITH_WFS=TRUE \
      -DWITH_XMLMAPFILE=TRUE \
      -DWITH_POINT_Z_M=TRUE \
      -DWITH_APACHE_MODULE=FALSE \
      -DWITH_SVGCAIRO=FALSE \
      -DWITH_CSHARP=FALSE \
      -DWITH_ORACLESPATIAL=FALSE \
      -DWITH_ORACLE_PLUGIN=FALSE \
      -DWITH_MSSQL2008=FALSE \
      -DWITH_SDE=FALSE \
      -DWITH_SDE_PLUGIN=FALSE \
      -DWITH_EXEMPI=FALSE \
      -Wno-dev

%cmake_build

%install
%cmake_install

%if 0%{python_mapscript}
# cmake tries to invoke pip and download things. we'll just use setuptools.
mkdir -p %{buildroot}%{python3_sitearch}
pushd redhat-linux-build/src/mapscript/python
%py3_install
popd
%endif

mkdir -p %{buildroot}%{_datadir}/%{name}
install -p -m 644 src/xmlmapfile/mapfile.xsd %{buildroot}%{_datadir}/%{name}
install -p -m 644 src/xmlmapfile/mapfile.xsl %{buildroot}%{_datadir}/%{name}

%if %{with java}
# install java
mkdir -p %{buildroot}%{_javadir}
install -p -m 644 %{_vpath_builddir}/src/mapscript/java/mapscript.jar %{buildroot}%{_javadir}/
%endif

%if %{with php}
# install php config file
mkdir -p %{buildroot}%{php_inidir}
cat > %{buildroot}%{php_inidir}/%{ini_name} <<EOF
; Enable %{name} extension module
extension=php_mapscriptng.so
EOF
%endif

# Install sample config file as %%doc
rm %{buildroot}%{_usr}/%{_sysconfdir}/mapserver-sample.conf

%files
%doc README.md
%doc etc/mapserver-sample.conf
%{_bindir}/coshp
%{_bindir}/legend
%{_bindir}/mapserv
%{_bindir}/map2img
%{_bindir}/msencrypt
%{_bindir}/scalebar
%{_bindir}/shptree
%{_bindir}/shptreetst
%{_bindir}/shptreevis
%{_bindir}/sortshp
%{_bindir}/tile4ms
%{_datadir}/%{name}/

%files libs
%doc README.md
%{_libdir}/libmapserver.so.%{version}
%{_libdir}/libmapserver.so.2

%files devel
%doc README.md
%{_libdir}/libmapserver.so
%{_includedir}/%{name}/

%if %{with php}
%files -n php-%{name}
%doc src/mapscript/php/README.md
%config(noreplace) %{php_inidir}/%{ini_name}

# this is only installed when swig < 4.0.2 https://github.com/MapServer/MapServer/blob/25ef061bec310773511eb84ef03f4a91e0f5a081/src/mapscript/phpng/CMakeLists.txt#L86
%if ! 0%{?fedora} && 0%{?rhel} < 10
%{php_extdir}/mapscript.php
%endif

%{php_extdir}/php_mapscriptng.so
%endif
# end php-mapcache

%files perl
%doc README.md
%doc src/mapscript/perl/examples
%dir %{perl_vendorarch}/auto/mapscript
%{perl_vendorarch}/auto/mapscript/*
%{perl_vendorarch}/mapscript.pm

%if 0%{python_mapscript}
%files -n python3-mapserver
%doc src/mapscript/python/README.rst
%doc src/mapscript/python/examples
%doc src/mapscript/python/tests
%{python3_sitearch}/mapscript*
%endif

%if %{with java}
%files java
%doc src/mapscript/java/README
%doc src/mapscript/java/examples
%doc src/mapscript/java/tests
%{_javadir}/*.jar
%{_libdir}/libjavamapscript.so
%endif

%files ruby
%doc src/mapscript/ruby/README
%doc src/mapscript/ruby/examples
%doc mapserver-ruby/README
%doc mapserver-ruby/examples
%{ruby_sitearchdir}/mapscript.so

%changelog
%autochangelog
