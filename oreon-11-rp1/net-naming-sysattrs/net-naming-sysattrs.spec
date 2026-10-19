%global source0_hash ba2e5f1280b3ecc182c4cb00ad464ffafd497b492fb2659f3fcd50cc478dbaae
%global dracutmoddir %{_prefix}/lib/dracut/modules.d
Name:           net-naming-sysattrs
Version:        263
Release:        1%{?dist}
Summary:        Mechanism to emulate older network device naming behavior
License:        MIT
URL:            https://gitlab.com/mschmidt2/%{name}
Source0:        https://gitlab.com/mschmidt2/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.gz
BuildArch:      noarch
Requires:       systemd-udev
Requires:       dracut
Obsoletes:      rhel-net-naming-sysattrs < 253
Provides:       rhel-net-naming-sysattrs = %{version}-%{release}
# oreon:deps
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(dracut)
BuildRequires:  pkgconfig(udev)
# /oreon:deps
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-v%{version}
%oreon_prep
%build

%check

make test
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 263-1
- Import
