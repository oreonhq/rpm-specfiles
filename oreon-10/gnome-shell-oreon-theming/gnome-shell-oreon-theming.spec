Name:           gnome-shell-oreon-theming
Version:        3
Release:        1%{?dist}
#Release:        5.%%{commit_date}git%%{commit_short}%%{?dist}
Summary:        Provides configuration for theming, etc.

License:        GPLv2+
Source0:        00-gnome-oreon-extensions.conf

BuildArch:      noarch

Requires:       dconf-editor
Requires:       dconf
Requires:	oreon-shell-theme

%description
Provides /etc/dconf/db/local.d/00-gnome-oreon-extensions.conf

%prep

# Cleanup crap.
mkdir -p %{buildroot}%{_sysconfdir}/dconf/db/local.d/
cp %{SOURCE0} %{buildroot}%{_sysconfdir}/dconf/db/local.d/

%posttrans
dconf update

%files
%{_sysconfdir}/dconf/db/local.d/00-gnome-oreon-extensions.conf
