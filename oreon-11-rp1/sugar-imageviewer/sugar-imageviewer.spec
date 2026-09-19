%global source0_hash 2dc9853a5103b8021632c7c2d8b2c6a9aeeacdac670f1840766e08a7b198e2ae

Name:          sugar-imageviewer
Version:       65
Release:       15%{?dist}
Summary:       Simple Image viewer for Sugar

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:       GPL-2.0-or-later
URL:           http://wiki.laptop.org/go/Image_Viewer
Source0:       http://download.sugarlabs.org/sources/sucrose/fructose/ImageViewer/ImageViewer-%{version}.tar.bz2
BuildArch:     noarch

BuildRequires: python3-devel
BuildRequires: sugar-toolkit-gtk3
BuildRequires: gettext
Requires: sugar

%description
The Image Viewer activity is a simple and fast image viewer tool for Sugar.
It has features one would expect of a standard image viewer, like zoom,
rotate, etc. 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n ImageViewer-%{version}

sed -i 's/python/python3/' setup.py

%build
python3 ./setup.py build

%install
python3 ./setup.py install --prefix=%{buildroot}/%{_prefix}
rm %{buildroot}%{_prefix}/share/applications/*.desktop || true

# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_3
%py_byte_compile %{python3} %{buildroot}%{_datadir}/{sugaractivitydir}/ImageViewer.activity/

%find_lang org.laptop.ImageViewerActivity

%files -f org.laptop.ImageViewerActivity.lang
%license COPYING
%doc AUTHORS NEWS
%{sugaractivitydir}/ImageViewer.activity/

%changelog
%autochangelog
