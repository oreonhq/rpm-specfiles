%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-te
Summary: Telugu hunspell dictionaries
Version: 1.0.0
Release: 28%{?dist}
Epoch:   1
##Upstream is unresponsive so unable to verify license version
License:        GPL-1.0-or-later
URL:            https://gitorious.org/hunspell_dictionaries/hunspell_dictionaries.git
Source0:        http://anishpatil.fedorapeople.org/te_in.%{version}.tar.gz
BuildArch:      noarch

Requires:       hunspell
Supplements: (hunspell and langpacks-te)

%description
Telugu hunspell dictionaries.

%prep
%autosetup -c -n te_IN

%build


%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p te_IN/*.dic te_IN/*.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}

%files 
%license te_IN/COPYING te_IN/Copyright
%doc te_IN/README
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.0-28
- Prepare for Oreon 11 (RP1)
