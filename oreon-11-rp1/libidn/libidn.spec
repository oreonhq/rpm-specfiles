%global source0_hash 499608bab3a65650a0ea52888c13a8deebe3f71408e319acd9ec52e02eb13959
%bcond_without libidn_enables_emacs
%ifarch %{java_arches}
%bcond_without libidn_enables_java
%endif
Summary:        Internationalized Domain Name support library
Name: libidn
Version: 1.44
Release:        1%{?dist}
URL: http://www.gnu.org/software/libidn/
License: (LGPL-3.0-or-later OR GPL-2.0-or-later) AND GPL-3.0-or-later AND GFDL-1.3-or-later
Source0:        https://ftp.gnu.org/gnu/libidn/libidn-%{version}.tar.gz
Patch0: libidn-emacsopt.patch
%if %{with libidn_enables_emacs}
%endif
Provides: bundled(gnulib)
%if %{with libidn_enables_emacs}
Obsoletes: emacs-libidn < 1.30-4
Provides: emacs-libidn < 1.30-4
Requires: emacs-filesystem >= %{_emacs_version}
%endif
%if %{without libidn_enables_java}
Obsoletes: libidn-java < %{version}-%{release}
Obsoletes: libidn-javadoc < %{version}-%{release}
%endif
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  emacs
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gettext-devel
BuildRequires:  gtk-doc
BuildRequires:  help2man
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  texinfo
# /oreon:deps
%description
GNU Libidn is an implementation of the Stringprep, Punycode and
IDNA specifications defined by the IETF Internationalized Domain
Names (IDN) working group, used for internationalized domain
names.

%package devel
Summary: Development files for the libidn library
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconfig
%description devel
This package includes header files and libraries necessary for
developing programs which use the GNU libidn library.

%if %{with libidn_enables_java}
%package java
Summary:       Java port of the GNU Libidn library
BuildRequires: java-devel
BuildRequires: javapackages-local-openjdk25
BuildRequires: mvn(com.google.guava:guava)
BuildRequires: mvn(junit:junit)
BuildRequires: make
BuildArch:     noarch
%description java
GNU Libidn is a fully documented implementation of the Stringprep,
Punycode and IDNA specifications. Libidn's purpose is to encode
and decode internationalized domain names.

This package contains the native Java port of the library.

%package javadoc
Summary:       Javadoc for %{name}-java
BuildArch:     noarch
%description javadoc
This package contains javadoc for %{name}-java.
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q
%patch -P0 -p1 -b .emacsopt
autoreconf -vif
# Prevent from regenerating sources by gengetopt because it's broken.
touch src/idn_cmd.c src/idn_cmd.h

# Cleanup
find . -name '*.jar' -print -delete
find . -name '*.class' -print -delete

%if %{with libidn_enables_java}
# Not available test dep
%pom_remove_dep com.google.caliper:caliper java/pom.xml.in

# Unused dependency
%pom_remove_dep com.google.code.findbugs:annotations java/pom.xml.in
%endif

%build

%configure --disable-csharp --disable-static \
%if %{with libidn_enables_emacs}
    --enable-emacs \
    --with-lispdir=%{_emacs_sitelispdir}/%{name} \
%else
    --disable-emacs \
%endif
%if %{with libidn_enables_java}
    --enable-java
%else
    --disable-java
%endif
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
export LD_LIBRARY_PATH=$(pwd)/lib/.libs
%make_build
%check

export LD_LIBRARY_PATH=$(pwd)/lib/.libs
%make_build -C tests check VALGRIND=env
%install
%make_install pkgconfigdir=%{_libdir}/pkgconfig \
%if %{with libidn_enables_java}
    libidn_jardir=%{_javadir} \
%endif
    ;
%make_build -C examples distclean
find doc -name "Makefile*" | xargs rm
rm -rf $RPM_BUILD_ROOT%{_datadir}/info/dir
sed -i '/gnu compiler/d' $RPM_BUILD_ROOT%{_includedir}/idn-int.h
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la \
      $RPM_BUILD_ROOT%{_datadir}/info/*.png
%if %{with libidn_enables_emacs}
%{_emacs_bytecompile} $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{name}/*.el
%endif
%if %{with libidn_enables_java}
rm -rf doc/java/*
%javadoc -d doc/java $(find java/src/main/java -name "*.java")
rm -rf $RPM_BUILD_ROOT%{_javadir}/libidn*.jar
%mvn_artifact java/pom.xml java/libidn-%{version}.jar
%mvn_file org.gnu.inet:libidn libidn
%mvn_install -J doc/java
%endif
%find_lang %{name}
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libidn-devel -f %{oreon_filedir}/libidn-devel.list

%changelog

%autochangelog
