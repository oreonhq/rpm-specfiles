%global source0_hash de1847f7b59021c16bdc72abb4d8e2d9187cd6124d69156f3326dd34ee043681
Name:           redland
Version:        1.0.17
Release:        1%{?dist}
Summary:        RDF Application Framework
License:        LGPL-2.1-or-later OR Apache-2.0
URL:            http://librdf.org/
Source0:        http://download.librdf.org/source/%{name}-%{version}.tar.gz
Patch1:         0001-rhbz-1936659-stub-deprecated.patch
Obsoletes: redland-virtuoso < 1.0.17-8
# oreon:deps
BuildRequires:  curl-devel
BuildRequires:  gcc-c++
BuildRequires:  gtk-doc
BuildRequires:  libtool
BuildRequires:  libtool-ltdl-devel
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  raptor2-devel
BuildRequires:  rasqal-devel
BuildRequires:  sqlite-devel
# /oreon:deps
%description
Redland is a library that provides a high-level interface for RDF
(Resource Description Framework) implemented in an object-based API.
It is modular and supports different RDF/XML parsers, storage
mechanisms and other elements. Redland is designed for applications
developers to provide RDF support in their applications as well as
for RDF developers to experiment with the technology.

%package         devel
Summary:         Libraries and header files for programs that use Redland
Requires:        %{name}%{?_isa} = %{version}-%{release}
%description     devel
Header files for development with Redland.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

NOCONFIGURE=1 ./autogen.sh

# hack to nuke rpaths
%if "%{_libdir}" != "/usr/lib"
sed -i -e 's|"/lib /usr/lib|"/%{_lib} %{_libdir}|' configure
%endif

%build

%define distrooptions --with-mysql --with-postgresql
export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
export CXXFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
%configure \
  --enable-release \
  --disable-static \
  --with-sqlite \
  --without-bdb \
  --without-threestone \
  --without-virtuoso \
  %{distrooptions} \
%make_build
%install
%make_install
find $RPM_BUILD_ROOT -name \*.la -exec rm -v {} \;
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make check
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n redland-devel -f %{oreon_filedir}/redland-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.17-41
- Prepare for Oreon 11 (RP1)
