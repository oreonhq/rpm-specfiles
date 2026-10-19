%global source0_hash none
Name: joystick-support          
Version:        1.0.0
Release:        1%{?dist}
Summary:        Load joystick / game pad drivers at boot time
License:        MIT
Requires:       kmod(joydev.ko)
Requires:       kmod(analog.ko)
Requires:       systemd
BuildArch:      noarch
# oreon:deps

# /oreon:deps
%description
By default the joystick and game pad drivers are not loaded at boot time. Nor
are they installed by default. Installing this package will load the main
joystick and game pad drivers as part of the install, will bring in
kernel-modules-extra if it is needed (which it currently is), and will set 
things so that they will be loaded during future boots.

%prep

%build

%install
mkdir -p $RPM_BUILD_ROOT%{_libdir}/../lib/modules-load.d
echo -e "joydev\nanalog" > $RPM_BUILD_ROOT%{_libdir}/../lib/modules-load.d/joystick.conf
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
