%global source0_hash 94202a33bd6b19cc3c1cbf6a8e1779d7c72d8b3b48b96267f97d61ced4e1753f

Name: cdlabelgen
Summary: Generates frontcards and traycards for inserting in CD jewelcases
Version: 4.3.0
Release: 26%{?dist}
Source: http://www.aczoom.com/pub/tools/cdlabelgen-%{version}.tgz
URL: http://www.aczoom.com/tools/cdinsert/
# Automatically converted from old format: BSD with advertising - review is highly recommended.
License: LicenseRef-Callaway-BSD-with-advertising
BuildArch: noarch
BuildRequires: perl-generators

%description
Cdlabelgen is a utility which generates frontcards and traycards (in
PostScript(TM) format) for CD jewelcases.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
iconv -f iso8859-1 -t utf8 ChangeLog > ChangeLog.utf8 && \
touch -r ChangeLog ChangeLog.utf8 && \
mv ChangeLog.utf8 ChangeLog

%build
# nothing to build

%install
mkdir -p $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/cdlabelgen,%{_mandir}/man1}
install -pm755 cdlabelgen $RPM_BUILD_ROOT%{_bindir}/
install -pm644 postscript/* $RPM_BUILD_ROOT%{_datadir}/cdlabelgen/
install -pm644 cdlabelgen.1 $RPM_BUILD_ROOT%{_mandir}/man1/

%files
%doc ChangeLog README cdlabelgen.html
%{_bindir}/cdlabelgen
%{_datadir}/cdlabelgen/
%{_mandir}/man1/*

%changelog
%autochangelog
