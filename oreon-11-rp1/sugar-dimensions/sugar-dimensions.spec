%global source0_hash de8dc7e379d2209736b78840b4517e8ec1ba2c503d28eab77524e871ca866683

Name:           sugar-dimensions
Version:        60
Release:        13%{?dist}
Summary:        A pattern matching game

# namingalert.py is licensed as LGPLv2+
# sprites.py is licensed under the MIT license
# other files are licensed as GPLv3+
# Automatically converted from old format: GPLv3+ and LGPLv2+ and MIT - review is highly recommended.
License:        GPL-3.0-or-later AND LicenseRef-Callaway-LGPLv2+ AND LicenseRef-Callaway-MIT
URL:            https://github.com/sugarlabs/dimensions
Source0:        http://download.sugarlabs.org/sources/honey/Dimensions/Dimensions-%{version}.tar.bz2

BuildRequires:  gettext
BuildRequires:  gobject-introspection-devel
BuildRequires:  python3-devel
BuildRequires:  sugar-toolkit-gtk3-devel
BuildArch:      noarch
Requires:       sugar >= 0.116

%description
The object is to find sets of three cards where each attribute—color,
shape, number of elements, and shading—either match on all three cards
or are different on all three cards. The current version doesn't yet
support sharing with multiple players or saving to the Journal, but it
can be played by a single player.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n Dimensions-%{version}

for lib in $(find . -name "*.py" -type f); do
  sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new &&
  touch -r $lib $lib.new &&
  mv $lib.new $lib
done

%build
python3 ./setup.py build

%install
python3 ./setup.py install --prefix=$RPM_BUILD_ROOT/%{_prefix}
chmod 0644 %{buildroot}/%{sugaractivitydir}/Dimensions.activity/gencards.py
rm %{buildroot}%{_prefix}/share/applications/*.desktop || true

# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_3
%py_byte_compile %{__python3} %{buildroot}/%{sugaractivitydir}/Dimensions.activity/

%find_lang org.sugarlabs.VisualMatchActivity

%files -f org.sugarlabs.VisualMatchActivity.lang
%license COPYING COPYING.MIT
%doc NEWS
%{sugaractivitydir}/Dimensions.activity/

%changelog
%autochangelog
