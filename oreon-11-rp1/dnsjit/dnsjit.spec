%global source0_hash b8cd7a4ca4133262d0dd27f26dbad840237f59a4e6c76effab4d8da7b66c2bd0
%global url_files https://www.dns-oarc.net/files/%{name}
Name:           dnsjit
Version:        1.6.0
Release:        1%{?dist}
Summary:        Engine for capturing, parsing and replaying DNS
Group:          Productivity/Networking/DNS/Utilities
License:        GPL-3.0-or-later
URL:            https://codeberg.org/DNS-OARC/dnsjit
VCS:            git:%{url}
Source0:        %{url_files}/%{name}-%{version}.tar.gz
%if 0%{?suse_version} || 0%{?sle_version}
%else
%endif
ExcludeArch:    riscv64 ppc64 ppc64le
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  ck-devel
BuildRequires:  gcc
BuildRequires:  gnutls-devel
BuildRequires:  libpcap-devel
BuildRequires:  libtool
BuildRequires:  libzstd-devel
BuildRequires:  lmdb-devel
BuildRequires:  luajit-devel
BuildRequires:  lz4-devel
BuildRequires:  make
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
dnsjit is a combination of parts taken from dsc, dnscap, drool,
and put together around Lua to create a script-based engine for easy
capturing, parsing and statistics gathering of DNS message while also
providing facilities for replaying DNS traffic.

%package devel
Summary:    Engine for capturing, parsing and replaying DNS - development files
Group:      Development/Libraries/C and C++
Requires:   %{name}%{?_isa} = %{version}-%{release}
Requires:   libpcap-devel
Requires:   luajit-devel >= 2.0.0
Requires:   lmdb-devel
Requires:   ck-devel
Requires:   gnutls-devel
%if 0%{?suse_version} || 0%{?sle_version}
Requires:   liblz4-devel
%else
Requires:   lz4-devel
%endif
Requires:   libzstd-devel
Requires:   zlib-devel
Requires:   xz-devel
%description devel
dnsjit is a combination of parts taken from dsc, dnscap, drool,
and put together around Lua to create a script-based engine for easy
capturing, parsing and statistics gathering of DNS message while also
providing facilities for replaying DNS traffic.

This package includes development files needed to create dnsjit modules.

%package examples
BuildArch:  noarch
Summary:    Engine for capturing, parsing and replaying DNS - examples
Group:      Productivity/Networking/DNS/Utilities
Requires:   %{name} = %{version}-%{release}
%description examples
dnsjit is a combination of parts taken from dsc, dnscap, drool,
and put together around Lua to create a script-based engine for easy
capturing, parsing and statistics gathering of DNS message while also
providing facilities for replaying DNS traffic.

This package includes examples of prepared scripts.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf
%configure
%make_build
%install
%make_install
rm -f %{buildroot}%{_datadir}/doc/%{name}/*.lua
rm -f %{buildroot}%{_datadir}/doc/%{name}/LICENSE
mkdir -p %{buildroot}%{_libexecdir}/%{name}/
cp -p examples/*.lua %{buildroot}%{_libexecdir}/%{name}/
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%make_build test
%files -f %{oreon_filedir}/main.list
%files -n dnsjit-devel -f %{oreon_filedir}/dnsjit-devel.list
%files -n dnsjit-examples -f %{oreon_filedir}/dnsjit-examples.list

%changelog

%autochangelog
