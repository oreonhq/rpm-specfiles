%global source0_hash 92f3e76d12da79e116e4e68487ffdddfc2abe5f50f509247905414daa5c38fff

%global		rubyabi		1.9.1
%define		qdbm_ver	1.8.75

# Workaround for ruby side bug (bug 226381 c11)
%{!?ruby_arch:	%define ruby_arch	%(ruby -rrbconfig -e "puts RbConfig::CONFIG['archdir']")}

%define set_javaver() \
%if 	0%{?fedora}%{?rhel} == %1 \
BuildRequires:	java-%2-openjdk-devel \
%if	%1 >= 42 \
BuildRequires:	javapackages-local-openjdk%2 \
%endif \
%endif \
%{nil}

Name:		hyperestraier
Version:	1.4.13
Release:	73%{?dist}
Summary:	A full-text search system

# Overall	LGPL-2.1-or-later
# javapure/*.java	BSD-3-Clause
# md5.c	Zlib
# rubypure/estcall.rb	BSD-3-Clause
# SPDX confimed
License:	LGPL-2.1-or-later AND BSD-3-Clause
URL:		http://hyperestraier.sourceforge.net/
Source0:	http://hyperestraier.sourceforge.net/%{name}-%{version}.tar.gz
# Taken from Debian:
# http://packages.debian.org/testing/ruby/libestraier-ruby1.9.1
Patch0:		huperestraier-1.4.13-ruby-19-compat.patch
# Make javanative/configure c99 compat manually
# instead of rerunning autoupdate -> autoconf
Patch1:		hyperestraier-1.4.13-javanative-configure-c99-compat.patch
# rubynative: fix function prototype passed to rb_rescue
Patch2:		hyperestraier-1.4.13-rubyext-functype.patch

BuildRequires:	gcc
BuildRequires:	bzip2-devel zlib-devel
BuildRequires:	lzo-devel >= 2.02
BuildRequires:	qdbm-devel >= %{qdbm_ver}
BuildRequires:	rubygem(rdoc)
BuildRequires:	ruby-devel
BuildRequires:	perl-devel
BuildRequires:	perl-generators
BuildRequires:	perl(ExtUtils::MakeMaker)
# java related macros
%ifarch %java_arches
%set_javaver	45	25
%set_javaver	44	25
%set_javaver	43	21
%set_javaver	42	21
BuildRequires:	javapackages-tools
%endif
BuildRequires:	make

%description
Hyper Estraier is a full-text search system. You can search 
lots of documents for some documents including specified words. 
If you run a web site, it is useful as your own search engine 
for pages in your site. Also, it is useful as search utilities 
of mail boxes and file servers.

%package devel
Summary:	Libraries and Header files for Hyper Estraier
Requires:	%{name} = %{version}-%{release}
Requires:	qdbm-devel >= %{qdbm_ver}
Requires:	pkgconfig

%description devel
This is the development package that provides header files and libraries
for Hyper Estraier.

%package java
Summary:	Hyper Estraier library for Java
Requires:	%{name} = %{version}-%{release}

%description java
This package contains a Java interface for Hyper Estraier

%package perl
Summary:	Hyper Estraier library for Perl
Requires:	%{name} = %{version}-%{release}

%description perl
This package contains a Perl interface for Hyper Estraier

%package -n ruby-hyperestraier
Summary:	Hyper Estraier Library for Ruby
Requires:	%{name} = %{version}-%{release}
Requires:	ruby(release)
Provides:	ruby(hyperestraier) = %{version}-%{release}

%description -n ruby-hyperestraier
This package contains a Ruby interface for Hyper Estraier.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

%build
## 0. First:
## - remove rpath
## - fix pkgconfig file to hide header files
## - fix Makefile to keep timestamps
%{__sed} -i.rpath -e '/^LDENV/d' `find . -name Makefile.in`
%{__sed} -i.misc \
	 -e '/^Libs/s|@[A-Z][A-Z]*@||g' \
	 -e '/Cflags/s|^\(.*\)|\1 -I\${includedir}/%{name}|' \
	 %{name}.pc.in

%{__sed} -i.path \
	-e '/^cflags/s|^\(.*\)\"$|\1 -I%{_datadir}/qdbm -I%{_datadir}/%{name}\"|' \
	estconfig.in

%{__sed} -i.stamp \
	 -e 's|cp \(-R*f \)|cp -p \1| ' \
	 -e 's|^CP =.*$|CP = cp -p|' \
	`find . -name Makefile.in -or -name \*[mM]akefile`

## 1. For main
%{__sed} -i.flags \
	-e '/^CFLAGS/s|^\(.*\)$|\1 %{optflags}|' Makefile.in
%configure \
	--enable-devel \
	--enable-zlib \
	--enable-bzip \
	--enable-lzo

