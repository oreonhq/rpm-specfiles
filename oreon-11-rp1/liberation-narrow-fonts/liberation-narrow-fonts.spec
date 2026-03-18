%global priority 59
%global fontname liberation-narrow
%global fontconf %{priority}-%{fontname}.conf
%global catalogue %{_sysconfdir}/X11/fontpath.d

Name:		%{fontname}-fonts
Summary:	Sans-serif Narrow fonts to replace commonly used Microsoft Arial Narrow
Version:	1.07.6
Release:	19%{?dist}
Epoch:		2
# The license of the Liberation Fonts is a EULA that contains GPLv2 and two
# exceptions:
# The first exception is the standard FSF font exception.
# The second exception is an anti-lockdown clause somewhat like the one in
# GPLv3. This license is Free, but GPLv2 and GPLv3 incompatible.
License:	LicenseRef-Liberation
URL:		https://github.com/liberationfonts/liberation-sans-narrow
Source0:	%{url}/files/2579431/%{name}-ttf-%{version}.tar.gz
Source1:	%{name}.conf
Source2:	%{name}.metainfo.xml
BuildArch:	noarch
BuildRequires:	fontpackages-devel
BuildRequires:	mkfontscale mkfontdir
BuildRequires:	libappstream-glib
Requires:	fontpackages-filesystem

%description
The Liberation Sans Narrow Fonts are intended to be replacements for
the Arial Narrow.

%prep
%autosetup -n %{name}-ttf-%{version}


%build

%install
# fonts .ttf
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

# catalogue
install -m 0755 -d %{buildroot}%{catalogue}
ln -s %{_fontdir} %{buildroot}%{catalogue}/%{name}

# fonts.{dir,scale}
mkfontscale %{buildroot}%{_fontdir}
mkfontdir %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
		%{buildroot}%{_fontconfig_confdir}
install -m 0644 -p %{SOURCE1} \
		%{buildroot}%{_fontconfig_templatedir}/%{fontconf}
install -Dm 0644 -p %{SOURCE2} \
	%{buildroot}%{_datadir}/metainfo/%{fontname}.metainfo.xml

ln -s %{_fontconfig_templatedir}/%{fontconf} \
		%{buildroot}%{_fontconfig_confdir}/%{fontconf}


%check
appstream-util validate-relax --nonet \
	%{buildroot}%{_datadir}/metainfo/%{fontname}.metainfo.xml

%_font_pkg -f %{fontconf} *.ttf

%doc AUTHORS ChangeLog COPYING README.rst TODO
%license License.txt
%{_datadir}/metainfo/%{fontname}.metainfo.xml
%verify(not md5 size mtime) %{_fontdir}/fonts.dir
%verify(not md5 size mtime) %{_fontdir}/fonts.scale
%{catalogue}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.07.6-19
- Prepare for Oreon 11 (RP1)
