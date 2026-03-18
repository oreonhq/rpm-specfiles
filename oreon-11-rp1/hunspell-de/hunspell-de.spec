Name:          hunspell-de
Summary:       German hunspell dictionaries
Version:       20240224
Release:       5%{?dist}

License:       GPL-2.0-only OR GPL-3.0-only
URL:           https://cgit.freedesktop.org/libreoffice/dictionaries/tree/de
# ./make_source.sh
Source0:       dict-de-%{version}.tar.xz
BuildArch:     noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-de)

%description
German (Germany, Switzerland, etc.) hunspell dictionaries.

%prep
%autosetup -p1 -n dict-de-%{version}


%build
# Nothing to build


%install
mkdir -p %{buildroot}%{_datadir}/hunspell

install -pm 0644 de_AT_frami.aff %{buildroot}%{_datadir}/hunspell/de_AT.aff
install -pm 0644 de_AT_frami.dic %{buildroot}%{_datadir}/hunspell/de_AT.dic

install -pm 0644 de_CH_frami.aff %{buildroot}%{_datadir}/hunspell/de_CH.aff
install -pm 0644 de_CH_frami.dic %{buildroot}%{_datadir}/hunspell/de_CH.dic
install -pm 0644 de_DE_frami.aff %{buildroot}%{_datadir}/hunspell/de_LI.aff
install -pm 0644 de_DE_frami.dic %{buildroot}%{_datadir}/hunspell/de_LI.dic

install -pm 0644 de_DE_frami.aff %{buildroot}%{_datadir}/hunspell/de_DE.aff
install -pm 0644 de_DE_frami.dic %{buildroot}%{_datadir}/hunspell/de_DE.dic
install -pm 0644 de_DE_frami.aff %{buildroot}%{_datadir}/hunspell/de_BE.aff
install -pm 0644 de_DE_frami.dic %{buildroot}%{_datadir}/hunspell/de_BE.dic
install -pm 0644 de_DE_frami.aff %{buildroot}%{_datadir}/hunspell/de_LU.aff
install -pm 0644 de_DE_frami.dic %{buildroot}%{_datadir}/hunspell/de_LU.dic


%files
%doc README_de_DE_frami.txt README_extension_owner.txt
%license COPYING_GPLv2 COPYING_GPLv3
%{_datadir}/hunspell/*


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 20240224-5
- Prepare for Oreon 11 (RP1)
