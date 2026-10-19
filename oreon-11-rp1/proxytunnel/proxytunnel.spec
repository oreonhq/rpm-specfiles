%global source0_hash 1b1ae36327254cac351aa5358767c177b050ab4ce4a75fa100244da7816849e9
Name:           proxytunnel
Version:        1.13.0
Release:        1%{?dist}
Summary:        Tool to tunnel a connection through an standard HTTP(S) proxy
License:        GPL-2.0-or-later AND LicenseRef-Callaway-BSD AND LicenseRef-Callaway-MIT
URL:            https://github.com/proxytunnel/proxytunnel
Source0:        https://github.com/%{name}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  asciidoc
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  xmlto
# /oreon:deps
%description
ProxyTunnel is a program that connects stdin and stdout to a server somewhere 
on the network, through a standard HTTPS proxy. We mostly use it to tunnel SSH
sessions through HTTP(S) proxies.
Proxytunnel can currently do the following:
* Create tunnels using HTTP and HTTPS proxies (That understand the HTTP 
  CONNECT command).
* Work as a back-end driver for an OpenSSH client, and create SSH
  connections through HTTP(S) proxies.
* Work as a stand-alone application, listening on a port for connections, 
  and then tunneling these connections to a specified destination. 

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
# Fix permissions
chmod -c 644 CHANGES
# Convert docs to UTF-8
for f in CHANGES; do
    iconv -f iso-8859-1 -t utf-8 $f > $f.tmp
    touch -r $f $f.tmp
    mv -f $f.tmp $f
done

%build

%make_build CFLAGS="%{optflags}"
%install
%make_install prefix=%{_prefix} DESTDIR=%{buildroot}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
