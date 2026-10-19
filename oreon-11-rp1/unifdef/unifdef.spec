%global source0_hash 43ce0f02ecdcdc723b2475575563ddb192e988c886d368260bc0a63aee3ac400
Name:           unifdef
Version:        2.12
Release:        1%{?dist}
Summary:        Selectively remove C preprocessor conditionals
License:        BSD-2-Clause AND BSD-3-Clause
URL:            https://dotat.at/prog/unifdef/
%global forgeurl https://github.com/fanf2/unifdef
Source0:        https://dotat.at/prog/unifdef/unifdef-%{version}.tar.xz
Patch:        https://github.com/fanf2/unifdef/pull/14.patch
Patch:        https://github.com/fanf2/unifdef/pull/15.patch
Patch:        https://github.com/fanf2/unifdef/pull/19.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
The unifdef utility selectively processes conditional C preprocessor #if
and #ifdef directives. It removes from a file both the directives and the
additional text that they delimit, while otherwise leaving the file alone.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1
# Show that we do not use the sources in FreeBSD – even though this does not
# simplify the License, since unifdef.1 is still BSD-3-Clause.
rm -rv FreeBSD/

%build

%make_build
%install
%make_install prefix='%{_prefix}'
%oreon_autofiles main

%check

PATH="%{buildroot}%{_bindir}:${PATH}" %make_build test
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.12-1
- Prepare for Oreon 11 (RP1)