%{__make} %{?_smp_mflags}

## 2. For java
%ifarch %java_arches
pushd javanative/
%{__sed} -i.flags -e '/^MYCFLAGS/s|-O2.*|%{optflags}\"|' configure
export JAVA_HOME=%{java_home}
%configure
# Failed with -j8 on Matt's mass build
%{__make} -j1 JAR=%{jar} JAVAC=%{javac}
popd
%endif

## 3. For perl:
pushd perlnative
%configure
%{__make} %{?_smp_mflags} \
	CC="gcc %optflags $(pkg-config --cflags qdbm)" \
	OPTIMIZE="" \
	LDDLFLAGS="-shared"
popd

##4. For ruby
pushd rubynative

# Workaround for ruby side bug (bug 226381 c11)
%{__cp} -p %{ruby_arch}/rbconfig.rb .
%{__sed} -i.static -e 's|-static||g' rbconfig.rb
export RUBYLIB=$(pwd)

%{__sed} -i.path -e 's|-O3.*|\`pkg-config --cflags qdbm\`\"|' src/extconf.rb

# Fix placement for Ruby 1.9.
%{__sed} -i.vendor \
	-e 's|myrblibdir=.*|myrblibdir=%{ruby_vendorarchdir}|' configure

%configure
%{__make} %{?_smp_mflags}
popd

%install
%{__rm} -rf $RPM_BUILD_ROOT

## 1. For main
%{__make} install DESTDIR=$RPM_BUILD_ROOT

# clean up
%{__rm} -f $RPM_BUILD_ROOT%{_libdir}/lib*.a
%{__rm} -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/doc/
%{__rm} -f $RPM_BUILD_ROOT%{_datadir}/%{name}/[A-Z]*

# hide header files to name specific directory
pushd $RPM_BUILD_ROOT%{_includedir}
mkdir %{name}
for f in *.h ; do
	for g in *.h ; do
		eval sed -i -e \'s\|include \<$g\>\|include \"$g\"\|\' $f
	done
done
%{__mv} *.h %{name}/
popd

%ifarch %java_arches
## 2. For java
pushd javanative/
%{__make} DESTDIR=$RPM_BUILD_ROOT install JAR=%{jar}
popd
%{__mkdir_p} $RPM_BUILD_ROOT%{_jnidir}
%{__mv} -f $RPM_BUILD_ROOT%{_libdir}/*.jar \
	$RPM_BUILD_ROOT%{_jnidir}
%endif

## 3. For perl
pushd perlnative
%{__make} install DESTDIR=$RPM_BUILD_ROOT INSTALLDIRS=vendor
popd
# clean up
%{__rm} $RPM_BUILD_ROOT%{perl_archlib}/perllocal.pod
find $RPM_BUILD_ROOT%{perl_vendorarch} \
	-name \*.bs -or -name .packlist | \
	xargs rm -f
find $RPM_BUILD_ROOT%{perl_vendorarch} \
	-name \*.so | \
	xargs chmod 0755

## 4. For ruby
pushd rubynative/
%{__make} DESTDIR=$RPM_BUILD_ROOT install \
	ruby_headers=

popd

%ldconfig_scriptlets

%files
%defattr(-,root,root,-)
%license COPYING
%doc ChangeLog
%doc THANKS
%doc example/
%doc doc/*guide-en.html doc/*.png doc/*.css
%lang(ja) %doc doc/*guide-ja.html

%{_libdir}/libestraier.so.*
%{_bindir}/est*
%exclude %{_bindir}/estconfig
%exclude %{_bindir}/*.pl
%exclude %{_bindir}/*.rb
%{_libexecdir}/*.cgi
%{_datadir}/%{name}/

%{_mandir}/man1/*.1*

%files devel
%defattr(-,root,root,-)

%{_bindir}/estconfig
%{_includedir}/%{name}/
%{_libdir}/libestraier.so
%{_libdir}/pkgconfig/*.pc

%{_mandir}/man3/est*.3*

%ifarch %java_arches
%files java
%defattr(-,root,root,-)
%doc doc/javanativeapi/*
%doc javanative/overview.html
%doc javanative/example/

%{_jnidir}/*.jar
%{_libdir}/libj*.so*
%endif

%files perl
%defattr(-,root,root,-)
%doc doc/perlnativeapi/index.html
%doc perlnative/example/

%{_bindir}/*.pl
%{perl_vendorarch}/*.p*
%{perl_vendorarch}/auto/*/
%{_mandir}/man3/*.3pm*

%files -n ruby-hyperestraier
%defattr(-,root,root,-)
%doc doc/rubynativeapi/*
%doc rubynative/example/

%{_bindir}/*.rb
%{ruby_vendorarchdir}/*.so

%changelog
%autochangelog
