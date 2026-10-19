%global source0_hash b466fe730d751e4bfc5900d1f37b0fb955f2826ac456e70012785e012cdcb73e
%define set_javaver() \
%{nil}
Name:		qdbm
Version:	1.8.78
Release:        1%{?dist}
License:	LGPL-2.1-or-later
URL:		http://fallabs.com/qdbm/
Source0:        http://deb.debian.org/debian/pool/main/q/qdbm/qdbm_%{version}.orig.tar.gz
Patch0:		qdbm-ruby-1.9-compat.patch
Patch1:		qdbm-1.8.78-java17-yield-usage.patch
Patch2:		qdbm-1.8.78-ruby-module-c99-conformant.patch
%ifarch %java_arches
%set_javaver	45	25
%set_javaver	44	25
%set_javaver	43	21
%set_javaver	42	21
%endif
%ifarch %java_arches
%endif
Summary:        Quick Database Manager
# oreon:deps
BuildRequires:  bzip2-devel
BuildRequires:  gcc-c++
BuildRequires:  lzo-devel
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  ruby
BuildRequires:  ruby-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
QDBM is an embedded database library compatible with GDBM and NDBM.
It features hash database and B+ tree database and is developed referring
to GDBM for the purpose of the following three points: higher processing
speed, smaller size of a database file, and simpler API.

%package devel
Summary:	Libraries and Header files for QDBM Database library
Requires:	%{name} = %{version}-%{release}
%description devel
This is the development package that provides header files and libraries
for QDBM library.

%package cgi
Summary:	CGI interface for QDBM Database
Requires:	%{name} = %{version}-%{release}
Requires:	webserver
%description cgi
This package contains a CGI interface for QDBM Database.

%package java
Summary:	QDBM Database Library for Java
Requires:	%{name} = %{version}-%{release}
Requires:	java-headless
%description java
This package contains a Java interface for QDBM Database library.

%package javadoc
Summary:	API docs for QDBM Database Library Java interface
BuildArch:	noarch
%description javadoc
This package contains the API documentation for the QDBM Database library Java
interface.

%package perl
Summary:	QDBM Database Library for Perl
Requires:	%{name} = %{version}-%{release}
%description perl
This package contains a Perl interface for QDBM Database library.

%package -n qdbm++
Summary:	QDBM Database Library for C++
Requires:	%{name} = %{version}-%{release}
%description -n qdbm++
This package contains a C++ interface for QDBM Database library.

%package -n qdbm++-devel
Summary:	Libraries and Header files for QDBM C++ interface
Requires:	qdbm++ = %{version}-%{release}
%description -n qdbm++-devel
This is the development package that provides header files and libraries
for QDBM C++ interface.

%package -n ruby-qdbm
Summary:	QDBM Database Library for Ruby
Requires:	%{name} = %{version}-%{release}
Requires:	ruby(release)
Provides:	ruby(qdbm) = %{version}-%{release}
%description -n ruby-qdbm
This package contains a Ruby interface for QDBM Database library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Fix path in doc/index*.html
sed -i.link  \
	-e 's|"spex|"../%{name}-devel-%{version}/spex|' \
	-e 's|"xspex|"../%{name}++-devel-%{version}/xspex|' \
	-e 's|"jspex|"../%{name}-java-%{version}/jspex|' \
	-e 's|"plspex|"../%{name}-perl-%{version}/plspex|' \
	-e 's|"rbspex|"../ruby-%{name}-%{version}/rbspex|' \
	-e 's|"cgispex|"../%{name}-cgi-%{version}/cgispex|' \
	doc/index*.html
	
%build

for f in `find . -name Makefile.in` ; do
	%{__sed} -i.rpath -e '/^LDENV/d' $f
done
%{__sed} -i.misc \
	 -e '/^Libs/s|@LIBS@||' \
	 -e '/Cflags/s|^\(.*\)|\1 -I\${includedir}/qdbm|' \
	 qdbm.pc.in
%{__sed} -i.stamp \
	 -e 's|cp \(-R*f \)|cp -p \1| ' \
	 -e 's|^CP =.*$|CP = cp -p|' \
	`find . -name \*[mM]akefile.in -or -name \*[mM]akefile`
%{__sed} -i.flags -e '/^CFLAGS/s|-O3.*$|%{optflags}|' Makefile.in
%configure \
	--enable-pthread \
	--enable-zlib \
	--enable-bzip \
	--enable-iconv \
	--enable-lzo
%{__make} %{?_smp_mflags}
pushd plus
%{__sed} -i.flags -e '/^CXXFLAGS/s|@MYOPTS@|%{optflags}|' Makefile.in
%configure
%{__make} %{?_smp_mflags}
popd
%ifarch %java_arches
pushd java
%{__sed} -i.flags -e '/^CFLAGS/s|@MYOPTS@|%{optflags}|' Makefile.in
export JAVA_HOME=%{java_home}
%configure
%{__make} JAR=%{jar} JAVAC=%{javac}
popd
%endif
pushd cgi
%{__sed} -i.flags -e \
	 '/^CFLAGS/s|-O2.*$|%{optflags} -DCONFDIR="\"@sysconfdir@/qdbm/\""|' Makefile.in
