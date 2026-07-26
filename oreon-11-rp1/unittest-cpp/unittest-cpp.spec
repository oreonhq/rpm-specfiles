%global source0_hash 74852198877dc2fdebdc4e5e9bd074018bf8ee03a13de139bfe41f4585b2f5b9

%global         _hardened_build 1
%global         oldname     UnitTest++

Name:           unittest-cpp
Version:        2.0.0
Release:        22%{?dist}
Summary:        Lightweight unit testing framework for C++
License:        MIT

URL:            https://github.com/%{name}/%{name}
Source0:        %url/archive/v%{version}/%{name}-%{version}.tar.gz
# documentation from 1.4 tarball: docs/UnitTest++.html
Source1:        %{name}.html
# Fix configure.ac version test
Patch0:         fix_version_2.0.0.patch

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  autoconf
BuildRequires:  libtool

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
# rpmlint unused-direct-shlib-dependency
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
%make_build

%check
make check

%install
%make_install
rm -f %{buildroot}%{_libdir}/lib%{oldname}.la

%files
%doc AUTHORS README.md
%license LICENSE
%{_libdir}/lib%{oldname}.so.2*

%files devel
%doc %{name}.html
%{_includedir}/%{oldname}
%{_libdir}/lib%{oldname}.so
%{_libdir}/pkgconfig/UnitTest++.pc

%files static
%{_libdir}/lib%{oldname}.a

%ldconfig_scriptlets

%changelog
%autochangelog
