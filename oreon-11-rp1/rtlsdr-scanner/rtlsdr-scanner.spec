%global source0_hash 35ab9a55959d04619a9919c8a3e7a267aebc9e161342985927e36f355b80b873
Name:		rtlsdr-scanner
Version:	1.3.2
Release:        1%{?dist}
Summary:        Frequency scanning GUI for RTL2832 based DVB-T dongles
License:	GPL-3.0-only
URL:		http://eartoearoak.com/software/rtlsdr-scanner
Source0:        https://github.com/EarToEarOak/RTLSDR-Scanner/archive/v%{version}.tar.gz#/RTLSDR-Scanner-%{version}.tar.gz
Source1:	rtlsdr-scanner.desktop
Source2:	rtlsdr_scan.png
Requires:	python3-wxpython4
Requires:	python3-matplotlib
Requires:	python3-matplotlib-wx
Requires:	python3-numpy
Requires:	python3-pillow
Requires:	python3-pyserial
Requires:	python3-pyrtlsdr
Requires:	python3-visvis
Requires:	hicolor-icon-theme
BuildArch:	noarch
Patch:		rtlsdr-scanner-1.3.2-fedora.patch
Patch:		rtlsdr-scanner-1.3.2-python3.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-rtlsdr-scanner = %{version}-%{release}
# /oreon:deps
%description
Frequency scanning GUI for RTL2832 based DVB-T dongles. In other
words a cheap, simple Spectrum Analyser.

%package doc
Summary:	Documentation files for rtlsdr-scanner
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch
%description doc
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n RTLSDR-Scanner-%{version}

find rtlsdr_scanner -name '*.py' | xargs sed -i '1s|^#!.*|#!%{__python3}|'

# rtlsdr_scan_diag.py is not needed in distribution
rm -f rtlsdr_scanner/rtlsdr_scan_diag.py

# fix name of the application
mv rtlsdr_scanner/__main__.py rtlsdr_scan

# drop python artefact from resources
rm -f rtlsdr_scanner/res/__init__.py

%build

%pyproject_wheel
%install
%pyproject_install
install -Dpm 0755 ./rtlsdr_scan %{buildroot}%{_bindir}/rtlsdr_scan
install -Dpm 0644 -t %{buildroot}%{_datadir}/%{name}/res rtlsdr_scanner/res/*
install -Dpm 0644 %{S:2} %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/rtlsdr_scan.png
mkdir -p  %{buildroot}%{_datadir}/applications
desktop-file-install --add-category="Utility" \
  --dir=%{buildroot}%{_datadir}/applications \
  %{SOURCE1}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files
%files -n rtlsdr-scanner-doc -f %{oreon_filedir}/rtlsdr-scanner-doc.list

%changelog

%autochangelog
