%global source0_hash 13a4699047916b018c16b10b79cd085381534f49d0026ae773d6b991c9e0f02c

%global includetests 1
# 0=no, 1=yes
%global cryptlibdir %{_libdir}/%{name}

Name:       cryptlib
Version:    3.4.9
Release:    2%{?dist}
Summary:    Security library and toolkit for encryption and authentication services    

License:    Sleepycat and OpenSSL and BSD-3-Clause   
URL:        https://github.com/cryptlib/cryptlib      
Source0:    https://senderek.ie/fedora/cl349_fedora.zip     
Source1:    https://senderek.ie/fedora/cl349_fedora.zip.sig
# for security reasons a public signing key should always be stored in distgit
# and never be used with a URL to make impersonation attacks harder
# (verified: https://senderek.ie/keys/codesigningkey)
Source2:    gpgkey-3274CB29956498038A9C874BFBF6E2C28E9C98DD.asc
Source3:    https://senderek.ie/fedora/README-details
Source4:    https://senderek.ie/fedora/cryptlib-tests.tar.gz
Source5:    https://senderek.ie/fedora/cryptlib-perlfiles.tar.gz
Source6:    https://senderek.ie/fedora/cryptlib-tools.tar.gz

# soname is now libcl.so.3.4
Patch0:     m64patch

ExclusiveArch: x86_64 aarch64 ppc64le riscv64

BuildRequires: gcc 
BuildRequires: libbsd-devel   
BuildRequires: gnupg2
BuildRequires: coreutils
BuildRequires: python3-devel
BuildRequires: java-25-devel
BuildRequires: perl-interpreter
BuildRequires: perl-devel
BuildRequires: perl-generators
BuildRequires: perl-Data-Dumper
BuildRequires: perl-ExtUtils-MakeMaker
BuildRequires: make

%description
Cryptlib is a powerful security toolkit that allows even inexperienced crypto
programmers to easily add encryption and authentication services to their
software. The high-level interface provides anyone with the ability to add
strong security capabilities to an application in as little as half an hour,
without needing to know any of the low-level details that make the encryption
or authentication work.  Because of this, cryptlib dramatically reduces the
cost involved in adding security to new or existing applications.

At the highest level, cryptlib provides implementations of complete security
services such as S/MIME and PGP/OpenPGP secure enveloping, SSL/TLS and
SSH secure sessions, CA services such as CMP, SCEP, RTCS, and OCSP, and other
security operations such as secure time-stamping. Since cryptlib uses
industry-standard X.509, S/MIME, PGP/OpenPGP, and SSH/SSL/TLS data formats,
the resulting encrypted or signed data can be easily transported to other
systems and processed there, and cryptlib itself runs on virtually any
operating system - cryptlib doesn't tie you to a single system.
This allows email, files and EDI transactions to be authenticated with
digital signatures and encrypted in an industry-standard format.

%package devel
Summary:  Cryptlib application development files 
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and code for application development in C (and C++)

%package test
Summary:  Cryptlib test program
Requires: %{name}%{?_isa} = %{version}-%{release}

%description test
Cryptlib test programs for C, Java, Perl and Python3

%package java
Summary:  Cryptlib bindings for Java
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: java-25-headless

%description java
Cryptlib module for application development in Java

%package javadoc
Summary:  Cryptlib Java documentation
Buildarch : noarch

%description javadoc
Cryptlib Javadoc information

%package python3
Summary:  Cryptlib bindings for python3
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: python3 >= 3.5  

%description python3
Cryptlib module for application development in Python3

%package perl
Summary:  Cryptlib bindings for perl
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: man

%description perl
Cryptlib module for application development in Perl

%package tools
Summary:  Collection of stand-alone programs that use Cryptlib
Requires: python3 >= 3.5
Requires: man
Requires: %{name}%-python3
Requires: dumpasn1

%description tools
Collection of stand-alone programs that use Cryptlib

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# source code signature check with GnuPG
KEYRING=$(echo %{SOURCE2})
KEYRING=${KEYRING%%.asc}.gpg
mkdir -p .gnupg
gpg2 --homedir .gnupg --no-default-keyring --quiet --yes --output $KEYRING --dearmor  %{SOURCE2}
gpg2 --homedir .gnupg --no-default-keyring --keyring $KEYRING --verify %{SOURCE1} %{SOURCE0}

rm -rf %{name}-%{version}
mkdir %{name}-%{version}
cd %{name}-%{version}
/usr/bin/unzip %{SOURCE0}

# patches and updates
%patch 0 -p1

