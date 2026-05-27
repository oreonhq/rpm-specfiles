%global source0_hash none

Summary: RPM local_generator support
Name: rpm-local-generator-support
Version: 1
Release: 9%{?dist}

# It is not really clear if the one empty file shipped by this package is even
# copyrightable. But let's go with GPLv2+ which is the license used by RPM,
# where this file should ideally come from or be replaced by different
# implementation.
#
# The license was discussed in this thread:
# https://lists.fedoraproject.org/archives/list/legal@lists.fedoraproject.org/thread/X6RUQK5R6KIMVIQ6FQPNVGTJJXSNRD4V/
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: https://src.fedoraproject.org/rpms/rpm-local-generator-support
Source1: README.md
BuildArch: noarch

%description
local_generator.attr file enabling RPM dependency generator to be used on .spec
files, which ships them.



%prep


%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%build


%install
cp %{SOURCE1} .

install -d %{buildroot}%{_fileattrsdir}
touch %{buildroot}%{_fileattrsdir}/local_generator.attr


%files
%doc README.md
%{_fileattrsdir}/local_generator.attr



%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1-9
- Prepare for Oreon 11 (RP1)
