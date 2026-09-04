%global source0_hash c2f8eb98e60530df53211985d4b403b6e97a7a969833c1a6d1bf83561da0c781

Summary:      Platform independent library for scheme
Name:         slib
Version:      3c1
Release:      %autorelease
License:      LicenseRef-SLIB
BuildArch:    noarch
Source0:      http://groups.csail.mit.edu/mac/ftpdir/scm/slib-%{version}.zip
URL:          http://swissnet.ai.mit.edu/~jaffer/SLIB.html

%description
"SLIB" is a portable library for the programming language Scheme.
It provides a platform independent framework for using "packages" of
Scheme procedures and syntax.  As distributed, SLIB contains useful
packages for all Scheme implementations.  Its catalog can be
transparently extended to accommodate packages specific to a site,
implementation, user, or directory.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}
sed -r -i "s,/usr/(local/)?lib/slib,%{_datadir}/slib,g" *.init

%build

%install
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/slib
cp *.scm *.init *.xyz *.txt *.dat *.ps ${RPM_BUILD_ROOT}%{_datadir}/slib
mkdir -p ${RPM_BUILD_ROOT}%{_infodir}
install -m644 slib.info $RPM_BUILD_ROOT%{_infodir}

%files
%dir %{_datadir}/slib
%doc ANNOUNCE README COPYING FAQ ChangeLog
%{_datadir}/slib/*
%{_infodir}/slib.*

%changelog
%autochangelog
