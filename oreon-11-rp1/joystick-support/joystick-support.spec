%global source0_hash none

Name: joystick-support          
Version:        1.0.0
Release:        37%{?dist}
Summary:        Load joystick / game pad drivers at boot time

License:        MIT
# The package is built just using this specfile.
#URL:            
#Source0:        

Requires:       kmod(joydev.ko)
Requires:       kmod(analog.ko)
Requires:       systemd

BuildArch:      noarch

%description
By default the joystick and game pad drivers are not loaded at boot time. Nor
are they installed by default. Installing this package will load the main
joystick and game pad drivers as part of the install, will bring in
kernel-modules-extra if it is needed (which it currently is), and will set 
things so that they will be loaded during future boots.

%prep

%build

%install
# Note that the modules-load.d man page states that packages should install
# files in /usr/lib/modules-load.d and that /etc/modules-load.d is
# reserved for local administration.
mkdir -p $RPM_BUILD_ROOT%{_libdir}/../lib/modules-load.d
echo -e "joydev\nanalog" > $RPM_BUILD_ROOT%{_libdir}/../lib/modules-load.d/joystick.conf

%files
%{_libdir}/../lib/modules-load.d/joystick.conf

%changelog
%autochangelog
