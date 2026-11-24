# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 24c345b5c077c1b2b2fcbc1a364f1da051650fb6743ad5213096adc04c862ed4
%global source1_hash d17123e101ada18cce7022d9794fb97344d3151028c4f51f652fcf992e8d0da2
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global with_python3 %{?_without_python3: 0} %{?!_without_python3: 1}
%global with_php %{?_without_php: 0} %{?!_without_php: 0}
%global with_tcl %{?_without_tcl: 0} %{?!_without_tcl: 1}
%global with_ruby %{?_without_ruby: 0} %{?!_without_ruby: 1}
%global with_lua %{?_without_lua: 0} %{?!_without_lua: 1}
%if 0%{?rhel} || 0%{?oreon}
%global with_dbi 0
%else
%global with_dbi 1
%endif
%global php_extdir %(php-config --extension-dir 2>/dev/null || echo %{_libdir}/php4)
%global svnrev r1190

%if "%{php_version}" < "5.6"
%global ini_name     %{name}.ini
%else
%global ini_name     40-%{name}.ini
%endif

Summary: Round Robin Database Tool to store and display time-series data
Name: rrdtool
Version: 1.11.0
Release: 1%{?dist}
License: gpl-1.0-or-later AND gpl-2.0-or-later AND gpl-2.0-or-later WITH rrdtool-floss-exception-2.0 AND mit AND lgpl-2.0-or-later AND lgpl-2.1-or-later AND bsd-source-code AND snprintf AND bsd-3-clause AND gpl-2.0-only AND licenseref-fedora-public-domain AND gtkbook
URL: https://oss.oetiker.ch/rrdtool/
Source0: https://github.com/oetiker/rrdtool-1.x/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1: php4-%{svnrev}.tar.gz
Patch1: rrdtool-1.4.4-php54.patch
Patch2: rrdtool-1.4.7-php55.patch
Patch3: rrdtool-1.10.3-ruby-2-fix.patch
Patch4: rrdtool-1.4.8-php-ppc-fix.patch

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: freetype-devel
BuildRequires: libpng-devel
BuildRequires: zlib-devel
BuildRequires: intltool >= 0.35.0
BuildRequires: cairo-devel >= 1.4.6
BuildRequires: pango-devel >= 1.17
BuildRequires: libtool
BuildRequires: groff
BuildRequires: gettext
BuildRequires: libxml2-devel
BuildRequires: systemd
BuildRequires: sed
%if %{with_dbi}
BuildRequires: libdbi-devel
%endif
BuildRequires: perl-ExtUtils-MakeMaker
BuildRequires: perl-generators
BuildRequires: perl-Pod-Html
BuildRequires: perl-devel
BuildRequires: automake
BuildRequires: autoconf
Requires: dejavu-sans-mono-fonts
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%description
RRD is the Acronym for Round Robin Database. RRD is a system to store and
display time-series data (i.e. network bandwidth, machine-room temperature,
server load average). It stores the data in a very compact way that will not
expand over time, and it presents useful graphs by processing the data to
enforce a certain data density. It can be used either via simple wrapper
scripts (from shell or Perl) or via frontends that poll network devices and
put a friendly user interface on it.

%package devel
Summary: RRDtool libraries and header files
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
RRD is the Acronym for Round Robin Database. RRD is a system to store and
display time-series data (i.e. network bandwidth, machine-room temperature,
server load average). This package allow you to use directly this library.

%package doc
Summary: RRDtool documentation

%description doc
RRD is the Acronym for Round Robin Database. RRD is a system to store and
display time-series data (i.e. network bandwidth, machine-room temperature,
server load average). This package contains documentation on using RRD.

%package perl
Summary: Perl RRDtool bindings
Requires: %{name} = %{version}-%{release}
Obsoletes: perl-%{name} < %{version}-%{release}
Provides: perl-%{name} = %{version}-%{release}

%description perl
The Perl RRDtool bindings

%package -n python3-rrdtool
%{?python_provide:%python_provide python3-rrdtool}
Summary: Python RRDtool bindings
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-pip
Requires: %{name} = %{version}-%{release}

%description -n python3-rrdtool
Python RRDtool bindings.

