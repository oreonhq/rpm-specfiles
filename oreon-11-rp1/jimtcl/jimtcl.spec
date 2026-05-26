%bcond_without tests

Name:           jimtcl
Version:        0.83
Release:        %autorelease
Summary:        A small embeddable Tcl interpreter

License:        BSD-2-Clause-Views
URL:            http://jim.tcl.tk
Source:         https://github.com/msteveb/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# readline expects applications to include stdio.h, jimtcl was not
Patch:          https://github.com/msteveb/jimtcl/commit/35e0e1f9b1f018666e5170a35366c5fc3b97309c.patch#/jimtcl-stdio-for-readline.diff
# oreon url source checksums begin
%global source0_sha256 6f2df00009f5ac4ad654c1ae1d2f8ed18191de38d1f5a88a54ea99cc16936686
%global source0_file jimtcl-0.83.tar.gz
# oreon url source checksums end

BuildRequires:  gcc-c++
BuildRequires:  asciidoc
BuildRequires:  make
# Extension dependencies
BuildRequires:  pkgconfig(hiredis)
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(SDL2_gfx)
BuildRequires:  pkgconfig(SDL2_ttf)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(zlib)
%if %{with tests}
BuildRequires:  hostname
%endif

%global _description %{expand:
Jim is an opensource small-footprint implementation of the Tcl programming
language. It implements a large subset of Tcl and adds new features like 
references with garbage collection, closures, built-in Object Oriented 
Programming system, Functional Programming commands, first-class arrays and 
UTF-8 support.}

%description %{_description}


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel %{_description}

The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/jimtcl-0.83.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "6f2df00009f5ac4ad654c1ae1d2f8ed18191de38d1f5a88a54ea99cc16936686" || { echo "oreon: Source0 SHA256 mismatch for jimtcl-0.83.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup
rm -rf sqlite3

%build
#configure is not able to locate the needed binaries, so specify it manualy
# export CC=gcc
# export LD=ld
export AR=ar
export RANLIB=ranlib
export STRIP=strip

# compile extensions that are disabled by default
# as modules
# see ./configure --extinfo for list
%configure --shared --disable-option-checking \
  --allextmod \
%ifarch s390x # zlib test fails on s390x
  --without-ext=zlib \
%endif
  --docdir=%{_datadir}/doc/%{name}
%make_build


%install
%make_install INSTALL_DOCS=nodocs
rm %{buildroot}/%{_libdir}/jim/README.extensions


%if %{with tests}
%check
# remove tests that require network access
rm tests/ssl.test
make test
%endif


%files
%license LICENSE
%doc AUTHORS README README.*
%doc EastAsianWidth.txt
%doc %{_datadir}/doc/%{name}/Tcl.html
%{_bindir}/jimdb
%{_bindir}/jimsh
%dir %{_libdir}/jim
%{_libdir}/jim/*.tcl
%{_libdir}/jim/*.so
%{_libdir}/libjim.so.*


%files devel
%doc CONTRIBUTING.md STYLE
%{_includedir}/*
%{_bindir}/build-jim-ext
%{_libdir}/libjim.so
%{_libdir}/pkgconfig/jimtcl.pc

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.83-1
- Prepare for Oreon 11 (RP1)
