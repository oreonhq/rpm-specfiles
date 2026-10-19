%global source0_hash ab7eb3680ba0d16f4a9eb1e05b7fcbb7d23438e25185462c55cd032a1954a985
%?mingw_package_header
%global name1 jimtcl
Name:           mingw-%{name1}
Version:        0.81
Release:        1%{?dist}
Summary:        MinGW small embeddable Tcl interpreter
License:        LicenseRef-Callaway-BSD
URL:            http://jim.tcl.tk
Source0:        https://github.com/msteveb/%{name1}/archive/%{version}/%{name1}-%{version}.tar.gz
Patch0:         jimtcl-fix_doc_paths.patch
Patch1:         jimtcl-implib.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  asciidoc
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
# /oreon:deps
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-jimtcl -f %{oreon_filedir}/mingw32-jimtcl.list
%files -n mingw64-jimtcl -f %{oreon_filedir}/mingw64-jimtcl.list

%changelog

%autochangelog
