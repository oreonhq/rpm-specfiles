%if 0%{?fedora} > 35
%global dict_dirname hunspell 
%else
%global dict_dirname myspell
%endif
Name: hunspell-sq
Summary: Albanian hunspell dictionaries
Version: 1.6.4
Release: 31%{?dist}
Source: http://www.shkenca.org/shkarkime/myspell-sq_AL-%{version}.zip
# oreon url source checksums begin
%global source0_sha256 40f95495ddc790cd98b68d60b4686dcd5886f7db9ff3d06f8aa1dfd8c51dd02e
%global source0_file myspell-sq_AL-1.6.4.zip
# oreon url source checksums end
URL: http://www.shkenca.org/k6i/albanian_dictionary_for_myspell_en.html
License: GPL-2.0-or-later
BuildArch: noarch

Requires: hunspell
Supplements: (hunspell and langpacks-sq)

%description
Albanian hunspell dictionaries.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/myspell-sq_AL-1.6.4.zip; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "40f95495ddc790cd98b68d60b4686dcd5886f7db9ff3d06f8aa1dfd8c51dd02e" || { echo "oreon: Source0 SHA256 mismatch for myspell-sq_AL-1.6.4.zip" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n myspell-sq_AL-%{version}

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p sq_AL.* $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/


%files
%doc README.txt Copyright
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.6.4-31
- Prepare for Oreon 11 (RP1)
