%global source0_hash 12d930dad94a822756e5622f17d234afbf83f731709fce0fad33e5ce60775e3b
Name: chan
Version: 0.0.4
Release:        17%{?dist}
Summary:        Pure C implementation of Go channels
License: Apache-2.0
URL: https://github.com/tylertreat/%{name}
Source0:        https://github.com/tylertreat/%{name}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
Pure C implementation of Go channels. Unbuffered, buffered
and closing channels are available.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

./autogen.sh
%configure --disable-static
%make_build
%check

%make_build src/chan_test
./src/chan_test
%install
rm -rf $RPM_BUILD_ROOT
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
%ldconfig_post
%ldconfig_postun
%oreon_autofiles chan-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n chan-devel -f %{oreon_filedir}/chan-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.0.4-17
- Prepare for Oreon 11 (RP1)
