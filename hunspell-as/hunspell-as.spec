%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-as
Summary: Assamese hunspell dictionaries
Epoch: 1
Version: 1.0.1.2resigned1
Release: 3%{?dist}
Source0: https://addons.mozilla.org/firefox/downloads/file/4270589/assamese_spell_checker-1.0.1.2resigned1.xpi
Source1: https://github.com/LibreOffice/dictionaries/raw/refs/heads/master/as_IN/README_as_IN.txt
URL: https://addons.mozilla.org/en-US/firefox/addon/assamese-spell-checker/
# license tag explicitly mentioned on website
License: GPL-3.0-only
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-as)

%description
Assamese hunspell dictionaries.

%prep
%autosetup -c
cp -p %{SOURCE1} .

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p dictionaries/as-IN.dic $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/as_IN.dic
cp -p dictionaries/as-IN.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/as_IN.aff

%files
%doc README_as_IN.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.1.2resigned1-3
- Prepare for Oreon 11 (RP1)