%configure
%{__make} %{?_smp_mflags}
popd
pushd perl
%configure
%{__make} %{?_smp_mflags} CC="gcc %optflags" LDDLFLAGS="-shared" INSTALLDIRS=vendor
popd
pushd ruby
%configure
sed -i 's|extconf.rb |extconf.rb --vendor |' Makefile
%{__make} %{?_smp_mflags} CC="gcc %optflags"
popd
%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT
%{__rm} -rf $RPM_BUILD_ROOT%{_libdir}/lib*.a
%{__rm} -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/
pushd cgi
%{__make} install DESTDIR=$RPM_BUILD_ROOT
popd
%{__rm} -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/cgi/*.html
%{__install} -d $RPM_BUILD_ROOT%{_sysconfdir}/qdbm
%{__mv} $RPM_BUILD_ROOT%{_datadir}/qdbm/cgi/*.conf \
	$RPM_BUILD_ROOT%{_sysconfdir}/qdbm/
rmdir $RPM_BUILD_ROOT%{_datadir}/qdbm/cgi
rmdir $RPM_BUILD_ROOT%{_datadir}/qdbm
%ifarch %java_arches
pushd java
%{__make} install DESTDIR=$RPM_BUILD_ROOT JAR=%{jar}
popd
%{__mkdir_p} $RPM_BUILD_ROOT%{_jnidir}
%{__mv} -f $RPM_BUILD_ROOT%{_libdir}/*.jar \
	$RPM_BUILD_ROOT%{_jnidir}
%{__mkdir_p} $RPM_BUILD_ROOT%{_javadocdir}
%{__mv} $RPM_BUILD_ROOT%{_datadir}/qdbm/java/japidoc \
	$RPM_BUILD_ROOT%{_javadocdir}/%{name}
%{__rm} $RPM_BUILD_ROOT%{_datadir}/qdbm/java/*.html
rmdir $RPM_BUILD_ROOT%{_datadir}/qdbm/java
rmdir $RPM_BUILD_ROOT%{_datadir}/qdbm
%endif
pushd perl
%{__make} install DESTDIR=$RPM_BUILD_ROOT INSTALLDIRS=vendor
popd
%{__rm} -rf $RPM_BUILD_ROOT%{_datadir}/qdbm/perl/plapidoc
%{__rm} $RPM_BUILD_ROOT%{_datadir}/qdbm/perl/*.html
rmdir $RPM_BUILD_ROOT%{_datadir}/qdbm/perl
rmdir $RPM_BUILD_ROOT%{_datadir}/qdbm
%{__rm} $RPM_BUILD_ROOT%{perl_archlib}/perllocal.pod
find $RPM_BUILD_ROOT%{perl_vendorarch} \
	-name \*.bs -or -name .packlist | \
	xargs rm -f
find $RPM_BUILD_ROOT%{perl_vendorarch} \
	-name \*.so | \
	xargs chmod 0755
pushd plus
make install DESTDIR=$RPM_BUILD_ROOT
popd
%{__rm} -rf $RPM_BUILD_ROOT%{_libdir}/lib*.a
%{__rm} -rf $RPM_BUILD_ROOT%{_datadir}/qdbm/plus/xapidoc
%{__rm} $RPM_BUILD_ROOT%{_datadir}/qdbm/plus/*.html
rmdir $RPM_BUILD_ROOT%{_datadir}/qdbm/plus
rmdir $RPM_BUILD_ROOT%{_datadir}/qdbm
pushd ruby
make install DESTDIR=$RPM_BUILD_ROOT
popd
%{__rm} -rf $RPM_BUILD_ROOT%{_datadir}/qdbm/ruby/rbapidoc
%{__rm} $RPM_BUILD_ROOT%{_datadir}/qdbm/ruby/*.html
rmdir $RPM_BUILD_ROOT%{_datadir}/qdbm/ruby
rmdir $RPM_BUILD_ROOT%{_datadir}/qdbm
pushd $RPM_BUILD_ROOT%{_includedir}
for f in *.h ; do
	for g in *.h ; do
		eval sed -i -e \'s\|include \<$g\>\|include \"$g\"\|\' $f
	done
done
%{__mkdir} qdbm
%{__mv} *.h qdbm/
popd
%ldconfig_scriptlets
%ldconfig_scriptlets java
%ldconfig_scriptlets -n qdbm++
%oreon_autofiles ruby-qdbm usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n qdbm-devel -f %{oreon_filedir}/qdbm-devel.list
%files -n qdbm-cgi -f %{oreon_filedir}/qdbm-cgi.list
%files -n qdbm-java -f %{oreon_filedir}/qdbm-java.list
%files -n qdbm-javadoc -f %{oreon_filedir}/qdbm-javadoc.list
%files -n qdbm-perl -f %{oreon_filedir}/qdbm-perl.list
%files -n ruby-qdbm -f %{oreon_filedir}/ruby-qdbm.list

%changelog

%autochangelog
