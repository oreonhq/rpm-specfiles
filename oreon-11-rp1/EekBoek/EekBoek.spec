%global source0_hash 4c227030e653d039702cf372332ee114ce97aefaa796e0aa30cd6fdc2d0240fc
%define dbtests 1
%{?_with_dbtests:    %{expand: %%global dbtests 1}}
%{?_without_dbtests: %{expand: %%global dbtests 0}}
%define debug_package %{nil}
Name: EekBoek
Summary:        Bookkeeping software for small and medium-size businesses
License: GPL-1.0-or-later OR Artistic-1.0-Perl
Version: 2.051
Release:        15%{?dist}
Source0:        https://www.eekboek.nl/dl/%{name}-%{version}.tar.gz
URL: https://www.eekboek.nl
%global lcname eekboek
BuildArch: noarch
AutoReqProv: 0
Requires: perl-interpreter
Requires: perl-generators
Requires: perl(:VERSION) >= 5.10.1
Requires: perl(Archive::Zip)
Requires: perl(HTML::Parser)
Requires: perl(Term::ReadLine)
Requires: perl(Term::ReadLine::Gnu)
Requires: perl(DBI) >= 1.40
Requires: perl(DBD::SQLite) >= 1.12
Requires: perl(App::Packager) >= 1.430
Obsoletes: %{name}-core < 2.00.01
Obsoletes: %{name}-contrib < 2.00.01
Conflicts: %{name}-core < 2.00.01
%global __zip   /usr/bin/zip
%global __rmdir /bin/rmdir
%global __find  /usr/bin/find
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  make
BuildRequires:  perl(App::Packager)
BuildRequires:  perl(Archive::Zip)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBI)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTML::Parser)
BuildRequires:  perl(IPC::Run3)
BuildRequires:  perl(Term::ReadLine)
BuildRequires:  perl(Term::ReadLine::Gnu)
BuildRequires:  perl(Test::More)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  zip
# /oreon:deps
%description
EekBoek is a bookkeeping package for small and medium-size businesses.
Unlike other accounting software, EekBoek has both a command-line
interface (CLI) and a graphical user-interface (GUI, currently under
development and not included in this package). Furthermore, it has a
complete Perl API to create your own custom applications. EekBoek is
designed for the Dutch/European market and currently available in
Dutch only. An English translation is in the works (help appreciated).

EekBoek can make use of several database systems for its storage.
Support for the SQLite database is included.

For GUI support, install %{name}-gui.

For production use, you are invited to install the %{name}-db-postgresql
database package.

%package gui
Summary: %{name} graphical user interface
AutoReqProv: 0
Requires: %{name} = %{version}-%{release}
Requires: perl(Wx) >= 0.99
%description gui
This package contains the wxWidgets (GUI) extension for %{name}.

%package db-postgresql
Summary: PostgreSQL database driver for %{name}
AutoReqProv: 0
Requires: %{name} = %{version}-%{release}
Requires: perl(DBD::Pg) >= 1.41
%description db-postgresql
EekBoek can make use of several database systems for its storage.
This package contains the PostgreSQL database driver for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

chmod 0664 MANIFEST

%build

%{__perl} Makefile.PL
make
%{__mkdir} examples
%{__mv} emacs/eekboek-mode.el examples
%install
%{__rm} -rf %{buildroot}
%global ebconf  %{_sysconfdir}/%{lcname}
%global ebshare %{_datadir}/%{name}-%{version}
%{__mkdir_p} %{buildroot}%{ebconf}
%{__mkdir_p} %{buildroot}%{ebshare}/lib
%{__mkdir_p} %{buildroot}%{_bindir}
%{__install} -p -m 0644 blib/lib/EB/examples/%{lcname}.conf %{buildroot}%{ebconf}/%{lcname}.conf
%{__find} blib/lib -type f -name .exists -delete
%{__find} blib/lib -depth -type d -name auto -exec rm -fr {} \;
%{__find} blib/lib -type d -printf "%{__mkdir} %{buildroot}%{ebshare}/lib/%%P\n" | sh -x
%{__find} blib/lib ! -type d -printf "%{__install} -p -m 0644 %p %{buildroot}%{ebshare}/lib/%%P\n" | sh -x
for script in ebshell ebwxshell
do
  echo "#!%{__perl}" > %{buildroot}%{_bindir}/${script}
  %{__sed} -s "s;# use lib qw(EekBoekLibrary;use lib qw(%{ebshare}/lib;" \
    < script/${script} >> %{buildroot}%{_bindir}/${script}
  %{__chmod} 0755 %{buildroot}%{_bindir}/${script}
  %{__mkdir_p} %{buildroot}%{_mandir}/man1
  pod2man blib/script/${script} > %{buildroot}%{_mandir}/man1/${script}.1
done
%{__mkdir_p} %{buildroot}%{_datadir}/pixmaps
%{__install} -p -m 0664 lib/EB/res/Wx/icons/ebicon.png %{buildroot}%{_datadir}/pixmaps/
for script in ebwxshell
do
  desktop-file-install --delete-original \
    --dir=%{buildroot}%{_datadir}/applications ${script}.desktop
  desktop-file-validate %{buildroot}/%{_datadir}/applications/${script}.desktop
done
%oreon_autofiles EekBoek-gui usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles EekBoek-db-postgresql usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if %{dbtests}
make test
%else
env EB_SKIPDBTESTS=1 make test
%endif
%files -f %{oreon_filedir}/main.list
%files -n EekBoek-gui -f %{oreon_filedir}/EekBoek-gui.list
%files -n EekBoek-db-postgresql -f %{oreon_filedir}/EekBoek-db-postgresql.list

%changelog

%autochangelog
