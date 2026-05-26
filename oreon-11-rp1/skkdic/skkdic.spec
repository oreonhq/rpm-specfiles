%global         githash     b798a46b886f71c0c25ad2a9e78b1c3e8933970c
%global         shorthash   %(TMP=%githash ; echo ${TMP:0:10})
%global         gitdate     Wed Jan 31 21:19:24 2024 +0900
%global         gitdate_num 20240131

%global         githash_tools     0fe2106fbc052445c611e6c5b2a79899d740edcb

%global         baserelease       6

%undefine        _changelog_trimtime

Summary:	Dictionaries for SKK (Simple Kana-Kanji conversion program)
Name:		skkdic
Version:	%{gitdate_num}
Release:	%{baserelease}.git%{shorthash}%{?dist}
# See Source2
# Automatically converted from old format: GPLv2+ and CC-BY-SA and Unicode and Public Domain and MIT - review is highly recommended.
License:	GPL-2.0-or-later AND LicenseRef-Callaway-CC-BY-SA AND Unicode-DFS-2015 AND LicenseRef-Callaway-Public-Domain AND LicenseRef-Callaway-MIT

Source0:	https://github.com/skk-dev/dict/archive/%{githash}/%{name}-%{gitdate_num}.git%{githash}.tar.gz
Source1:	https://raw.githubusercontent.com/skk-dev/skktools/%{githash_tools}/unannotation.awk
Source2:	license-investigation.txt
Source200:	README-skkdic.rh.ja
# oreon url source checksums begin
%global source0_sha256 59b32e1a664ac8ed90f2ef8558f3d26eabeaa4e9de930b5b0ce9d3b85ed928cf
%global source0_file skkdic-20240131.gitb798a46b886f71c0c25ad2a9e78b1c3e8933970c.tar.gz
# oreon url source checksums end

URL:		https://skk-dev.github.io/dict/
BuildArch:	noarch

BuildRequires: make

%description
This package includes the SKK dictionaries, including the large dictionary
SKK-JISYO.L and pubdic+ dictionary.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/skkdic-20240131.gitb798a46b886f71c0c25ad2a9e78b1c3e8933970c.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "59b32e1a664ac8ed90f2ef8558f3d26eabeaa4e9de930b5b0ce9d3b85ed928cf" || { echo "oreon: Source0 SHA256 mismatch for skkdic-20240131.gitb798a46b886f71c0c25ad2a9e78b1c3e8933970c.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -c -T -a 0
ln -sf dict-%{githash} src
mkdir tools

cp -p %SOURCE200 .
cp -p %SOURCE1 tools

pushd src
cp -a zipcode/README.md zipcode/README-zipcode.md
popd

%build
pushd src

for dic in \
	SKK-JISYO.L.unannotated \
	SKK-JISYO.wrong
do
	rm -f $dic
	make $dic
done

popd

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/skk

pushd src
for f in SKK-JISYO* zipcode/SKK-JISYO*
do
	install -p -m 644 $f $RPM_BUILD_ROOT%{_datadir}/skk
done
gzip -9 ChangeLog

popd

%files
%doc	src/ChangeLog.gz
%doc	README-skkdic.rh.ja
%doc	src/committers.md
%doc	src/edict_doc.html
%doc	src/zipcode/README-zipcode.md

%{_datadir}/skk/

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 20240131-6.gitb798a46b88
- Import
