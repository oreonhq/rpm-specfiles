%global source0_hash cbc3297bfc939e5b3818164b0a704cb551d72d4fe530119e00c2e20c10d36a8a
Name:           dynamite
Version:        0.1.1
Release:        1%{?dist}
Summary:        Extract data compressed with PKWARE Data Compression Library
License:        MIT
URL:            http://synce.sourceforge.net/
Source0:        http://dl.sf.net/synce/libdynamite-0.1.1.tar.gz
# oreon:deps
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
%{summary}

%package devel
Summary:        Files needed for software development with %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig
%description devel
The %{name}-devel package contains the files needed for development with
%{name}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n libdynamite-%{version}

%build

%configure --disable-static --disable-rpath
make LIBTOOL=%{_bindir}/libtool %{?_smp_mflags}
%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_libdir}/libdynamite.{l,}a
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n dynamite-devel -f %{oreon_filedir}/dynamite-devel.list

%changelog

%autochangelog
