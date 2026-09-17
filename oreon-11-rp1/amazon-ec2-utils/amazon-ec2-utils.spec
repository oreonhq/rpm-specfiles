%global source0_hash 4fd0c06dfa6959d6e0b197ce4f5eddb9f07822d8d9810d1ae7e886d7fd055df6

Name:           amazon-ec2-utils
Version:        2.2.0
Release:        %autorelease
Summary:        Utilities and settings for Amazon EC2
License:        MIT AND CC-BY-SA-4.0
URL:            https://github.com/amazonlinux/%{name}/
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

# Skip the EBS udev rules as they create invalid symlinks.
Patch0:         remove-EBS-udev-rules.patch

BuildArch:      noarch

Requires:       curl
Requires:       python3

BuildRequires:  python3-devel
BuildRequires:  systemd-rpm-macros

# ec2-metadata was once provided directly from a page on the AWS website,
# but an updated and maintained version is now offered in this package. ✨
Provides:       ec2-metadata = %{version}-%{release}
Obsoletes:      ec2-metadata <= 0.1.3

%description
Contains a set of utilities and settings for Linux deployments in EC2.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}

%build
# Nothing to build for this package.

%install
# Install regular udev rules for EC2 instances.
install -d -m 0755                              %{buildroot}%{_udevrulesdir}/
install -p -m 0644 51-ec2-hvm-devices.rules     %{buildroot}%{_udevrulesdir}/
install -p -m 0644 51-ec2-xen-vbd-devices.rules %{buildroot}%{_udevrulesdir}/
install -p -m 0644 53-ec2-read-ahead-kb.rules   %{buildroot}%{_udevrulesdir}/
install -p -m 0644 70-ec2-nvme-devices.rules    %{buildroot}%{_udevrulesdir}/

# The rules for cdrom are meant to override existing systemd udev rules.
install -d -m 0755                              %{buildroot}%{_sysconfdir}/udev/rules.d/
install -p -m 0644 60-cdrom_id.rules            %{buildroot}%{_sysconfdir}/udev/rules.d/

# Some executables are meant for all users.
install -d -m 0755                              %{buildroot}%{_bindir}
install -p -m 0755 ec2-metadata                 %{buildroot}%{_bindir}

# Other executables are meant only for root.
install -d -m 0755                              %{buildroot}%{_sbindir}
install -p -m 0755 ec2udev-vbd                  %{buildroot}%{_sbindir}
install -p -m 0755 ebsnvme-id                   %{buildroot}%{_sbindir}
install -p -m 0755 ec2nvme-nsid                 %{buildroot}%{_sbindir}

# 📚 Documentation
install -d -m 0755                              %{buildroot}%{_mandir}/man8/
install -p -m 0644 doc/ebsnvme-id.8             %{buildroot}%{_mandir}/man8/
install -p -m 0644 doc/ec2-metadata.8           %{buildroot}%{_mandir}/man8/

%files
%license LICENSE
%doc CODE_OF_CONDUCT.md CONTRIBUTING.md NOTICE README.md
%{_bindir}/ec2-metadata
%{_sbindir}/ebsnvme-id
%{_sbindir}/ec2nvme-nsid
%{_sbindir}/ec2udev-vbd
%{_mandir}/man8/ebsnvme-id.8*
%{_mandir}/man8/ec2-metadata.8*
%{_udevrulesdir}/51-ec2-hvm-devices.rules
%{_udevrulesdir}/51-ec2-xen-vbd-devices.rules
%{_udevrulesdir}/53-ec2-read-ahead-kb.rules
%{_udevrulesdir}/70-ec2-nvme-devices.rules
%{_sysconfdir}/udev/rules.d//60-cdrom_id.rules

%changelog
%autochangelog
