%global source0_hash 043877c0857d8d46067cd2f18809d54fc876c399f0ecd438f60ea7f4d8037451

%if 0%{?rhel} >= 8 || (0%{?oreon} >= 11)
%bcond_with php
%bcond_with guile
%else
# temporal drop of PHP support due to https://gitlab.com/graphviz/graphviz/-/issues/2277
%bcond_with php
%bcond_without guile
%endif
%bcond_with python2

# Macro for creating an option which enables bootstraping build without dependencies,
# which cause problems during rebuilds. Currently it is circular dependency of graphviz and
# doxygen - in case a dependency of graphviz/doxygen bumps SONAME and graphviz/doxygen
# has to be rebuilt, we can break the circular dependency by building with --with bootstrap.
%bcond_with bootstrap

# Temporarily disable gtk & gdkpixbuf in Fedora 43 due to issues
# with GDKPixbuf 2.44
# see: https://bugzilla.redhat.com/show_bug.cgi?id=2395533
%if 0%{?fedora} >= 43 || (0%{?oreon} >= 11)
%bcond_with gtk2
%bcond_with gdkpixbuf
%else
%bcond_without gdkpixbuf
%if 0%{?rhel} >= 10 || (0%{?oreon} >= 11)
%bcond_with gtk2
%else
%bcond_without gtk2
%endif
%endif

# Necessary conditionals
%ifarch %{mono_arches}
%global SHARP  1
%else
%global SHARP  0
%endif

%global DEVIL  1
%global ARRRR  1

# Build with QT applications (currently only gvedit)
# Disabled until the package gets better structuring, see bug #447133
%global QTAPPS 0

%global GTS    0
%global LASI   0

# Not in Fedora yet.
%global MING   0

%ifarch %{java_arches}
%global JAVA 1
%else
%global JAVA 0
%endif

%if 0%{?rhel} || (0%{?oreon} >= 11)
%global SHARP  0
%global ARRRR  0
%global DEVIL  0
%global GTS    0
%global LASI   0
%endif

%if %{GTS} && %{with gtk2}
%global SMYRNA 1
%else
%global SMYRNA 0
%endif

%if %{with php}
%global PHP 1
%else
%global PHP 0
%endif

%if %{with guile}
%global GUILE 1
%else
%global GUILE 0
%endif

%ifarch %{golang_arches}
%global GOLANG 1
%else
%global GOLANG 0
%endif

# Plugins version
%global pluginsver 6

%global php_extdir %(php-config --extension-dir 2>/dev/null || echo %{_libdir}/php4)

%if "%{php_version}" < "5.6"
%global ini_name     %{name}.ini
%else
%global ini_name     40-%{name}.ini
%endif

# Fix for the 387 extended precision (rhbz#772637)
%ifarch i386 i686
%global FFSTORE -ffloat-store
%endif

