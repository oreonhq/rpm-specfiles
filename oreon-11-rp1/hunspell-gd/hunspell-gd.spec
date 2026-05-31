%global source0_hash none

%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-gd
Summary: Scots Gaelic hunspell dictionaries
Version: 2.6
Release: 29%{?dist}
Source: http://downloads.sourceforge.net/project/aoo-extensions/4587/8/hunspell-gd-2.6.oxt
URL: http://extensions.services.openoffice.org/en/project/faclair-afb
License: GPL-2.0-or-later AND GPL-3.0-or-later
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-gd)

%description
Scots Gaelic hunspell dictionaries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -c hunspell-gd-%{version}

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p dictionaries/gd_GB.dic dictionaries/gd_GB.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}


%files
%doc dictionaries/README_gd_GB.txt LICENSES-en.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.6-29
- Prepare for Oreon 11 (RP1)
