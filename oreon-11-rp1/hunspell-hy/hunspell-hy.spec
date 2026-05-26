%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-hy
Summary: Armenian hunspell dictionaries
Version: 0.20.0
Release: 32%{?dist}
Source: http://downloads.sourceforge.net/armspell/myspell-hy-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 aaf9880bff7091a613f7130f6d02abb93ba5eff5797c7f185c594d9d74046107
%global source0_file myspell-hy-0.20.0.tar.gz
# oreon url source checksums end
URL: http://sourceforge.net/projects/armspell
License: GPL-2.0-or-later
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-hy)

%description
Armenian hunspell dictionaries.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/myspell-hy-0.20.0.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "aaf9880bff7091a613f7130f6d02abb93ba5eff5797c7f185c594d9d74046107" || { echo "oreon: Source0 SHA256 mismatch for myspell-hy-0.20.0.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n myspell-hy-%{version}

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p hy_AM.* $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/


%files
%doc Copyright ChangeLog COPYING
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.20.0-32
- Prepare for Oreon 11 (RP1)
