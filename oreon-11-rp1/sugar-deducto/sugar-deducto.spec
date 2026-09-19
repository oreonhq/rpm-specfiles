%global source0_hash fc37f935c667c7b971c3a387e4b597edde235148c7eaac0cc10620720ff9b55c

Name:		sugar-deducto
Version:	11
Release:	14%{?dist}
Summary:	A learning activity aimed towards improving children’s skills to deducing logic

# sprites.py is in MIT and all other files in GPLv3+
# Automatically converted from old format: GPLv3+ and MIT - review is highly recommended.
License:	GPL-3.0-or-later AND LicenseRef-Callaway-MIT
URL:		http://activities.sugarlabs.org/en-US/sugar/addon/4220
Source0:	http://download.sugarlabs.org/sources/honey/Deducto/Deducto-%{version}.tar.bz2

BuildRequires:	gettext
BuildRequires:	python3-devel
BuildRequires:	sugar-toolkit-gtk3
Requires:	sugar
Requires:	sugar-toolkit-gtk3
BuildArch:	noarch

%description
A learning activity aimed towards improving children's skills 
to deducing logic through pattern recognition.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Deducto-%{version}
#sed -i "s|python|python2|g" setup.py

%build
python3 ./setup.py build

%install
python3 ./setup.py install --prefix=%{buildroot}%{_prefix}
rm %{buildroot}%{_prefix}/share/applications/*.desktop || true

# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_3
%py_byte_compile %{python3} %{buildroot}/%{sugaractivitydir}/Deducto.activity/

%find_lang  in.seeta.Deducto

%files -f in.seeta.Deducto.lang
%license COPYING
%doc NEWS
%{sugaractivitydir}/Deducto.activity/

%changelog
%autochangelog
