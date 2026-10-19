%global source0_hash none
Name:           tremulous-data
Version:        1.2.0
Release:        1%{?dist}
Summary:        Data files for tremulous the FPS game
License:        LicenseRef-Callaway-CC-BY-SA
URL:            http://tremulous.net
Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}-copyright.txt
BuildArch:      noarch
# oreon:deps

# /oreon:deps
%description
Data files for tremulous the Quake 3 based FPS game.

%prep

%setup -q
install -p -m 644 %{SOURCE1} fedora-copyright.txt

# %build
# nothing to build data only

%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/tremulous/base
install -p -m 0644 base/*.pk3 $RPM_BUILD_ROOT%{_datadir}/tremulous/base/
install -p -m 0644 base/*.cfg $RPM_BUILD_ROOT%{_datadir}/tremulous/base/
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
