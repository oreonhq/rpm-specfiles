%global source0_hash none
%global source1_hash none

Name: hyphen-pt
Summary: Portuguese hyphenation rules
%global upstreamid 20140727
Version: 0.%{upstreamid}
Release: 13%{?dist}
# latest seen in Hifenizador section of https://download.documentfoundation.org/libreoffice/src/projetos/vero/
Source0:        https://deb.debian.org/debian/pool/main/libr/libreoffice-dictionaries/libreoffice-dictionaries_25.2.3.orig.tar.xz#/libreoffice-dictionaries-25.2.3.tar.xz
# The contents of Source1 are the same rules that are currently (2022-05-16) in
# use for pt-PT at https://cgit.freedesktop.org/libreoffice/dictionaries/tree/pt_PT
# so we continue to use those rules in the absence of a contrary opinion
Source1:        hyph_pt_PT.zip
URL: https://download.documentfoundation.org/libreoffice/src/projetos/vero/
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n libreoffice-25.2.3.2

# Fix world writable permission on files
chmod 644 dictionaries/pt_PT/hyph_pt_PT.dic dictionaries/pt_PT/README_hyph_pt_PT.txt dictionaries/pt_BR/hyph_pt_BR.dic dictionaries/pt_BR/README_hyph_pt_BR.txt

for i in dictionaries/pt_BR/README_hyph_pt_BR.txt; do
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
cp -p dictionaries/pt_PT/hyph_pt_PT.dic dictionaries/pt_BR/hyph_pt_BR.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen
pushd $RPM_BUILD_ROOT/%{_datadir}/hyphen/
pt_PT_aliases="pt_AO"
for lang in $pt_PT_aliases; do
        ln -s hyph_pt_PT.dic "hyph_"$lang".dic"
done

%files
%doc dictionaries/pt_PT/README_hyph_pt_PT.txt
%{_datadir}/hyphen/hyph_pt_*.dic
%exclude %{_datadir}/hyphen/hyph_pt_BR.dic

%files BR
%doc dictionaries/pt_BR/README_hyph_pt_BR.txt
%{_datadir}/hyphen/hyph_pt_BR.dic

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.20140727-13
- Import
