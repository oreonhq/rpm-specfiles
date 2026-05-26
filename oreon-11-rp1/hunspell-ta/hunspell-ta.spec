%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-ta
Summary: Tamil hunspell dictionaries
Version: 1.0.0
Release: 28%{?dist}
Epoch:   1
Source: http://anishpatil.fedorapeople.org/ta_in.%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 59e76d6b16657bbcd4d85c9c379cd9d28f4bd5bbfe952c754f427949cc2f5db2
%global source0_file ta_in.1.0.0.tar.gz
# oreon url source checksums end
URL: https://gitorious.org/hunspell_dictionaries/hunspell_dictionaries.git
License: GPL-2.0-or-later
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-ta)

%description
Tamil hunspell dictionaries.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/ta_in.1.0.0.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "59e76d6b16657bbcd4d85c9c379cd9d28f4bd5bbfe952c754f427949cc2f5db2" || { echo "oreon: Source0 SHA256 mismatch for ta_in.1.0.0.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -c -n ta_IN

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p ta_IN/*.dic ta_IN/*.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}

%files
%doc ta_IN/README
%license ta_IN/LICENSE ta_IN/Copyright
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.0-28
- Prepare for Oreon 11 (RP1)
