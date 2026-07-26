%global source0_hash f66012278f534e955203c3e8f2ffe03a5c5296c53943d6a4cd9aa52046b5da1c

Name:          sugar-memorize
Version:       58
Release:       13%{?dist}
Summary:       Memorize for Sugar
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:       GPL-2.0-or-later
URL:           http://wiki.sugarlabs.org/go/Activities/Memorize
Source0:       https://download.sugarlabs.org/sources/honey/Memorize/Memorize-%{version}.tar.bz2
# Upstream has applied this.
Patch0:        Fix-use-of-getchildren-with-Element-object.patch 
BuildArch:     noarch

BuildRequires: python3-devel
BuildRequires: sugar-toolkit-gtk3
BuildRequires: gettext
Requires: gstreamer-plugins-espeak
Requires: sugar

%description
The game memorize is about finding matching pairs. A pair can consist of any
multimedia object. At the moment these are images, sounds and text but this
could be extended to animations or movie snippets as well. Which pairs do 
match is up to the creator of the game. Memorize is actually more than just
a predefined game you can play, it allows you to create new games yourself
as well.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n Memorize-%{version}

sed -i 's/python/python3/' setup.py

%build
python3 ./setup.py build

%install
python3 ./setup.py install --prefix=%{buildroot}/%{_prefix}
rm %{buildroot}%{_prefix}/share/applications/*.desktop || true

# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_3
%py_byte_compile %{python3} %{buildroot}%{_datadir}/{sugaractivitydir}/Memorize.activity/

%find_lang org.laptop.Memorize

%files -f org.laptop.Memorize.lang
%license COPYING
%doc AUTHORS NEWS
%{sugaractivitydir}/Memorize.activity/
%{_datadir}/metainfo/org.laptop.Memorize.appdata.xml

%changelog
%autochangelog
