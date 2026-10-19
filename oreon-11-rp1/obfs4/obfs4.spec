%global source0_hash 6ed94258433665a11a4631c6bbbb45b4452d65bdfbe4d30365a87b3d43a3a7ec
%bcond check 0
%global goipath         gitlab.com/yawning/obfs4.git
%global forgeurl        https://gitlab.com/yawning/obfs4
Version:                0.0.14
%global tag             obfs4proxy-0.0.14
%gometa -f
%global goname          obfs4
%global common_description %{expand:
This is a look-like nothing obfuscation protocol that incorporates ideas and
concepts from Philipp Winter's ScrambleSuit protocol.  The obfs naming was
chosen primarily because it was shorter, in terms of protocol ancestry obfs4
is much closer to ScrambleSuit than obfs2/obfs3.
The notable differences between ScrambleSuit and obfs4:
 * The handshake always does a full key exchange (no such thing as a Session
   Ticket Handshake).
 * The handshake uses the Tor Project's ntor handshake with public keys
   obfuscated via the Elligator 2 mapping.
 * The link layer encryption uses NaCl secret boxes (Poly1305/XSalsa20).
As an added bonus, obfs4proxy also supports acting as an obfs2/3 client and
bridge to ease the transition to the new protocol.}
%global golicenses      LICENSE LICENSE-GPL3.txt
%global godocs          doc README.md ChangeLog
Name:           %{goname}
Release:        1%{?dist}
Summary:        The obfourscator, a pluggable transport for Tor
License:        GPL-3.0-only AND LicenseRef-Callaway-BSD
URL:            %{gourl}
Source0:        %{forgeurl}/-/archive/%{tag}/%{name}-%{tag}.tar.bz2
Source1:        obfs4.torrc
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

%build

for cmd in obfs4proxy; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
install -m 0755 -vd                     %{buildroot}%{_mandir}/man1
install -m 0644 -vp doc/obfs4proxy.1    %{buildroot}%{_mandir}/man1/
install -m 0755 -vd                     %{buildroot}%{_sysconfdir}/tor
install -m 0644 -vp %{SOURCE1}          %{buildroot}%{_sysconfdir}/tor/
%oreon_autofiles main
%if %{with check}
%check

%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
