%global source0_hash 1c5661549c4351e14315ba166068ae2581bc7dbfb179604a2a2ffab81883a7ce

Name:           quisk
Version:        4.2.50
Release:        3%{?dist}
Summary:        Software Defined Radio (SDR) software

# Automatically converted from old format: GPLv2 and BSD - review is highly recommended.
License:        GPL-2.0-only AND LicenseRef-Callaway-BSD
URL:            http://james.ahlstrom.name/quisk/
Source0:        https://files.pythonhosted.org/packages/source/q/%{name}/%{name}-%{version}.tar.gz
Source1:        quisk.desktop
Source2:        quisk.png
Source3:        name.ahlstrom.james.Quisk.metainfo.xml

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3-wxpython4
BuildRequires:  fftw-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  portaudio-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  dos2unix
BuildRequires:  libsoundio-devel
BuildRequires:  desktop-file-utils
BuildRequires:  hicolor-icon-theme
Requires:       hicolor-icon-theme
Requires:       python3-wxpython4
Requires:       wdsp
Suggests:       codec2-devel

%description
QUISK is a Software Defined Radio (SDR) which can control various
radio hardware. QUISK supports CW, SSB, and AM.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

dos2unix afedrinet/sdr_control.py

# remove binaries, etc
find . -name \*.pyc -exec rm {} \;
find . -name \*.pyd -exec rm {} \;
find . -name \*.so -exec rm {} \;
find . -name \*.o -exec rm {} \;
find . -name \*.dll -exec rm {} \;

# remove execute permissions from everything
find . -type f -exec chmod a-x {} \;

# fix shebangs
sed -i 's|#!\s*/usr/bin/python|#!/usr/bin/python3|;s|#!\s*/usr/bin/env\s\+python3\?|#!/usr/bin/python3|' \
  quisk.py quisk_vna.py portaudio.py n2adr/startup.py \
  afedrinet/sdr_control.py afedrinet/afedri.py

%generate_buildrequires
%pyproject_buildrequires

%build
CFLAGS="%{optflags}" %{__python3} setup.py build_ext --inplace
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files quisk

# make Python scripts with shebangs executable
for f in `find %{buildroot}%{python3_sitearch}/%{name} -name \*.py`
do
    grep -E -q '^#!' $f && chmod a+x $f
done

desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}

install -Dpm 0644 %{SOURCE2} \
  %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/quisk.png

install -Dpm 0644 %{SOURCE3} \
  %{buildroot}%{_metainfodir}/name.ahlstrom.james.Quisk.metainfo.xml

%files -f %{pyproject_files}
%license license.txt
%doc docs.html defaults.html
%doc help.html help_vna.html
%{_bindir}/%{name}{,_vna}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%{_metainfodir}/name.ahlstrom.james.Quisk.metainfo.xml

%changelog
%autochangelog
