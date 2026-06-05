%global source0_hash 6dfe0c5de0f2ff71d2183b2ee8765c79737e544151fae61e037dd21386f2fa3d

%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-ga
Summary: Irish hunspell dictionaries
Version: 5.1
Release: 10%{?dist}
URL: https://cadhan.com/gaelspell/
License: GPL-2.0-or-later
BuildArch: noarch
BuildRequires: make
BuildRequires: hunspell-devel

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-ga)

Patch0: ispell-gaeilge-5.0-buildhunspell.patch
Source1: myspell-header
Source2: hunspell-header
Source0:        https://github.com/kscanne/gaelspell/releases/download/v5.0/ispell-gaeilge-5.0.tar.gz

%description
Irish hunspell dictionaries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n ispell-gaeilge-5.0
%patch -p0 -i %{PATCH0}

%build
make
cat %{SOURCE1} %{SOURCE2} > header
export LANG=en_IE.UTF-8
iconv -f utf-8 -t iso-8859-1 < gaeilge.aff > gaeilge.aff.iso-8859-1
ispellaff2myspell gaeilge.aff.iso-8859-1 --myheader header | sed -e "s/\"\"/0/g" | sed -e "s/\"//g" > ga_IE.aff

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p ga_IE.dic ga_IE.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}

%files
%doc README ChangeLog
%license COPYING
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.1-10
- Prepare for Oreon 11 (RP1)
