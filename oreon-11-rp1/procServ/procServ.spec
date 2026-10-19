%global source0_hash 8a471ea9ad3bfde3d886edbe05ca0c39889b81c44e8b6e52d6ed31175815dd07
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}
Summary:        Process server with telnet console and log access
Name: procServ
Version: 2.8.0
Release:        1%{?dist}
License: GPL-3.0-only
URL: https://github.com/ralphlange/procServ
Source0:        https://github.com/ralphlange/procServ/releases/download/V%{version}/procServ-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  libtelnet-devel
BuildRequires:  make
# /oreon:deps
%description
procServ is a wrapper that starts an arbitrary command as a child process in
the background, connecting its standard input and output to a Unix domain
socket or a TCP port for telnet access.
It supports logging, child restart (manual or automatic on exit), and more.

procServ does not have the rich feature set of the screen utility,
but is intended to provide running a command in a system service style,
in a small, robust way.
Handling multiple users, authorization, authentication, central logging
is done best on a higher level, using a package like conserver.

For security reasons, procServ only accepts connections from localhost.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%configure --docdir=%{_pkgdocdir}
make %{?_smp_mflags}
%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
