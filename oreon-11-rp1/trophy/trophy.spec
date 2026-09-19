%global source0_hash e3f6c76bdbb19e4d08f2310b3a0039de575aebfb9c9855e6138c88a0edd476be

Name:           trophy
Version:        2.0.4
Release:        16%{?dist}
Summary:        Car racing game with special features
License:        GPL-1.0-or-later
URL:            http://trophy.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}.appdata.xml
BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  gcc
BuildRequires:  ClanLib1-devel desktop-file-utils libappstream-glib
Requires:       hicolor-icon-theme

%description
TROPHY is a car racing game with some special features
like shooting and dropping bombs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
export LDFLAGS=-L%{_libdir}/ClanLib-1.0
export CXXFLAGS="%{optflags} -Wno-template-body"

%configure
make %{?_smp_mflags}

%install
%make_install

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-edit --set-key=Terminal --set-value=false \
  --set-key=StartupNotify --set-value=false \
  $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/72x72/apps
mv $RPM_BUILD_ROOT%{_datadir}/icons/trophy.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/72x72/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/appdata
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml

%ldconfig_scriptlets

%files
%doc AUTHORS ChangeLog README TODO
%license COPYING
%{_mandir}/man6/%{name}.6.gz
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/72x72/apps/%{name}.png

%changelog
%autochangelog
