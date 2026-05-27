%global source0_hash 8909616b007139138d9d1cb51cc234edaf728f20a26897ef2959a570da02dc0a

Name: omping
Version: 0.0.4
Release: 36%{?dist}
Summary: Utility to test IP multicast functionality
License: ISC
URL: https://github.com/jfriesse/omping
Source0: https://github.com/jfriesse/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: make
BuildRequires: git

%description
Omping (Open Multicast Ping) is tool to test IP multicast functionality
primarily in local network.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -S git_am

%build
%set_build_flags
%make_build

%install
%make_install PREFIX="%{_prefix}"

%files
%doc AUTHORS
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man8/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.0.4-36
- Import
