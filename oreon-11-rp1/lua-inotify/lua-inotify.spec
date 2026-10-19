%global source0_hash 21d005f16043397a85913a7d14a267716d6384f0228718d5de464bfc0274e338
%global luaver 5.4
%global lualibdir %{_libdir}/lua/%{luaver}
Name:           lua-inotify
Epoch:          1
Version:        0.5
Release:        1%{?dist}
Summary:        Inotify bindings for Lua
License:        MIT
URL:            http://hoelz.ro/projects/linotify
Source0:        https://github.com/hoelzro/linotify/archive/%{version}.tar.gz#/linotify-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  lua-devel
BuildRequires:  make
# /oreon:deps
%description
This is linotify, a binding for Linux's inotify library to Lua.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n linotify-%{version}
# do not strip when installing; preserve modtime (not strictly required)
sed -i.nostrip -e 's|install -D -s|install -D -p|' Makefile

%build

make %{?_smp_mflags} CFLAGS="%{optflags} -fPIC"
%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL_PATH=%{lualibdir}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
