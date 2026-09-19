%global source0_hash none

Name:           nogravity-data
Version:        2.00
Release:        %autorelease
Summary:        Data files for No Gravity game
License:        GPL-2.0-or-later
URL:            https://www.realtech-vr.com/home/?page_id=948
Source0:        https://downloads.sourceforge.net/nogravity/rt-%{name}.zip
BuildArch:      noarch
# So that we get removed together with nogravity itself
Requires:       nogravity >= %{version}

%description
Data files (audio, maps, etc) for No Gravity.

%prep
%setup -q -c
sed -i 's/\r//g' GNU.TXT

%build
# nothing to build, data only

%install
install -D -p -m 0644 NOGRAVITY.RMX %{buildroot}%{_datadir}/nogravity/NOGRAVITY.RMX

%files
%license GNU.TXT
%{_datadir}/nogravity/

%changelog
%autochangelog