# enable ADDFLAGS
sed -i '98s/-I./-I. \$(ADDFLAGS)/' makefile
# enable JAVA in config
sed -i 's/\/\* #define USE_JAVA \*\// #define USE_JAVA /' misc/config.h

# remove pre-build jar file
rm %{_builddir}/%{name}-%{version}/bindings/cryptlib.jar
# adapt perl files in bindings
cd %{_builddir}/%{name}-%{version}/bindings
/usr/bin/tar xpzf %{SOURCE5}

%generate_buildrequires
cd %{name}-%{version}/bindings
%pyproject_buildrequires 

%build
cd %{name}-%{version}
chmod +x tools/mkhdr.sh

tools/mkhdr.sh

# rename cryptlib symbols that may collide with openssl symbols
chmod +x tools/rename.sh
tools/rename.sh

# build java bindings
cp /etc/alternatives/java_sdk/include/jni.h .
cp /etc/alternatives/java_sdk/include/linux/jni_md.h .

# remove duplications in %{optflags}
# -D_GLIBCXX_ASSERTIONS and -D_FORTIFY_SOURCE=3 must be removed from %{optflags},
# because both are enabled later with -fhardened set by tools/ccopts.sh.
# As -Wall is enabled, -fhardened will trigger unnecessary warnings, because
# -fhardened cannot enable these flags if they are already set.

FLAGS="%{optflags}"
FLAGS=${FLAGS//"-Wp,-D_GLIBCXX_ASSERTIONS"/}
FLAGS=${FLAGS//"-Wp,-U_FORTIFY_SOURCE,-D_FORTIFY_SOURCE=3"/}

make clean
make shared  ADDFLAGS="${FLAGS}"
ln -s libcl.so.3.4.9 libcl.so
ln -s libcl.so libcl.so.3.4
make stestlib  ADDFLAGS="%{optflags}"

# build python modules
cd bindings
%pyproject_wheel

# build javadoc
mkdir javadoc
cd javadoc
jar -xf ../cryptlib.jar
javadoc cryptlib

%install
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_datadir}/licenses/%{name}
mkdir -p %{buildroot}%{_docdir}/%{name}
cp %{_builddir}/%{name}-%{version}/libcl.so.3.4.9 %{buildroot}%{_libdir}
cd %{buildroot}%{_libdir}
ln -s libcl.so.3.4.9 libcl.so.3.4
ln -s libcl.so.3.4 libcl.so

# install header files
mkdir -p %{buildroot}/%{_includedir}/%{name}
cp %{_builddir}/%{name}-%{version}/crypt.h %{buildroot}%{_includedir}/%{name}
cp %{_builddir}/%{name}-%{version}/cryptkrn.h %{buildroot}%{_includedir}/%{name}
cp %{_builddir}/%{name}-%{version}/cryptlib.h %{buildroot}%{_includedir}/%{name}

# add Java bindings
mkdir -p %{buildroot}/%{cryptlibdir}/java
mkdir -p %{buildroot}/usr/lib/java
cp %{_builddir}/%{name}-%{version}/bindings/cryptlib.jar %{buildroot}/usr/lib/java

# install docs
cp %{_builddir}/%{name}-%{version}/COPYING %{buildroot}%{_datadir}/licenses/%{name}
cp %{_builddir}/%{name}-%{version}/README %{buildroot}%{_docdir}/%{name}/README
echo "No tests performed." > %{_builddir}/%{name}-%{version}/stestlib.log
cp %{_builddir}/%{name}-%{version}/stestlib.log %{buildroot}%{_docdir}/%{name}/stestlib.log
cp %{SOURCE3} %{buildroot}%{_docdir}/%{name}
cp %{_builddir}/%{name}-%{version}/README.md %{buildroot}%{cryptlibdir}
cp %{_builddir}/%{name}-%{version}/architecture.md %{buildroot}%{cryptlibdir}
cp %{_builddir}/%{name}-%{version}/SECURITY.md %{buildroot}%{cryptlibdir}

# install javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}
rm -rf %{_builddir}/%{name}-%{version}/bindings/javadoc/META-INF
cp -r %{_builddir}/%{name}-%{version}/bindings/javadoc/* %{buildroot}%{_javadocdir}/%{name}

# install python3 module
mkdir -p %{buildroot}%{python3_sitelib}
cp %{_builddir}/%{name}-%{version}/bindings/build/lib.linux-*/cryptlib_py%{python3_ext_suffix} %{buildroot}%{python3_sitelib}/cryptlib_py.so

# install Perl module
mkdir -p %{buildroot}/usr/local/lib64
mkdir -p %{buildroot}%{_libdir}/perl5
mkdir -p %{buildroot}%{_mandir}/man3
cd %{_builddir}/%{name}-%{version}/bindings
mkdir -p %{_builddir}/include
cp ../cryptlib.h %{_builddir}/include
cp ../tools/GenPerl.pl .
export PERL_CRYPT_LIB_HEADER=%{_builddir}/include/cryptlib.h
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor
sed -i '/LDLOADLIBS = /s/thread/thread -L.. -lcl/' Makefile
make
make pure_install DESTDIR=%{buildroot}
# clean the install
find %{buildroot} -type f -name .packlist -delete
find %{buildroot} -type f -name 'PerlCryptLib.so' -exec chmod 0755 {} \;

# install test programs
cp %{_builddir}/%{name}-%{version}/stestlib %{buildroot}%{cryptlibdir}
cp -r %{_builddir}/%{name}-%{version}/test %{buildroot}%{cryptlibdir}/test
# remove all c code from the test directory
rm -rf $(find %{buildroot}%{cryptlibdir}/test -name "*.c")

# extract test files
cd %{buildroot}%{cryptlibdir}
tar xpzf %{SOURCE4} 

# install cryptlib tools 
mkdir -p %{buildroot}%{cryptlibdir}/tools
cd %{buildroot}%{cryptlibdir}/tools
tar xpzf %{SOURCE6} 
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_bindir}
cp /%{buildroot}%{cryptlibdir}/tools/clsha1 %{buildroot}%{_bindir}
cp /%{buildroot}%{cryptlibdir}/tools/clsha2 %{buildroot}%{_bindir}
cp /%{buildroot}%{cryptlibdir}/tools/claes %{buildroot}%{_bindir}
cp /%{buildroot}%{cryptlibdir}/tools/clkeys %{buildroot}%{_bindir}
cp /%{buildroot}%{cryptlibdir}/tools/clsmime %{buildroot}%{_bindir}
cp /%{buildroot}%{cryptlibdir}/tools/man/clsha1.1 %{buildroot}%{_mandir}/man1
cp /%{buildroot}%{cryptlibdir}/tools/man/clsha2.1 %{buildroot}%{_mandir}/man1
cp /%{buildroot}%{cryptlibdir}/tools/man/claes.1  %{buildroot}%{_mandir}/man1
cp /%{buildroot}%{cryptlibdir}/tools/man/clkeys.1 %{buildroot}%{_mandir}/man1
cp /%{buildroot}%{cryptlibdir}/tools/man/clsmime.1 %{buildroot}%{_mandir}/man1

