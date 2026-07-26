%global source0_hash c00de34d88569299c1683e1ea0cca4f91fdc2d485244bae6cab5cce4d18b9671

%global forgeurl    https://github.com/numixproject/numix-icon-theme
%global tag         %{version}

%forgemeta

Name:		numix-icon-theme
Summary:	Numix Project icon theme
Version:	24.04.22
Release:	%autorelease
License:	GPL-3.0-or-later

URL:		%{forgeurl}
Source:     %{forgesource}

BuildArch:	noarch
Requires:	filesystem
Requires:	gnome-icon-theme
Requires:	hicolor-icon-theme

%description
Numix is the official icon theme from the Numix project.
It is heavily inspired by, and based upon parts of the Elementary,
Humanity and Gnome icon themes.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgesetup

%build
find -type f -executable -exec chmod -x {} \;

%install
install -d %{buildroot}%{_datadir}/icons

mkdir -p %{buildroot}%{_datadir}/doc/%{name}
cp -pr Numix %{buildroot}%{_datadir}/icons/Numix
cp -pr Numix-Light %{buildroot}%{_datadir}/icons/Numix-Light

%post
/bin/touch --no-create %{_datadir}/icons/Numix &>/dev/null || :
/bin/touch --no-create %{_datadir}/icons/Numix-Light &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/Numix &>/dev/null
    /bin/touch --no-create %{_datadir}/icons/Numix-Light &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/Numix &>/dev/null || :
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/Numix-Light &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/Numix &>/dev/null || :
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/Numix-Light &>/dev/null || :

%files
%license license
%doc readme.md
%{_datadir}/icons/Numix
%{_datadir}/icons/Numix-Light

%changelog
%autochangelog
