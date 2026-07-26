%global source0_hash e8fa1bacfc7708911f6d2966f34aae45e926648729077947fada4d8635a0b4a7

# spec file for package battray
#

Name:           battray
Version:        2.3
Release:        37%{?dist}
Summary:        Tool for displaying a laptop's battery status in the system traiy
License:        MIT
URL:            https://github.com/arp242/battray
Source0:        https://github.com/Carpetsmoker/battray/archive/version-%{version}/%{name}-version-%{version}.tar.bz2

BuildArch:      noarch
BuildRequires:  python3-setuptools
BuildRequires:  python3-devel
Requires:       python3
Requires:       python3-notify2

%description
Battray is a fairly simple tray icon to show a laptop’s battery status. It’s 
simple, easy, fairly environment-independent, and ‘just works’ without tons of
{Gnome,KDE,..} dependencies.

One can also configure it to play annoying sounds if your battery is getting 
low, dim the screen when you switch from AC to battery, etc.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-version-%{version}

%build
%py3_build

%check

%install
%py3_install

%files
%{python3_sitelib}/*
%{_bindir}/%{name}
%{_datadir}/%{name}
%doc README.markdown
%license LICENSE

%changelog
%autochangelog
