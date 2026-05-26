# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 989682ed7b250a2c7a8127e362ffc5d29f5c370127abe405be09c73216da2b97
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

# RHEL 8 compatibility
%{!?version_no_tilde: %define version_no_tilde %{shrink:%(echo '%{version}' | tr '~' '-')}}

%global nmlibdir %{_prefix}/lib/NetworkManager

Name:           nvme-cli
Version:        2.16
Release:        2%{?dist}
Summary:        NVMe management command line interface

License:        GPL-2.0-only
URL:            https://github.com/linux-nvme/nvme-cli
Source0:        https://github.com/linux-nvme/nvme-cli/archive/v2.16/nvme-cli-2.16.tar.gz
Source1:        99-nvme-nbft-connect.sh
Source2:        99-nvme-nbft-no-ignore-carrier.conf

BuildRequires:  meson >= 0.53
BuildRequires:  gcc gcc-c++
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  zlib-devel
BuildRequires:  openssl-devel
%if (0%{?rhel} == 0) || (0%{?rhel} > 9)
BuildRequires:  kernel-headers
%endif

BuildRequires:  libnvme-devel >= 1.16.1
BuildRequires:  json-c-devel >= 0.14

BuildRequires:  asciidoc
BuildRequires:  xmlto

Requires:       util-linux


%description
nvme-cli provides NVM-Express user space tooling for Linux.

%prep
%oreon_verify_sources
%autosetup -p1 -n %{name}-%{version_no_tilde}


%build
%meson -Dudevrulesdir=%{_udevrulesdir} -Dsystemddir=%{_unitdir} -Dpdc-enabled=false -Ddocs=all -Ddocs-build=true -Dhtmldir=%{_pkgdocdir}
%meson_build


%install
%meson_install
%{__install} -pm 644 README.md %{buildroot}%{_pkgdocdir}
mkdir -p $RPM_BUILD_ROOT%{nmlibdir}/dispatcher.d
mkdir -p $RPM_BUILD_ROOT%{nmlibdir}/conf.d
%{__install} -pm 755 %{SOURCE1} $RPM_BUILD_ROOT%{nmlibdir}/dispatcher.d/
%{__install} -pm 644 %{SOURCE2} $RPM_BUILD_ROOT%{nmlibdir}/conf.d/

# hostid and hostnqn are supposed to be unique per machine.  We obviously
# can't package them.
# nvme-stas ships the stas-config@.service that will take care
# of generating these files if missing. See rhbz 2065886#c19
rm -f %{buildroot}%{_sysconfdir}/nvme/hostid
rm -f %{buildroot}%{_sysconfdir}/nvme/hostnqn

# Do not install the dracut rule yet.  See rhbz 1742764
rm -f %{buildroot}/usr/lib/dracut/dracut.conf.d/70-nvmf-autoconnect.conf

# Move html docs into the right place
mv %{buildroot}%{_pkgdocdir}/nvme %{buildroot}%{_pkgdocdir}/html
rm -rf %{buildroot}%{_pkgdocdir}/nvme


%post
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Scriptlets/#_systemd
%systemd_post nvmefc-boot-connections.service
%systemd_post nvmf-autoconnect.service
%systemd_post nvmf-connect@.service
%systemd_post nvmf-connect-nbft.service
if [ -S /run/udev/control ]; then
    udevadm control --reload
    udevadm trigger
fi

%preun
%systemd_preun nvmefc-boot-connections.service
%systemd_preun nvmf-autoconnect.service
%systemd_preun nvmf-connect@.service
%systemd_preun nvmf-connect-nbft.service

%postun
%systemd_postun nvmefc-boot-connections.service
%systemd_postun nvmf-autoconnect.service
%systemd_postun nvmf-connect@.service
%systemd_postun nvmf-connect-nbft.service


%files
%license LICENSE
%doc %{_pkgdocdir}
%{_sbindir}/nvme
%{_mandir}/man1/nvme*.gz
%{_datadir}/bash-completion/completions/nvme
%{_datadir}/zsh/site-functions/_nvme
%dir %{_sysconfdir}/nvme
%config(noreplace) %{_sysconfdir}/nvme/discovery.conf
%{_unitdir}/nvmefc-boot-connections.service
%{_unitdir}/nvmf-autoconnect.service
%{_unitdir}/nvmf-connect.target
%{_unitdir}/nvmf-connect@.service
%{_unitdir}/nvmf-connect-nbft.service
%{_udevrulesdir}/65-persistent-net-nbft.rules
%{_udevrulesdir}/70-nvmf-autoconnect.rules
%{_udevrulesdir}/70-nvmf-keys.rules
%{_udevrulesdir}/71-nvmf-netapp.rules
%{_udevrulesdir}/71-nvmf-vastdata.rules
%{_udevrulesdir}/71-nvmf-hpe.rules
# Do not install the dracut rule yet.  See rhbz 1742764
# /usr/lib/dracut/dracut.conf.d/70-nvmf-autoconnect.conf
%{nmlibdir}/dispatcher.d/99-nvme-nbft-connect.sh
%{nmlibdir}/conf.d/99-nvme-nbft-no-ignore-carrier.conf


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.16-2
- Prepare for Oreon 11 (RP1)
