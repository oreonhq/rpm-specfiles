%global source0_hash 6ff5fd8c061f000bcf89b7afb74050a3d99d9cc02bf44de24a12c9dbed89667a

%global github_owner    coreos
%global github_project  console-login-helper-messages

Name:           console-login-helper-messages
Version:        0.21.3
Release:        13%{?dist}
Summary:        Combines motd, issue, profile features to show system information to the user before/on login
License:        BSD-3-Clause
URL:            https://github.com/%{github_owner}/%{github_project}
Source0:        https://github.com/coreos/console-login-helper-messages/archive/v0.21.3.tar.gz

BuildArch:      noarch
BuildRequires:  systemd make
%{?systemd_requires}
Requires:       bash systemd

%description
%{summary}.

%package motdgen
Summary:        Message of the day generator script showing system information
Requires:       console-login-helper-messages
# sshd reads /run/motd.d, where the generated MOTD message is written.
Recommends:     openssh
# bash: bash scripts are included in this package
# systemd: systemd service units, and querying for failed units
# (the above applies to the issuegen and profile subpackages too)
Requires:       bash systemd
# setup: filesystem paths need setting up.
#   * https://pagure.io/setup/pull-request/14
#   * https://pagure.io/setup/pull-request/15
#   * https://pagure.io/setup/pull-request/16
# Make exception for fc29 - soft requires as we will create /run/motd.d
# ourselves if it doesn't already exist.
%if 0%{?fc29}
Requires:       setup
%else
Requires:       setup >= 2.12.7-1
%endif
# pam: to display motds in /run/motd.d.
#   * https://github.com/linux-pam/linux-pam/issues/47
#   * https://github.com/linux-pam/linux-pam/pull/69
#   * https://github.com/linux-pam/linux-pam/pull/76
Requires:       ((pam >= 1.3.1-15) if openssh)
# selinux-policy: to apply pam_var_run_t contexts:
#   * https://github.com/fedora-selinux/selinux-policy/pull/244
# Make exception for fc29, as PAM will create the tmpfiles. (In Fedora 30 and
# above, setup is responsible for this).
%if 0%{?fc29}
Requires:       ((selinux-policy >= 3.14.2-50) if openssh)
%else
Requires:       ((selinux-policy >= 3.14.3-23) if openssh)
%endif
# Needed to display MOTDs in `/run/motd.d` before upon login through 
# the serial console.
Requires:       util-linux >= 2.36-1

%description motdgen
%{summary}.

%package issuegen
Summary:        Issue generator scripts showing SSH keys and IP address
Requires:       console-login-helper-messages
Requires:       bash systemd setup
# NetworkManager: for displaying IP info using NetworkManager dispatcher script
Requires:       (NetworkManager)
Requires:       /etc/issue.d
# Needed to display issues in /etc/issue.d before login through the serial console.
Requires:       util-linux >= 2.36-1

%description issuegen
%{summary}.

%package profile
Summary:        Profile script showing systemd failed units
Requires:       console-login-helper-messages
Requires:       bash systemd setup

%description profile
%{summary}.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1

%build

%install
make install DESTDIR=%{buildroot}
# /run/motd.d is now provided by the setup package on Fedora
rm %{buildroot}/%{_tmpfilesdir}/%{name}-motdgen.conf

%post issuegen
%systemd_post %{name}-gensnippet-ssh-keys.service

%preun issuegen
%systemd_preun %{name}-gensnippet-ssh-keys.service

%postun issuegen
%systemd_postun_with_restart %{name}-gensnippet-ssh-keys.service

%post motdgen
%systemd_post %{name}-gensnippet-os-release.service

%preun motdgen
%systemd_preun %{name}-gensnippet-os-release.service

%postun motdgen
%systemd_postun_with_restart %{name}-gensnippet-os-release.service

# TODO: %%check

%files
%doc README.md
%doc doc/manual.md
%license LICENSE
%dir %{_libexecdir}/%{name}
%dir %{_prefix}/lib/%{name}
%dir %{_prefix}/share/%{name}
%{_prefix}/lib/%{name}/libutil.sh
%{_tmpfilesdir}/%{name}.conf

%files issuegen
%{_unitdir}/%{name}-gensnippet-ssh-keys.service
%{_sysconfdir}/NetworkManager/dispatcher.d/90-%{name}-gensnippet_if
%{_prefix}/lib/%{name}/issue.defs
%{_tmpfilesdir}/%{name}-issuegen.conf
%{_libexecdir}/%{name}/gensnippet_ssh_keys
%{_libexecdir}/%{name}/gensnippet_if
%{_libexecdir}/%{name}/gensnippet_if_udev

%files motdgen
%{_unitdir}/%{name}-gensnippet-os-release.service
%{_prefix}/lib/%{name}/motd.defs
%{_libexecdir}/%{name}/gensnippet_os_release

%files profile
%{_prefix}/share/%{name}/profile.sh
%{_tmpfilesdir}/%{name}-profile.conf
%ghost %{_sysconfdir}/profile.d/%{name}-profile.sh

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.21.3-13
- Prepare for Oreon 11 (RP1)
