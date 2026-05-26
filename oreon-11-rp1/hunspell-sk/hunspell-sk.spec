%if 0%{?fedora} > 35
%global dict_dirname hunspell 
%else
%global dict_dirname myspell
%endif
Name: hunspell-sk
Summary: Slovak hunspell dictionaries
Epoch: 1
%global upstreamid 20110228
Version: 0.%{upstreamid}
Release: 31%{?dist}
Source: http://www.sk-spell.sk.cx/files/hunspell-sk-%{upstreamid}.zip
# oreon url source checksums begin
%global source0_sha256 216ad718fc761bd3a95c9271d8e1cfdf0e0d5967093da9e0ba4a7cfabbfd90c6
%global source0_file hunspell-sk-20110228.zip
# oreon url source checksums end
URL: http://www.sk-spell.sk.cx/
License: LGPL-2.1-only OR GPL-2.0-only OR MPL-1.1
BuildArch: noarch

Requires: hunspell
Supplements: (hunspell and langpacks-sk)

%description
Slovak hunspell dictionaries.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/hunspell-sk-20110228.zip; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "216ad718fc761bd3a95c9271d8e1cfdf0e0d5967093da9e0ba4a7cfabbfd90c6" || { echo "oreon: Source0 SHA256 mismatch for hunspell-sk-20110228.zip" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n %{name}-%{upstreamid}

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}


%files
%doc doc/*
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.%{upstreamid}-31
- Prepare for Oreon 11 (RP1)
