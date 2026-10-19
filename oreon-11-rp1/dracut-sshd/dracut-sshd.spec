%global source0_hash 077579ea41f9f315d389f2083523c6ddf73a8259df46ca5883f039d42cc0cce0
Name:           dracut-sshd
Version:        0.7.1
Release:        1%{?dist}
Summary:        OpenSSH initramfs dracut integration
License:        GPL-3.0-or-later
URL:            https://github.com/gsauthof/%{name}
Source0:        https://github.com/gsauthof/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       dracut
Requires:       dracut-network
Requires:       openssh-server
# oreon:deps

# /oreon:deps
%description
dracut-sshd provides SSH access to initramfs early user space.

It allows for remote unlocking of a fully encrypted root filesystem and remote
access to the Dracut emergency shell (i.e. early userspace).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%install
install -p -d       %{buildroot}%{_prefix}/lib/dracut/modules.d/46sshd
install -p -m644 -t %{buildroot}%{_prefix}/lib/dracut/modules.d/46sshd 46sshd/{motd,profile,sshd_config,sshd.service}
install -p -t       %{buildroot}%{_prefix}/lib/dracut/modules.d/46sshd 46sshd/module-setup.sh
mkdir -p %{buildroot}%{_sysconfdir}/dracut-sshd
touch    %{buildroot}%{_sysconfdir}/dracut-sshd/sshd_config
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
