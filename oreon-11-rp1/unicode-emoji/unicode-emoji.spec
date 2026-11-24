# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash f7830d126f59d83842565d3dddedc79db4ca978ed52aee0ebcc040ea76a85519
%global source1_hash f1d8c9f7ab8b3f4286e539b7b186ec75b1b08326ee30176e7fa709b2d213e930
%global source2_hash 80d00f8e616a0ef27fd6b8de3b758c06383b5d917e2977709578e68baf733bf1
%global source3_hash 1823dce71f3dd9cb0ad1976797baee4ffbdc1909756f43af8ce4c57f732843a4
%global source4_hash 8f3735cda1f92a779d78af67cf86066bb1f07143dc22f2ac29394d9bc57ab21a
%global source5_hash ff1707564aa1f1b2fcf4ec92d609d4cb26940bc0d4dcf07f5328ad6879e84da3
%global source6_hash f61b5213bdf85a57741a9f903cb38d0f39a3d13be6ff4aca3b39857e859a9191
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global unicodedir %{_datadir}/unicode
%global emojidir %{unicodedir}/emoji

Name:           unicode-emoji
Version:        18.0.0
Release:        %{autorelease}
Summary:        Unicode Emoji Data Files

License:        Unicode-DFS-2016
URL:            http://www.unicode.org/emoji/
Source0:        https://www.unicode.org/license.txt
Source1:        https://www.unicode.org/Public/%{version}/ucd/emoji/ReadMe.txt
Source2:        https://www.unicode.org/Public/%{version}/ucd/emoji/emoji-data.txt
Source3:        https://www.unicode.org/Public/%{version}/emoji/emoji-sequences.txt
Source4:        https://www.unicode.org/Public/%{version}/emoji/emoji-test.txt
Source5:        https://www.unicode.org/Public/%{version}/ucd/emoji/emoji-variation-sequences.txt
Source6:        https://www.unicode.org/Public/%{version}/emoji/emoji-zwj-sequences.txt
BuildArch:      noarch

%description
Unicode Emoji Data Files are the machine-readable
emoji data files associated with
http://www.unicode.org/reports/tr51/index.html

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
echo '%{source2_hash}  %{SOURCE2}' | sha256sum -c -
echo '%{source3_hash}  %{SOURCE3}' | sha256sum -c -
echo '%{source4_hash}  %{SOURCE4}' | sha256sum -c -
echo '%{source5_hash}  %{SOURCE5}' | sha256sum -c -
echo '%{source6_hash}  %{SOURCE6}' | sha256sum -c -
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

%files
%license license.txt
%dir %{unicodedir}
%dir %{emojidir}
%doc %{emojidir}/ReadMe.txt
%{emojidir}/emoji-*txt

%changelog
%autochangelog
