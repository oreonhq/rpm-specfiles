%global source0_hash d3fc02a6abc7719f0abb5336cf6333677dd3451ff7508ebc30947528c577746d

# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_3

%global __python %{__python3}

Summary:  Input method for entering unicode symbols and emoji by name
Name: ibus-uniemoji
Version: 0.7.0
Release: 6%{?dist}
# emojione.json is in MIT
# UnicodeData.txt is in Unicode
# uniemoji is in GPLv3+
License: Unicode-DFS-2015 AND MIT AND GPL-3.0-or-later
Source0: https://github.com/salty-horse/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
URL: https://github.com/salty-horse/ibus-uniemoji

BuildArch: noarch

BuildRequires: python3-devel
BuildRequires: make
Requires: ibus

%description
This simple input method for ibus allows you to
enter unicode emoji and other symbols by name.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%install
mkdir -p %{buildroot}/%{_datadir}/ibus/component
make install DESTDIR=%{buildroot}

%py_byte_compile %{python3} %{buildroot}%{_datadir}/ibus-uniemoji

%files
%license COPYING COPYING.*
%doc HISTORY README.md
%{_datadir}/ibus/component/*.xml
%{_datadir}/ibus-uniemoji
%dir %{_sysconfdir}/xdg/uniemoji
%config(noreplace) %{_sysconfdir}/xdg/uniemoji/custom.json

%changelog
%autochangelog
