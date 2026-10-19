%global source0_hash 0b3f3ce16eef060df6e0d90327ee82593dfd75281347908698747cfa3f8d0655
Name:           lsw
Version:        0.3
Release:        1%{?dist}
Summary:        Prints all window titles of DISPLAY to standard output
License:        MIT
URL:            http://tools.suckless.org/%{name}
Source0:        http://dl.suckless.org/tools/%{name}-%{version}.tar.gz
Patch0:         lsw-0.3-config.patch
Patch1:         lsw-0.3-segfault-avoidance.patch
# oreon:deps
BuildRequires:  binutils
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  libX11-devel
BuildRequires:  make
BuildRequires:  redhat-rpm-config
BuildRequires:  sed
# /oreon:deps
%description
Lists the titles of all running X windows to stdout, similar to ls(1). Might
be useful for script integration.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .config
%patch -P1 -p1

%build

export LDFLAGS="%{?__global_ldflags}"
make %{?_smp_mflags}
%install
make install DESTDIR=%{buildroot} PREFIX=%{_prefix}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
