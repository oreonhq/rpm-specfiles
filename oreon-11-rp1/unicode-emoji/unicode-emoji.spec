%global source6_hash 9a76a03dcacfcd8f9bfe08c49c8d90b55182b977cbcc87a694e8a8193efb0e57
%global source5_hash 8a67d0429a5831d91e744bc5170d43dc66ddccd42c6f532cbe421dc406b571fd
%global source4_hash d876ee249aa28eaa76cfa6dfaa702847a8d13b062aa488d465d0395ee8137ed9
%global source3_hash eb72c9115e3504fbbe1c8621b619f879471a46ccc56e2f445417b7c1cad050d1
%global source2_hash d7aef489c8fe4c14f09ea5695200277c6b93ac82ac60845cdd2161b0d6835cc1
%global source1_hash deae8f60470d2f4e3204b22979526a57ad1a9780fcaf3cb1344b505cd8a5013a
%global source0_hash e7a93b009565cfce55919a381437ac4db883e9da2126fa28b91d12732bc53d96
%global unicodedir %{_datadir}/unicode
%global emojidir %{unicodedir}/emoji
Name:           unicode-emoji
Version:        16.0
Release:        1%{?dist}
Summary:        Unicode Emoji Data Files
License:        Unicode-DFS-2016
URL:            http://www.unicode.org/emoji/
Source0:        https://www.unicode.org/license.txt
Source1:        https://www.unicode.org/Public/emoji/15.1/ReadMe.txt
Source2:        https://www.unicode.org/Public/15.1.0/ucd/emoji/emoji-data.txt
Source3:        https://www.unicode.org/Public/emoji/15.1/emoji-sequences.txt
Source4:        https://www.unicode.org/Public/emoji/15.1/emoji-test.txt
Source5:        https://www.unicode.org/Public/15.1.0/ucd/emoji/emoji-variation-sequences.txt
Source6:        https://www.unicode.org/Public/emoji/15.1/emoji-zwj-sequences.txt
BuildArch:      noarch
# oreon:deps

# /oreon:deps
%description
Unicode Emoji Data Files are the machine-readable
emoji data files associated with
http://www.unicode.org/reports/tr51/index.html

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%{nil}

%build

%{nil}
%install
cp -p %{SOURCE0} .
mkdir -p %{buildroot}%{emojidir}
cp -p %{SOURCE1} %{buildroot}%{emojidir}
cp -p %{SOURCE2} %{buildroot}%{emojidir}
cp -p %{SOURCE3} %{buildroot}%{emojidir}
cp -p %{SOURCE4} %{buildroot}%{emojidir}
cp -p %{SOURCE5} %{buildroot}%{emojidir}
cp -p %{SOURCE6} %{buildroot}%{emojidir}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 16.0-1
- Prepare for Oreon 11 (RP1)
