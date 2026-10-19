%global source0_hash none
Name: floppy-support          
Version:        1.0.0
Release:        1%{?dist}
Summary:        Load floppy driver at boot time
License:        MIT
Requires: kmod(floppy.ko)
Requires: systemd
Requires(post): module-init-tools
BuildArch:      noarch
ExcludeArch:    %{arm} aarch64 s390x
# oreon:deps

# /oreon:deps
%description
By default the floppy driver is not loaded at boot time. Installing this
package will load the floppy driver as part of the install and will set
things so that it will be loaded during future boots. While the floppy
driver is currently in kernel-modules, it may move to kernel-modules-extra
in the future, and if so this package will bring that in.

%prep

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_libdir}/../lib/modules-load.d
echo floppy > $RPM_BUILD_ROOT%{_libdir}/../lib/modules-load.d/floppy.conf
%oreon_autofiles main

%post

/sbin/modprobe floppy
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
