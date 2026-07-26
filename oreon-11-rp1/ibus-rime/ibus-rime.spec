%global source0_hash 46022d7577dd2d0e10ff1c66a7c61c78b6f01bd80ceccb37106fba9c2bf1e63a

Name:           ibus-rime
Version:        1.6.0
Release:        2%{?dist}
Summary:        Rime Input Method Engine for IBus
Summary(zh):    中州韻輸入法引擎

License:        GPL-3.0-only
URL:            https://rime.im/
Source0:        https://github.com/rime/ibus-rime/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  pkgconfig, cmake
BuildRequires:  librime-devel >= 1.2
BuildRequires:  ibus-devel, libnotify-devel
BuildRequires:  brise >= 0.35
Requires:       brise >= 0.35

%description
ibus-rime: Rime Input Method Engine for IBus

Support for shape-based and phonetic-based input methods,
including those for Chinese dialects.

A selected dictionary in Traditional Chinese,
powered by opencc for Simplified Chinese output.

%description -l zh
中州韻輸入法引擎

中州韻輸入法引擎，思想用鍵盤表達也行。

Rime 預設輸入方案有：朙月拼音、語句流、倉頡、速成、五筆、雙拼、
地球拼音、注音、粵拼、吳語、中古漢語拼音、五筆畫、國際音標等。

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc README.md LICENSE CHANGELOG.md
%{_libexecdir}/ibus-rime/ibus-engine-rime
%{_datadir}/ibus/component/rime.xml
%{_datadir}/ibus-rime/
%{_datadir}/rime-data/ibus_rime.yaml

%changelog
%autochangelog
