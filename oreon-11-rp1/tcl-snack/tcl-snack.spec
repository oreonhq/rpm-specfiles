%global source0_hash fb0d0e9d140396140987aeb50b97fae086590c2a769cfba011354d3977cc9b2d

# We used to define this dynamically, but the Fedora buildsystem chokes on
# using this for the versioned Requires on tcl(abi), so we hardcode it.
# This sucks, but there is no other clean way around it, because tcl
# (and tclsh) aren't in the default buildroot.
%{!?tcl_version: %global tcl_version 8.6}
%{!?tcl_sitearch: %global tcl_sitearch %{_libdir}/tcl%{tcl_version}}
%global realname snack

# ugly old code
%global optflags %{optflags} -std=gnu17

Name:		tcl-%{realname}
Version:	2.2.10
Release:	68%{?dist}
Summary:	Sound toolkit
# generic/snackDecls.h, generic/snackStubInit.c and generic/snackStubLib.c 
# are under the TCL "license.terms", a copy of which can be found in the tcl package.
# SnackMpg.c just says "BSD" so we pick the most common one. :P
License:	GPL-2.0-or-later AND TCL AND BSD-3-Clause
URL:		http://www.speech.kth.se/snack/
# The upstream source has two files which implement MP3 decoding.
# ./generic/jkFormatMP3.c and ./generic/jkFormatMP3.h
# Those files are non-free so we cannot ship that code, thus, the modified tarball.
# We implement MP3 support the same way that Debian does (libsnackmpg)
# Also, mac/snack.mcp.sit.hqx is a mysterious old compressed file with no clear license.
# It is removed.
# Upstream source can be found here: http://www.speech.kth.se/snack/dist/snack2.2.10.tar.gz
Source0:	%{realname}%{version}-nomp3.tar.gz
# License confirmation email for generic/ffa.c
Source1:	LICENSE-ffa.c.txt
# Copied from debian sources
Source2:	SnackMpg.c
Patch0:		snack2.2.10-mpg123.patch
Patch1:		snack2.2.10-extracflags.patch
Patch3:		snack2.2.10-newALSA.patch
Patch4:		tcl-snack-2.2.10-CVE-2012-6303-fix.patch
Patch5:		snack2.2.10-format-security.patch
# Credit to Sergei Golovan, patches taken from Debian
Patch6:		tcl-snack-2.2.10-python3.patch
Patch7:		snack2.2.10-seektell-fix.patch
Patch8:		tcl-snack-configure-c99.patch
Patch9:		tcl-snack-sigproc2-c99.patch
# Do not use obsolete distutils
Patch10:	snack2.2.10-python3-setuptools.patch
Patch11:	snack2.2.10-const-fix.patch
BuildRequires:	make
BuildRequires:	gcc-c++
# does not support tcl9, probably never will
BuildRequires:	tcl8-devel, tk8-devel, libogg-devel, libvorbis-devel
BuildRequires:	libXft-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	python3-devel, python3-setuptools
BuildRequires:	mpg123-devel
Requires:	tcl(abi) = %{tcl_version}
Provides:	%{realname} = %{version}-%{release}

%description
The Snack Sound Toolkit is designed to be used with a scripting language such 
as Tcl/Tk or Python. Using Snack you can create powerful multi-platform audio 
applications with just a few lines of code. Snack has commands for basic sound 
handling, such as playback, recording, file and socket I/O. Snack also provides 
primitives for sound visualization, e.g. waveforms and spectrograms. It was 
developed mainly to handle digital recordings of speech, but is just as useful 
for general audio. Snack has also successfully been applied to other 
one-dimensional signals. The combination of Snack and a scripting language 
makes it possible to create sound tools and applications with a minimum of 
effort. This is due to the rapid development nature of scripting languages. As 
a bonus you get an application that is cross-platform from start. It is also 
easy to integrate Snack based applications with existing sound analysis 
software.

%package devel
Summary:	Development files for Snack Sound Toolkit
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains development files for the Snack Sound Toolkit.

%package -n python3-%{realname}
%{?python_provide:%python_provide python3-%{realname}}
%{?python_provide:%python_provide python3-tcl-snack}
Summary:	Python bindings for Snack Sound Toolkit
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description -n python3-%{realname}
This package contains python3 bindings for the Snack Sound Toolkit. Tcl, Tk, and
Tkinter are also required to use Snack.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{realname}%{version}
%patch -P0 -p1 -b .mpg123
%patch -P1 -p1 -b .extracflags
%patch -P3 -p1 -b .newALSA
%patch -P4 -p1 -b .CVE20126303
%patch -P5 -p1 -b .format-security
%patch -P6 -p1 -b .py3
%patch -P7 -p1 -b .seektell
%patch -P8 -p1 -b .configure-c99
%patch -P9 -p1 -b .sigproc2-c99
%patch -P10 -p1 -b .setuptools
%patch -P11 -p1 -b .const-fix
cp %{SOURCE1} .
cp %{SOURCE2} generic/
chmod -x generic/*.c generic/*.h unix/*.c COPYING README demos/python/*
iconv -f iso-8859-1 -t utf-8 -o README{.utf8,}
mv README{.utf8,}
sed -i -e 's|\r||g' demos/python/*.txt

%build
cd unix/
%configure --disable-static --with-tcl=%{_libdir} --with-tk=%{_libdir} --with-ogg-include=%{_includedir} --with-ogg-lib=%{_libdir} --enable-alsa
make %{?_smp_mflags} EXTRACFLAGS="%{optflags}" stublib all libsnackogg.so libsnackmpg.so
cd ../python
%{__python3} setup.py build

%install
pushd unix/
make install DESTDIR=%{buildroot}
find %{buildroot} -name '*.la' -exec rm -f {} ';'
popd

pushd python
%{__python3} setup.py install --skip-build --root %{buildroot}
install -d %{buildroot}%{tcl_sitearch}
mv %{buildroot}%{_libdir}/%{realname}2.2 %{buildroot}%{tcl_sitearch}/%{realname}2.2
chmod -x %{buildroot}%{tcl_sitearch}/%{realname}2.2/snack.tcl
popd

# Devel bits
mkdir -p %{buildroot}%{_includedir}
install -p generic/*.h %{buildroot}%{_includedir}
install -p unix/snackConfig.sh %{buildroot}%{_libdir}

%filter_from_requires /libsnackstub2.2.so/d

%ldconfig_scriptlets

%files
%doc README
%license COPYING LICENSE-ffa.c.txt
%{tcl_sitearch}/%{realname}2.2/
# %%{_libdir}/libsnackstub*.so

%files devel
%{_includedir}/*.h
%{_libdir}/libsnackstub2.2.a
%{_libdir}/snackConfig.sh

%files -n python3-%{realname}
%doc doc/python-man.html demos/python/
%{python3_sitelib}/tkSnack*
%{python3_sitelib}/__pycache__/tkSnack*

%changelog
%autochangelog
