%global source0_hash a1a77db725455210fb77fe714d97578285c09eed02b5b1b0da3b08b1ea3ee1a1

Name: painless-password-rotation
Version: 0.3
Release: 8%{?dist}
Summary: Manages root password rotation with Hashicorp Vault
License: MIT
URL: https://github.com/cn137/painless-password-rotation
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch: noarch
BuildRequires: systemd-rpm-macros

%description
This package automates password rotation using HashiCorp Vault and a simple
Bash script. Scripts run in a systemd timer to dynamically update local
system passwords on a regular basis.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version}

%build
# Nothing to build

%install
mkdir -vp %{buildroot}%{_bindir}
mkdir -vp %{buildroot}%{_unitdir}
mkdir -vp %{buildroot}%{_sysconfdir}/sysconfig

install -pm 0755 rotate-linux-password %{buildroot}%{_bindir}/rotate-linux-password
install -pm 0644 systemd/rotate-password.service %{buildroot}%{_unitdir}/rotate-password.service
install -pm 0644 systemd/rotate-password.timer %{buildroot}%{_unitdir}/rotate-password.timer
install -pm 0600 vault-rotate %{buildroot}%{_sysconfdir}/sysconfig/vault-rotate
install -pm 0644 systemd/rotate-password@.service %{buildroot}%{_unitdir}/rotate-password@.service
install -Dpm 0644 docs/man/rotate-linux-password.1 %{buildroot}%{_mandir}/man1/rotate-linux-password.1

%post
%systemd_post rotate-password.service
%systemd_post rotate-password.timer

%preun
%systemd_preun rotate-password.service
%systemd_preun rotate-password.timer

%postun
%systemd_postun rotate-password.service
%systemd_postun_with_restart rotate-password.timer

%files
%license LICENSE
%{_mandir}/man1/rotate-linux-password.1*
%doc README.md
%config(noreplace) %{_sysconfdir}/sysconfig/vault-rotate
%{_bindir}/rotate-linux-password
%{_unitdir}/rotate-password.service
%{_unitdir}/rotate-password.timer
%{_unitdir}/rotate-password@.service

%changelog
%autochangelog
