%global source0_hash 8d1e07c4509d07b4f637b178787542d235a81afad772989762c2dd88cef22741
Name:		libfep
Version:	0.1.0
Release:        30%{?dist}
Summary:        Library to implement FEP (front end processor) on ANSI terminals
License:	LicenseRef-Callaway-BSD AND GPL-3.0-or-later
URL:		http://github.com/ueno/libfep
Source0:        https://github.com/ueno/libfep/releases/download/%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gobject-introspection-devel
BuildRequires:  make
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  vala
# /oreon:deps
%description
The libfep project aims to provide a server and a library to implement
input method FEP (front end processor), running on ANSI compliant
terminals.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

GIO_LIBS=`pkg-config gio-2.0 gmodule-2.0 --libs`
export GIO_LIBS
%configure --disable-static
make %{?_smp_mflags}
%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f '{}' ';'
cp -p fep/README README.fep
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libfep-devel -f %{oreon_filedir}/libfep-devel.list

%changelog

%autochangelog
