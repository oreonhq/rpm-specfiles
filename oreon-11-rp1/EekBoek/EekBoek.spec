%global source0_hash 4c227030e653d039702cf372332ee114ce97aefaa796e0aa30cd6fdc2d0240fc

# -*- rpm-spec -*-

################ Build Options ###################
%define dbtests 1
%{?_with_dbtests:    %{expand: %%global dbtests 1}}
%{?_without_dbtests: %{expand: %%global dbtests 0}}
%define debug_package %{nil}
################ End Build Options ################

Name: EekBoek
Summary: Bookkeeping software for small and medium-size businesses
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License: GPL-1.0-or-later OR Artistic-1.0-Perl
Version: 2.051
Release: 15%{?dist}
Source: https://www.eekboek.nl/dl/%{name}-%{version}.tar.gz
URL: https://www.eekboek.nl

# The package name is CamelCased. However, for convenience some
# of its data is located in files and directories that are all
# lowercase. See the %%install section.
%global lcname eekboek

# It's all plain perl, nothing architecture dependent.
BuildArch: noarch

# This package would provide many (perl) modules, but these are
# note intended for general use.
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

BuildRequires: perl-interpreter
BuildRequires: perl-generators
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.5503
BuildRequires: perl(IPC::Run3)
BuildRequires: perl(Archive::Zip)
BuildRequires: perl(HTML::Parser)
BuildRequires: perl(Term::ReadLine)
BuildRequires: perl(Term::ReadLine::Gnu)
BuildRequires: perl(DBI) >= 1.40
BuildRequires: perl(DBD::SQLite) >= 1.12
BuildRequires: perl(App::Packager) >= 1.430
BuildRequires: perl(Test::More)
BuildRequires: desktop-file-utils
BuildRequires: zip
BuildRequires: make

Obsoletes: %{name}-core < 2.00.01
Obsoletes: %{name}-contrib < 2.00.01
Conflicts: %{name}-core < 2.00.01

# For symmetry.
%global __zip   /usr/bin/zip
%global __rmdir /bin/rmdir
%global __find  /usr/bin/find

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

# This package only contains the necessary module(s) for EekBoek
# to use the PostgreSQL database.
# Installing this package will pull in the main package and
# the Perl PostgreSQL modules, if necessary.
# No %%doc required.

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

# Move some files into better places.
%{__mkdir} examples
%{__mv} emacs/eekboek-mode.el examples

%install
%{__rm} -rf %{buildroot}

# Short names for our libraries.
%global ebconf  %{_sysconfdir}/%{lcname}
%global ebshare %{_datadir}/%{name}-%{version}

%{__mkdir_p} %{buildroot}%{ebconf}
%{__mkdir_p} %{buildroot}%{ebshare}/lib
%{__mkdir_p} %{buildroot}%{_bindir}

# Install the default, system-wide config file.
%{__install} -p -m 0644 blib/lib/EB/examples/%{lcname}.conf %{buildroot}%{ebconf}/%{lcname}.conf

# Create lib dirs and copy files.
%{__find} blib/lib -type f -name .exists -delete
%{__find} blib/lib -depth -type d -name auto -exec rm -fr {} \;
%{__find} blib/lib -type d -printf "%{__mkdir} %{buildroot}%{ebshare}/lib/%%P\n" | sh -x
%{__find} blib/lib ! -type d -printf "%{__install} -p -m 0644 %p %{buildroot}%{ebshare}/lib/%%P\n" | sh -x

for script in ebshell ebwxshell
do

  # Create the main scripts.
  echo "#!%{__perl}" > %{buildroot}%{_bindir}/${script}
  %{__sed} -s "s;# use lib qw(EekBoekLibrary;use lib qw(%{ebshare}/lib;" \
    < script/${script} >> %{buildroot}%{_bindir}/${script}
  %{__chmod} 0755 %{buildroot}%{_bindir}/${script}

  # And its manual page.
  %{__mkdir_p} %{buildroot}%{_mandir}/man1
  pod2man blib/script/${script} > %{buildroot}%{_mandir}/man1/${script}.1

done

# Desktop file, icons, ...
%{__mkdir_p} %{buildroot}%{_datadir}/pixmaps
%{__install} -p -m 0664 lib/EB/res/Wx/icons/ebicon.png %{buildroot}%{_datadir}/pixmaps/
for script in ebwxshell
do
  desktop-file-install --delete-original \
    --dir=%{buildroot}%{_datadir}/applications ${script}.desktop
  desktop-file-validate %{buildroot}/%{_datadir}/applications/${script}.desktop
done

# End of install section.

%check
%if %{dbtests}
make test
%else
env EB_SKIPDBTESTS=1 make test
%endif

%files
%doc CHANGES README examples/
%dir %{_sysconfdir}/%{lcname}
%config(noreplace) %{_sysconfdir}/%{lcname}/%{lcname}.conf
%{ebshare}/
%exclude %{ebshare}/lib/EB/DB/Postgres.pm
%exclude %{ebshare}/lib/EB/Wx
%{_bindir}/ebshell
%{_mandir}/man1/ebshell*

%files gui
%doc README.gui
%{ebshare}/lib/EB/Wx
%{_bindir}/ebwxshell
%{_mandir}/man1/ebwxshell*
%{_datadir}/applications/ebwxshell.desktop
%{_datadir}/pixmaps/ebicon.png

%files db-postgresql
%doc README.postgres
%{ebshare}/lib/EB/DB/Postgres.pm

%changelog
%autochangelog
