%global source0_hash none

Name:           mint-y-icons
Version:        1.9.1
Release:        2%{?dist}
Summary:        The Mint-Y icon theme

# Automatically converted from old format: CC-BY-SA - review is highly recommended.
License:        LicenseRef-Callaway-CC-BY-SA
URL:            https://github.com/linuxmint/%{name}
Source0:        %url/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  fdupes

Requires:       filesystem
Requires:       mint-x-icons
Requires:       gnome-icon-theme
Requires:       hicolor-icon-theme

%description
%{summary}.

%prep
%autosetup

%build

%install
%{__cp} -pr ${PWD}%{_prefix} %{buildroot}
%fdupes -s %{buildroot}

%transfiletriggerin -- %{_datadir}/icons/Mint-Y
for _dir in %{_datadir}/icons/Mint-Y*/ ; do
  %{_bindir}/gtk-update-icon-cache --force ${_dir} &>/dev/null || :
done

%transfiletriggerpostun -- %{_datadir}/icons/Mint-Y
for _dir in %{_datadir}/icons/Mint-Y*/ ; do
  %{_bindir}/gtk-update-icon-cache --force ${_dir} &>/dev/null || :
done

%files
%license debian/copyright
%doc debian/changelog
%doc README.md
%{_datadir}/icons/Mint-*/
%{_datadir}/folder-color-switcher/

%changelog
%autochangelog
