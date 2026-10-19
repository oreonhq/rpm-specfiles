%global source0_hash 8879d89b5ff7b506c9fc28efc31a5c0b954bbe9333e66e5283d27d20a8519ea3
%global priority 59
%global fontname liberation-narrow
%global fontconf %{priority}-%{fontname}.conf
%global catalogue %{_sysconfdir}/X11/fontpath.d
Name:		%{fontname}-fonts
Summary:        Sans-serif Narrow fonts to replace commonly used Microsoft Arial Narrow
Version:	1.07.6
Release:        19%{?dist}
Epoch:		2
License:	LicenseRef-Liberation
URL:		https://github.com/liberationfonts/liberation-sans-narrow
Source0:        https://github.com/liberationfonts/liberation-sans-narrow/files/2579431/liberation-narrow-fonts-ttf-1.07.6.tar.gz
Source1:	%{name}.conf
Source2:	%{name}.metainfo.xml
BuildArch:	noarch
Requires:	fontpackages-filesystem
# oreon:deps
BuildRequires:  fontpackages-devel
BuildRequires:  libappstream-glib
BuildRequires:  mkfontdir
BuildRequires:  mkfontscale
# /oreon:deps
%description
The Liberation Sans Narrow Fonts are intended to be replacements for
the Arial Narrow.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-ttf-%{version}
%oreon_prep
%build

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}
install -m 0755 -d %{buildroot}%{catalogue}
ln -s %{_fontdir} %{buildroot}%{catalogue}/%{name}
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
%oreon_autofiles main

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
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.07.6-19
- Prepare for Oreon 11 (RP1)
