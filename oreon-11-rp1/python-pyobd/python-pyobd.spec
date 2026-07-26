%global source0_hash f3004db4000e2bc166aae3b4342c98aa62f74f3372c5829472af0ee56c5e110c

%global srcname pyobd
%global ver_major 0
%global ver_minor 9
%global ver_patch 3
%global ver %{ver_major}.%{ver_minor}.%{ver_patch}

Name:           python-%{srcname}
Version:        %{ver}
Release:        41%{?dist}
Summary:        OBD-II (SAE-J1979) compliant scan tool software
# CC-BY-SA for icon, see README.Fedora for details
# Automatically converted from old format: GPLv2+ and CC-BY-SA - review is highly recommended.
License:        GPL-2.0-or-later AND LicenseRef-Callaway-CC-BY-SA
# contact for patches: support@secons.com
# upstream refuses patches to support "Chinese" ELM32X
URL:            http://www.obdtester.com/
Source0:        http://www.obdtester.com/download/%{srcname}_%{ver_major}.%{ver_minor}.%{ver_patch}.tar.gz
Source1:        pyobd-icon.svg
Source2:        README.Fedora
BuildArch:      noarch
# import from pyobd module
Patch0:         python-pyobd-0.9.3-pyobd-module.patch
Patch1:         python-pyobd-0.9.3-invalid-device-traceback-fix.patch
Patch2:         python-pyobd-0.9.3-configure-dialog-traceback-fix.patch
# part of the patch provided by Lumír Balhar <lbalhar@redhat.com>
Patch3:         python-pyobd-0.9.3-python3.patch
BuildRequires:  desktop-file-utils
BuildRequires:  dos2unix, ImageMagick

%global _description \
pyOBD is an OBD-II (SAE-J1979) compliant scan tool software written \
entirely in Python. It is meant to interface with the low cost ELM 32x \
devices such as ELM-USB.

%description
%{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel, python3-wxpython4
Provides:       pyobd = %{ver}
Obsoletes:      pyobd < 0.9.3-7
Requires:       python3-pyserial, python3-wxpython4, hicolor-icon-theme

%description -n python3-%{srcname}
%{_description}

Python 3 version of the pyOBD.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{srcname}-%{ver_major}.%{ver_minor}.%{ver_patch}

cp -p %{SOURCE2} README.Fedora

# convert CR/LF to LF
dos2unix pyobd.desktop
# fix encoding settings
sed -i '/Encoding=/ s|UTF8|UTF-8|' pyobd.desktop
# change icon in pyobd.desktop
sed -i 's|/usr/share/pyobd/pyobd.gif|pyobd|' pyobd.desktop
# create dummy module init
[ -f __init__.py ] || echo '# module init' > __init__.py

# remove hashbangs
for f in *.py
do
  sed -i '/^[ \t]*#!\/usr\/bin\/env/ d' $f
done

# fix hashbang
sed -i '1 s|/usr/bin/env python|%{__python3}|' pyobd

%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1

%build

%install
mkdir -p %{buildroot}%{_bindir}
install -pm 0755 pyobd %{buildroot}%{_bindir}

mkdir -p %{buildroot}%{python3_sitelib}/%{srcname}
install -pm 0644 -t %{buildroot}%{python3_sitelib}/%{srcname} *.py

# icon
install -Dpm 0644 %{SOURCE1} %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/pyobd.svg

# desktop file
mkdir -p  %{buildroot}%{_datadir}/applications
desktop-file-install --add-category="Utility" \
  --dir=%{buildroot}%{_datadir}/applications \
  pyobd.desktop

%files -n python3-%{srcname}
%license COPYING
%doc README.Fedora
%{_datadir}/icons/hicolor/scalable/apps/%{srcname}.svg
%{_datadir}/applications/pyobd.desktop
%{python3_sitelib}/pyobd/
%{_bindir}/pyobd

%changelog
%autochangelog
