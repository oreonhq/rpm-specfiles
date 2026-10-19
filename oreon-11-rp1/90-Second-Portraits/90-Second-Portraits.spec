%global source0_hash 058e515915b8535fe5209a3e6cdf41aa46b22e7e0c3f1184006b9b3c4a9a434a
Name:           90-Second-Portraits
Version:        1.01b
Release:        28%{?dist}
Summary:        Frantic street painting game
License:        Zlib AND CC-BY-SA-4.0 AND CC-BY-3.0 AND OFL-1.1 AND MIT AND X11
URL:            http://tangramgames.dk/games/90secondportraits/
Source0:        https://github.com/SimonLarsen/%{name}/releases/download/%{version}/90secondportraits-%{version}.love#/%{name}-%{version}.zip
Patch0:         %{name}-appdata.patch
BuildArch:      noarch
Requires:       love
ExclusiveArch: %{arm} %{ix86} x86_64 aarch64 ppc64le riscv64
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
# /oreon:deps
%description
90 Second Portraits is a silly speed painting game developed for Ludum Dare 31
Jam competition. Time is money and you have neither! In 90 SECOND PORTRAITS
you’re paying the bills by speed painting portraits of bypassing customers!
You have 90 seconds to paint the customer and his/her preferred background!
Your work day ends after 5 customers!

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c -p1
sed -i 's/VERSION/%{version}/g' appdata/%{name}.6
#Remove non-free font and replace with existing font:
rm data/fonts/yb.ttf
sed -i "s/yb.ttf/neuton.ttf/" *.lua

%build

zip -r %{name}.love . -x appdata/* -x appdata/ -x *.txt -x *.md
%install
install -p -D -m 0644 %{name}.love \
  %{buildroot}/%{_datadir}/%{name}/%{name}.love
install -p -D -m 0755 appdata/%{name} \
  %{buildroot}/%{_bindir}/%{name}
install -p -D -m 0644 appdata/%{name}.6 \
  %{buildroot}/%{_mandir}/man6/%{name}.6
install -p -D -m 0644 appdata/%{name}.appdata.xml \
  %{buildroot}/%{_datadir}/appdata/%{name}.appdata.xml
appstream-util validate-relax --nonet \
  %{buildroot}/%{_datadir}/appdata/*.appdata.xml
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  appdata/%{name}.desktop
install -p -D -m 0644 data/images/title_background.png \
  %{buildroot}/%{_datadir}/pixmaps/%{name}.png
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
