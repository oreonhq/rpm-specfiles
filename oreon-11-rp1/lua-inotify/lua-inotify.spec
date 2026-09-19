%global source0_hash 21d005f16043397a85913a7d14a267716d6384f0228718d5de464bfc0274e338

%global luaver 5.4
%global lualibdir %{_libdir}/lua/%{luaver}

Name:           lua-inotify
Epoch:          1
Version:        0.5
Release:        14%{?dist}
Summary:        Inotify bindings for Lua

License:        MIT
URL:            http://hoelz.ro/projects/linotify
Source0:        https://github.com/hoelzro/linotify/archive/%{version}.tar.gz#/linotify-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  lua-devel >= %{luaver}
BuildRequires: make

%description
This is linotify, a binding for Linux's inotify library to Lua.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n linotify-%{version}
# do not strip when installing; preserve modtime (not strictly required)
sed -i.nostrip -e 's|install -D -s|install -D -p|' Makefile

%build
# original CFLAGS is computed using Lua's pkgconfig file, but ours
# does not set any.
#
# Overriding with the default %%{optflags}, and keeping the -fPIC
# from the original CFLAGS as the build target is a shared object
make %{?_smp_mflags} CFLAGS="%{optflags} -fPIC"

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL_PATH=%{lualibdir}

%files
%license COPYRIGHT
%doc README.md Changes
%{lualibdir}/inotify.so

%changelog
%autochangelog
