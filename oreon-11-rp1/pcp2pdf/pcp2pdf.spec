%global source0_hash 0ab0b199cddd7e7e3ac15bd271b0a91e632c8801cad8628deb0e2d96e111f10a
Name:           pcp2pdf
Version:        0.3
Release:        41%{?dist}
Summary:        Utility to create PDF reports from PCP archives
License:        GPL-2.0-or-later
URL:            https://github.com/performancecopilot/pcp2pdf
Source0:        https://github.com/performancecopilot/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         fix-spurious-python-interpreter.patch
Requires:       python3-reportlab
Requires:       python3-matplotlib
Requires:       python3-pcp
BuildArch:      noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# /oreon:deps
%description
Utility to create PDF reports from Performance Co-Pilot archives. It allows to
choose sampling rate, custom graphs, custom labels and selection of which
metrics should appear in the report.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .orig

%build

%{__python3} setup.py build
%install
%{__python3} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man1
install -p -m 0644 man/pcp2pdf.1 $RPM_BUILD_ROOT%{_mandir}/man1
rm -rf $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
