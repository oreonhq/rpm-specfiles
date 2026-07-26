%global source0_hash d266d7fba64fbfedf13240d3d0eb21b8bacbedeaa5f22b26a27d472c8d23f103

Name:           alex4
Version:        1.0
Release:        48%{?dist}
Summary:        Alex the Allegator 4 - Platform game
License:        GPL-1.0-or-later
URL:            https://obiot.github.io/Alex4-WE/readme.html
Source0:        http://downloads.sf.net/allegator/Alex4/source%20and%20data/alex4src_data.zip
Source1:        alex4.desktop
Source2:        alex4.png
Source3:        alex4.appdata.xml
Patch0:         alex4-unix.patch
Patch1:         alex4-allegro-4.2.patch
Patch2:         alex4-dot-files-endian-clean.patch
Patch3:         alex4-fsf-address.patch
Patch4:         alex4-ini-comment.patch
Patch5:         alex4src-warnings.patch
Patch6:         alex4-fcommon-fix.patch
BuildRequires:  gcc
BuildRequires:  allegro-devel dumb-devel desktop-file-utils libappstream-glib
BuildRequires: make
Requires:       hicolor-icon-theme

%description
In the latest installment of the series Alex travels through the jungle in
search of his kidnapped girlfriend. Plenty of classic platforming in four
nice colors guaranteed!

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n alex4src
sed -i 's/\r//' *.txt *.ini

%build
pushd src
make %{?_smp_mflags} PREFIX=%{_prefix} \
  CFLAGS="$RPM_OPT_FLAGS -Wno-deprecated-declarations -Wno-unused-result -DALLEGRO_FIX_ALIASES"
popd

%install
pushd src
make install PREFIX=$RPM_BUILD_ROOT%{_prefix}
popd

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps
install -p -m 644 %{SOURCE2} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/appdata
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml

%files
%doc license.txt readme.txt alex4.ini
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png

%changelog
%autochangelog
