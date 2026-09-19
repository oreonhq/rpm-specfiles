%global source0_hash none

Name: floppy-support          
Version:        1.0.0
Release:        33%{?dist}
Summary:        Load floppy driver at boot time

License:        MIT
# The package is built just using this specfile.
#URL:            
#Source0:        

Requires: kmod(floppy.ko)
Requires: systemd
Requires(post): module-init-tools

BuildArch:      noarch
# The floppy module does not appear to be built for arm (or the kernel 
# auto provides feature isn't turned on there.
ExcludeArch:    %{arm} aarch64 s390x

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
# Note that the modules-load.d man page states that packages should install
# files in /usr/lib/modules-load.d and that /etc/modules-load.d is
# reserved for local administration.
mkdir -p $RPM_BUILD_ROOT%{_libdir}/../lib/modules-load.d
echo floppy > $RPM_BUILD_ROOT%{_libdir}/../lib/modules-load.d/floppy.conf

%files
%{_libdir}/../lib/modules-load.d/floppy.conf

%post
/sbin/modprobe floppy

%changelog
%autochangelog