%if %{with_php}
%package php
Summary: PHP RRDtool bindings
BuildRequires: php-devel >= 4.0
Requires: php >= 4.0
Requires: %{name} = %{version}-%{release}
Requires: php(zend-abi) = %{php_zend_api}
Requires: php(api) = %{php_core_api}
Obsoletes: php-%{name} < %{version}-%{release}
Provides: php-%{name} = %{version}-%{release}
Provides: php-pecl(rrdtool)

%description php
The %{name}-php package includes a dynamic shared object (DSO) that adds
RRDtool bindings to the PHP HTML-embedded scripting language.
%endif

%if %{with_tcl}
%package tcl
Summary: Tcl RRDtool bindings
BuildRequires: tcl-devel >= 8.0
Requires: tcl >= 8.0
Requires: %{name} = %{version}-%{release}
Obsoletes: tcl-%{name} < %{version}-%{release}
Provides: tcl-%{name} = %{version}-%{release}

%description tcl
The %{name}-tcl package includes RRDtool bindings for Tcl.
%endif

%if %{with_ruby}
%{!?ruby_vendorarchdir: %global ruby_vendorarchdir %(ruby -rrbconfig -e 'puts RbConfig::CONFIG["vendorarchdir"]')}

%package ruby
Summary: Ruby RRDtool bindings
BuildRequires: ruby
BuildRequires: ruby-devel
Requires: %{name} = %{version}-%{release}

%description ruby
The %{name}-ruby package includes RRDtool bindings for Ruby.
%endif

%if %{with_lua}
%{!?luaver: %global luaver %(lua -e "print(string.sub(_VERSION, 5))")}
%global lualibdir %{_libdir}/lua/%{luaver}
%global luapkgdir %{_datadir}/lua/%{luaver}

%package lua
Summary: Lua RRDtool bindings
BuildRequires: lua
BuildRequires: lua-devel
%if "%{luaver}" != ""
Requires: lua(abi) = %{luaver}
%endif
Requires: %{name} = %{version}-%{release}

%description lua
The %{name}-lua package includes RRDtool bindings for Lua.
%endif

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
%setup -q -n %{name}-%{version} %{?with_php: -a 1}
%if %{with_php}
%patch -P1 -p1 -b .php54
%patch -P2 -p1 -b .php55
%endif
%if %{?rhel} %{?!rhel:7} > 6
%patch -P3 -p1 -b .ruby-2-fix
%endif
%patch -P4 -p1 -b .php-ppc-fix

perl -pi.orig -e 's|/lib\b|/%{_lib}|g' \
    configure Makefile.in php4/configure php4/ltconfig*

perl -pi.orig -e 's|1.299907080300|1.29990708|' \
    bindings/perl-shared/RRDs.pm bindings/perl-piped/RRDp.pm

cp -p /usr/lib/rpm/redhat/config.{guess,sub} php4/

%if %{with_python3}
cd bindings/python
%generate_buildrequires
%pyproject_buildrequires -N
%endif

%build
./bootstrap
%configure \
    --with-perl-options='INSTALLDIRS="vendor"' \
    --disable-rpath \
%if %{with_tcl}
    --enable-tcl-site \
    --with-tcllib=%{_libdir} \
%else
    --disable-tcl \
%endif
%if %{with_ruby}
    --enable-ruby \
%else
    --disable-ruby \
%endif
%if %{with_dbi}
    --enable-libdbi \
%else
    --disable-libdbi \
%endif
    --disable-static \
    --with-pic \
    --disable-python

perl -pi.orig -e 's|-Wl,--rpath -Wl,\$rp||g' \
    bindings/perl-shared/Makefile.PL

%if %{with_ruby}
perl -pi.orig -e 's|-Wl,--rpath -Wl,\$\(EPREFIX\)/lib||g' \
    bindings/ruby/extconf.rb
sed -i 's|extconf.rb \\|extconf.rb --vendor \\|' bindings/Makefile
%endif

pushd bindings/perl-piped/
perl Makefile.PL INSTALLDIRS=vendor
perl -pi.orig -e 's|/lib/perl|/%{_lib}/perl|g' Makefile
popd

%{make_build}

