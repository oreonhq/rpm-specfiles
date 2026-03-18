Name:    bubblewrap
Version: 0.11.0
Release: 4%{?dist}
Summary: Core execution tool for unprivileged containers

License: LGPL-2.0-or-later
URL:     https://github.com/containers/bubblewrap/
Source0: https://github.com/containers/bubblewrap/releases/download/v%{version}/bubblewrap-%{version}.tar.xz

BuildRequires: pkgconfig(bash-completion) >= 2.0
BuildRequires: gcc
BuildRequires: docbook-style-xsl
BuildRequires: meson
BuildRequires: pkgconfig(libcap)
BuildRequires: pkgconfig(libselinux)
BuildRequires: /usr/bin/xsltproc

%description
Bubblewrap (/usr/bin/bwrap) is a core execution engine for unprivileged
containers that works as a setuid binary on kernels without
user namespaces.

%prep
%autosetup

%build
%meson -Dman=enabled -Dselinux=enabled
%meson_build

%install
%meson_install

%files
%license COPYING
%doc README.md
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/bwrap
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_bwrap
%if (0%{?rhel} != 0 && 0%{?rhel} <= 7)
%attr(0755,root,root) %caps(cap_sys_admin,cap_net_admin,cap_sys_chroot,cap_setuid,cap_setgid=ep) %{_bindir}/bwrap
%else
%{_bindir}/bwrap
%endif
%{_mandir}/man1/bwrap.1*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.11.0-4
- Prepare for Oreon 11 (RP1)
