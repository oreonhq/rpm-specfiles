%global source0_hash none
%bcond_with jemboss
%bcond_with sunjava
%if %{with sunjava}
%global _java /usr/java/default
%endif
%global emhome %{_datadir}/EMBOSS
Name:           EMBOSS
Version:        6.6.0
Release:        37%{?dist}
Summary:        The European Molecular Biology Open Software Suite
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND CC-BY-3.0 AND GPL-3.0-or-later AND LicenseRef-Fedora-Public-Domain
URL:            http://emboss.sf.net/
Source0:        ftp://emboss.open-bio.org/pub/EMBOSS/%{name}-%{version}.tar.gz
%if %{with jemboss}
Source2:        jemboss.desktop
%endif
Patch1:         EMBOSS-6.6.0-system-pcre.patch
Patch4:         EMBOSS-6.6.0-system-expat.patch
Patch5:         EMBOSS-6.6.0-system-zlib.patch
Patch7:         %{name}-fedora.patch
Patch9:		EMBOSS-6.6.0-fix-conflict-with-pscan.patch
Patch10:	EMBOSS-6.6.0-no-update.patch
Patch11:	EMBOSS-6.6.0-pcre2-v2.patch
Patch12:	EMBOSS-s390-too.patch
Patch13:	EMBOSS-6.6.0-ajax-nkeys-right-type.patch
Patch14:	EMBOSS-6.6.0-c23.patch
%if %{with jemboss}
%endif
%if %{with sunjava}
Requires:       jdk = 2000:1.6.0_17-fcs
%endif
Requires:       %{name}-libs = %{version}-%{release}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  expat-devel
BuildRequires:  gd-devel
BuildRequires:  libharu-devel
BuildRequires:  libpq-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  mariadb-connector-c-devel
BuildRequires:  openssl-devel
BuildRequires:  pam-devel
BuildRequires:  pcre2-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
EMBOSS is a new, free Open Source software analysis package specially
developed for the needs of the molecular biology (e.g. EMBnet) user community.
The software automatically copes with data in a variety of formats and even
allows transparent retrieval of sequence data from the web. Also, as extensive
libraries are provided with the package, it is a platform to allow other
scientists to develop and release software in true open source spirit.
EMBOSS also integrates a range of currently available packages and tools for
sequence analysis into a seamless whole.

Reference for EMBOSS: Rice,P. Longden,I. and Bleasby,A.
"EMBOSS: The European Molecular Biology Open Software Suite"
Trends in Genetics June 2000, vol 16, No 6. pp.276-277

%package devel
Summary:        Development tools for programs which will use the %{name} library
Requires:       %{name}-libs = %{version}-%{release}
Requires:       libeplplot-devel = %{version}-%{release}
%description devel
The %{name}-devel package includes the header files and static libraries
necessary for developing programs which will use the %{name} library.

%package libs
Summary:        Shared libraries for %{name}
%description libs
The %{name}-libs package includes the dynamic libraries
necessary for %{name}.

%if %{with jemboss}
%package -n jemboss
Summary:        Java interface to %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       java >= 1:1.6.0
Requires:       jpackage-utils
Requires:       axis jaf javamail jakarta-commons-discovery jakarta-commons-logging
Requires:       log4j regexp servlet xerces-j2 wsdl4j
%description -n jemboss
Jemboss is a Java interface to EMBOSS, developed at
the HGMP-RC and in close collaboration with the EMBOSS
development team. It is distributed as part of the EMBOSS
software.

Documentation on Jemboss can be found at:
http://www.hgmp.mrc.ac.uk/Software/EMBOSS/Jemboss/
%endif

%package -n libeplplot
Summary:        A modified version of plplot used by EMBOSS
%description -n libeplplot
A modified version of plplot used by EMBOSS.

%package -n libeplplot-devel
Summary:        Development files for eplplot
Requires:       libeplplot = %{version}-%{release}
%description -n libeplplot-devel
The libeplplot-devel package includes the header files and libraries
necessary for developing programs which will use the eplplot library.

%prep

%setup -q
%patch -P1 -p1 -b .system-pcre
%patch -P4 -p1 -b .system-expat
%patch -P5 -p1 -b .system-zlib
%patch -P7 -p0 -b .fedora
%patch -P9 -p1 -b .fixconflict
%patch -P10 -p1 -b .noupdate
%patch -P11 -p1 -b .pcre2
%patch -P12 -p1 -b .s390-too
%patch -P13 -p1 -b .nkeys-right-type
%patch -P14 -p1 -b .c23

