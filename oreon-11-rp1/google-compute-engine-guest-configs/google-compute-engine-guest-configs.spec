%global source0_hash d5ee32460148eacf15f0656bba826de5fe93332dd9febed3c30ca8f11c779ccd
%global         srcname     guest-configs
%global         dracutlibdir %{_prefix}/lib/dracut
Name:           google-compute-engine-guest-configs
Version:        20260916.00
Release:        1%{?dist}
Summary:        Google Compute Engine guest environment tools
License:        Apache-2.0
URL:            https://github.com/GoogleCloudPlatform/%{srcname}
Source0:        https://github.com/GoogleCloudPlatform/%{srcname}/archive/refs/tags/%{version}.tar.gz
ExcludeArch:    %{ix86}
BuildArch:      noarch
Requires:       dracut
Obsoletes:      google-compute-engine-tools < 2.8.12-11
Provides:       google-compute-engine-tools = 2.8.12-11
Provides:       google-compute-engine = %{version}-%{release}
Requires:       %name-rsyslog = %version-%release
Requires:       %name-udev = %version-%release
# oreon:deps
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
This package contains scripts, configuration, and init files for features
specific to the Google Compute Engine cloud environment.

%package rsyslog
Summary:        rsyslog configuration for %{name}
Requires:       rsyslog
%description rsyslog
The %{name}-udev package contains
rsyslog configuration which are specific to the Google Cloud Platform.

%package udev
Summary:        udev rules for %{name}
Requires:       nvme-cli
Requires:       coreutils
%description udev
The %{name}-udev package contains udev rules
which are specific to the Google Cloud Platform.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

# Remove APT configs (for Debian and Ubuntu).
rm -rf src/etc/apt
# Remove script for EL6.
rm -f  src/sbin/google-dhclient-script

# Move dracut and modprobe.d from /etc to /usr/lib to allow
# user to put modifications in /etc that will be retained
# after update.
# https://bugzilla.redhat.com/show_bug.cgi?id=1925323
mkdir -p src/usr/lib/dracut
mv src/etc/dracut.conf.d src/usr/lib/dracut
mv src/etc/modprobe.d src/usr/lib

%build

%install
cp -vpR                     src/{etc,usr}                   %{buildroot}
install -m 0755 -vdp        %{buildroot}%{_udevrulesdir}
cp -vp                      src/lib/udev/rules.d/*          %{buildroot}%{_udevrulesdir}
cp -vp                      src/lib/udev/google_nvme_id     %{buildroot}%{_udevrulesdir}/../
install -m 0755 -vdp %{buildroot}%{dracutlibdir}/modules.d/30gcp-udev-rules
cp -vp  src/lib/dracut/modules.d/30gcp-udev-rules/module-setup.sh %{buildroot}%{dracutlibdir}/modules.d/30gcp-udev-rules/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n google-compute-engine-guest-configs-rsyslog -f %{oreon_filedir}/google-compute-engine-guest-configs-rsyslog.list
%files -n google-compute-engine-guest-configs-udev -f %{oreon_filedir}/google-compute-engine-guest-configs-udev.list

%changelog

%autochangelog
