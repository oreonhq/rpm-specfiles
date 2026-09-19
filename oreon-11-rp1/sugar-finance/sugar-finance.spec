%global source0_hash 1f9428c3fac82f1b73d682a7adcd607b032880fbaee19098e7930e023012b04b

Name:           sugar-finance
Version:        15
Release:        16%{?dist}
Summary:        Financial planning for Sugar

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://wiki.laptop.org/go/Finance
Source0:        http://download.sugarlabs.org/sources/honey/Finance/Finance-%{version}.tar.bz2
BuildArch:      noarch

BuildRequires: python3-devel
BuildRequires: sugar-toolkit-gtk3
BuildRequires: gettext
Requires: sugar >= 0.116

%description
Finance is a simple financial planning activity. It can be integrated 
into classroom assignments, or else used to track finances for a school
club. It might also be useful for students who wish to help their parents
with home finances.

The register view allows students to enter income and expenses, assign
categories, and review past transactions. The chart view shows students
a visual breakdown of their expenses by category. The budget view allows
users to assign a monthly budget to each category, and to see how each
month's expenses compare to the budget.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n Finance-%{version}
chmod -x {icons/help.svg,finance.py}

sed -i 's/python/python3/' setup.py

%build
python3 ./setup.py build

%install
python3 ./setup.py install --prefix=%{buildroot}/%{_prefix}
rm %{buildroot}%{_prefix}/share/applications/*.desktop || true

# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_3
%py_byte_compile %{python3} %{buildroot}%{_datadir}/{sugaractivitydir}/Finance.activity/

%find_lang org.laptop.community.Finance

%files -f org.laptop.community.Finance.lang
%license COPYING
%doc NEWS TODO
%{sugaractivitydir}/Finance.activity/
%{_datadir}/metainfo/*.appdata.xml

%changelog
%autochangelog
