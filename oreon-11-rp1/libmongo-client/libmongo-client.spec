%global source0_hash b5dc1e0bb7d83e33f4aa325c460c1218dc59d00aff61d7b84c6b8b22c46d0ecb
Name:		libmongo-client
Version:	0.1.8
Release:        1%{?dist}
Summary:        Alternative C driver for MongoDB
License:	Apache-2.0
URL:		https://github.com/algernon/libmongo-client
Source0:        %{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  glib2-devel
BuildRequires:  graphviz
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%package devel
Summary: Development files for libmongo-client
Requires: %{name}%{?_isa} = %{version}-%{release}
%package doc
Summary: Documentation for libmongo-client
%{?fedora:BuildArch: noarch}
BuildRequires: graphviz
BuildRequires: doxygen
BuildRequires: make
%description
Alternative C driver for MongoDB. Libmongo-client is meant
to be a stable (API, ABI and quality alike), clean, well documented
and well tested shared library, that strives to make the most
common use cases as convenient as possible.

%description devel
Development files (libraries and include files) for libmongo-client

%description doc
Subpackage contains documentation for libmongo-client

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

autoreconf -i
%configure --disable-static
make %{?_smp_mflags}
make doxygen
%install
make install DESTDIR=%{buildroot} INSTALL="install -p"
rm -f %{buildroot}/%{_libdir}/*.{a,la}
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libmongo-client-devel -f %{oreon_filedir}/libmongo-client-devel.list
%files -n libmongo-client-doc -f %{oreon_filedir}/libmongo-client-doc.list

%changelog

%autochangelog
