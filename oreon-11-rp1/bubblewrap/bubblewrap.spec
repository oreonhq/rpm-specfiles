Name:    bubblewrap
Version: 0.11.0
Release: 4%{?dist}
Summary: Core execution tool for unprivileged containers

License: LGPL-2.0-or-later
URL:     https://github.com/containers/bubblewrap/
Source0: https://github.com/containers/bubblewrap/releases/download/v%{version}/bubblewrap-%{version}.tar.xz
# oreon url source checksums begin
%global source0_sha256 988fd6b232dafa04b8b8198723efeaccdb3c6aa9c1c7936219d5791a8b7a8646
%global source0_file bubblewrap-0.11.0.tar.xz
# oreon url source checksums end

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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/bubblewrap-0.11.0.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "988fd6b232dafa04b8b8198723efeaccdb3c6aa9c1c7936219d5791a8b7a8646" || { echo "oreon: Source0 SHA256 mismatch for bubblewrap-0.11.0.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
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
