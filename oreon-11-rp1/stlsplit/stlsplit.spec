%global source0_hash d2999b58ffc5c1e7cb5c6c346ff9b38d6729fd78e8663d4d5c496ecdec2fbbc6
Name:           stlsplit
Version:        1.2
Release:        1%{?dist}
Summary:        Split STL file to more files - one shell each
License:        AGPL-3.0-or-later
URL:            https://github.com/admesh/stlsplit/
Source0:        https://github.com/admesh/stlsplit/archive/v%{version}.tar.gz
%if 0%{?fedora} >= 39 || 0%{?rhel} >= 10 || 0%{?oreon} >= 11
ExcludeArch:    %{ix86}
%endif
# oreon:deps
BuildRequires:  admesh-devel
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  premake
# /oreon:deps
%description
stlsplit receives one STL file and splits it to several files -
one shell a file.

%package devel
Summary:        Development files for the %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
This tool receives one STL file and splits it to several files -
one shell a file.

This package contains the development files needed for building new
applications that utilize the %{name} library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

premake5 gmake
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' lib.make
CFLAGS="%{optflags} -fPIC" LDFLAGS="%{?__global_ldflags}" %make_build
%install
install -Dpm 755 build/%{name} %{buildroot}%{_bindir}/%{name}
install -Dpm 755 build/lib%{name}.so.1 %{buildroot}%{_libdir}/lib%{name}.so.1
ln -s lib%{name}.so.1 %{buildroot}%{_libdir}/lib%{name}.so
install -Dpm 644 %{name}.h %{buildroot}%{_includedir}/%{name}.h
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n stlsplit-devel -f %{oreon_filedir}/stlsplit-devel.list

%changelog

%autochangelog
