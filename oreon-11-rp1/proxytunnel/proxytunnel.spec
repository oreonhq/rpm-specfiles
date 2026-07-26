%global source0_hash b8740375c4f0f635fd22b197389d4268daeb70829648e15050fd4db2b41ef898

Name:           proxytunnel
Version:        1.10.20200907
Release:        15%{?dist}
Summary:        Tool to tunnel a connection through an standard HTTP(S) proxy

# Automatically converted from old format: GPLv2+ and BSD and MIT - review is highly recommended.
License:        GPL-2.0-or-later AND LicenseRef-Callaway-BSD AND LicenseRef-Callaway-MIT
URL:            https://github.com/proxytunnel/proxytunnel
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  asciidoc
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  xmlto

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

%files
%doc CHANGES CREDITS KNOWN_ISSUES README.md TODO
%license LICENSE.txt
%{_bindir}/proxytunnel
%{_mandir}/man1/proxytunnel.1*

%changelog
%autochangelog
