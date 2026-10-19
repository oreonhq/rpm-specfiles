%global source0_hash 04e6126670600115304b5cad1e6d41f66fe0bf860ca5c3941ccbce2fc0c52679
%global gitdate 20160511
%global commit0 d3b9ad212f14b862e9473126062c5eaf25bd9f55
%global srcname wildfire
%global project xenlism
Name:           %{project}-%{srcname}
Version:        2018.05beta2
Release:        1%{?dist}
Summary:        Minimalist theme for your desktop
License:        GPL-3.0-or-later
URL:            https://%{project}.github.io/%{srcname}
Source0:        https://github.com/%{project}/%{srcname}/archive/%{commit0}.zip#/%{name}-%{commit0}.zip
BuildArch:      noarch
# oreon:deps
BuildRequires:  coreutils
# /oreon:deps
%description
Xenlism Wildfire is a desktop theme collection based on
vector graphics (svg,ai). Goals are minimalism and realism.

%package day
Summary:     Day theme of Xenlism Wildfire
Requires:    %{name} = %{version}-%{release}
%description day
%{summary}.

%package night
Summary:     Night theme of Xenlism Wildfire
Requires:    %{name} = %{version}-%{release}
%description night
%{summary}.

%package midnight
Summary:     Midnight theme of Xenlism Wildfire
Requires:    %{name} = %{version}-%{release}
%description midnight
%{summary}.

%package monday
Summary:     Monday theme of Xenlism Wildfire
Requires:    %{name} = %{version}-%{release}
%description monday
%{summary}.

%package tuesday
Summary:     Tuesday theme of Xenlism Wildfire
Requires:    %{name} = %{version}-%{release}
%description tuesday
%{summary}.

%package wednesday
Summary:     Wednesday theme of Xenlism Wildfire
Requires:    %{name} = %{version}-%{release}
%description wednesday
%{summary}.

%package thursday
Summary:     Thursday theme of Xenlism Wildfire
Requires:    %{name} = %{version}-%{release}
%description thursday
%{summary}.

%package friday
Summary:     Friday theme of Xenlism Wildfire
Requires:    %{name} = %{version}-%{release}
%description friday
%{summary}.

%package saturday
Summary:     Saturday theme of Xenlism Wildfire
Requires:    %{name} = %{version}-%{release}
%description saturday
%{summary}.

%package sunday
Summary:     Sunday theme of Xenlism Wildfire
Requires:    %{name} = %{version}-%{release}
%description sunday
%{summary}.

%package backgrounds
Summary:     Backgrounds of Xenlism Wildfire
%description backgrounds
%{summary}.

%prep

%setup -qn%{srcname}-%{commit0}
# W: hidden-file-or-dir, E: zero-length
find icons -name '.*' -print -delete
# W: spurious-executable-perm
#chmod -x Screenshot/*.png
# W: dangling-relative-symlink
rm icons/Xenlism-Wildfire/Mimes/text-x-lyx.svg

%build

%install
install -dm755 %{buildroot}%{_datadir}
cp -pr icons %{buildroot}%{_datadir}
find  %{buildroot}%{_datadir}/icons -type d -exec chmod 755 '{}' \;
find  %{buildroot}%{_datadir}/icons -type f -exec chmod 644 '{}' \;
install -dm755 %{buildroot}%{_datadir}/backgrounds/xenlism
cp -pr wallpapers/* %{buildroot}%{_datadir}/backgrounds/%{project}
find %{buildroot}%{_datadir}/backgrounds/%{project} -type d -exec chmod 755 '{}' \;
find %{buildroot}%{_datadir}/backgrounds/%{project} -type f -exec chmod 644 '{}' \;
install -dm755 %{buildroot}%{_datadir}/gnome-background-properties
cp -pr background-properties/* %{buildroot}%{_datadir}/gnome-background-properties
find %{buildroot}%{_datadir}/gnome-background-properties -type d -exec chmod 755 '{}' \;
find %{buildroot}%{_datadir}/gnome-background-properties -type f -exec chmod 644 '{}' \;
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

/bin/touch --no-create %{_datadir}/icons/Xenlism-Wildfire* &>/dev/null || :
%postun

if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/Xenlism-Wildfire* &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/Xenlism-Wildfire* &>/dev/null || :
fi
%posttrans

/usr/bin/gtk-update-icon-cache %{_datadir}/icons/Xenlism-Wildfire* &>/dev/null || :
%files -f %{oreon_filedir}/main.list
%files -n xenlism-wildfire-day -f %{oreon_filedir}/xenlism-wildfire-day.list
%files -n xenlism-wildfire-night -f %{oreon_filedir}/xenlism-wildfire-night.list
%files -n xenlism-wildfire-midnight -f %{oreon_filedir}/xenlism-wildfire-midnight.list
%files -n xenlism-wildfire-monday -f %{oreon_filedir}/xenlism-wildfire-monday.list
%files -n xenlism-wildfire-tuesday -f %{oreon_filedir}/xenlism-wildfire-tuesday.list
%files -n xenlism-wildfire-wednesday -f %{oreon_filedir}/xenlism-wildfire-wednesday.list
%files -n xenlism-wildfire-thursday -f %{oreon_filedir}/xenlism-wildfire-thursday.list
%files -n xenlism-wildfire-friday -f %{oreon_filedir}/xenlism-wildfire-friday.list
%files -n xenlism-wildfire-saturday -f %{oreon_filedir}/xenlism-wildfire-saturday.list
%files -n xenlism-wildfire-sunday -f %{oreon_filedir}/xenlism-wildfire-sunday.list
%files -n xenlism-wildfire-backgrounds -f %{oreon_filedir}/xenlism-wildfire-backgrounds.list

%changelog

%autochangelog
