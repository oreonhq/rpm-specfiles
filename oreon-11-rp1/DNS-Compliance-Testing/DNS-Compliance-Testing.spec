%global source0_hash 3189531662915203bed16be8c82132e172303b2af17070f5b3dfe6b9b4c3e148
%global commit 4aea40ba0310de10560ba6deaa2d2e6eebbe8f48
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date 20230708
%global snapver %{date}git%{shortcommit}
%bcond_with ronn
Name:		DNS-Compliance-Testing
Version:	0%{?snapver:^%snapver}
Release:        1%{?dist}
Summary:        DNS Compliance Testing command line tool
License:	MPL-2.0
URL:		https://gitlab.isc.org/isc-projects/DNS-Compliance-Testing
Source0:        https://gitlab.isc.org/isc-projects/%{name}/-/archive/4aea40b/%{name}-4aea40b.tar.bz2
Source1:	mkronn.sed
Source2:	Makefile.doc
Patch1:		0001-Detect-few-functions-presence-in-libresolv.patch
%if %{with ronn}
%endif
Requires:	bind-utils
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  rubygem-ronn
BuildRequires:  sed
# /oreon:deps
%description
Provide tools to allow Registries and Registrars (amongst others) to
check the DNS protocol compliance of the servers they are delegating
zones to.

Offers genreport command line tool. Can test both authoritative and
recursive servers.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{shortcommit} -p1
echo "Source: date $(date "+%04Y%02m%02d" -r %{SOURCE0})"

%if %{with ronn}
	install %{SOURCE1} mkronn.sed
	install %{SOURCE2} Makefile.doc
%endif

%build

autoreconf -fis
%configure
%make_build
%if %{with ronn}
	make -f %{SOURCE2} man
%endif
%install
%make_install
%if %{with ronn}
	install -d %{buildroot}%{_mandir}/man1
	install -p -m 0644 genreport.1 %{buildroot}%{_mandir}/man1/genreport.1
%oreon_autofiles main
%endif
%check

%{buildroot}%{_bindir}/genreport -D
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
