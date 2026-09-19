%global source0_hash 62b61eb12ab394012c861f6b48ba0bc04ac8765abca13bdde5a4d9105cb16138

Name:           tmate
Version:        2.4.0
Release:        15%{?dist}

Summary:        Instant terminal sharing
License:        MIT
Url:            http://tmate.io

Source0:        https://github.com/tmate-io/tmate/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  ruby
BuildRequires:  libevent-devel
BuildRequires:  openssl-devel
BuildRequires:  ncurses-devel
BuildRequires:  zlib-devel
BuildRequires:  libssh-devel >= 0.9.0
BuildRequires:  msgpack-devel >= 1.1.8

%description
Tmate is a fork of tmux providing an instant pairing solution.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
./autogen.sh
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%files
%doc CHANGES FAQ README-tmux README.md
%license COPYING
%{_bindir}/tmate
%{_mandir}/man1/tmate.1*

%changelog
%autochangelog
