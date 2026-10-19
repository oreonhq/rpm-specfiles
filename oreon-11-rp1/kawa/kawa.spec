%global source0_hash 8c9a50cd6b100154c901bd190b3acd2fb8353f33622c4a2ce8fa392a7f09e019
Epoch:          1
Name:           kawa
Version:        3.1.1
Release:        1%{?dist}
Summary:        Scheme programming language
License:        MIT
URL:            https://www.gnu.org/software/kawa/
Source0:        https://ftp.gnu.org/gnu/kawa/kawa-%{version}.tar.gz
ExcludeArch:    i686
Requires:       jakarta-servlet
Requires:       java-25-headless
Patch0:         kawa-3.1.1-disable-servelet-tests.patch
Patch1:         kawa-3.1.1-remove-unfound-javadoc.patch
Patch2:         kawa-3.1.1-CharSequence-isEmpty-was-added-in-JDK15-so-override.patch
Patch3:         kawa-3.1.1-IString.java-isEmpty-New-method-added-for-Java-15.patch
Patch4:         kawa-3.1.1-standard-make.java-Explicitly-import-kawa.lang.Recor.patch
Patch5:         kawa-3.1.1-gnu-.java-kawa-.java-Fix-Java17-depreciation-warning.patch
# oreon:deps
BuildRequires:  ant-openjdk25
BuildRequires:  antlr
BuildRequires:  groff
BuildRequires:  jakarta-servlet
BuildRequires:  java-25-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  readline-devel
BuildRequires:  texinfo
BuildRequires:  util-linux-ng
# /oreon:deps
%description
Kawa is an implementation of the Scheme programming language.  It is
implemented in Java, and compiles Scheme into Java byte-codes.  It
also includes an XQuery implementation, accessible via the qexo
script.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure --enable-kawa-frontend \
           --with-servlet=$(build-classpath jboss-servlet-3.0-api) \
           --with-libtool
export CLASSPATH=$(build-classpath jboss-servlet-3.0-api antlr)
make
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
%oreon_autofiles main

%check

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
