%global source0_hash 8c9a50cd6b100154c901bd190b3acd2fb8353f33622c4a2ce8fa392a7f09e019

Epoch:          1
Name:           kawa
Version:        3.1.1
Release:        25%{?dist}
Summary:        Scheme programming language
License:        MIT
URL:            https://www.gnu.org/software/kawa/
Source0:        https://ftp.gnu.org/gnu/kawa/kawa-%{version}.tar.gz
# Exclude i686 due to dropping i686 JDKS: https://fedoraproject.org/wiki/Changes/Drop_i686_JDKs
ExcludeArch:    i686
BuildRequires:  ant-openjdk25 
BuildRequires:  antlr
BuildRequires:  groff
BuildRequires:  java-25-devel
BuildRequires:  libtool
BuildRequires:  ncurses-devel
BuildRequires:  readline-devel
BuildRequires:  jakarta-servlet
BuildRequires:  texinfo
BuildRequires:  util-linux-ng
BuildRequires:  make
Requires:       jakarta-servlet
Requires:       java-25-headless

#Test doesn't pass against Jboss servlet 3.0 till Kawa support Tomcat servlet 4.0
#See https://gitlab.com/kashell/Kawa/issues/41
Patch0:         kawa-3.1.1-disable-servelet-tests.patch
Patch1:         kawa-3.1.1-remove-unfound-javadoc.patch
# Port https://gitlab.com/kashell/Kawa/-/commit/53b9750e1a4707902ecb0743284d667cba944031
# Removed ChangLog modification
Patch2:         kawa-3.1.1-CharSequence-isEmpty-was-added-in-JDK15-so-override.patch
# Port https://gitlab.com/kashell/Kawa/-/commit/42f88a1dcba7264587fc177a2721a012d035ef66
# Removed ChangLog modification
Patch3:         kawa-3.1.1-IString.java-isEmpty-New-method-added-for-Java-15.patch
# Port https://gitlab.com/kashell/Kawa/-/commit/2b9674927ba82847cc830eb05466086d3fdcebd2
# Removed ChangLog modification
Patch4:         kawa-3.1.1-standard-make.java-Explicitly-import-kawa.lang.Recor.patch
# Port https://gitlab.com/kashell/Kawa/-/commit/dd940c01f4ee9dd3263bca844f035bc4a31c76c4
# Removed ChangLog modification
Patch5:         kawa-3.1.1-gnu-.java-kawa-.java-Fix-Java17-depreciation-warning.patch

%description
Kawa is an implementation of the Scheme programming language.  It is
implemented in Java, and compiles Scheme into Java byte-codes.  It
also includes an XQuery implementation, accessible via the qexo
script.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%configure --enable-kawa-frontend \
           --with-servlet=$(build-classpath jboss-servlet-3.0-api) \
           --with-libtool
export CLASSPATH=$(build-classpath jboss-servlet-3.0-api antlr)
make

# Override the Makefile for generating kawa.1, since it should be
# unformatted man page source.
cp -p doc/kawa.man doc/kawa.1
cp -p doc/qexo.man doc/qexo.1

%install
%make_install
rm -frv %{buildroot}%{_infodir}/dir
mkdir -p %{buildroot}%{_javadir}
mv %{buildroot}%{_datadir}/kawa/lib/kawa.jar %{buildroot}%{_javadir}/kawa.jar
ln -s %{_javadir}/kawa.jar %{buildroot}%{_datadir}/kawa/lib/kawa.jar
cp -p bin/cgi-servlet %{buildroot}%{_bindir}/cgi-servlet
rm -rf %{buildroot}%{_datadir}/kawa/bin

%check
# Current test scripts don't compatible with JAVA11
#make check

%files
%doc AUTHORS ChangeLog NEWS TODO
%license COPYING
%{_bindir}/cgi-servlet
%{_bindir}/kawa
%{_bindir}/qexo
%{_datadir}/java/kawa*.jar
%{_mandir}/man1/*
%{_infodir}/kawa*
#Just links
%{_datadir}/kawa/lib/*

%changelog
%autochangelog
