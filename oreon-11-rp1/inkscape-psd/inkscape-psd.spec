%global source0_hash 3f5adaaf6c77f71a1c8f56efde69b96e95e1e29b39741971143a56652fecb2bd

Name:		inkscape-psd
Version:	0.1.1
Release:	26%{?dist}
Summary:	Inkscape PSD Importer
# Automatically converted from old format: BSD - review is highly recommended.
License:	LicenseRef-Callaway-BSD
URL:		http://pernsteiner.org/inkscape/psd_import/
Source:		http://pernsteiner.org/inkscape/psd_import/inkscape-psd_import-%{version}.zip
Patch0:         inkscape-psd-python3.patch
Requires:	inkscape
Requires:	python3
BuildArch:	noarch

%description
This Inkscape extension allows you to load Photoshop PSD files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c %{name}-%{version}

%patch -P0 -p1

# Documentation of Licence (as it written in every file) :
ln -s %{_datadir}/inkscape/extensions/psd_import/__init__.py LICENSE

%build
# Nothing to build.

%install
mkdir -p %{buildroot}%{_datadir}/inkscape/extensions
cp -p psd_import.inx %{buildroot}%{_datadir}/inkscape/extensions
cp -p psd_import_main.py %{buildroot}%{_datadir}/inkscape/extensions
cp -rp psd_import %{buildroot}%{_datadir}/inkscape/extensions

%files
%license LICENSE
%{_datadir}/inkscape/extensions/*

%changelog
%autochangelog
