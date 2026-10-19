%global source0_hash 37ffd4c49b049194d50de66c0e4ea5e7df81f58e56a939b2d02fcb10cea6e3f1
Name:           quotatool
Version:        1.8.0
Release:        1%{?dist}
Summary:        Command-line utility for filesystem quotas
License:        GPL-2.0-only
URL:            http://quotatool.ekenberg.se
Source0:        http://quotatool.ekenberg.se/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
Quotatool is a utility to manipulate filesystem quotas from the commandline.
Most quota-utilities are interactive, requiring manual intervention from the
user. Quotatool on the other hand is not, making it suitable for use in
scripts and other non-interactive situations.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%configure
%make_build
%install
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_mandir}/man8
%make_install INSTALL_PROGRAM="%{_bindir}/install -p"
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
