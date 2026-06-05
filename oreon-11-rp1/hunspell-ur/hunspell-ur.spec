%global source0_hash ac112fadff1f5977965f6328170bdad7b20d1c0bdebeec933f10076fa143d2c6

%if 0%{?fedora} >= 36 || 0%{?rhel} > 9 || (0%{?oreon} >= 11)
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-ur
Summary: Urdu hunspell dictionaries
Version: 0.64
Release: 35%{?dist}
Source0:        https://github.com/gooselinux/hunspell-ur/raw/master/UrduDictionary.xpi
URL: http://urdudictionary.codeplex.com
License: LGPL-2.1-or-later
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-ur)

%description
Urdu hunspell dictionaries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -c -T -n %{name}-%{version}
unzip -q %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{_datadir}/%{dict_dirname}
install -pm 0644 dictionaries/ur.aff %{buildroot}%{_datadir}/%{dict_dirname}/ur_PK.aff
install -pm 0644 dictionaries/ur.dic %{buildroot}%{_datadir}/%{dict_dirname}/ur_PK.dic
pushd %{buildroot}%{_datadir}/%{dict_dirname}/
ln -s ur_PK.aff ur_IN.aff
ln -s ur_PK.dic ur_IN.dic
popd

%files
%{_datadir}/%{dict_dirname}/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.64-35
- Import
