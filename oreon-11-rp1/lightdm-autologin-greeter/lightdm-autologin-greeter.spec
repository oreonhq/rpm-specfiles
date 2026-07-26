%global source0_hash c0b0be8d5d59cd44f7f4e52ab1bd27c985a8263bc6b2bcd1510e9a100a113214

Name:           lightdm-autologin-greeter
Version:        1.0
Release:        24%{?dist}
Summary:        Autologin greeter using LightDM

License:        MIT
URL:            https://github.com/spanezz/lightdm-autologin-greeter
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

Source1:        %{name}.README.distro

%if 0%{?fedora} || 0%{?rhel} >= 8
BuildRequires:  python3-devel
Requires:       python3-gobject
%else
BuildRequires:  python2-devel
Requires:       pygobject3
%endif
Requires:       lightdm-gobject

# LightDM is required for this to be useful
Requires:       lightdm

# All LightDM greeters provide this
Provides:       lightdm-greeter = 1.2

BuildArch:      noarch

%description
%{name} is a minimal greeter for LightDM that has
the same autologin behavior as nodm, but being based on LightDM,
it stays on top of modern display manager requirements.

The difference between LightDM's built-in autologin and this greeter,
is the behavior in case of 0-seconds autologin delay. When LightDM
automatically logs in with no delay, upon logout it will show the
login window again. The intent is that if the default user logged out,
they probably intend to log in again as a different user.

In the case of managing a kiosk-like setup, if the X session quits, then
the desired behavior is to just start it again.

LightDM with an autologin timeout of 1 or more seconds would work,
but one sees the login dialog window appear and disappear
on-screen at each system startup.

With this greeter, the X session starts right away, and is restarted
if it quits, without any flicker of a login dialog box.

If one is not setting up a kiosk-like setup, it's very likely that the
default autologin behavior of LightDM is the way to go, and that this
greeter is not needed.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
# Install Source1 into source tree
cp %{S:1} README.distro

%build
# Nothing to build

%install
mkdir -p %{buildroot}%{_prefix}

cp -a bin %{buildroot}%{_prefix}
cp -a share %{buildroot}%{_prefix}

%if 0%{?fedora} || 0%{?rhel} >= 8
sed -i "s:#!/usr/bin/python:#!%{__python3}:" %{buildroot}%{_bindir}/%{name}
%else
sed -i "s:#!/usr/bin/python:#!%{__python2}:" %{buildroot}%{_bindir}/%{name}
%endif

%files
%license LICENSE
%doc README.md README.distro
%{_bindir}/%{name}
%{_datadir}/xgreeters/%{name}.desktop
%{_datadir}/lightdm/lightdm.conf.d/60-%{name}.conf

%changelog
%autochangelog
