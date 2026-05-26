%global dracutmoddir %{_prefix}/lib/dracut/modules.d

Name:           net-naming-sysattrs
Version:        263
Release:        1%{?dist}
Summary:        Mechanism to emulate older network device naming behavior

License:        MIT
URL:            https://gitlab.com/mschmidt2/%{name}
Source0:        https://gitlab.com/mschmidt2/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 ba2e5f1280b3ecc182c4cb00ad464ffafd497b492fb2659f3fcd50cc478dbaae
%global source0_file net-naming-sysattrs-v263.tar.gz
# oreon url source checksums end

BuildArch:      noarch
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(dracut)
BuildRequires:  pkgconfig(udev)
Requires:       systemd-udev
Requires:       dracut

# RHEL 9 had this stuff in the package "rhel-net-naming-sysattrs",
# versioned together with systemd, so rhel-net-naming-sysattrs-252-*
Obsoletes:      rhel-net-naming-sysattrs < 253
Provides:       rhel-net-naming-sysattrs = %{version}-%{release}

%description
This package provides hwdb and udev rules to filter the sysfs attributes used
by systemd-udev for network device naming.

Historically, the introduction of the "phys_port_name" attribute in newer
kernels caused interface names to change for certain drivers. While these names
can be manually reconfigured with systemd.link files or custom udev rules, this
package offers a streamlined mechanism to emulate the naming behavior of older
distribution releases (RHEL 9.0 and later).

The desired naming scheme can be specified on the kernel command line:
  net.naming-scheme=rhel-9.6
(Default: rhel-9.0)

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/net-naming-sysattrs-v263.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "ba2e5f1280b3ecc182c4cb00ad464ffafd497b492fb2659f3fcd50cc478dbaae" || { echo "oreon: Source0 SHA256 mismatch for net-naming-sysattrs-v263.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -n %{name}-v%{version}

%build
# nothing

%check
make test

%install
%make_install

%files
%license LICENSE
%doc README
%{_udevrulesdir}/70-net-naming-sysattrs.rules
%{_udevhwdbdir}/50-net-naming-sysattr-allowlist.hwdb
%dir %{dracutmoddir}/70net-naming-sysattrs
%{dracutmoddir}/70net-naming-sysattrs/module-setup.sh

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 263-1
- Import
