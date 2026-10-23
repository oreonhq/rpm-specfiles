Name:           oreon-shell-theme
Version:        1
Release:        1%{?dist}
Summary:        Gnome Shell

License:        GPLv2+
URL:            https://oreonproject.org/os
Source0:        oreon-shell-theme.zip

BuildArch:      noarch

Requires:       dconf-editor
Requires:       dconf

%description
Themes


%prep
%autosetup -n oreon-shell-theme -p 1

%install
mkdir -p %{buildroot}/usr/share/themes/
cp -r %{_builddir}/oreon-shell-theme/oreon-shell-theme/. %{buildroot}/usr/share/themes/

%files
/usr/share/themes/OreonBlue-Dark
/usr/share/themes/OreonBlue-Light
/usr/share/themes/OreonGreen-Dark
/usr/share/themes/OreonGreen-Light
/usr/share/themes/OreonGrey-Dark
/usr/share/themes/OreonGrey-Light
/usr/share/themes/OreonOrange-Dark
/usr/share/themes/OreonOrange-Light
/usr/share/themes/OreonPurple-Dark
/usr/share/themes/OreonPurple-Light
/usr/share/themes/OreonRed-Dark
/usr/share/themes/OreonRed-Light

