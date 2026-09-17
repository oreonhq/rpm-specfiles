%global source0_hash 890674996168ef5ba143d80d49ab8b61594a4eb70198dcac76caf6e1bd264a41
%global tag libunibreak_6_1

Name:           libunibreak
Version:        6.1
Release:        %autorelease
Summary:        A Unicode line-breaking library
License:        Zlib
URL:            https://github.com/adah1972/libunibreak
Source0:        https://github.com/adah1972/libunibreak/archive/%{tag}.tar.gz#/libunibreak-%{version}.tar.gz
Source1:        libunibreak-test-data.tar.gz

Patch0:         offline_files.patch
Patch1:         remove_unused_var.patch

ExcludeArch:    %{ix86}

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libtool

%description
Libunibreak is an implementation of the line breaking and word
breaking algorithms as described in Unicode Standard Annex 14 and
Unicode Standard Annex 29. It is designed to be used in a generic text
renderer.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n libunibreak-%{tag} -p1

tar xzf %{SOURCE1}

sed -r -i 's|^(#!/usr/bin/)env (python)|\1\2|' src/*.py
chmod a+x src/*.py

%build
./autogen.sh
%configure --disable-static
%make_build

%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%check
%make_build check

%ldconfig_scriptlets

%files
%doc AUTHORS NEWS README.md
%license LICENCE
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
%autochangelog
