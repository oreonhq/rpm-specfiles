%global source0_hash ff74209a8a11c918e173f6854b52d6fbd5291d2ebf66d4284408a9b390721d0a
%global _lto_cflags %{nil}
%global _package_note_file "%{_builddir}/%{realname}-%{version}-%{commit}/genesis/.package_note-%{name}-%{version}-%{release}.%{_arch}.ld"
%global commit 7b0a66b71ba98d5b7802c32ed856b75b8334fb05
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global realname genesis
%global instdir %{_datadir}/%{name}
Name:       %{realname}-simulator
Summary:        A general purpose simulation platform
Version:    2.4
Release:        1%{?dist}
Url:        http://www.genesis-sim.org/GENESIS/
Source0:        https://github.com/%{realname}-sim/%{realname}-%{version}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Patch0:     0001-use-CFLAGS_IN-instead-of-COPT.patch
Patch1:     0002-feat-pass-RNG_CFLAGS.patch
License:    GPL-2.0-or-later AND LGPL-2.0-or-later AND MIT AND LicenseRef-Fedora-Public-Domain
# oreon:deps
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  flex-static
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  libX11-devel
BuildRequires:  libXt-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  netcdf-devel
# /oreon:deps
%description
GENESIS (short for GEneral NEural SImulation System) is a general
purpose simulation platform that was developed to support the
simulation of neural systems ranging from subcellular components and
biochemical reactions to complex models of single neurons, simulations
of large networks, and systems-level models. As such, GENESIS, and its
version for parallel and networked computers (PGENESIS) was the first
broad scale modeling system in computational biology to encourage
modelers to develop and share model features and components. Most
current GENESIS applications involve realistic simulations of
biological neural systems. Although the software can also model more
abstract networks, other simulators are more suitable for
backpropagation and similar connectionist modeling.

Please install the %{name}-doc sub package for documentation.

%package devel
Summary: Static library and tools for building genesis extensions
%description devel
%{summary}.

%package doc
BuildArch: noarch
Summary: Documentation for %{name}
%description doc
%{summary}.

%ifarch x86_64
%global extraflags -DLONGWORDS
%endif

%prep

%autosetup -n %{realname}-%{version}-%{commit}/genesis -S git -p2

# Correct spurious perms
find Doc -type f -exec chmod -x '{}' \;
# Correct shebang for perl scripts
find Scripts/purkinje/perl -exec sed -i 's|#!/usr/local/bin/perl -w|#!/usr/bin/perl -w|' '{}' \;

# Correct executable perms
find Scripts -type f -exec chmod -x '{}' \;
find Tutorials -type f -exec chmod -x '{}' \;

# file-not-utf8
pushd Scripts/burster
# Convert to utf-8
for file in README README.txt; do
    iconv -f ISO-8859-1 -t UTF-8 -o $file.new $file && \
    touch -r $file $file.new && \
    mv $file.new $file
done
popd

# Remove the binaries they ship
rm -rf ../%{realname}-binaries

# Remove unrelated programs
rm -rf ./src/contrib

# Remove bundled netcdf
rm -rf ./src/diskio/interface/netcdf/netcdf-3.4
# Do not use bundled netcdflib
sed -i 's/netcdflib.o: netcdflib/netcdflib.o:/' ./src/diskio/interface/netcdf/Makefile

# Set up Makefile for Linux installation
# Using configure doesn't quite work for us because the build scripts use ld
# instead of gcc, and the Fedora LD flags are set to be used with gcc. Setting
# them for ld breaks the configure script.
%global build_type_safety_c 0
cp src/Makefile.dist src/Makefile
cat >>src/Makefile <<EOF
MACHINE=Linux
OS=BSD
XLIB=%{_libdir}
CC=gcc -std=gnu89
CPP=cpp -P
RNG_CFLAGS=%{optflags} %{?extraflags}
CFLAGS=%{optflags} %{?extraflags}
CXXFLAGS=%{optflags} %{?extraflags}
LD=gcc
RANLIB=ranlib
AR=ar
YACC=bison -y
LEX=flex -l
LEXLIB=-lfl
LIBS=\$(LEXLIB) -lm -lnetcdf
TERMCAP=-lncurses
TERMOPT=-DTERMIO -DDONT_USE_SIGIO
NETCDFOBJ = \
        \$(DISKIODIR)/interface/\$(NETCDFSUBDIR)/netcdflib.o
EOF

%build

make -C src genesis
%install
make -C src install INSTALLDIR=%{buildroot}%{_libdir}/genesis
rm -r %{buildroot}%{_libdir}/genesis/{src,man}
rm -v %{buildroot}%{_libdir}/genesis/.*simrc
chmod -x %{buildroot}%{_libdir}/genesis/startup/*
mkdir -p %{buildroot}%{_bindir}
mv %{buildroot}%{_libdir}/genesis/genesis %{buildroot}%{_bindir}/
mkdir -p %{buildroot}%{_includedir}
mv %{buildroot}%{_libdir}/genesis/include %{buildroot}%{_includedir}/genesis
mv %{buildroot}%{_libdir}/genesis/bin/convert %{buildroot}%{_bindir}/genesis-convert
install -D man/man1/convert.1 %{buildroot}%{_mandir}/man1/genesis-convert.1
cp src/libsh %{buildroot}%{_libdir}/genesis/lib
find %{buildroot}%{_libdir}/genesis/startup/ -name '*simrc' -exec \
    sed -i -e 's|%{buildroot}||g' -e 's|GENESIS_HELP .*|GENESIS_HELP  %{_docdir}/%{name}-doc/Doc/|' {} \;
chmod -x %{buildroot}%{_mandir}/man1/%{realname}-convert.1*
rm -rf %{buildroot}%{_libdir}/%{realname}/Doc
rm -rf %{buildroot}%{_libdir}/%{realname}/Hyperdoc
rm -rf %{buildroot}%{_libdir}/%{realname}/Tutorials
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n genesis-simulator-devel -f %{oreon_filedir}/genesis-simulator-devel.list
%files -n genesis-simulator-doc -f %{oreon_filedir}/genesis-simulator-doc.list

%changelog

%autochangelog
