%global source0_hash 175b997518073ea82c95dadea50a0f01ffa4ff292cbb84b5e64f82e7e6c94fc9

Name:           wsdd
Version:        0.8
Release:        6%{?dist}
Summary:        Web Services Dynamic Discovery host daemon
License:        MIT 
URL:            https://github.com/christgau/wsdd 
Source0:        https://github.com/christgau/wsdd/archive/refs/tags/v%{version}.tar.gz#/wsdd-%{version}.tar.gz

Patch:          Modify-systemd-service-for-Fedora.patch

BuildArch:      noarch
BuildRequires:  systemd


%description
wsdd implements a Web Service Discovery host daemon. This enables (Samba)
hosts, like your local NAS device, to be found by Web Service Discovery Clients
like Windows.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1


%install
install -pDm644 etc/firewalld/services/wsdd.xml %{buildroot}%{_usr}/lib/firewalld/services/wsdd.xml
install -pDm644 etc/firewalld/services/wsdd-http.xml %{buildroot}%{_usr}/lib/firewalld/services/wsdd-http.xml
install -pDm644 etc/systemd/wsdd.defaults %{buildroot}%{_sysconfdir}/sysconfig/wsdd
install -pDm644 etc/systemd/wsdd.service %{buildroot}%{_unitdir}/wsdd.service
install -pDm644 man/wsdd.8 %{buildroot}%{_mandir}/man8/wsdd.8
install -pDm755 src/wsdd.py %{buildroot}%{_bindir}/wsdd

# Create a sysusers.d config file
cat >wsdd.sysusers.conf <<EOF
u wsdd - '%{summary}' - -
EOF

install -m0644 -D wsdd.sysusers.conf %{buildroot}%{_sysusersdir}/wsdd.conf



%post
%systemd_post wsdd.service

%preun
%systemd_preun wsdd.service

%postun
%systemd_postun_with_restart wsdd.service

%files
%{_unitdir}/wsdd.service
%{_usr}/lib/firewalld/services/wsdd.xml
%{_usr}/lib/firewalld/services/wsdd-http.xml
%config(noreplace) %{_sysconfdir}/sysconfig/wsdd
%{_bindir}/wsdd
%{_mandir}/man8/wsdd.8*
%license LICENSE
%doc AUTHORS README.md
%{_sysusersdir}/wsdd.conf


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.8-6
- Prepare for Oreon 11 (RP1)
