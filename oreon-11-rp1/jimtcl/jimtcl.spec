%global source0_hash 435095b436b38b96dd85e8cda13878144813bf52066057f76368db178dd8fea2
%bcond_without tests
Name:           jimtcl
Version:        0.84
Release:        1%{?dist}
Summary:        A small embeddable Tcl interpreter
License:        BSD-2-Clause-Views
URL:            http://jim.tcl.tk
Source0:        https://github.com/msteveb/%{name}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  asciidoc
BuildRequires:  gcc-c++
BuildRequires:  hostname
BuildRequires:  make
BuildRequires:  pkgconfig(SDL2_gfx)
BuildRequires:  pkgconfig(SDL2_ttf)
BuildRequires:  pkgconfig(hiredis)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(zlib)
# /oreon:deps
%description

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel

The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup
rm -rf sqlite3

%build

export AR=ar
export RANLIB=ranlib
export STRIP=strip
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with tests}
%check

rm tests/ssl.test
make test
%endif
%files -f %{oreon_filedir}/main.list
%files -n jimtcl-devel -f %{oreon_filedir}/jimtcl-devel.list

%changelog

%autochangelog
