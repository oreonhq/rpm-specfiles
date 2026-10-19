%global source0_hash e1db403c01b0407a276a84b2aaf54515faebe1a5c1a31ec10857a1917161d109
Name:		libmacaroons
Version:	0.3.0
Release:        24%{?dist}
Summary:        C library supporting generation and use of macaroons
License:	BSD-3-Clause AND ISC
URL:		https://github.com/rescrv/libmacaroons
Source0:        https://github.com/rescrv/%{name}/archive/releases/%{version}/%{name}-%{version}.tar.gz
Patch0:		libmacaroons-hex-encoding.patch
Patch1:		libmacaroons-deserialize-memleak.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libsodium-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  python3
# /oreon:deps
%description
%{summary}

%package devel
Summary:	Development libraries linking against libmacaroons
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-releases-%{version}
%patch -P0 -p 1
%patch -P1 -p 1

%build

autoreconf -i
%configure --disable-static
%make_build
%install
%make_install
rm -f %{buildroot}%{_libdir}/%{name}.la
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libmacaroons-devel -f %{oreon_filedir}/libmacaroons-devel.list

%changelog

%autochangelog
