%global source0_hash dd1503f1b0dd1a3b5e03e80e9c3da93d856bf38c39c31fc63cdb9ac0b48eec31

%global forgeurl    https://github.com/numixproject/numix-icon-theme-circle
%global tag         %{version}

%forgemeta

Name:		numix-icon-theme-circle
Summary:	Numix Project circle icon theme
Version:	24.07.19
Release:	%autorelease
License:	GPL-3.0-or-later

URL:		%{forgeurl}
Source:     %{forgesource}

BuildArch:	noarch
Requires:	filesystem
Requires:	numix-icon-theme

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
cp -pr Numix-Circle %{buildroot}%{_datadir}/icons/Numix-Circle
cp -pr Numix-Circle-Light %{buildroot}%{_datadir}/icons/Numix-Circle-Light

%post
/bin/touch --no-create %{_datadir}/icons/Numix-Circle &>/dev/null || :
/bin/touch --no-create %{_datadir}/icons/Numix-Circle-Light &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/Numix-Circle &>/dev/null
    /bin/touch --no-create %{_datadir}/icons/Numix-Circle-Light &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/Numix-Circle &>/dev/null || :
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/Numix-Circle-Light &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/Numix-Circle &>/dev/null || :
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/Numix-Circle-Light &>/dev/null || :

%files
%license LICENSE
%doc README.md
%{_datadir}/icons/Numix-Circle
%{_datadir}/icons/Numix-Circle-Light

%changelog
%autochangelog
