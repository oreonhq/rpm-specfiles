%global source0_hash 70f2b3590f9b3c92d07135c51f5bb1a8d82f21b0d265484db92f3f13797f5165
%global priority 67
%global fontname paktype-tehreer
%global fontconf %{priority}-%{fontname}
Name:        %{fontname}-fonts
Version:     6.0
Release:        1%{?dist}
Summary:        Fonts for Arabic from PakType
License:     GPL-2.0-only WITH Font-exception-2.0
URL:	     https://sourceforge.net/projects/paktype/
Source0:        https://deb.debian.org/debian/pool/main/f/fonts-paktype/fonts-paktype_0.0svn20121225.orig.tar.bz2
Source1:     %{fontconf}.conf
BuildArch:   noarch
Requires:   fontpackages-filesystem
Obsoletes: paktype-fonts-common < %{version}i-%{release}
# oreon:deps
BuildRequires:  fontpackages-devel
# /oreon:deps
%description 
The paktype-tehreer-fonts package contains fonts for the display of \
Arabic from the PakType by Lateef Sagar.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -c -T
tar xf %{SOURCE0}
cp fonts-paktype-0.0svn20121225/Deployment/PakType\ Tehreer.ttf PakTypeTehreer.ttf
cp -r fonts-paktype-0.0svn20121225/License\ files .
rm -rf fonts-paktype-0.0svn20121225
mv License\ files/PakType\ Tehreer\ License.txt PakType_Tehreer_License.txt

%{__sed} -i 's/\r//' PakType_Tehreer_License.txt
chmod a-x PakType_Tehreer_License.txt

%build

echo "Nothing to do in Build."
%install
install -m 0755 -d $RPM_BUILD_ROOT%{_fontdir}
install -m 0644 -p PakTypeTehreer.ttf $RPM_BUILD_ROOT%{_fontdir}
install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
		%{buildroot}%{_fontconfig_confdir}
install -m 0644 -p %{SOURCE1} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}.conf
ln -s %{_fontconfig_templatedir}/%{fontconf}.conf \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}.conf
%_font_pkg -f %{fontconf}.conf PakTypeTehreer.ttf
%ghost %attr(644, root, root) %{_fontdir}/.uuid
%license PakType_Tehreer_License.txt
%doc For\ Code\ and\ Features.txt
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.0-13
- Import
