%global source0_hash 7d6474d3e429ceceaa75fccc9191f663811ae53d0241f7107371432d11331ca2
Name:		timeline
Version:	2.12.0
Release:        1%{?dist}
Summary:        Displays and navigates events on a timeline
License:	GPL-3.0-only
URL:		http://thetimelineproj.sourceforge.net/
Source0:        http://downloads.sourceforge.net/thetimelineproj/%{name}-%{version}.zip
Source1:	timeline.desktop
Patch0:		paths.patch
BuildArch:	noarch
Requires:	python3-wxpython4
Requires:	python3-markdown
Requires:	python3-icalendar
Requires:	python3-svg
Requires:	python3-humblewx
Requires:	hicolor-icon-theme
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  python3-devel
# /oreon:deps
%description
Timeline is a cross-platform application for displaying and navigating 
events on a timeline.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%patch -P 0 -p0

%build

python3 ./tools/generate-mo-files.py
%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/timeline
install -m 755 source/timeline.py $RPM_BUILD_ROOT%{_bindir}/timeline
cp -pr icons $RPM_BUILD_ROOT%{_datadir}/timeline/
mkdir -p $RPM_BUILD_ROOT%{python3_sitelib}/timelinelib
cp -pr source/timelinelib/* $RPM_BUILD_ROOT%{python3_sitelib}/timelinelib/
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
install -p -m 644 icons/48.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/timeline.png
desktop-file-install \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/locale
cp -a translations/*/ $RPM_BUILD_ROOT%{_datadir}/locale/
rm -rf $RPM_BUILD_ROOT%{_datadir}/timeline/dependencies
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
