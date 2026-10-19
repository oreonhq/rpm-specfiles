%global source0_hash d48b4c1976d866f6cf493340dc48e4c2b67d2394b6b5467ddc760b0f82466c4d
Name:           cvechecker
Version:        4.0
Release:        1%{?dist}
Summary:        Tool for compare packages installed in your system with CVE database
License:        GPL-3.0-only
URL:            https://github.com/sjvermeu/cvechecker
Source0:        https://github.com/sjvermeu/%{name}/archive/%{name}-%{version}/%{name}-%{version}.tar.gz
Patch0:         cvechecker-c99.patch
Requires:       jq
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libconfig-devel
BuildRequires:  make
BuildRequires:  mariadb-connector-c-devel
BuildRequires:  openssl-devel
BuildRequires:  pkgconf
BuildRequires:  pkgconfig(libbsd)
BuildRequires:  sqlite-devel
BuildRequires:  xmlto
# /oreon:deps
%description
The goal of cvechecker is to report about possible vulnerabilities on your
system, by scanning a list of installed software and matching results with the
CVE database.
This is not a bullet-proof method and you will have many false positives
(i.e.: vulnerability is fixed with a revision-release, but the tool isn't able
to detect the revision itself).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{name}-%{version}
%oreon_prep
%build

autoreconf --force --install
%configure --enable-sqlite3 --enable-mysql --localstatedir=%{_sharedstatedir}
sed -i 's/\/mysql/\/mariadb/g;s/-lmysqlclient/-lmariadb/g' Makefile
%make_build
%install
%make_install PREFIX="%{_prefix}"  CONFDIR="%{buildroot}%{_sysconfdir}"
xmlto --skip-validation html-nochunks %{buildroot}%{_docdir}/cvechecker/acknowledgements.xml 
xmlto --skip-validation html-nochunks %{buildroot}%{_docdir}/cvechecker/userguide.xml
install -Dm644 userguide.html  %{buildroot}%{_docdir}/cvechecker/userguide.html
install -Dm644 acknowledgements.html  %{buildroot}%{_docdir}/cvechecker/acknowledgements.html
rm -f %{buildroot}%{_docdir}/cvechecker/acknowledgements.xml %{buildroot}%{_docdir}/cvechecker/userguide.xml
%oreon_autofiles main

%check

make check
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