Name:			graphviz
Summary:		Graph Visualization Tools
Version:		14.1.4
Release:		3%{?dist}
License:		epl-1.0 AND cpl-1.0 AND bsd-3-clause AND mit AND gpl-3.0-or-later WITH bison-exception-2.2 AND apache-1.1 AND lgpl-2.0-or-later WITH libtool-exception AND smlnj AND hpnd-uc
URL:			http://www.graphviz.org/
#Source0:		https://gitlab.com/%%{name}/%%{name}/-/archive/%%{version}/%%{name}-%%{version}.tar.bz2
Source0:        https://gitlab.com/api/v4/projects/%{name}%2F%{name}/packages/generic/%{name}-releases/%{version}/%{name}-%{version}.tar.xz
BuildRequires:		gcc-g++
BuildRequires:		zlib-devel
BuildRequires:		libpng-devel
BuildRequires:		libjpeg-devel
BuildRequires:          libxcrypt-devel
BuildRequires:		expat-devel
BuildRequires:		freetype-devel >= 2
BuildRequires:		ksh
BuildRequires:		bison
BuildRequires:		m4
BuildRequires:		flex
BuildRequires:		tk-devel
BuildRequires:		tcl-devel
BuildRequires:		swig
BuildRequires:		sed
BuildRequires:		fontconfig-devel
BuildRequires:		libtool-ltdl-devel
BuildRequires:		ruby-devel
BuildRequires:		ruby
BuildRequires:		libXt-devel
BuildRequires:		libXmu-devel
%if %{GUILE}
BuildRequires:		guile30-devel
%endif
%if %{with python2}
BuildRequires:		python2-devel
%endif
BuildRequires:		python3-devel
BuildRequires:		libXaw-devel
BuildRequires:		libSM-devel
BuildRequires:		libXext-devel
%if %{JAVA}
BuildRequires:		java-devel
BuildRequires:		javapackages-tools
%endif
%if %{with gdkpixbuf}
BuildRequires:		gdk-pixbuf2-devel
%endif
BuildRequires:		cairo-devel >= 1.1.10
BuildRequires:		pango-devel
BuildRequires:		gmp-devel
BuildRequires:		lua-devel
%if %{with gtk2}
BuildRequires:		gtk2-devel
BuildRequires:		gtk3-devel
%endif
BuildRequires:		gd-devel
BuildRequires:		perl-devel
BuildRequires:		swig >= 1.3.33
BuildRequires:		automake
BuildRequires:		autoconf
BuildRequires:		libtool
BuildRequires:		qpdf
# Temporary workaound for perl(Carp) not pulled
BuildRequires:		perl-Carp
%if %{PHP}
BuildRequires:		php-devel
%endif
%if %{SHARP}
BuildRequires:		mono-core
%endif
%if %{DEVIL}
BuildRequires:		DevIL-devel
%endif
%if %{ARRRR}
BuildRequires:		R-devel
%endif
%if %{QTAPPS}
BuildRequires:		qt-devel
%endif
%if %{GTS}
BuildRequires:		gts-devel
%endif
%if %{LASI}
BuildRequires:		lasi-devel
%endif
BuildRequires:		urw-base35-fonts
BuildRequires:		perl-ExtUtils-Embed
BuildRequires:		perl-generators
BuildRequires:		librsvg2-devel
# for ps2pdf
BuildRequires:		ghostscript
BuildRequires:		libgs-devel
BuildRequires:		make
BuildRequires:		poppler-glib-devel
BuildRequires:		freeglut-devel
%if %{SMYRNA}
BuildRequires:		libglade2-devel
BuildRequires:		gtkglext-devel
%endif
%if %{without bootstrap}
BuildRequires:		doxygen
%endif
%if %{GOLANG}
BuildRequires:		golang
%endif
Requires:		urw-base35-fonts
# rhbz#1838679
Patch0:			graphviz-12.0.0-gvpack-neato-static.patch
# fixes for R API 4.6
Patch1:     swig-4.4.1-r-api-4.6.patch

%if ! %{JAVA}
Obsoletes:              graphviz-java < %{version}-%{release}
%endif
%if %{without gtk2}
Obsoletes:		graphviz-gtk2 < %{version}-%{release}
%endif

%description
A collection of tools for the manipulation and layout of graphs (as in nodes
and edges, not as in barcharts).

%package libs
Summary:		Graphviz libraries

%description libs
Graphviz libraries.

%package devel
Summary:		Development package for graphviz
Requires:		%{name}-libs%{?_isa} = %{version}-%{release}, pkgconfig
Requires:		%{name}-gd = %{version}-%{release}

%description devel
A collection of tools for the manipulation and layout of graphs (as in nodes
and edges, not as in barcharts). This package contains development files for
graphviz.

%if %{DEVIL}
%package devil
Summary:		Graphviz plugin for renderers based on DevIL
Requires:		%{name}%{?_isa} = %{version}-%{release}

%description devil
Graphviz plugin for renderers based on DevIL. (Unless you absolutely have
to use BMP, TIF, or TGA, you are recommended to use the PNG format instead
supported directly by the cairo+pango based renderer in the base graphviz rpm.)
%endif

%package doc
Summary:		PDF and HTML documents for graphviz

%description doc
Provides some additional PDF and HTML documentation for graphviz.

%if %{SMYRNA}
%package smyrna
Summary:		Graphviz interactive graph viewer

%description smyrna
Smyrna is a viewer for graphs in the DOT format.
%endif

%package gd
Summary:		Graphviz plugin for renderers based on gd
Requires:		%{name}%{?_isa} = %{version}-%{release}

%description gd
Graphviz plugin for renderers based on gd.  (Unless you absolutely have to use
GIF, you are recommended to use the PNG format instead because of the better
quality anti-aliased lines provided by the cairo+pango based renderer.)

%if %{with gtk2}
%package gtk2
Summary:		Graphviz plugin for renderers based on gtk2
Requires:		%{name}%{?_isa} = %{version}-%{release}

%description gtk2
Graphviz plugin for renderers based on gtk2.
%endif

%package graphs
Summary:		Demo graphs for graphviz

%description graphs
Some demo graphs for graphviz.

