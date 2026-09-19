%global source0_hash 449cbc46556cc2cc9f9d6736904169a8df6415f6960528ee658998f96ca0e7cf

Summary:    C++ wrapper for the MySQL C API
Name:       mysql++
Version:    3.3.0
Release:    12%{?dist}
License:    LGPL-2.1-or-later
URL:        https://tangentsoft.com/mysqlpp/home

Source0:    https://tangentsoft.com/mysqlpp/releases/mysql++-%{version}.tar.gz
Source1:    mysql++.devhelp

BuildRequires: mariadb-connector-c-devel
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: sed

%description
MySQL++ is a C++ wrapper for MySQL’s C API. 

It is built around STL principles, to make dealing with the database as easy
as dealing with an STL container. MySQL++ relieves the programmer of dealing
with cumbersome C data structures, generation of repetitive SQL statements,
and manual creation of C++ data structures to mirror the database schema.

If you are building your own MySQL++-based programs, you also need 
to install the -devel package.

%package devel
Summary:   MySQL++ developer files (headers, examples, etc.)
Requires:  mysql++%{?_isa} = %{version}-%{release}
Requires:  mariadb-connector-c-devel%{?_isa}

%description devel
These are the files needed to compile MySQL++ based programs, 
plus some sample code to get you started.You probably need to
install the -manuals package.  

If you aren't building your own programs, you probably don't need 
to install this package.

%package manuals
Summary:   MySQL++ user and reference manuals
License:   LGPL-2.1-or-later AND LicenseRef-LDPL
BuildArch: noarch
Requires:  devhelp

%description manuals
This is the MySQL++ documentation.  It's a separate RPM just because
it's so large, and it doesn't change with every release.

User Manual and Reference Manual are provided both in PDF and in
HTML format. You can use devhelp to browse it.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

for file in CREDITS COPYING LICENSE; do
  touch -r $file.txt timestamp
  %{__sed} -i -e 's/\r//' $file.txt
  touch -r timestamp $file.txt 
done

%build
%configure --enable-thread-check \
           PTHREAD_CFLAGS=-pthread PTHREAD_LIBS=-lpthread

%{__make} %{?_smp_mflags}

%install
%{__make} DESTDIR=%{buildroot} install

# Copy example programs to doc directory
%{__mkdir_p} doc/examples/{ssx,test}
cp --preserve=timestamps examples/*.{cpp,h} doc/examples/
cp --preserve=timestamps config.h doc/examples/
cp --preserve=timestamps ssx/{parsev2,genv2,main}.cpp doc/examples/ssx
cp --preserve=timestamps ssx/{parsev2,genv2}.h doc/examples/ssx
cp --preserve=timestamps test/ssqls2.cpp doc/examples/test
sed -i -e s@../config.h@config.h@ doc/examples/threads.h

# Fix up simple example Makefile to allow it to build on the install
# system, as opposed to the system where the Makefile was created.
# Only build examples, not test_
%{__sed} -e 's@./examples/@@' \
  -e 's@^CPPFLAGS ?=.*$@CPPFLAGS ?= $(shell mariadb_config --cflags)@' \
  -e 's@^LDFLAGS ?=.*$@LDFLAGS ?= $(shell mariadb_config --libs_r)@' \
  -e '/^all:/s/test_[a-z,_]* //g' \
  Makefile.simple > doc/examples/Makefile

# DevHelp stuff
%{__mkdir_p} %{buildroot}%{_datadir}/devhelp/books/%{name}
cp --preserve=timestamps %{SOURCE1} %{buildroot}%{_datadir}/devhelp/books/%{name}/%{name}.devhelp
cp --recursive --preserve=timestamps --no-preserve=mode doc/html/userman %{buildroot}%{_datadir}/devhelp/books/%{name}/userman
cp --recursive --preserve=timestamps --no-preserve=mode doc/html/refman %{buildroot}%{_datadir}/devhelp/books/%{name}/refman
# --no-preserve=mode prevents copying bogus execute permissions on the HTML and
# CSS files.

# Collect the license files in one directory.
mkdir --parents %{buildroot}%{_licensedir}/%{name}
sed --expression=s:doc/userman/LICENSE.txt:LICENSE.userman.txt:g <COPYING.txt >%{buildroot}%{_licensedir}/%{name}/COPYING.txt
cp --preserve=timestamps LICENSE.txt %{buildroot}%{_licensedir}/%{name}/
cp --preserve=timestamps doc/userman/LICENSE.txt %{buildroot}%{_licensedir}/%{name}/LICENSE.userman.txt

%files
%dir %{_licensedir}/%{name}
%license %{_licensedir}/%{name}/COPYING.txt
%license %{_licensedir}/%{name}/LICENSE.txt
%doc ChangeLog.md CREDITS.txt README.md
%{_libdir}/libmysqlpp.so.*

%files devel
%doc doc/examples doc/README-devel-RPM.txt README-examples.txt
%{_includedir}/mysql++
%{_libdir}/libmysqlpp.so

%files manuals
# The licenses and the directory need to be replicated in the manuals
# subpackage as it doesn't depend on the main package.
%dir %{_licensedir}/%{name}
%license %{_licensedir}/%{name}/COPYING.txt
%license %{_licensedir}/%{name}/LICENSE.txt
%license %{_licensedir}/%{name}/LICENSE.userman.txt
%doc doc/pdf/* doc/README-manuals-RPM.txt
%{_datadir}/devhelp/books/%{name}

%changelog
%autochangelog
