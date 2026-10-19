%global source0_hash ce94fb0e6f6433e68316c958d75b760e977e0bd61c010b877479c318a44a611a
Name:		sugar-yupana
Version:	19
Release:        1%{?dist}
Summary:        Counting and calculating device used by the Incan
License:	GPL-3.0-or-later
URL:		http://wiki.sugarlabs.org/go/Activities/Yupana
Source0:        http://download.sugarlabs.org/sources/honey/Yupana/Yupana-%{version}.tar.bz2
BuildArch:	noarch
Requires:	sugar
# oreon:deps
BuildRequires:  gettext
BuildRequires:  python3
BuildRequires:  sugar-toolkit-gtk3
# /oreon:deps
%description
Counting and calculating device used by the Incan

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n Yupana-%{version}
sed -i 's/python/python3/g' setup.py

%build

python3 ./setup.py build
%install
python3 ./setup.py install --prefix=%{buildroot}/%{_prefix}
rm %{buildroot}%{_prefix}/share/applications/*.desktop || true
%find_lang org.sugarlabs.YupanaActivity
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
