%global source0_hash e23ddcd94c4c65284f8b68c00ce8500dbfaba4a4dbb7a9c264732a1ae264380e

Name:           pem
Version:        0.7.9
Release:        31%{?dist}
Summary:        Personal Expenses Manager

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only 
URL:            http://pjp.dgplug.org/tools/ 
Source0:        http://pjp.dgplug.org/tools/%{name}-%{version}.tar.gz 

BuildArch:      noarch
BuildRequires: make
BuildRequires:      perl-generators
Requires:       perl-interpreter

%description
GNU Pem, is a personal expenses manager. Pem lets keep track of
personal income and expense in an extremely elegant manner.
On Linux like systems, Pem works by storing the details in
a CSV file, placed in the  ~/.pem directory under your $HOME
directory; On Windows, the same file is placed in pem directory,
under the USERPROFILE directory. Each such file is named after
the current month, and is automatically created by Pem when you
enter the first record  for the month. It is not advisable to
edit these files by hand.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT/%{_infodir}/dir

%files
%doc README COPYING
%{_bindir}/pem
%{_mandir}/man1/pem.*
%{_infodir}/pem.*
%{_datadir}/pem/pem.txt

%changelog
%autochangelog
