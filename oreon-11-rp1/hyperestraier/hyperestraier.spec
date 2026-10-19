%global source0_hash 92f3e76d12da79e116e4e68487ffdddfc2abe5f50f509247905414daa5c38fff
%global		rubyabi		1.9.1
%define		qdbm_ver	1.8.75
%{!?ruby_arch:	%define ruby_arch	%(ruby -rrbconfig -e "puts RbConfig::CONFIG['archdir']")}
%define set_javaver() \
%{nil}
Name:		hyperestraier
Version:	1.4.13
Release:        1%{?dist}
Summary:        A full-text search system
License:	LGPL-2.1-or-later AND BSD-3-Clause
URL:		http://hyperestraier.sourceforge.net/
Source0:        http://hyperestraier.sourceforge.net/%{name}-%{version}.tar.gz
Patch0:		huperestraier-1.4.13-ruby-19-compat.patch
Patch1:		hyperestraier-1.4.13-javanative-configure-c99-compat.patch
Patch2:		hyperestraier-1.4.13-rubyext-functype.patch
%ifarch %java_arches
%set_javaver	45	25
%set_javaver	44	25
%set_javaver	43	21
%set_javaver	42	21
%endif
# oreon:deps
BuildRequires:  bzip2-devel
BuildRequires:  gcc
BuildRequires:  lzo-devel
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  qdbm-devel
BuildRequires:  ruby-devel
BuildRequires:  rubygem(rdoc)
BuildRequires:  zlib-devel
# /oreon:deps
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
%{__sed} -i.flags \
	-e '/^CFLAGS/s|^\(.*\)$|\1 %{optflags}|' Makefile.in
%configure \
	--enable-devel \
	--enable-zlib \
	--enable-bzip \
	--enable-lzo
%{__make} %{?_smp_mflags}
%ifarch %java_arches
pushd javanative/
%{__sed} -i.flags -e '/^MYCFLAGS/s|-O2.*|%{optflags}\"|' configure
export JAVA_HOME=%{java_home}
%configure
%{__make} -j1 JAR=%{jar} JAVAC=%{javac}
popd
%endif
pushd perlnative
%configure
%{__make} %{?_smp_mflags} \
	CC="gcc %optflags $(pkg-config --cflags qdbm)" \
	OPTIMIZE="" \
	LDDLFLAGS="-shared"
popd
pushd rubynative
%{__cp} -p %{ruby_arch}/rbconfig.rb .
%{__sed} -i.static -e 's|-static||g' rbconfig.rb
export RUBYLIB=$(pwd)
%{__sed} -i.path -e 's|-O3.*|\`pkg-config --cflags qdbm\`\"|' src/extconf.rb
%{__sed} -i.vendor \
	-e 's|myrblibdir=.*|myrblibdir=%{ruby_vendorarchdir}|' configure
%configure
%{__make} %{?_smp_mflags}
popd
%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT
%{__rm} -f $RPM_BUILD_ROOT%{_libdir}/lib*.a
%{__rm} -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/doc/
%{__rm} -f $RPM_BUILD_ROOT%{_datadir}/%{name}/[A-Z]*
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
pushd javanative/
%{__make} DESTDIR=$RPM_BUILD_ROOT install JAR=%{jar}
popd
%{__mkdir_p} $RPM_BUILD_ROOT%{_jnidir}
%{__mv} -f $RPM_BUILD_ROOT%{_libdir}/*.jar \
	$RPM_BUILD_ROOT%{_jnidir}
%endif
pushd perlnative
%{__make} install DESTDIR=$RPM_BUILD_ROOT INSTALLDIRS=vendor
popd
%{__rm} $RPM_BUILD_ROOT%{perl_archlib}/perllocal.pod
find $RPM_BUILD_ROOT%{perl_vendorarch} \
	-name \*.bs -or -name .packlist | \
	xargs rm -f
find $RPM_BUILD_ROOT%{perl_vendorarch} \
	-name \*.so | \
	xargs chmod 0755
pushd rubynative/
%{__make} DESTDIR=$RPM_BUILD_ROOT install \
	ruby_headers=
popd
%ldconfig_scriptlets
%oreon_autofiles ruby-hyperestraier usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n hyperestraier-devel -f %{oreon_filedir}/hyperestraier-devel.list
%files -n hyperestraier-java -f %{oreon_filedir}/hyperestraier-java.list
%files -n hyperestraier-perl -f %{oreon_filedir}/hyperestraier-perl.list
%files -n ruby-hyperestraier -f %{oreon_filedir}/ruby-hyperestraier.list

%changelog

%autochangelog