# Remove bundled expat, pcre and zlib files to make sure that system versions are used
rm -rf ajax/{expat,pcre,zlib}/*

#install the patch readme
# install -pm 644 %{SOURCE1} README.fixes

#these files were executable for some reason
chmod 644 emboss/prettyplot.c emboss/polydot.c emboss/supermatcher.c

%if %{with jemboss}
#use newer log4j version
sed -i "s@log4j-1.2.8@log4j-1.2.14@" \
    jemboss/lib/axis/Makefile.am \
    jemboss/lib/axis/Makefile.in \
    jemboss/utils/makeFileManagerJNLP.sh \
    jemboss/utils/makeJNLP.sh

#use system java libraries
rm jemboss/lib/{activation,jakarta-regexp-1.2,jemboss,mail,xerces}.jar
build-jar-repository -s -p jemboss/lib activation regexp javamail xerces-j2
mv jemboss/lib/regexp.jar jemboss/lib/jakarta-regexp-1.2.jar
mv jemboss/lib/javamail.jar jemboss/lib/mail.jar
mv jemboss/lib/xerces-j2.jar jemboss/lib/xerces.jar
rm jemboss/lib/axis/*.jar
build-jar-repository -s -p jemboss/lib/axis axis/axis-ant axis/axis axis/jaxrpc axis/saaj commons-discovery commons-logging log4j-1.2.14 servlet wsdl4j
for i in axis axis-ant jaxrpc saaj;
do
mv jemboss/lib/axis/axis_$i.jar jemboss/lib/axis/$i.jar;
done
%endif

%build

%if %{with sunjava}
export PATH=$PATH:%{_java}/bin/
%endif
autoreconf -i
%configure \
  --disable-static \
  --with-x \
  --with-auth \
  --with-thread \
  --includedir=%{_includedir}/EMBOSS \
  --enable-systemlibs \
%ifarch ppc64 sparc64 x86_64
  --enable-64 \
%endif
%if %{with jemboss}
  --with-java=/usr/lib/jvm/java/include \
  --with-javaos=/usr/lib/jvm/java/include/linux
%endif
%if %{with sunjava}
  --with-java=%{_java}/include
  --with-javaos=%{_java}/include/linux
%endif
%{__make} %{?_smp_mflags}
%install
%if %{with sunjava}
export PATH=$PATH:%{_java}/bin/
%endif
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT
install -m 755 -d $RPM_BUILD_ROOT/%{_sysconfdir}/profile.d
cat << __EOF__ >> $RPM_BUILD_ROOT/%{_sysconfdir}/profile.d/emboss.sh
export PLPLOT_LIB=%{emhome}
export EMBOSS_ACDROOT=%{emhome}/acd
export EMBOSS_DOCROOT=%{emhome}/doc
export EMBOSS_DATABASE_DIR=%{emhome}/data
export EMBOSS_DATA=%{emhome}/data
__EOF__
cat << __EOF__ >> $RPM_BUILD_ROOT/%{_sysconfdir}/profile.d/emboss.csh
setenv PLPLOT_LIB %{emhome}
setenv EMBOSS_ACDROOT %{emhome}/acd
setenv EMBOSS_DOCROOT %{emhome}/doc
setenv EMBOSS_DATABASE_DIR %{emhome}/data
setenv EMBOSS_DATA %{emhome}/data
__EOF__
rm $RPM_BUILD_ROOT%{_libdir}/*.la
rm $RPM_BUILD_ROOT%{_datadir}/EMBOSS/test/data/dna.aln
pushd $RPM_BUILD_ROOT%{_datadir}/EMBOSS/jemboss/utils
chmod +x install-jemboss-server.sh keys.sh makeFileManagerJNLP.sh makeJar.csh \
     makeJNLP.sh
popd
mv $RPM_BUILD_ROOT%{_bindir}/chaos $RPM_BUILD_ROOT%{_bindir}/em_chaos
mv $RPM_BUILD_ROOT%{_bindir}/remap $RPM_BUILD_ROOT%{_bindir}/em_remap
mv $RPM_BUILD_ROOT%{_bindir}/wordcount $RPM_BUILD_ROOT%{_bindir}/em_wordcount
%if %{with jemboss}
desktop-file-install                                    \
--dir=${RPM_BUILD_ROOT}%{_datadir}/applications         \
%{SOURCE2}
%else
rm -rf ${RPM_BUILD_ROOT}%{_bindir}/runJemboss.csh
rm -rf ${RPM_BUILD_ROOT}%{_bindir}/jembossctl
rm -rf ${RPM_BUILD_ROOT}%{_datadir}/EMBOSS/jemboss
%endif
%ldconfig_scriptlets libs
%ldconfig_scriptlets -n libeplplot
%oreon_autofiles EMBOSS-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles EMBOSS-libs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles libeplplot usr/*/lib*.so.*
%oreon_autofiles libeplplot-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n EMBOSS-devel -f %{oreon_filedir}/EMBOSS-devel.list
%files -n EMBOSS-libs -f %{oreon_filedir}/EMBOSS-libs.list
%files -n libeplplot -f %{oreon_filedir}/libeplplot.list
%files -n libeplplot-devel -f %{oreon_filedir}/libeplplot-devel.list

%changelog

%autochangelog
