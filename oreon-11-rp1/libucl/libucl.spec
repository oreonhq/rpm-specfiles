%global source0_hash d95a0e2151cc167a0f3e51864fea4e8977a0f4c473faa805269a347f7fb4e165
Name:           libucl
Version:        0.8.2
Release:        12%{?dist}
Summary:        Universal configuration library parser
License:        LicenseRef-Callaway-BSD AND LicenseRef-Callaway-MIT
URL:            https://github.com/vstakhov/libucl
Source0:        https://github.com/vstakhov/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Provides: bundled(uthash) = 1.9.8
Provides: bundled(klib)
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  curl-devel
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  libtree-devel
BuildRequires:  make
BuildRequires:  mum-hash-devel
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# /oreon:deps
%description
%{summary}.

%package        devel
Summary:        libucl development files
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
%{summary}.

%package     -n python3-libucl
Summary:        Python bindings for libucl
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description -n python3-libucl
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

# pkg-config: remove trailing slash from standard include dir.
sed -i 's/includedir}\/$/includedir}/' libucl.pc.in

# Remove bundled libraries.
sed -i '/mum\.h/d' src/Makefile.am
sed -i '/tree\.h/d' src/Makefile.am
sed -i 's/ucl_chartable.h \\/ucl_chartable.h/' src/Makefile.am
rm src/mum.h src/tree.h

# Set include/lib dir for python bindings.
sed -i "s%language = 'c'%language = \'c\', include_dirs = [ \"../include\"],  library_dirs = [ \"../src/.libs\"]%" python/setup.py

# Remove network-dependent tests.
for def in schema/ref.json schema/refRemote.json schema/definitions.json; do
  rm tests/$def
done

%build

./autogen.sh
%configure --disable-static
V=1 %make_build
(cd python; %py3_build)
%install
%make_install
(cd python; %py3_install)
rm %{buildroot}%{_libdir}/%{name}.la
%oreon_autofiles python3-libucl usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%make_build check
%files -f %{oreon_filedir}/main.list
%files -n libucl-devel -f %{oreon_filedir}/libucl-devel.list
%files -n python3-libucl -f %{oreon_filedir}/python3-libucl.list

%changelog

%autochangelog
