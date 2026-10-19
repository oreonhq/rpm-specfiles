%global source2_hash dd0ffdf7d4262e887208af17617c7b84781969b832ebfd4ac24e9fcfddf93241
%global source0_hash 920dde485e15eda0cce8d2310b41d492c534e5e3d89ad407a0b4176dd2ff88fe
Summary:        An XML parser library
Name: expat
Version: 2.8.5
Release:        1%{?dist}
Source0:        https://github.com/lib%{name}/lib%{name}/releases/download/R_2_8_5/%{name}-%{version}.tar.gz
Source1:        https://github.com/libexpat/libexpat/releases/download/R_%(echo %{version} | tr . _)/expat-%{version}.tar.gz.asc
Source2: https://keys.openpgp.org/vks/v1/by-fingerprint/3176EF7DB2367F1FCA4F306B1F9B0E909AF37285
URL: https://libexpat.github.io/
VCS: git:https://github.com/libexpat/libexpat.git
License: MIT
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  gcc-c++
BuildRequires:  gnupg2
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  xmlto
# /oreon:deps
%description
This is expat, the C library for parsing XML, written by James Clark. Expat
is a stream oriented XML parser. This means that you register handlers with
the parser prior to starting the parse. These handlers are called when the
parser discovers the associated structures in the document being parsed. A
start tag is an example of the kind of structures for which you may
register handlers.

%package devel
Summary: Libraries and header files to develop applications using expat
Requires: expat%{?_isa} = %{version}-%{release}
%description devel
The expat-devel package contains the libraries, include files and documentation
to develop XML applications with expat.

%package static
Summary: expat XML parser static library
Requires: expat-devel%{?_isa} = %{version}-%{release}
%description static
The expat-static package contains the static version of the expat library.
Install it if you need to link statically with expat.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup
sed -i 's/install-data-hook/do-nothing-please/' lib/Makefile.am
./buildconf.sh

%build

export CFLAGS="$RPM_OPT_FLAGS -fPIC"
export DOCBOOK_TO_MAN="xmlto man"
%configure --enable-symbol-versioning
%make_build
%install
%make_install
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make check
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n expat-devel -f %{oreon_filedir}/expat-devel.list
%files -n expat-static -f %{oreon_filedir}/expat-static.list

%changelog

%autochangelog