%if %{with_php}
%global rrdtmp %{_tmppath}/%{name}-%{version}-tmpinstall
%{__make} install DESTDIR="%{rrdtmp}"
pushd php4/

%configure \
    --with-rrdtool="%{rrdtmp}%{_prefix}" \
    --disable-static
%{make_build}
popd
rm -rf %{rrdtmp}
%endif

find examples/ -type f \
    -exec perl -pi -e 's|^#! \@perl\@|#!%{__perl}|gi' {} \;
find examples/ -name "*.pl" \
    -exec perl -pi -e 's|\015||gi' {} \;

%if %{with_python3}
cd bindings/python
%pyproject_wheel
%endif

%install
export
%{make_install}

%if %{with_php}
install -D -m0755 php4/modules/rrdtool.so \
    %{buildroot}%{php_extdir}/rrdtool.so
rm -rf php4/examples/.svn
mkdir -p %{buildroot}%{_sysconfdir}/php.d
cat << __EOF__ > %{buildroot}%{_sysconfdir}/php.d/%{ini_name}
; Enable rrdtool extension module
extension=rrdtool.so
__EOF__
%endif

mv $RPM_BUILD_ROOT%{perl_vendorlib}/RRDp.pm $RPM_BUILD_ROOT%{perl_vendorarch}/

rm -f $RPM_BUILD_ROOT%{perl_vendorlib}/leaktest.pl

mkdir -p doc2/html doc2/txt
cp -a doc/*.txt doc2/txt/
cp -a doc/*.html doc2/html/

mkdir -p doc3/html
mv doc2/html/RRD*.html doc3/html/

rm -f examples/Makefile* examples/*.in examples/rrdcached/Makefile*

find examples/ -type f -exec chmod 0644 {} \;

rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}-* \
        $RPM_BUILD_ROOT%{perl_vendorarch}/ntmake.pl \
        $RPM_BUILD_ROOT%{perl_archlib}/perllocal.pod \
        $RPM_BUILD_ROOT%{_datadir}/%{name}/examples \
        $RPM_BUILD_ROOT%{perl_vendorarch}/auto/*/{.packlist,*.bs}

%find_lang %{name}

%if %{with_python3}
cd bindings/python
%pyproject_install
%pyproject_save_files %{name} '%{name}*'
%endif

%check
%if %{with_php}
LD_LIBRARY_PATH=%{buildroot}%{_libdir} php -n \
    -d extension_dir=%{buildroot}%{php_extdir} \
    -d extension=rrdtool.so -m \
    | grep rrdtool
%endif

%post
%systemd_post rrdcached.service rrdcached.socket

%preun
%systemd_post rrdcached.service rrdcached.socket

%postun
%systemd_post rrdcached.service rrdcached.socket

%files -f %{name}.lang
%license LICENSE
%doc CONTRIBUTORS COPYRIGHT TODO NEWS CHANGES THREADS
%{_bindir}/*
%{_libdir}/*.so.*
%{_unitdir}/rrdcached.service
%{_unitdir}/rrdcached.socket
%{_datadir}/%{name}
%{_mandir}/man1/*
%{_mandir}/man3/lib*.3*

%files devel
%{_includedir}/*.h
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc

%files doc
%doc examples doc2/html doc2/txt

%files perl
%doc doc3/html
%{_mandir}/man3/*.3pm*
%{perl_vendorarch}/*.pm
%attr(0755,root,root) %{perl_vendorarch}/auto/RRDs/

%if %{with_python3}
%files -n python3-rrdtool -f %{pyproject_files}
%doc bindings/python/COPYING bindings/python/README.md
%endif

%if %{with_php}
%files php
%doc php4/examples php4/README
%config(noreplace) %{_sysconfdir}/php.d/%{ini_name}
%{php_extdir}/rrdtool.so
%endif

%if %{with_tcl}
%files tcl
%doc bindings/tcl/README
%{_libdir}/tclrrd*.so
%{_libdir}/rrdtool/*.tcl
%endif

%if %{with_ruby}
%files ruby
%doc bindings/ruby/README
%{ruby_vendorarchdir}/RRD.so
%endif

%if %{with_lua}
%files lua
%doc bindings/lua/README
%{lualibdir}/*
%endif

%changelog
%autochangelog
