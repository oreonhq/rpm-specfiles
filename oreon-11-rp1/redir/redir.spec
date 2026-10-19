%global source0_hash 7311731097aabd390bd4d8f390980278b16b25d0bae8e21a9e768cd824f846f7
Name:           redir
Version:        3.3
Release:        1%{?dist}
Summary:        A TCP port redirector for UNIX
License:        GPL-2.0-or-later
URL:            https://github.com/troglobit/redir
Source0:        https://github.com/troglobit/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gettext
# /oreon:deps
%description
This is a TCP port redirector for UNIX. It can be run under inetd or as 
standalone (in which case it handles multiple connections). It is 8 bit 
clean, not limited to line mode, is small and lightweight. If you want 
access control, run it under xinetd, or inetd with TCP wrappers.
Redir listens for TCP connections on a given port, and, when it receives 
a connection, then connects to a given destination address:port, and 
pass data between them. It finds most of its applications in traversing 
firewalls, but, of course, there are other uses.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

./autogen.sh
%configure
%make_build CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_OPT_FLAGS"
%check

make check
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