%if %{GUILE}
%package guile
Summary:		Guile extension for graphviz
Requires:		%{name}%{?_isa} = %{version}-%{release}

%description guile
Guile extension for graphviz.
%endif

%if %{JAVA}
%package java
Summary:		Java extension for graphviz
Requires:		%{name}%{?_isa} = %{version}-%{release}

%description java
Java extension for graphviz.
%endif

%package lua
Summary:		Lua extension for graphviz
Requires:		%{name}%{?_isa} = %{version}-%{release}, lua

%description lua
Lua extension for graphviz.

%if %{MING}
%package ming
Summary:		Graphviz plugin for flash renderer based on ming
Requires:		%{name}%{?_isa} = %{version}-%{release}

%description ming
Graphviz plugin for -Tswf (flash) renderer based on ming.
%endif

%package perl
Summary:		Perl extension for graphviz
Requires:		%{name}%{?_isa} = %{version}-%{release}

%description perl
Perl extension for graphviz.

%if %{PHP}
%package php
Summary:		PHP extension for graphviz
Requires:		%{name}%{?_isa} = %{version}-%{release}
Requires:	php(zend-abi) = %{?php_zend_api}%{?!php_zend_api:UNDEFINED}
Requires:	php(api) = %{?php_core_api}%{?!php_core_api:UNDEFINED}

%description php
PHP extension for graphviz.
%endif

%if %{with python2}
%package python2
Summary:		Python extension for graphviz
Requires:		%{name}%{?_isa} = %{version}-%{release}
# Manually add provides that would be generated automatically if .egg-info was present
Provides: python2dist(gv) = %{version}
Provides: python%{python2_version}dist(gv) = %{version}
# Remove before F30
Provides: %{name}-python = %{version}-%{release}
Provides: %{name}-python%{?_isa} = %{version}-%{release}
Obsoletes: %{name}-python < 2.40.1-25
Obsoletes: python2-%{name} < 2.40.1-25

%description python2
Python extension for graphviz.
%endif

%package python3
Summary:		Python 3 extension for graphviz
Requires:		%{name}%{?_isa} = %{version}-%{release}
# Manually add provides that would be generated automatically if .egg-info was present
Provides: python3dist(gv) = %{version}
Provides: python%{python3_version}dist(gv) = %{version}

%description python3
Python 3 extension for graphviz.

%if %{ARRRR}
%package R
Summary:		R extension for graphviz
Requires:		%{name}%{?_isa} = %{version}-%{release}, R-core

%description R
R extension for graphviz.
%endif

%package ruby
Summary:		Ruby extension for graphviz
Requires:		%{name}%{?_isa} = %{version}-%{release}, ruby

%description ruby
Ruby extension for graphviz.

%if %{SHARP}
%package sharp
Summary:		C# extension for graphviz
Requires:		%{name}%{?_isa} = %{version}-%{release}, mono-core

%description sharp
C# extension for graphviz.
%endif

%package tcl
Summary:		Tcl extension & tools for graphviz
Requires:		%{name}%{?_isa} = %{version}-%{release}, tcl >= 8.3, tk

%description tcl
Various tcl packages (extensions) for the graphviz tools.

%if %{GOLANG}
%package go
Summary:		Go extension for graphviz
Requires:		%{name}%{?_isa} = %{version}-%{release}, golang

%description go
Go extension for graphviz.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1

# Attempt to fix rpmlint warnings about executable sources
find -type f -regex '.*\.\(c\|h\)$' -exec chmod a-x {} ';'

%build
autoreconf -fi

%if %{JAVA}
# Hack in the java includes we need
sed -i 's|for try_java_include in|& %{java_home}/include/ %{java_home}/include/linux/|' configure
%endif
# Rewrite config_ruby.rb to work with Ruby 2.2
sed -i 's|expand(|expand(RbConfig::|' config/config_ruby.rb
sed -i 's|sitearchdir|vendorarchdir|' config/config_ruby.rb

# get the path to search for ruby/config.h to CPPFLAGS, so that configure can find it
export CPPFLAGS=-I`ruby -e "puts File.join(RbConfig::CONFIG['includedir'], RbConfig::CONFIG['sitearch'])" || echo /dev/null`
%configure --with-x --disable-static --disable-dependency-tracking \
%if ! %{JAVA}
--enable-java=no \
%endif
	--without-mylibgd --with-ipsepcola --with-pangocairo \
	--with-visio --disable-silent-rules --enable-lefty \
%if ! %{LASI}
	--without-lasi \
