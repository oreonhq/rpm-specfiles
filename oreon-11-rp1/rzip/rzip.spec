%global source0_hash 4bb96f4d58ccf16749ed3f836957ce97dbcff3e3ee5fd50266229a48f89815b7

Name:           rzip
Version:        2.1
Release:        38%{?dist}
Summary:        A large-file compression program
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://rzip.samba.org
Source0:        http://rzip.samba.org/ftp/rzip/%{name}-%{version}.tar.gz
Patch0:         rzip-configure.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  bzip2-devel

%description
rzip is a compression program, similar in functionality to gzip or
bzip2, but able to take advantage of long distance redundancies in
files, which can sometimes allow rzip to produce much better
compression ratios than other programs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
export CFLAGS="${RPM_OPT_FLAGS} -fPIE -pie"
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install INSTALL_BIN=$RPM_BUILD_ROOT%{_bindir} INSTALL_MAN=$RPM_BUILD_ROOT%{_mandir}

%files
%doc COPYING
%{_bindir}/rzip
%{_mandir}/man1/*

%changelog
%autochangelog
