%global source0_hash 533b9902340ee3b829837218eb352c078674bf2a0658ba4d9e46924af1b37934

Name:           sugar-distance
Version:        36
Release:        16%{?dist}
Summary:        Distance measurement for Sugar

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://wiki.laptop.org/go/Distance
Source0:        http://download.sugarlabs.org/sources/honey/Distance/Distance-%{version}.tar.bz2

BuildArch:      noarch
BuildRequires:  gettext
BuildRequires:  python3-devel
BuildRequires:  sugar-toolkit-gtk3
Requires:       sugar >= 0.116

%description
Distance (aka Acoustic Tape Measure) determines the physical distance 
between two XOs by measuring how long it takes sound pulses to travel 
between them. 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n Distance-%{version}

sed -i 's/python/python3/' setup.py

%build
python3 ./setup.py build

%install
mkdir -p %{buildroot}%{sugaractivitydir}
python3 ./setup.py install --prefix=%{buildroot}/%{_prefix}
rm %{buildroot}%{_prefix}/share/applications/*.desktop || true
find %{buildroot}%{sugaractivitydir}Distance.activity/arange.py -type f -name \* -exec chmod 644 {} \;

# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_3
%py_byte_compile %{python3} %{buildroot}%{_datadir}/{sugaractivitydir}/Distance.activity/

%find_lang org.laptop.AcousticMeasure

%files -f org.laptop.AcousticMeasure.lang
%doc NEWS
%{sugaractivitydir}/Distance.activity/

%changelog
%autochangelog
