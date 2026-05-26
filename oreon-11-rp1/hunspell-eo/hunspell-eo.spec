%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-eo
Summary: Esperanto hunspell dictionaries
%global upstreamid 20100218
Version: 0.%{upstreamid}
Epoch: 1
Release: 19%{?dist}
Source: http://www.esperantilo.org/literumilo-fontoj.tar.gz
# oreon url source checksums begin
%global source0_sha256 a02697a885da3655c55c15eb155148b79d25ca57c5ac7578cb1ca9ac8f141b89
%global source0_file literumilo-fontoj.tar.gz
# oreon url source checksums end
URL: http://www.esperantilo.org
License: GPL-2.0-or-later
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-eo)

%description
Esperanto hunspell dictionaries.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/literumilo-fontoj.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "a02697a885da3655c55c15eb155148b79d25ca57c5ac7578cb1ca9ac8f141b89" || { echo "oreon: Source0 SHA256 mismatch for literumilo-fontoj.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -n literumilo-fontoj

%build
chmod -x *
for i in LEGUMIN.txt; do
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p eo_morf.dic $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/eo.dic
cp -p eo_morf.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/eo.aff


%files
%doc LEGUMIN.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.%{upstreamid}-19
- Prepare for Oreon 11 (RP1)
