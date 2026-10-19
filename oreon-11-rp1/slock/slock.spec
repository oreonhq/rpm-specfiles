%global source0_hash 99711e6b419b221ae9fc3e9c8f31e6b168db51154278996f3d02ce65cc198301
Name:           slock
Version:        1.7
Release:        1%{?dist}
Summary:        Simple X display locker
License:        MIT
URL:            http://tools.suckless.org/%{name}
Source0:        http://dl.suckless.org/tools/%{name}-%{version}.tar.gz
Patch0:         %{name}-1.4-libxcrypt.patch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  libX11-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libxcrypt-devel
BuildRequires:  make
BuildRequires:  sed
BuildRequires:  xorg-x11-proto-devel
# /oreon:deps
%description
This is the simplest X screen locker we are aware of.  It is stable and
quite a lot people in this community are using it every day when they
are out with friends or fetching some food from the local pub.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1
sed -e 's/^CFLAGS =/CFLAGS +=/g' -e 's/^LDFLAGS = -s/LDFLAGS +=/g' -i config.mk
sed -e 's/explicit_bzero\.c//' -i config.mk && rm -f explicit_bzero.c
sed -e 's/^\t@/\t/' -i Makefile
sed -e 's/nogroup/nobody/' config.def.h > config.h

%build

export CFLAGS="%{optflags}"
export LDFLAGS="%{?__global_ldflags}"
make %{?_smp_mflags}
%install
make install DESTDIR=%{buildroot} PREFIX=%{_prefix}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
