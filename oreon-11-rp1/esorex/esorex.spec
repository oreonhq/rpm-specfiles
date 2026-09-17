%global source0_hash 13cf719c5babbad3ee12d807676cd25df8bc84068b7f6f2179a56877ea7d47b4

Name: esorex
Version: 3.13.7
Release: 9%{?dist}
Summary: Recipe Execution Tool of the European Southern Observatory 

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: http://www.eso.org/observing/cpl/esorex.html
Source0: https://ftp.eso.org/pub/dfs/pipelines/libraries/%{name}/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires: gcc gcc-c++
BuildRequires: cpl-devel
BuildRequires: cfitsio-devel
BuildRequires: autoconf >= 2.71
BuildRequires: automake

%description
EsoRex is the ESO Recipe Execution Tool. It can list, configure and 
execute CPL-based recipes from the command line.
One of the features provided by the CPL is the ability to create 
data-reduction algorithms that run as plugins (dynamic libraries). These 
are called recipes and are one of the main aspects of the 
CPL data-reduction development environment.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
autoreconf
%configure  --with-cpl-libs=%{_libdir}
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%files
%doc AUTHORS README BUGS ChangeLog
%license COPYING
%config(noreplace) %{_sysconfdir}/*
%{_bindir}/*
%{_datadir}/bash-completion/completions/esorex

%changelog
%autochangelog
