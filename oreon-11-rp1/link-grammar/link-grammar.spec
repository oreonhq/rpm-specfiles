%global source0_hash d9572ab811aedcbdb102d5d97b9f2c1fc4f491616a507de8d5c6d1388d5adda5

%ifarch %{java_arches}
%global JAVA 1
%else
%global JAVA 0
%endif

Summary: A full-service natural language dependency parser
Name: link-grammar
Version: 5.12.7
Release: 3%{?dist}
License: LGPL-2.1-or-later
Source: https://www.gnucash.org/link-grammar/downloads/%{version}/link-grammar-%{version}.tar.gz
URL: https://opencog.github.io/link-grammar-website/
BuildRequires: hunspell-devel, libedit-devel, perl-devel, python3-devel, python3-setuptools
%if %{JAVA}
BuildRequires: java-devel, jpackage-utils, ant-openjdk25, javapackages-local-openjdk25
%endif
BuildRequires: perl-generators, swig, minisat2-devel, gcc-c++
BuildRequires: make, flex, pcre2-devel

%description
A full-service natural language dependency parser for
English and Russian, with prototypes for other assorted languages.

%package devel
Summary: Support files necessary to compile applications with liblink-grammar
Requires: link-grammar = %{version}-%{release}

%description devel
Libraries, headers, and support files needed for using liblink-grammar.

%if %{JAVA}
%package java
Summary: Java libraries for liblink-grammar
Requires: java-headless >= 1:1.6.0
Requires: jpackage-utils
Requires: link-grammar = %{version}-%{release}

%description java
Java libraries for liblink-grammar

%package java-devel
Summary: Support files necessary to compile Java applications with liblink-grammar
Requires: link-grammar-java = %{version}-%{release}
Requires: link-grammar-devel = %{version}-%{release}

%description java-devel
Libraries for developing Java components using liblink-grammar.
%endif

%package perl
Summary: Perl libraries for liblink-grammar
Requires: perl-interpreter
Requires: link-grammar = %{version}-%{release}

%description perl
Perl libraries for liblink-grammar

%package python3
Summary: Python 3 libraries for liblink-grammar
Requires: link-grammar = %{version}-%{release}

%description python3
Python 3 libraries for liblink-grammar

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%if %{JAVA}
# help configure find jni.h
export JAVA_HOME=%{java_home}
%endif
PYTHON_NOVERSIONCHECK=1 PYTHON=%{__python3} PYTHON_VERSION=%{python3_version} %configure --disable-static --enable-pthreads --disable-aspell --enable-perl-bindings
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
#make
# currently the build system can not handle smp_flags properly
make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install
%if %{JAVA}
mv $RPM_BUILD_ROOT/%{_datadir}/java/linkgrammar-%{version}.jar $RPM_BUILD_ROOT/%{_datadir}/java/linkgrammar.jar
%endif
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/perl5/
mv $RPM_BUILD_ROOT%{_prefix}/local/lib*/perl5/* $RPM_BUILD_ROOT/%{_libdir}/perl5/
find $RPM_BUILD_ROOT/%{_libdir}/ -name '*.la' | xargs rm -f

%files
%license LICENSE
%doc AUTHORS
%{_bindir}/*
%{_libdir}/liblink-grammar.so.5*
%{_datadir}/link-grammar
%{_mandir}/man1/link-parser.1*
%{_mandir}/man1/link-generator.1*

%files devel
%{_libdir}/liblink-grammar.so
%{_libdir}/pkgconfig/link-grammar.pc
%{_includedir}/link-grammar

%if %{JAVA}
%files java
%{_libdir}/liblink-grammar-java.so.5*
%{_javadir}/linkgrammar.jar

%files java-devel
%{_libdir}/liblink-grammar-java.so
%endif

%files perl
%{_libdir}/perl5/*

%files python3
%{python3_sitelib}/linkgrammar*
%{python3_sitearch}/linkgrammar*

%ldconfig_scriptlets

%if %{JAVA}
%ldconfig_scriptlets java
%endif

%changelog
%autochangelog
