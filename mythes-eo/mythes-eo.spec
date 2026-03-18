Name: mythes-eo
Summary: Esperanto thesaurus
%global upstreamid 20180330
Version: 0.%{upstreamid}
Release: 18%{?dist}
Source: http://esperanto.mv.ru/Download/dict-eo.oxt
URL: http://esperanto.mv.ru/Download/
License: GPL-3.0-or-later
BuildArch: noarch

%description
Esperanto thesaurus.

%package -n hyphen-eo
Summary: Esperanto hyphen rules
Requires: hyphen
Supplements: (hyphen and langpacks-eo)

%description -n hyphen-eo
Esperanto hyphenation rules.

%prep
%autosetup -c

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p dictionaries/hyph_eo.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen/

mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p dictionaries/th_eo.dat $RPM_BUILD_ROOT/%{_datadir}/mythes/th_eo.dat
cp -p dictionaries/th_eo.idx $RPM_BUILD_ROOT/%{_datadir}/mythes/th_eo.idx

%files
%doc description/desc_en.txt
%license licenses/license-en.txt
%{_datadir}/mythes/*

%files -n hyphen-eo
%doc description/desc_en.txt
%license licenses/license-en.txt
%{_datadir}/hyphen/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.%{upstreamid}-18
- Prepare for Oreon 11 (RP1)
