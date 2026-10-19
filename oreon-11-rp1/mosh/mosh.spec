%global source0_hash d93ec9b2b0a012f59c4b8d5902b8a70b45db01e32c7c1ef7e5acd84ecebbb95f
Name:		mosh
Version:	1.4.0
Release:        1%{?dist}
Summary:        Mobile shell that supports roaming and intelligent local echo
License:	GPL-3.0-or-later
URL:		https://mosh.mit.edu/
Source0:        https://mosh.mit.edu/mosh-%{version}.tar.gz
Requires:	openssh-clients
Requires:	openssl
Requires:	perl(IO::Socket::IP)
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libutempter-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  openssl-devel
BuildRequires:  perl-diagnostics
BuildRequires:  perl-generators
BuildRequires:  protobuf-compiler
BuildRequires:  protobuf-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
Mosh is a remote terminal application that supports:
  - intermittent network connectivity,
  - roaming to different IP address without dropping the connection, and
  - intelligent local echo and line editing to reduce the effects
    of "network lag" on high-latency connections.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%configure --disable-silent-rules
%make_build
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
