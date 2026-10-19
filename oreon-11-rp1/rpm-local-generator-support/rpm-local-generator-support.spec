%global source0_hash none
Summary:        RPM local_generator support
Name: rpm-local-generator-support
Version: 1
Release:        1%{?dist}
License: GPL-2.0-or-later
URL: https://src.fedoraproject.org/rpms/rpm-local-generator-support
Source1: README.md
BuildArch: noarch
# oreon:deps

# /oreon:deps
%description
local_generator.attr file enabling RPM dependency generator to be used on .spec
files, which ships them.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%build

%install
cp %{SOURCE1} .
install -d %{buildroot}%{_fileattrsdir}
touch %{buildroot}%{_fileattrsdir}/local_generator.attr
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1-9
- Prepare for Oreon 11 (RP1)
