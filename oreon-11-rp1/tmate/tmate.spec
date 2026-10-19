%global source0_hash 62b61eb12ab394012c861f6b48ba0bc04ac8765abca13bdde5a4d9105cb16138
Name:           tmate
Version:        2.4.0
Release:        15%{?dist}
Summary:        Instant terminal sharing
License:        MIT
Url:            http://tmate.io
Source0:        https://github.com/tmate-io/tmate/archive/%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  libevent-devel
BuildRequires:  libssh-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  msgpack-devel
BuildRequires:  ncurses-devel
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  ruby
BuildRequires:  zlib-devel
# /oreon:deps
%description
Tmate is a fork of tmux providing an instant pairing solution.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

./autogen.sh
%configure
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
