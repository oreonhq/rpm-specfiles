## START: Set by rpmautospec
## (rpmautospec version 0.7.3)
## RPMAUTOSPEC: autorelease, autochangelog
%define autorelease(e:s:pb:n) %{?-p:0.}%{lua:
    release_number = 1;
    base_release_number = tonumber(rpm.expand("%{?-b*}%{!?-b:1}"));
    print(release_number + base_release_number - 1);
}%{?-e:.%{-e*}}%{?-s:.%{-s*}}%{!?-n:%{?dist}}
## END: Set by rpmautospec

%global extension   blur-my-shell
%global uuid        %{extension}@aunetx
%global extdir      %{_datadir}/gnome-shell/extensions/blur-my-shell@aunetx
%global gschemadir  %{_datadir}/glib-2.0/schemas

Name:           gnome-shell-extension-%{extension}-oreon
Version:        72
Release:        %autorelease
Summary:        Adds a blur look to different parts of the GNOME Shell
License:        GPL-3.0-or-later
URL:            https://github.com/aunetx/blur-my-shell
BuildArch:      noarch

Source:         %{url}/archive/v%{version}/%{extension}-%{version}.tar.gz
# https://github.com/aunetx/blur-my-shell/pull/626
# Patch:          0001-Use-meson-build-system.patch
# https://github.com/aunetx/blur-my-shell/commit/b39c53630ef16384dfb567894bffd50afd76d469
# Patch:          0002-Fix-incompatibility-with-just-perfection.patch

BuildRequires:  gettext
BuildRequires:  glib2
BuildRequires:  gnome-shell
BuildRequires:  unzip
Requires:       gnome-shell >= 46
Provides:       %{extension} = %{version}-%{release}


%description
Adds a blur look to different parts of the GNOME Shell, including the top
panel, dash and overview.


%prep
%autosetup -n %{extension}-%{version} -p 1


%build
%make_build


%install
mkdir -p %{buildroot}%{extdir}
unzip -q %{_builddir}/%{extension}-%{version}/build/%{uuid}.shell-extension.zip -d %{buildroot}%{extdir}

# Cleanup crap.
mkdir -p %{buildroot}%{gschemadir}
cp %{buildroot}%{extdir}/schemas/*gschema.xml %{buildroot}%{gschemadir}/
%{__rm} -fr %{buildroot}%{extdir}/{COPYING*,README*,schemas}

# Fedora handles this using triggers.
%postun
if [ $1 -eq 0 ] ; then
  %{_bindir}/glib-compile-schemas %{gschemadir} &> /dev/null || :
fi

%posttrans
%{_bindir}/glib-compile-schemas %{gschemadir} &> /dev/null || :



%files
%license LICENSE
%{_datadir}/gnome-shell/extensions/%{uuid}
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.%{extension}.gschema.xml
