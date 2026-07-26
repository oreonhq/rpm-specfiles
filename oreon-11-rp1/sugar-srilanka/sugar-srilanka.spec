%global source0_hash efd2dcd343b9e832bbc97904df68e68f273dceac8df24273e1f3de54486aebd0

Name:		sugar-srilanka
Version:	4
Release:	13%{?dist}
Summary:	Game about the geography of Sri Lanka

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:	GPL-3.0-or-later
URL:		http://activities.sugarlabs.org//en-US/sugar/addon/4600
Source0:	http://download.sugarlabs.org/sources/honey/IKnowSriLanka/IknowSriLanka-%{version}.tar.bz2

BuildRequires:	gettext
BuildRequires:	python3-devel
BuildRequires:	sugar-toolkit-gtk3
BuildArch:	noarch
Requires:	sugar
Requires:	sugar-toolkit-gtk3

%description
Game about the geography of Sri Lanka.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n IknowSriLanka-%{version}
sed -i 's/python/python3/g' *.py

%build
python3 ./setup.py build

%install
python3 ./setup.py install --prefix=%{buildroot}/%{_prefix}
rm %{buildroot}%{_prefix}/share/applications/*.desktop || true

# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_3
%py_byte_compile %{python3} %{buildroot}/%{sugaractivitydir}/IknowSriLanka.activity/

%find_lang org.ceibaljam.conozcosrilanka

%files -f org.ceibaljam.conozcosrilanka.lang
%license LICENSE.md
%{sugaractivitydir}/IknowSriLanka.activity/

%changelog
%autochangelog
