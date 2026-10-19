%global source2_hash 6c8dfecfc81c901404013798978c18d9c53a72e065824b4d96ee7ea1c9156477
%global source1_hash 71fb1f93061fe0a422b6ce10a0c0cb2988513ea776319e099f3f30109e11f7bb
%global source0_hash 31fdbdb449c7143cd2968567bef7599e9f031950e6158ee7bb76e40aebf6ffb8
Summary:        A tool for monitoring the progress of data through a pipeline
Name: pv
Version: 1.12.0
Release:        1%{?dist}
License: GPL-3.0-or-later
URL: https://www.ivarch.com/programs/pv.shtml
Source0:        https://www.ivarch.com/programs/sources/%{name}-%{version}.tar.gz
Source1: https://www.ivarch.com/programs/sources/%{name}-%{version}.tar.gz.txt
Source2: https://www.ivarch.com/personal/public-key.txt
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gnupg2
BuildRequires:  make
# /oreon:deps
%description
PV ("Pipe Viewer") is a tool for monitoring the progress of data through a
pipeline.  It can be inserted into any normal pipeline between two processes
to give a visual indication of how quickly data is passing through, how long
it has taken, how near to completion it is, and an estimate of how long it
will be until completion.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build

%configure
%make_build
%install
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}         # /usr/bin
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man1    # /usr/share/man/man1
%make_install
%find_lang %{name}
rm -v ${RPM_BUILD_ROOT}%{_docdir}/%{name}/{COPYING,INSTALL}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
