%global source0_hash cdaa56671506133e2ed8e1e318d793c2a21c4a00adc53f31ffdef1ece8ace0b1
%define _hardened_build 1
Name:           stress
Version:        1.0.7
Release:        8%{?dist}
Summary:        A tool to put given subsystems under a specified load
License:        GPL-2.0-or-later
URL:            https://github.com/resurrecting-open-source-projects/stress
Source0:        https://github.com/resurrecting-open-source-projects/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
stress is not a benchmark, but is rather a tool designed to put given
subsytems under a specified load. Instances in which this is useful
include those in which a system administrator wishes to perform tuning
activities, a kernel or libc programmer wishes to evaluate denial of 
service possibilities, etc.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
chmod -x README TODO AUTHORS NEWS src/stress.c

%build

./autogen.sh
%configure
%make_build
%install
%make_install
rm -f $RPM_BUILD_ROOT%{_infodir}/dir
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
