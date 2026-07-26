%global source0_hash none

Name:           opengl-games-utils
Version:        0.2
Release:        31%{?dist}
Summary:        Utilities to check proper 3d support before launching 3d games
License:        LicenseRef-Fedora-Public-Domain
URL:            http://fedoraproject.org/wiki/SIGs/Games
Source0:        opengl-game-wrapper.sh
Source1:        opengl-game-functions.sh
Source2:        README
BuildArch:      noarch
Requires:       zenity glx-utils

%description
This package contains various shell scripts which are intented for use by
3D games packages. These shell scripts can be used to check if direct rendering
is available before launching an OpenGL game. This package is intended for use
by other packages and is not intended for direct end user use!

%prep
%setup -c -T
cp %{SOURCE2} .

%build
# nothing to build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
install -p -m 755 %{SOURCE0} $RPM_BUILD_ROOT%{_bindir}
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/%{name}

if [ "%{_prefix}" != "/usr" ]; then
  sed -i "s/\/usr/\%{_prefix}/g" $RPM_BUILD_ROOT%{_bindir}/opengl-game-wrapper.sh
fi

%files
%doc README
%{_bindir}/opengl-game-wrapper.sh
%{_datadir}/%{name}

%changelog
%autochangelog
