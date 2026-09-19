%global source0_hash 3a1a9d3dbd16bed3c686eca177a0c00059e266d1d7758cdffedd05130f835d07

Name:           keychecker
Version:        1.0
Release:        23%{?dist}
Summary:        Generate list of installed packages sorted by GPG key
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/jds2001/keychecker
Source0:        %{url}/archive/v%{version}.tar.gz

# https://github.com/jds2001/keychecker/pull/2
Patch0:         0001-Fix-rpm-4.15-compatibility.patch

BuildArch:      noarch
%if %{undefined el7}
Requires:       python3-rpm
%else
Requires:       rpm-python
%endif

%description
Separately list rpm's based on the GPG key they were signed with

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1
%if %{undefined el7}
sed -e '1 s|python|python3|' -i key_checker.py
%endif

%install
install -Dpm 0755 key_checker.py %{buildroot}%{_bindir}/keychecker

%files
%license LICENSE
%doc README
%{_bindir}/keychecker

%changelog
%autochangelog
