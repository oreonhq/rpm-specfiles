%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-vi
Summary: Vietnamese hunspell dictionaries
%global upstreamid 20120418
Version: 0.%{upstreamid}
Release: 20%{?dist}
Source: https://downloads.sourceforge.net/project/aoo-extensions/917/3/vi_spellchecker_ooo3.oxt
URL: https://extensions.openoffice.org/en/project/vietnamese-spellchecker
License: GPL-2.0-only
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-vi)

%description
Vietnamese hunspell dictionaries.

%prep
%autosetup -c -n hunspell-vi

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p dictionaries/*.dic dictionaries/*.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}


%files
%license LICENSES-en.txt LICENSES-vi.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.%{upstreamid}-20
- Prepare for Oreon 11 (RP1)