%check
# checks are performed after install
# in KOJI tests must be disabled as there is no networking
%if %{includetests}
     cd %{_builddir}/%{name}-%{version}
     export LD_LIBRARY_PATH=.
     echo "Running one basic test on the cryptlib library."
     cp %{buildroot}%{cryptlibdir}/c/sha2-test.c .
     sed -i '41s/<cryptlib\/cryptlib.h>/\".\/cryptlib.h\"/' sha2-test.c
     gcc  -o sha2-test sha2-test.c -L. libcl.so.3.4.9
     ./sha2-test
%endif

%ldconfig_scriptlets

%files
%{_libdir}/libcl.so.3.4.9
%{_libdir}/libcl.so.3.4
%{_libdir}/libcl.so

%license   %{_datadir}/licenses/%{name}/COPYING
%doc       %{_docdir}/%{name}/README
%doc       %{_docdir}/%{name}/stestlib.log
%doc       %{_docdir}/%{name}/README-details

%files devel
%{_libdir}/libcl.so
%{_includedir}/%{name}/crypt.h
%{_includedir}/%{name}/cryptkrn.h
%{_includedir}/%{name}/cryptlib.h

%files java
/usr/lib/java/cryptlib.jar

%files javadoc
%{_javadocdir}/%{name}

%files python3
%{python3_sitelib}/cryptlib_py.so

%files perl
%{_libdir}/perl5
%{_mandir}/man3/PerlCryptLib.3pm.gz

%files test
%{cryptlibdir}

%files tools
%{_bindir}/clsha1
%{_bindir}/clsha2
%{_bindir}/claes
%{_bindir}/clkeys
%{_bindir}/clsmime
%{_mandir}/man1/clsha2.1.gz
%{_mandir}/man1/clsha1.1.gz
%{_mandir}/man1/claes.1.gz
%{_mandir}/man1/clkeys.1.gz
%{_mandir}/man1/clsmime.1.gz

%changelog
%autochangelog
