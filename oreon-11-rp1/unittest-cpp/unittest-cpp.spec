%global source0_hash 74852198877dc2fdebdc4e5e9bd074018bf8ee03a13de139bfe41f4585b2f5b9
%global         _hardened_build 1
%global         oldname     UnitTest++
Name:           unittest-cpp
Version:        2.0.0
Release:        1%{?dist}
Summary:        Lightweight unit testing framework for C++
License:        MIT
URL:            https://github.com/%{name}/%{name}
Source0:        https://github.com/%{name}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.html
Patch0:         fix_version_2.0.0.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
%{name} is a lightweight unit testing framework for C++.
Simplicity, portability, speed, and small footprint are all
very important aspects of %{name}.

%package devel
Summary:        Object files for development using %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
The %{name}-devel package contains the object files
necessary for developing test programs.

%package static
Summary:        Static library for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description static
The %{name}-static package contains the object files
necessary for statically linking test programs.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
cp -p %SOURCE1 .
# autoreconf will complain about missing NEWS and README files
touch NEWS
ln README.md README
# autoreconf will add a GPLv3 license text in COPYING
ln LICENSE COPYING
autoreconf -i

%build

%configure
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
%make_build
%check

make check
%install
%make_install
rm -f %{buildroot}%{_libdir}/lib%{oldname}.la
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n unittest-cpp-devel -f %{oreon_filedir}/unittest-cpp-devel.list
%files -n unittest-cpp-static -f %{oreon_filedir}/unittest-cpp-static.list

%changelog

%autochangelog
