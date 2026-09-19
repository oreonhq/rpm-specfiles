%global source0_hash 675744d1ddf3f355f285dac331359c783b666634741982196afff76ae452a800

Name:          sugar-stopwatch
Version:       21
Release:       15%{?dist}
Summary:       Simple stopwatch for Sugar
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:       GPL-3.0-or-later
URL:           http://wiki.laptop.org/go/Stopwatch
Source0:       https://download.sugarlabs.org/sources/honey/StopWatch/StopWatch-%{version}.tar.bz2
BuildArch:     noarch

BuildRequires: python3-devel
BuildRequires: sugar-toolkit-gtk3
BuildRequires: telepathy-glib-devel
BuildRequires: gettext
Requires: sugar

%description
This activity provides multiple stopwatches to time events with. Provide a 
useful timer for races, velocity measurements, etc.  Be accessible to 
innumerate users. Help develop numeracy. Sharing of stopwatch sets, which 
anyone can manipulate. 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n StopWatch-%{version}

sed -i 's/python/python3/' setup.py

%build
python3 ./setup.py build

%install
python3 ./setup.py install --prefix=%{buildroot}/%{_prefix}
rm %{buildroot}%{_prefix}/share/applications/*.desktop || true

# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_3
%py_byte_compile %{python3} %{buildroot}%{_datadir}/{sugaractivitydir}/StopWatch.activity/

%find_lang org.laptop.StopWatchActivity

%files -f org.laptop.StopWatchActivity.lang
%license COPYING
%doc NEWS
%{sugaractivitydir}/StopWatch.activity/

%changelog
%autochangelog
