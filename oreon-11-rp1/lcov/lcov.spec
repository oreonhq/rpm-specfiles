%global source0_hash 1857bb18e27abe8bcec701a907d5c47e01db4d4c512fc098d1a6acd29267bf46

Name: lcov
Version: 2.0
Release: 7%{?dist}

Summary: LTP GCOV extension code coverage tool
License: GPL-2.0-or-later

URL: https://github.com/linux-test-project/lcov/
Source0: https://github.com/linux-test-project/lcov/releases/download/v%{version}/lcov-%{version}.tar.gz

BuildArch: noarch
BuildRequires: perl-generators
BuildRequires: git-core
BuildRequires: make

Requires: /usr/bin/gcov
Requires: /usr/bin/find
Requires: perl(GD::Image)
Requires: perl(JSON::XS)

# lcovutil.pm is a private helper file
%global __requires_exclude ^perl\\(lcovutil\\)$
%global __provides_exclude ^perl.*$

%description
LCOV is an extension of GCOV, a GNU tool which provides information
about what parts of a program are actually executed (i.e. "covered")
while running a particular test case. The extension consists of a set
of PERL scripts which build on the textual GCOV output to implement
HTML output and support for large projects.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%install
make install DESTDIR=$RPM_BUILD_ROOT PREFIX=%{_prefix} \
     CFG_DIR=%{_sysconfdir} LIB_DIR=%{_datadir}/lcov

%files
%{_bindir}/gendesc
%{_bindir}/genhtml
%{_bindir}/geninfo
%{_bindir}/genpng
%{_bindir}/lcov
%{_mandir}/man1/gendesc.1*
%{_mandir}/man1/genhtml.1*
%{_mandir}/man1/geninfo.1*
%{_mandir}/man1/genpng.1*
%{_mandir}/man1/lcov.1*
%{_mandir}/man5/lcovrc.5*
%dir %{_datadir}/lcov
%dir %{_datadir}/lcov/support-scripts
%{_datadir}/lcov/lcovutil.pm
%{_datadir}/lcov/support-scripts/analyzeInfoFiles
%{_datadir}/lcov/support-scripts/criteria
%{_datadir}/lcov/support-scripts/get_signature
%{_datadir}/lcov/support-scripts/getp4version
%{_datadir}/lcov/support-scripts/gitblame
%{_datadir}/lcov/support-scripts/gitdiff
%{_datadir}/lcov/support-scripts/p4annotate
%{_datadir}/lcov/support-scripts/p4udiff
%{_datadir}/lcov/support-scripts/py2lcov
%{_datadir}/lcov/support-scripts/spreadsheet.py
%config(noreplace) %attr(0644,root,root) %{_sysconfdir}/lcovrc

%changelog
%autochangelog