%endif
%if %{without gdkpixbuf}
	--without-gdk-pixbuf \
%else
	--with-gdk-pixbuf \
%endif
%if %{without gtk2}
	--without-gtk \
	--without-gtkgl \
	--without-gtkglext \
	--without-glade \
%endif
%if ! %{GTS}
	--without-gts \
%endif
%if ! %{SMYRNA}
	--without-smyrna \
%endif
%if ! %{SHARP}
	--disable-sharp \
%endif
%if ! %{MING}
	--without-ming \
%endif
%if ! %{ARRRR}
	--disable-r \
%endif
%if ! %{DEVIL}
	--without-devil \
%endif
%if ! %{QTAPPS}
	--without-qt \
%endif
%if %{GUILE}
	--enable-guile=yes \
%else
	--enable-guile=no \
%endif
%if %{GOLANG}
	--enable-go=yes
%else
	--enable-go=no
%endif

# drop rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing -fno-strict-overflow %{?FFSTORE}" \
  CXXFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing -fno-strict-overflow %{?FFSTORE}"

%if %{without bootstrap}
make doxygen
%endif

%install
%make_install docdir=%{_docdir}/%{name} \
	pkgconfigdir=%{_libdir}/pkgconfig
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

# Install README
install -m0644 README.md %{buildroot}%{_docdir}/%{name}

%if %{PHP}
# PHP configuration file
%{__mkdir_p} %{buildroot}%{_sysconfdir}/php.d
%{__cat} << __EOF__ > %{buildroot}%{_sysconfdir}/php.d/%{ini_name}
; Enable %{name} extension module
extension=gv.so
__EOF__
%endif

# Remove executable modes from demos
find %{buildroot}%{_datadir}/%{name}/demo -type f -exec chmod a-x {} ';'

# Move demos to doc
mv %{buildroot}%{_datadir}/%{name}/demo %{buildroot}%{_docdir}/%{name}/

# Rename python demos to prevent byte compilation
find %{buildroot}%{_docdir}/%{name}/demo -type f -name "*.py" -exec mv {} {}.demo ';'

# Remove dot_builtins, on demand loading should be sufficient
rm -f %{buildroot}%{_bindir}/dot_builtins

# Remove metadata from generated PDFs
pushd %{buildroot}%{_docdir}/%{name}
for f in prune gvgen.1 gc.1 dot.1 cluster.1
do
  if [ -f $f.pdf ]
  then
# ugly, but there is probably no better solution
    qpdf --empty --static-id --pages $f.pdf -- $f.pdf.$$
    mv -f $f.pdf.$$ $f.pdf
  fi
done
popd

%if %{with python2}
install -pD tclpkg/gv/.libs/libgv_python2.so %{buildroot}%{python2_sitearch}/_gv.so
install -p tclpkg/gv/gv.py %{buildroot}%{python2_sitearch}/gv.py
%endif

# python 3
install -pD tclpkg/gv/.libs/libgv_python3.so %{buildroot}%{python3_sitearch}/_gv.so
install -p tclpkg/gv/gv.py %{buildroot}%{python3_sitearch}/gv.py

# Ghost plugins config
touch %{buildroot}%{_libdir}/graphviz/config%{pluginsver}

