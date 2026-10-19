%global source0_hash f644cb446ab5bed3fbeb0a6a468cadad00a1895fab7a6f98f590c8f1800bd6f6
Name:           pdfmerge
Version:        1.0.6
Release:        19%{?dist}
Summary:        Command line utility program for merging PDF files
License:        GPL-2.0-or-later
URL:            http://dmaphy.github.com/pdfmerge/
Source0:        https://github.com/dmaphy/%{name}/archive/%{version}.tar.gz
BuildArch:      noarch
Requires:       ghostscript, perl-interpreter  
# oreon:deps
BuildRequires:  perl-generators
# /oreon:deps
%description
pdfmerge is a command line program that merges PDF files. It can merge
any number of pdf files from command line.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -Dpm 755 %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
