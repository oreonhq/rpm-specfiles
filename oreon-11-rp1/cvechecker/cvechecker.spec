%global source0_hash d48b4c1976d866f6cf493340dc48e4c2b67d2394b6b5467ddc760b0f82466c4d

# commit
# Use a commit newer than 3.8 release for pulling in some bugfixes
#%%global _commit 0f1ae263b8279e8cca103cf28ae37ab20340ec04
#%%global _shortcommit %%(c=%%{_commit}; echo ${c:0:7})

Name:           cvechecker
Version:        4.0
Release:        18%{?dist}
Summary:        Tool for compare packages installed in your system with CVE database
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            https://github.com/sjvermeu/cvechecker
#Source0:       %%{url}/archive/%%{_commit}/%%{_commit}.tar.gz
#Source0:        %%{name}/archive/%%{version}/%%{name}-%%{version}.tar.gz
# The developer marked the version "cvechecker-4.0" instead of 4.0, so we need to hack the URL
Source0:        %{url}/archive/%{name}-%{version}/%{name}-%{version}.tar.gz
Patch0:         cvechecker-c99.patch
BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  pkgconf
BuildRequires:  libconfig-devel
BuildRequires:  mariadb-connector-c-devel
BuildRequires:  openssl-devel
BuildRequires:  sqlite-devel
BuildRequires:  xmlto
BuildRequires:  pkgconfig(libbsd)
BuildRequires: make
Requires:       jq

%description
The goal of cvechecker is to report about possible vulnerabilities on your
system, by scanning a list of installed software and matching results with the
CVE database.
This is not a bullet-proof method and you will have many false positives
(i.e.: vulnerability is fixed with a revision-release, but the tool isn't able
to detect the revision itself).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# The developer marked the version "cvechecker-4.0" instead of 4.0, so we need to specify the folder name
# https://github.com/sjvermeu/cvechecker/issues/49
%autosetup -p1 -n %{name}-%{name}-%{version}

%build
autoreconf --force --install
%configure --enable-sqlite3 --enable-mysql --localstatedir=%{_sharedstatedir}
sed -i 's/\/mysql/\/mariadb/g;s/-lmysqlclient/-lmariadb/g' Makefile

%make_build

%install
%make_install PREFIX="%{_prefix}"  CONFDIR="%{buildroot}%{_sysconfdir}"
xmlto --skip-validation html-nochunks %{buildroot}%{_docdir}/cvechecker/acknowledgements.xml 
xmlto --skip-validation html-nochunks %{buildroot}%{_docdir}/cvechecker/userguide.xml
#/usr/share/doc/cvechecker/
install -Dm644 userguide.html  %{buildroot}%{_docdir}/cvechecker/userguide.html
install -Dm644 acknowledgements.html  %{buildroot}%{_docdir}/cvechecker/acknowledgements.html
rm -f %{buildroot}%{_docdir}/cvechecker/acknowledgements.xml %{buildroot}%{_docdir}/cvechecker/userguide.xml

%check
make check

%files
%doc README.md
%doc ChangeLog
%{_docdir}/cvechecker/acknowledgements.html
%{_docdir}/cvechecker/userguide.html
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/cvechecker.conf
%{_bindir}/*
%attr(0644,root,root) %{_mandir}/man1/*
%{_datadir}/cvechecker
%{_sharedstatedir}/cvechecker/*

%changelog
%autochangelog
