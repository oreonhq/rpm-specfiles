%global source0_hash 088b58d66c420e5eddc51327caec8dcbe8bddae557c308aa739231ed0490db01

Name:		git-ftp		
Version:	1.6.0
Release:	14%{?dist}
Summary:	Git powered FTP client written as shell script
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:	GPL-3.0-only	
URL:		https://github.com/git-ftp
Source0:	https://github.com/git-ftp/git-ftp/archive/%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	pandoc
BuildRequires:	man-db
BuildRequires: make
Requires:	git
Requires:	curl	

%description
A shell script for pushing git tracked changed files to a 
remote host by FTP

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{name}-%{version}

%build
#Nothing to build 

%install
make install-all  bindir=%{buildroot}%{_bindir} mandir=%{buildroot}%{_mandir}/man1

%check
# The testing environment expects to have Xampp installed 
# not applicable in this case

%files
%doc LICENSE README.md AUTHORS CHANGELOG.md
%{_bindir}/%{name}
%{_mandir}/man1/git-ftp.1*
%exclude %{_mandir}/man1/CACHEDIR.TAG.gz

%changelog
%autochangelog
