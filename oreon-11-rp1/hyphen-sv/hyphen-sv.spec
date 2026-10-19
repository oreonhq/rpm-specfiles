%global source0_hash 8921687c36254b185f76ce8f32b380e8af75d663a70f2153cae6787bff5d2b5a
Name: hyphen-sv
Summary:        Swedish hyphenation rules
Version: 1.00.1
Release:        1%{?dist}
Source0:        https://downloads.sourceforge.net/project/aoo-extensions/1966/4/hyph_sv_se.oxt
URL: http://extensions.services.openoffice.org/node/1968
License: LGPL-2.1-or-later OR GPL-2.0-or-later
BuildArch: noarch
Requires: hyphen
Supplements: (hyphen and langpacks-sv)
# oreon:deps

# /oreon:deps
%description
Swedish hyphenation rules.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir hyphen-sv
%oreon_prep
%build

chmod -x *.dic *.txt
for i in README_sv_SE.txt; do
  if ! iconv -f utf-8 -t utf-8 -o /dev/null $i > /dev/null 2>&1; then
    iconv -f ISO-8859-1 -t UTF-8 $i > $i.new
    touch -r $i $i.new
    mv -f $i.new $i
  fi
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done
%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_sv_SE.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen
pushd $RPM_BUILD_ROOT/%{_datadir}/hyphen
sv_SE_aliases="sv_FI"
for lang in $sv_SE_aliases; do
        ln -s hyph_sv_SE.dic hyph_$lang.dic
done
popd
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.00.1-38
- Prepare for Oreon 11 (RP1)
