%global source0_hash b9389f8bfe3f78469e5208fef14137c2d025422020b0afd0a2da21b1c803a7bd
Name: esorex
Version: 3.14a2
Release:        1%{?dist}
Summary:        Recipe Execution Tool of the European Southern Observatory
License: GPL-2.0-or-later
URL: http://www.eso.org/observing/cpl/esorex.html
Source0:        https://ftp.eso.org/pub/dfs/pipelines/libraries/%{name}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  cfitsio-devel
BuildRequires:  cpl-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
