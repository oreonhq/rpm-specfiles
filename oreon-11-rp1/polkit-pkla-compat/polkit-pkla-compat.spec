%global source0_hash cbf804dfc235b40f2f7ea694c37d577f1cb5d3042d53063de1753016a46c39af

Name:		polkit-pkla-compat
Version:	0.1
Release:	32%{?dist}
Summary:	Rules for polkit to add compatibility with pklocalauthority
# GPLv2-licensed ltmain.sh and Apache-licensed mocklibc are not shipped in
# the binary package.
License:	LGPL-2.0-or-later
URL:		https://pagure.io/polkit-pkla-compat
Source0:        http://releases.pagure.org/polkit-pkla-compat/polkit-pkla-compat-%{version}.tar.xz

BuildRequires: make
BuildRequires:  gcc
BuildRequires:	docbook-style-xsl, libxslt, glib2-devel, polkit-devel
# To ensure the polkitd group already exists when this is installed
Requires(pre): polkit

%global _hardened_build 1

%description
A polkit JavaScript rule and associated helpers that mostly provide
compatibility with the .pkla file format supported in polkit <= 0.105 for users
of later polkit releases.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q

%build
%configure
%make_build

%install
%make_install

%check
make check

%files
%doc AUTHORS COPYING NEWS README
%dir %attr(0750,root,polkitd) %dir %{_sysconfdir}/polkit-1/localauthority
%dir %{_sysconfdir}/polkit-1/localauthority/*.d
%dir %{_sysconfdir}/polkit-1/localauthority.conf.d
%config(noreplace) %{_sysconfdir}/polkit-1/rules.d/49-polkit-pkla-compat.rules
%{_bindir}/pkla-admin-identities
%{_bindir}/pkla-check-authorization
%{_mandir}/man8/pkla-admin-identities.8*
%{_mandir}/man8/pkla-check-authorization.8*
%{_mandir}/man8/pklocalauthority.8*
%dir %attr(0750,root,polkitd) %{_localstatedir}/lib/polkit-1
%dir %{_localstatedir}/lib/polkit-1/localauthority
%dir %{_localstatedir}/lib/polkit-1/localauthority/*.d

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.1-32
- Prepare for Oreon 11 (RP1)
