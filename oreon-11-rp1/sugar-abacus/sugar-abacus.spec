%global source0_hash 5245abce021d8cc8fea6ae81feeab3b2f4e3b5662c166fc6b8497897eb0078e1

Name:           sugar-abacus
Version:        61
Release:        16%{?dist}
Summary:        A simple abacus activity for Sugar

License:        LGPL-3.0-or-later
URL:            http://activities.sugarlabs.org/addon/4293
Source0:        http://download.sugarlabs.org/sources/honey/Abacus/Abacus-%{version}.tar.bz2

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  sugar-toolkit-gtk3
BuildRequires:  gettext
Requires:       sugar >= 0.116

%description
Abacus lets the learner explore different representations of numbers using 
different mechanical counting systems developed by the ancient Romans and 
Chinese. There are several different variants available for exploration: a 
suanpan, the traditional Chinese abacus with 2 beads on top and 5 beads below; 
a soroban, the traditional Japanese abacus with 1 bead on top and 4 beads below;
the schety, the traditional Russian abacus, with 10 beads per column, with the 
exception of one column with just 4 beads used for counting in fourths; and the 
nepohualtzintzin, the traditional Mayan abacus, with 3 beads on top and 4 beads 
below (it uses base 20).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n Abacus-%{version}

sed -i 's/python/python3/' abacus.py

%build
python3 ./setup.py build

# %find_lang org.sugarlabs.AbacusActivity

%install
python3 ./setup.py install --prefix=%{buildroot}/%{_prefix}
rm %{buildroot}%{_prefix}/share/applications/*.desktop || true

# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_3
%py_byte_compile %{python3} %{buildroot}}/%{sugaractivitydir}/Abacus.activity/

%find_lang org.sugarlabs.AbacusActivity

%files -f org.sugarlabs.AbacusActivity.lang
%license COPYING
%doc NEWS
%{sugaractivitydir}/Abacus.activity/

%changelog
%autochangelog
