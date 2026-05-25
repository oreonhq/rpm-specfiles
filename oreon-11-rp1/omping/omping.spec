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
