%global source0_hash 7c7b45481f600e133964c5fe70efa85f3a12ab158c05623a23b78fc3b3ede131
Name:           mint-y-icons
Version:        1.9.4
Release:        1%{?dist}
Summary:        The Mint-Y icon theme
License:        LicenseRef-Callaway-CC-BY-SA
URL:            https://github.com/linuxmint/%{name}
Source0:        https://github.com/linuxmint/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       filesystem
Requires:       mint-x-icons
Requires:       gnome-icon-theme
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  fdupes
# /oreon:deps
%description
%{summary}.

%prep
%oreon_prep
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
