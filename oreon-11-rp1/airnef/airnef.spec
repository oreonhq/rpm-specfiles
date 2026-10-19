%global source0_hash 58610d66fe0adc902bfa137f9c05dba5194e96f60c659d4fa9ce823c4e890067
%global python    python3
%global appdir    %python3_sitelib/%name
%global appresdir %python3_sitelib/%name/appresource
Name:           airnef
Version:        1.1
Release:        36%{?dist}
Summary:        Wireless download from your Nikon/Canon Camera
License:        GPL-3.0-only
URL:            http://www.testcams.com/airnef/
BuildArch:      noarch
Source0:        http://www.testcams.com/airnef/Version_%{version}/airnef_v%{version}_Source.zip
Patch0:         airnef-1.1-rpm-paths.patch
Patch1:         airnef-1.1-missing-re-import.patch
Requires:       %python-six
Requires:       %python-tkinter
# oreon:deps
BuildRequires:  python3-devel
# /oreon:deps
%description
Open-source utility for downloading images and videos from WiFi-equipped
cameras.  Airnef supports all Nikon cameras that have built-in WiFi interfaces,
along with those using external Nikon WU-1a and WU-1b WiFi adapters, Canon and
Sony cameras.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n airnef

# six is available in fedora
rm six.py

# OSX only file is not needed
rm airnefcmd_OSX_Frozen_Wrapper.py

# TODO: ??
rm appresource/airnef.icns

for i in `grep -l -r '#!/usr/bin/env python'`; do
    sed -i '1 s|#!/usr/bin/env python.*||g' "$i"
done

%build

%install
mkdir -p %buildroot%appdir
for i in *.py *.pyw; do
    dest=${i/%pyw/py} # drop pyw suffixes
    install "$i" -p -m 644 %buildroot%appdir/"$dest"
done
mkdir -p %buildroot%appresdir
for i in appresource/*; do
    install "$i" -p -m 644 %buildroot%appresdir
done
cat > wrapper <<'EOF'
exec %python %appdir/"$(basename "$0").py" "$@"
EOF
mkdir -p %buildroot%_bindir
install -m 755 wrapper %buildroot%_bindir/airnef
install -m 755 wrapper %buildroot%_bindir/airnefcmd
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
