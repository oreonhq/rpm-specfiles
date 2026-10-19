%global source0_hash 2fbdf9c8fedff331a87eb4d774359094d9d8628e9b5b3de6a68f25287b532f35
Name:           inkscape-silhouette
Version:        1.29
Release:        1%{?dist}
Summary:        Plotter software
License:        GPL-2.0-only AND GPL-2.0-or-later
URL:            https://github.com/fablabnbg/inkscape-silhouette
VCS:            git:https://github.com/fablabnbg/inkscape-silhouette.git
Source0:        https://github.com/fablabnbg/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch:          python3.patch
BuildArch:      noarch
Requires: inkscape
Requires: python3dist(cssselect)
Requires: python3dist(lxml)
Requires: python3dist(matplotlib)
Requires: python3dist(numpy)
Requires: python3dist(pyusb)
Requires: python3dist(tinycss2)
Requires: python3dist(xmltodict)
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-inkscape-silhouette = %{version}-%{release}
# /oreon:deps
%description
An application for controlling 2D plotters, cutters, engravers, and CNC
machines.

%package doc
Summary: Examples
%description doc
Examples for Inkscape Silhouette.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}
# Remove bundled unused libusb
# https://github.com/fablabnbg/inkscape-silhouette/pull/186
rm -r silhouette/pyusb-1.0.2/

%build

%make_build mo
%install
find silhouette -type f -exec install -Dm 755 "{}" \
  "%{buildroot}%{_datadir}/inkscape/extensions/silhouette/{}" \;
install -Dpm 755 render_silhouette_regmarks.py \
  %{buildroot}%{_datadir}/inkscape/extensions/render_silhouette_regmarks.py
install -Dpm 755 sendto_silhouette.py \
  %{buildroot}%{_datadir}/inkscape/extensions/sendto_silhouette.py
install -Dpm 755 silhouette_multi.py \
  %{buildroot}%{_datadir}/inkscape/extensions/silhouette_multi.py
install -Dpm 644 silhouette_multi.inx \
  %{buildroot}%{_datadir}/inkscape/extensions/silhouette_multi.inx
install -Dpm 644 sendto_silhouette.inx \
  %{buildroot}%{_datadir}/inkscape/extensions/sendto_silhouette.inx
install -Dpm 644 render_silhouette_regmarks.inx \
  %{buildroot}%{_datadir}/inkscape/extensions/render_silhouette_regmarks.inx
find locale -type f -exec install -Dm 644 "{}" \
  "%{buildroot}%{_datadir}/{}" \;
install -Dpm 644 silhouette-udev.rules \
  %{buildroot}%{_prefix}/lib/udev/rules.d/40-silhouette-udev.rules
install -Dpm 644 silhouette-icon.png \
  %{buildroot}%{_prefix}/lib/udev/silhouette-icon.png
install -Dpm 644 silhouette-udev-notify.sh \
  %{buildroot}%{_prefix}/lib/udev/silhouette-udev-notify.sh
install -Dpm 644 templates/silhouette-cameo-registration-marks-a4.svg \
  %{buildroot}%{_datadir}/inkscape/templates/silhouette-cameo-registration-marks-a4.svg
%find_lang %{name}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%pytest test
%files
%files -n inkscape-silhouette-doc -f %{oreon_filedir}/inkscape-silhouette-doc.list

%changelog

%autochangelog
