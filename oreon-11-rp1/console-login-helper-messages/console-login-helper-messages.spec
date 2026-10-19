%global source0_hash 6edbeed6681a8c4a3a8b1909173be762449ba178544ac961eb98068c05df84ee
%global github_owner    coreos
%global github_project  console-login-helper-messages
Name:           console-login-helper-messages
Version:        0.23.1
Release:        1%{?dist}
Summary:        Combines motd, issue, profile features to show system information to the user before/on login
License:        BSD-3-Clause
URL:            https://github.com/%{github_owner}/%{github_project}
Source0:        https://github.com/%{github_owner}/%{name}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch
%{?systemd_requires}
Requires:       bash systemd
# oreon:deps
BuildRequires:  make
BuildRequires:  systemd
# /oreon:deps
%description
%{summary}.

%package motdgen
Summary:        Message of the day generator script showing system information
Requires:       console-login-helper-messages
Recommends:     openssh
Requires:       bash systemd
%if 0%{?fc29}
Requires:       setup
%else
Requires:       setup >= 2.12.7-1
%endif
Requires:       ((pam >= 1.3.1-15) if openssh)
%if 0%{?fc29}
Requires:       ((selinux-policy >= 3.14.2-50) if openssh)
%else
Requires:       ((selinux-policy >= 3.14.3-23) if openssh)
%endif
Requires:       util-linux >= 2.36-1
%description motdgen
%{summary}.

%package issuegen
Summary:        Issue generator scripts showing SSH keys and IP address
Requires:       console-login-helper-messages
Requires:       bash systemd setup
Requires:       (NetworkManager)
Requires:       /etc/issue.d
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%install
make install DESTDIR=%{buildroot}
rm %{buildroot}/%{_tmpfilesdir}/%{name}-motdgen.conf
%oreon_autofiles console-login-helper-messages-motdgen usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles console-login-helper-messages-issuegen usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles console-login-helper-messages-profile usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

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
%files -f %{oreon_filedir}/main.list
%files -n console-login-helper-messages-motdgen -f %{oreon_filedir}/console-login-helper-messages-motdgen.list
%files -n console-login-helper-messages-issuegen -f %{oreon_filedir}/console-login-helper-messages-issuegen.list
%files -n console-login-helper-messages-profile -f %{oreon_filedir}/console-login-helper-messages-profile.list

%changelog

%autochangelog
