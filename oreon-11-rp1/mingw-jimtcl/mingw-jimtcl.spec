%global source0_hash ab7eb3680ba0d16f4a9eb1e05b7fcbb7d23438e25185462c55cd032a1954a985

%?mingw_package_header

%global name1 jimtcl
Name:           mingw-%{name1}
Version:        0.81
Release:        13%{?dist}
Summary:        MinGW small embeddable Tcl interpreter

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://jim.tcl.tk
Source0:        https://github.com/msteveb/%{name1}/archive/%{version}/%{name1}-%{version}.tar.gz
# install documentation into /usr/share/doc/mingw{32,64}-jimtcl instead of
# /usr/{i686,x86_64}-w64-mingw32/sys-root/mingw/lib/mingw{32,64}-jimtcl
# patch from the native jimtcl package
Patch0:         jimtcl-fix_doc_paths.patch
# install libjim.dll into bindir (instead of libdir), and install the implib
# libjim.dll.a into libdir, to comply with mingw packaging guidelines
Patch1:         jimtcl-implib.patch
BuildArch:      noarch

BuildRequires: make
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw64-binutils
BuildRequires:  asciidoc
BuildRequires:  gcc

%description
Jim is an opensource small-footprint implementation of the Tcl programming 
language. It implements a large subset of Tcl and adds new features like 
references with garbage collection, closures, built-in Object Oriented 
Programming system, Functional Programming commands, first-class arrays and 
UTF-8 support.

%package -n mingw32-%{name1}
Summary:        MinGW small embeddable Tcl interpreter
Requires:       jimtcl

%description -n mingw32-%{name1}
Jim is an opensource small-footprint implementation of the Tcl programming 
language. It implements a large subset of Tcl and adds new features like 
references with garbage collection, closures, built-in Object Oriented 
Programming system, Functional Programming commands, first-class arrays and 
UTF-8 support.

%package -n mingw64-%{name1}
Summary:        MinGW small embeddable Tcl interpreter
Requires:       jimtcl

%description -n mingw64-%{name1}
Jim is an opensource small-footprint implementation of the Tcl programming 
language. It implements a large subset of Tcl and adds new features like 
references with garbage collection, closures, built-in Object Oriented 
Programming system, Functional Programming commands, first-class arrays and 
UTF-8 support.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name1}-%{version}
%patch -P0 -p0 -b .doc
%patch -P1 -p0 -b .implib

%build
%mingw_configure --full --shared --disable-option-checking

%mingw_make %{?_smp_mflags}

%install
install -d %{buildroot}/%{mingw32_datadir}/doc/%{name1}
install -d %{buildroot}/%{mingw64_datadir}/doc/%{name1}
%mingw_make install DESTDIR=%{buildroot} INSTALL_PROGRAM="cp -p" INSTALL_DATA="cp -p"
find %{buildroot} -name '*.la' -exec rm -f {} ';'
rm -rf %{buildroot}/%{mingw32_datadir}/doc/%{name1}
rm -rf %{buildroot}/%{mingw64_datadir}/doc/%{name1}
rm -rf %{buildroot}/%{mingw32_datadir}/%{mingw32_prefix}/docs
rm -rf %{buildroot}/%{mingw64_datadir}/%{mingw64_prefix}/docs
rm -rf %{buildroot}/%{mingw32_libdir}/jim/tcltest.tcl
rm -rf %{buildroot}/%{mingw64_libdir}/jim/tcltest.tcl
install -d %{buildroot}/%{_bindir}
rm -f %{buildroot}/%{mingw32_bindir}/build-jim-ext
rm -f %{buildroot}/%{mingw64_bindir}/build-jim-ext
rm -f %{buildroot}/%{mingw32_bindir}/jimdb
rm -f %{buildroot}/%{mingw64_bindir}/jimdb

%files -n mingw32-%{name1}
%license LICENSE
%doc AUTHORS README DEVELOPING STYLE
%doc README.extensions README.metakit README.namespaces README.oo README.utf-8
%{mingw32_bindir}/jimsh.exe
%{mingw32_bindir}/libjim.dll
%{mingw32_includedir}/*
%{mingw32_libdir}/libjim.dll.a
%{mingw32_libdir}/pkgconfig/jimtcl.pc

%files -n mingw64-%{name1}
%license LICENSE
%doc AUTHORS README DEVELOPING STYLE
%doc README.extensions README.metakit README.namespaces README.oo README.utf-8
%{mingw64_bindir}/jimsh.exe
%{mingw64_bindir}/libjim.dll
%{mingw64_includedir}/*
%{mingw64_libdir}/libjim.dll.a
%{mingw64_libdir}/pkgconfig/jimtcl.pc

%changelog
%autochangelog
