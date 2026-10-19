%global source0_hash eb47820db9deaa356b2417ac4ead14e6446b6e38e32f1a2939a1bf97c2049277
Name:           amazon-ec2-utils
Version:        2.3.0
Release:        1%{?dist}
Summary:        Utilities and settings for Amazon EC2
License:        MIT AND CC-BY-SA-4.0
URL:            https://github.com/amazonlinux/%{name}/
Source0:        https://github.com/amazonlinux/%{name}//archive/refs/tags/v%{version}.tar.gz
Patch0:         remove-EBS-udev-rules.patch
BuildArch:      noarch
Requires:       curl
Requires:       python3
Provides:       ec2-metadata = %{version}-%{release}
Obsoletes:      ec2-metadata <= 0.1.3
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
Contains a set of utilities and settings for Linux deployments in EC2.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%install
install -d -m 0755                              %{buildroot}%{_udevrulesdir}/
install -p -m 0644 51-ec2-hvm-devices.rules     %{buildroot}%{_udevrulesdir}/
install -p -m 0644 51-ec2-xen-vbd-devices.rules %{buildroot}%{_udevrulesdir}/
install -p -m 0644 53-ec2-read-ahead-kb.rules   %{buildroot}%{_udevrulesdir}/
install -p -m 0644 70-ec2-nvme-devices.rules    %{buildroot}%{_udevrulesdir}/
install -d -m 0755                              %{buildroot}%{_sysconfdir}/udev/rules.d/
install -p -m 0644 60-cdrom_id.rules            %{buildroot}%{_sysconfdir}/udev/rules.d/
install -d -m 0755                              %{buildroot}%{_bindir}
install -p -m 0755 ec2-metadata                 %{buildroot}%{_bindir}
install -d -m 0755                              %{buildroot}%{_sbindir}
install -p -m 0755 ec2udev-vbd                  %{buildroot}%{_sbindir}
install -p -m 0755 ebsnvme-id                   %{buildroot}%{_sbindir}
install -p -m 0755 ec2nvme-nsid                 %{buildroot}%{_sbindir}
install -d -m 0755                              %{buildroot}%{_mandir}/man8/
install -p -m 0644 doc/ebsnvme-id.8             %{buildroot}%{_mandir}/man8/
install -p -m 0644 doc/ec2-metadata.8           %{buildroot}%{_mandir}/man8/
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