# Fix lua file placement for flatpak
if [ "%{_prefix}" != "/usr" ]; then
  cp -ru %{buildroot}/usr/* %{buildroot}%{_prefix}/
  rm -rf %{buildroot}/usr/*
fi

# Explicitly create examples directory to always have it.
# At the moment there are only examples dependant on smyrna. I.e. if smyrna is not
# built this directory is empty.
mkdir -p %{buildroot}%{_datadir}/%{name}/examples

%check
%if %{PHP}
# Minimal load test of php extension
LD_LIBRARY_PATH=%{buildroot}%{_libdir} \
php --no-php-ini \
    --define extension_dir=%{buildroot}%{_libdir}/graphviz/php/ \
    --define extension=libgv_php.so \
    --modules | grep gv
%endif

# upstream test suite
# testsuite seems broken, disabling it for now
# cd rtest
# make rtest

%transfiletriggerin -- %{_libdir}/graphviz
%{_bindir}/dot -c 2>/dev/null || :

%transfiletriggerpostun -- %{_libdir}/graphviz
%{_bindir}/dot -c 2>/dev/null || :

%files
%license COPYING
%doc %{_docdir}/%{name}
%if %{SMYRNA}
%exclude %{_bindir}/smyrna
%exclude %{_mandir}/man1/smyrna.1*
%endif
%{_bindir}/*
%dir %{_libdir}/graphviz
%{_libdir}/graphviz/*.so.*
%{_mandir}/man1/*.1*
%{_mandir}/man7/*.7*
%dir %{_datadir}/%{name}
%exclude %{_docdir}/%{name}/*.html
%exclude %{_docdir}/%{name}/*.pdf
%exclude %{_docdir}/%{name}/demo
%{_datadir}/%{name}/gvpr
%{_datadir}/%{name}/examples
%ghost %{_libdir}/%{name}/config%{pluginsver}

%if %{QTAPPS}
%{_datadir}/%{name}/gvedit
%endif

%exclude %{_libdir}/graphviz/*/*
%exclude %{_libdir}/graphviz/libgvplugin_gd.*
%if %{with gtk2}
%exclude %{_libdir}/graphviz/libgvplugin_gdk.*
%endif
%if %{DEVIL}
%exclude %{_libdir}/graphviz/libgvplugin_devil.*
%endif
%if %{MING}
%exclude %{_libdir}/graphviz/libgvplugin_ming.*
%exclude %{_libdir}/graphviz/*fdb
%endif

%files libs
%license COPYING
%{_libdir}/libcdt.so.6{,.*}
%{_libdir}/libcgraph.so.8{,.*}
%{_libdir}/libgvc.so.7{,.*}
%{_libdir}/libgvpr.so.2{,.*}
%{_libdir}/libpathplan.so.4{,.*}
%{_libdir}/libxdot.so.4{,.*}

%files devel
%{_includedir}/graphviz
%{_libdir}/*.so
%{_libdir}/graphviz/*.so
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man3/*.3.*

%if %{DEVIL}
%files devil
%{_libdir}/graphviz/libgvplugin_devil.so.*
%endif

%files doc
%doc %{_docdir}/%{name}/*.html
%doc %{_docdir}/%{name}/*.pdf
%doc %{_docdir}/%{name}/demo

%if %{SMYRNA}
%files smyrna
%{_bindir}/smyrna
%{_datadir}/%{name}/smyrna
%{_mandir}/man1/smyrna.1*
%endif

%files gd
%{_libdir}/graphviz/libgvplugin_gd.so.*

%if %{with gtk2}
%files gtk2
%{_libdir}/graphviz/libgvplugin_gdk.so.*
%endif

%files graphs
%dir %{_datadir}/graphviz
%{_datadir}/graphviz/graphs

%if %{GUILE}
%files guile
%{_libdir}/graphviz/guile/
%{_mandir}/man3/gv.3guile*
%endif

%if %{JAVA}
%files java
%{_libdir}/graphviz/java/
%{_mandir}/man3/gv.3java*
%endif

%files lua
%{_libdir}/graphviz/lua/
%{_libdir}/lua*/*
%{_mandir}/man3/gv.3lua*

%if %{MING}
%files ming
%{_libdir}/graphviz/libgvplugin_ming.so.*
%{_libdir}/graphviz/*fdb
%endif

%files perl
%{_libdir}/graphviz/perl/
%{_libdir}/perl*/*
%{_mandir}/man3/gv.3perl*

%if %{PHP}
%files php
%config(noreplace) %{_sysconfdir}/php.d/%{ini_name}
%{_libdir}/graphviz/php/
%{php_extdir}/gv.so
%{_datadir}/php*/*
%{_mandir}/man3/gv.3php*
%endif

%if %{with python2}
%files python2
%{python2_sitearch}/*
%{_mandir}/man3/gv.3python*
%endif

%files python3
%{python3_sitearch}/*
%{_mandir}/man3/gv.3python*

%if %{ARRRR}
%files R
%{_libdir}/graphviz/R/
%{_mandir}/man3/gv.3r.*
%endif

%files ruby
%{_libdir}/graphviz/ruby/
%{_libdir}/*ruby*/*
%{_mandir}/man3/gv.3ruby*

%if %{SHARP}
%files sharp
%{_libdir}/graphviz/sharp/
%{_mandir}/man3/gv.3sharp*
%endif

%files tcl
%{_libdir}/graphviz/tcl/
%{_libdir}/tcl*/*
# hack to include gv.3tcl only if available
#  always includes tcldot.3tcl, gdtclft.3tcl
%{_mandir}/man3/*.3tcl*

%if %{GOLANG}
%files go
%{_libdir}/graphviz/go/
%{_mandir}/man3/gv.3go.*
%endif

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 14.1.4-2
- Import
