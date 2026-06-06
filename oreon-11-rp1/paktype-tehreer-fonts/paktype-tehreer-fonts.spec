%global source0_hash none

%global priority 67
%global fontname paktype-tehreer
%global fontconf %{priority}-%{fontname}

Name:        %{fontname}-fonts
Version:     6.0
Release:     13%{?dist}
Summary:     Fonts for Arabic from PakType
License:     GPL-2.0-only WITH Font-exception-2.0
URL:	     https://sourceforge.net/projects/paktype/
Source0:        https://downloads.sourceforge.net/project/paktype/PakType-Tehreer-6.0.tar.gz#/paktype-tehreer-fonts-6.0.tar.gz

Source1:     %{fontconf}.conf
BuildArch:   noarch
BuildRequires:	fontpackages-devel
Requires:   fontpackages-filesystem
Obsoletes: paktype-fonts-common < %{version}i-%{release}

%description 
The paktype-tehreer-fonts package contains fonts for the display of \
Arabic from the PakType by Lateef Sagar.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -c
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

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.0-13
- Import
