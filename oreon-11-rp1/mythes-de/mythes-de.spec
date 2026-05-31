%global source0_hash none

%global upstreamid 20240601

Summary:        German thesaurus
Name:           mythes-de
Version:        0.%{upstreamid}
Release:        5%{?dist}
License:        LGPL-2.1-or-later OR CC-BY-SA-4.0
URL:            https://www.openthesaurus.de/
Source0:        https://www.openthesaurus.de/export/Deutscher-Thesaurus.oxt
Source1:        https://www.openthesaurus.de/export/Schweizer-Thesaurus.oxt
BuildArch:      noarch
Requires:       mythes
%if 0%{?fedora} || 0%{?rhel} > 7
Supplements:    (mythes and langpacks-de)
%endif

%description
German thesaurus.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -c
rm -rf mythes-ch-%{upstreamid}
mkdir mythes-ch-%{upstreamid}
cd mythes-ch-%{upstreamid}
unzip -q %{SOURCE1}

%build
for i in README.txt; do
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
mkdir -p $RPM_BUILD_ROOT%{_datadir}/mythes/
cp -p th_de_DE_v2.* $RPM_BUILD_ROOT%{_datadir}/mythes/
cp -p mythes-ch-%{upstreamid}/th_de_DE_v2.idx $RPM_BUILD_ROOT%{_datadir}/mythes/th_de_CH_v2.idx
cp -p mythes-ch-%{upstreamid}/th_de_DE_v2.dat $RPM_BUILD_ROOT%{_datadir}/mythes/th_de_CH_v2.dat

pushd $RPM_BUILD_ROOT%{_datadir}/mythes/
  de_DE_aliases="de_AT de_BE de_LI de_LU"
  for lang in $de_DE_aliases; do
    ln -s th_de_DE_v2.idx "th_"$lang"_v2.idx"
    ln -s th_de_DE_v2.dat "th_"$lang"_v2.dat"
  done
popd

%files
%doc README.txt
%{_datadir}/mythes/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.%{upstreamid}-5
- Prepare for Oreon 11 (RP1)
