%global source0_hash 84988748a48ee952607fe93344589f72befe1a5dbecebdc15612adf287941ce6

%global commit d79eacf77abe3b799387bb8a4e07a18f1f1031e8
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date 20250123

Name: compsize
Version: 1.5^git%{date}.%{shortcommit}
Release: 15%{?dist}
Summary: Utility for measuring compression ratio of files on btrfs
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: https://github.com/kilobyte/compsize
Source: https://github.com/kilobyte/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz   
# https://github.com/kilobyte/compsize/pull/54
Patch: %{name}-1.5_fix_includes.patch
BuildRequires: gcc
BuildRequires: btrfs-progs-devel
BuildRequires: make

%description
compsize takes a list of files (given as arguments) on a btrfs filesystem and
measures used compression types and effective compression ratio, producing
a report.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{commit}

%build
%set_build_flags
%make_build

%install
install -D -m 0755 %{name} %{buildroot}%{_bindir}/%{name}
install -D -m 0644 %{name}.8 %{buildroot}%{_mandir}/man8/%{name}.8

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man8/%{name}.8*

%changelog
%autochangelog
