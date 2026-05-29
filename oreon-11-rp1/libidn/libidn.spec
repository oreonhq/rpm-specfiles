%global source0_hash none

# Build with Emacs support
%bcond_without libidn_enables_emacs

%ifarch %{java_arches}
# Build with Java support
%bcond_without libidn_enables_java
%endif

Summary: Internationalized Domain Name support library
Name: libidn
Version: 1.43
Release: 4%{?dist}
URL: http://www.gnu.org/software/libidn/
License: (LGPL-3.0-or-later OR GPL-2.0-or-later) AND GPL-3.0-or-later AND GFDL-1.3-or-later
Source0:        https://ftp.gnu.org/gnu/libidn/libidn-%{version}.tar.gz
# Allow disabling Emacs support
Patch0: libidn-emacsopt.patch

BuildRequires: autoconf autoconf-archive
BuildRequires: automake
BuildRequires: libtool
BuildRequires: texinfo
BuildRequires: gcc
BuildRequires: gettext gettext-devel
BuildRequires: gtk-doc
%if %{with libidn_enables_emacs}
BuildRequires: emacs
%endif
BuildRequires: pkgconfig
BuildRequires: help2man
# gnulib is a copylib, bundling is allowed
Provides: bundled(gnulib)
%if %{with libidn_enables_emacs}
# emacs-libidn merged with main package in 1.30-4
Obsoletes: emacs-libidn < 1.30-4
Provides: emacs-libidn < 1.30-4
Requires: emacs-filesystem >= %{_emacs_version}
%endif
%if %{without libidn_enables_java}
# Remove old java packages on arches removed from %%java_arches
Obsoletes: libidn-java < %{version}-%{release}
Obsoletes: libidn-javadoc < %{version}-%{release}
%endif

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
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
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

# remove RPATH hardcoding
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

# without RPATH this needs to be set for idn executed by help2man
export LD_LIBRARY_PATH=$(pwd)/lib/.libs

%make_build

%check
# without RPATH this needs to be set to test the compiled library
export LD_LIBRARY_PATH=$(pwd)/lib/.libs
%make_build -C tests check VALGRIND=env

%install
%make_install pkgconfigdir=%{_libdir}/pkgconfig \
%if %{with libidn_enables_java}
    libidn_jardir=%{_javadir} \
%endif
    ;

# provide more examples
%make_build -C examples distclean

# clean up docs
find doc -name "Makefile*" | xargs rm
rm -rf $RPM_BUILD_ROOT%{_datadir}/info/dir

# Make multilib safe:
sed -i '/gnu compiler/d' $RPM_BUILD_ROOT%{_includedir}/idn-int.h

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la \
      $RPM_BUILD_ROOT%{_datadir}/info/*.png

%if %{with libidn_enables_emacs}
%{_emacs_bytecompile} $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{name}/*.el
%endif

%if %{with libidn_enables_java}
# regenerate java documentation
rm -rf doc/java/*
%javadoc -d doc/java $(find java/src/main/java -name "*.java")
# generate maven depmap
rm -rf $RPM_BUILD_ROOT%{_javadir}/libidn*.jar
%mvn_artifact java/pom.xml java/libidn-%{version}.jar
%mvn_file org.gnu.inet:libidn libidn
%mvn_install -J doc/java
%endif

%find_lang %{name}

%ldconfig_scriptlets

%files -f %{name}.lang
%{!?_licensedir:%global license %%doc}
%license COPYING*
%doc AUTHORS NEWS FAQ README THANKS
%{_bindir}/idn
%{_mandir}/man1/idn.1*
%{_libdir}/libidn.so.12*
%{_infodir}/%{name}.info*
%if %{with libidn_enables_emacs}
%{_emacs_sitelispdir}/%{name}
%endif

%files devel
%doc examples
%{_libdir}/libidn.so
%{_includedir}/*.h
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man3/*

%if %{with libidn_enables_java}
%files java -f .mfiles
%license COPYING* java/LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%license COPYING* java/LICENSE-2.0.txt
%endif

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.43-4
- Import
