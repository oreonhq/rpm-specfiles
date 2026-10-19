%global source0_hash 26f00d4afcb70b5839047bc6f62e4253073ac437bdb526f01e8c04b220e97762
%global _hardened_build 1
Name:           pdfcrack
Version:        0.21
Release:        1%{?dist}
Summary:        A Password Recovery Tool for PDF files
License:        GPL-2.0-or-later
URL:            http://pdfcrack.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
PDFCrack is a GNU/Linux tool for recovering passwords and content
from PDF-files. It is small, command line driven without external
dependencies.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%make_build
%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}/
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -pm0755 %{name} $RPM_BUILD_ROOT%{_bindir}/
install -pm0644 %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1/
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
