%global source0_hash 65a313a76fd5cc1c58c9e19fbc80fc0e418a4cbfbd46d54b35ed5b6e0025d4ee

%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

Name:           shunit2
Version:        2.1.6
Release:        31%{?dist}
Summary:        A xUnit based unit testing for Unix shell scripts

# Automatically converted from old format: LGPLv2 - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2
URL:            http://code.google.com/p/shunit2
Source0:        http://shunit2.googlecode.com/files/%{name}-%{version}.tgz
# add makefiles to do install
Source1:        LGPL-2.1
Patch0:         add_makefiles.patch
Patch1:         fix_examples_source_path.patch
BuildArch:      noarch

BuildRequires:  make

%description
shUnit2 is a xUnit unit test framework for Bourne based shell scripts,
and it is designed to work in a similar manner to JUnit, PyUnit, etc.
If you have ever had the desire to write a unit test for a shell script,
shUnit2 can do the job.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1
%patch -P1 -p1
iconv -f ISO88592 -t UTF8 doc/shunit2.txt -o doc/shunit2.txt
cp -p %{SOURCE1} doc/

%build
# This section is empty because this package ccontains shell scripts
# to be sourced: there's nothing to build

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} DOCDIR=%{_pkgdocdir}

%files
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_pkgdocdir}

%changelog
%autochangelog
