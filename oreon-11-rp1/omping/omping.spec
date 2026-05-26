Name: omping
Version: 0.0.4
Release: 36%{?dist}
Summary: Utility to test IP multicast functionality
License: ISC
URL: https://github.com/jfriesse/omping
Source0: https://github.com/jfriesse/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 8909616b007139138d9d1cb51cc234edaf728f20a26897ef2959a570da02dc0a
%global source0_file omping-0.0.4.tar.gz
# oreon url source checksums end

BuildRequires: gcc
BuildRequires: make
BuildRequires: git

%description
Omping (Open Multicast Ping) is tool to test IP multicast functionality
primarily in local network.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/omping-0.0.4.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "8909616b007139138d9d1cb51cc234edaf728f20a26897ef2959a570da02dc0a" || { echo "oreon: Source0 SHA256 mismatch for omping-0.0.4.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
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
