%global source0_hash 2aa5ebf37bee37ba9efd130440961f2dd6333e6c33d5abbb775958895f96e21d

Name:           sugar-xoirc
Version:        14
Release:        13%{?dist}
Summary:        IRC client for Sugar
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/sugarlabs/irc-activity/
Source0:        http://download.sugarlabs.org/sources/honey/IRC/IRC-%{version}.tar.bz2
BuildArch:      noarch

BuildRequires:  gobject-introspection-devel
BuildRequires:  python3-devel
BuildRequires:  sugar-toolkit-gtk3-devel
Requires:       sugar >= 0.116
Requires:       sugar-toolkit-gtk3

%description
This activity allows you to contact other OLPC users and enthusiasts
on the internet, and chat with them. 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n IRC-%{version}

sed -i 's/python/python3/' *.py

%build
python3 ./setup.py build

%install
python3 ./setup.py install --prefix=%{buildroot}/%{_prefix}
rm %{buildroot}%{_prefix}/share/applications/*.desktop || true

# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_3
%py_byte_compile %{python3} %{buildroot}/%{sugaractivitydir}/IRC.activity/

%files
%license COPYING
%doc README TODO
%{sugaractivitydir}/IRC.activity/

%changelog
%autochangelog
