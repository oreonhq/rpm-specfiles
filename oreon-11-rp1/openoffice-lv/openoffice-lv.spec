%global source0_hash none

%if 0%{?rhel} && 0%{?rhel} > 9
%bcond_with mythes
%else
%bcond_without mythes
%endif

Name: openoffice-lv
Summary: Latvian linguistic dictionaries
Version: 1.4.0
Release: 12%{?dist}
Source: http://dict.dv.lv/download/lv_LV-%{version}.oxt
URL: http://dict.dv.lv/
License: LGPL-2.1-or-later
BuildArch: noarch

%description
Latvian linguistic dictionaries.

%package -n hunspell-lv
Summary: Latvian hunspell dictionaries
Requires: hunspell

%description -n hunspell-lv
Latvian hunspell dictionaries.

%package -n hyphen-lv
Summary: Latvian hyphenation rules
Requires: hyphen

%description -n hyphen-lv
Latvian hyphenation rules.

%if %{with mythes}
%package -n mythes-lv
Summary: Latvian thesaurus
Requires: mythes

%description -n mythes-lv
Latvian thesaurus.
%endif

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -c

%build
for i in README_lv_LV.txt README_hyph_lv_LV.txt; do
  if ! iconv -f utf-8 -t utf-8 -o /dev/null $i > /dev/null 2>&1; then
    iconv -f ISO-8859-4 -t UTF-8 $i > $i.new
    touch -r $i $i.new
    mv -f $i.new $i
  fi
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hunspell
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p lv_LV.dic lv_LV.aff $RPM_BUILD_ROOT/%{_datadir}/hunspell
cp -p hyph_lv_LV.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen

%if %{with mythes}
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p th_lv_LV_v2.* $RPM_BUILD_ROOT/%{_datadir}/mythes
%endif

%files -n hunspell-lv
%doc README_lv_LV.txt
%license license.txt
%{_datadir}/hunspell/*

%files -n hyphen-lv
%doc README_hyph_lv_LV.txt
%license license.txt
%{_datadir}/hyphen/*

%if %{with mythes}
%files -n mythes-lv
%doc package-description.txt
%license license.txt
%{_datadir}/mythes/*
%endif

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.4.0-12
- Prepare for Oreon 11 (RP1)
