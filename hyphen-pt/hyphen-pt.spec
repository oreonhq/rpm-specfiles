Name: hyphen-pt
Summary: Portuguese hyphenation rules
%global upstreamid 20140727
Version: 0.%{upstreamid}
Release: 13%{?dist}
# latest seen in Hifenizador section of https://pt-br.libreoffice.org/projetos/vero/
Source0: https://pt-br.libreoffice.org/assets/Uploads/PT-BR-Documents/VERO/hyphptBR-213.zip
# The contents of Source1 are the same rules that are currently (2022-05-16) in
# use for pt-PT at https://cgit.freedesktop.org/libreoffice/dictionaries/tree/pt_PT
# so we continue to use those rules in the absence of a contrary opinion
Source1: http://download.services.openoffice.org/contrib/dictionaries/hyph_pt_PT.zip
URL: https://pt-br.libreoffice.org/projetos/vero/
License: LGPL-3.0-only AND GPL-1.0-or-later
BuildArch: noarch

Requires: hyphen
Supplements: (hyphen and langpacks-pt)

%description
Portuguese hyphenation rules.

%package BR
Summary: Brazilian Portuguese hyphenation rules
Requires: hyphen
Supplements: (hyphen and langpacks-pt_BR)

%description BR
Brazilian Portuguese hyphenation rules.

%prep
%autosetup -c
unzip -q -o %{SOURCE1}

# Fix world writable permission on files
chmod 644 hyph_pt_PT.dic README_hyph_pt_PT.txt

for i in README_hyph_pt_BR.txt; do
  if ! iconv -f utf-8 -t utf-8 -o /dev/null $i > /dev/null 2>&1; then
    iconv -f ISO-8859-1 -t UTF-8 $i > $i.new
    touch -r $i $i.new
    mv -f $i.new $i
  fi
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done


%build
#nothing to build here

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p *.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen
pushd $RPM_BUILD_ROOT/%{_datadir}/hyphen/
pt_PT_aliases="pt_AO"
for lang in $pt_PT_aliases; do
        ln -s hyph_pt_PT.dic "hyph_"$lang".dic"
done

%files
%doc README_hyph_pt_PT.txt
%{_datadir}/hyphen/hyph_pt_*.dic
%exclude %{_datadir}/hyphen/hyph_pt_BR.dic

%files BR
%doc README_hyph_pt_BR.txt
%{_datadir}/hyphen/hyph_pt_BR.dic

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.%{upstreamid}-13
- Prepare for Oreon 11 (RP1)
