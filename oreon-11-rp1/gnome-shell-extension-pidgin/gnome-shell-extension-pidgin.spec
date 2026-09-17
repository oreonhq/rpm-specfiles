%global source0_hash db9a4fafbebcafca9a197626dd343d25401c1b30e9027c1c806e009cc8bdd535

%global extdir     %{_datadir}/gnome-shell/extensions/pidgin@muffinmad
%global gschemadir %{_datadir}/glib-2.0/schemas
%global gitname    pidgin-im-gnome-shell-extension
%global giturl     https://github.com/muffinmad/%{gitname}

Name:		gnome-shell-extension-pidgin
Version:	47
Release:	5%{?dist}
Summary:	Make Pidgin IM conversations appear in the Gnome Shell message tray

License:	GPL-2.0-or-later
URL:		https://extensions.gnome.org/extension/782/pidgin-im-integration/
Source0:	%{giturl}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:	noarch

BuildRequires:	gettext

Requires:	gnome-shell-extension-common

%description
This package contains the necessary components to integrate pidgin with 
GNOME Shell.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gitname}-%{version}

# It works in 46 too, which is what rawhide has (2024-02-10)
sed -i 's|"45"|"45", "46"|g' metadata.json

%build
# Remove useless files.
%{_bindir}/find . -name '*.po' -print -delete
%{_bindir}/find . -name '*.pot' -print -delete

%install
# Create needed dirs.
%{__mkdir} -p %{buildroot}%{extdir} %{buildroot}%{gschemadir}

# Install everything to its proper location.
%{__cp} -pr . %{buildroot}%{extdir}
%{__cp} -pr ./locale %{buildroot}%{_datadir}
%{__cp} -pr ./schemas/*gschema.xml %{buildroot}%{gschemadir}

# Remove unneded files.
%{__rm} -fr %{buildroot}%{extdir}/{LICENSE,README*,locale,schemas}

# Create manifest for i18n.
%find_lang %{name} --all-name

# Fedora handles this using triggers.
%if 0%{?rhel} && 0%{?rhel} <= 7
%postun
if [ $1 -eq 0 ] ; then
        %{_bindir}/glib-compile-schemas %{gschemadir} &> /dev/null || :
fi

%posttrans
%{_bindir}/glib-compile-schemas %{gschemadir} &> /dev/null || :
%endif

%files -f %{name}.lang
%license LICENSE
%doc README.md
%{extdir}
%{gschemadir}/*gschema.xml

%changelog
%autochangelog
