%global source0_hash 9a37771b0547f7b5110069f1653aacca60335daae1dba2a7a9edc99a54227a0b

Name:		fcode-utils
Version:	1.0.3
Release:	%autorelease
Summary:	Utilities for dealing with FCode
# The entire source code is GPL-2.0-only except localvalues/ and documentation/
# which are CPL-1.0 licensed
License:	GPL-2.0-only AND CPL-1.0
URL:		http://www.openfirmware.info/FCODE_suite
Source0:	https://github.com/openbios/fcode-utils/archive/v%{version}/%{name}-%{version}.tar.gz
# Submitted upstream: https://github.com/openbios/fcode-utils/pull/16
Patch1:		fcode-utils-0001-Allow-overriding-some-more-Makefile-variables.patch
# Submitted upstream: https://github.com/openbios/fcode-utils/pull/14
Patch2:		fcode-utils-0002-toke-Makefile-Declare-return-type-of-main-in-GCC-fla.patch
# For tests only
BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	tcsh

%description
Utilities for dealing with FCode, a Forth programming language dialect
compliant with ANS Forth.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
install -p -m 0644 detok/README README.detok
install -p -m 0644 toke/README README.toke

%build
CFLAGS="%{optflags}" STRIP="/bin/true" make %{?_smp_mflags}

%install
make DESTDIR="%{buildroot}/usr" install
# Install data-files
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -a localvalues $RPM_BUILD_ROOT%{_datadir}/%{name}

%check
make tests

%files
%license COPYING
%doc README README.detok README.toke documentation
%{_bindir}/detok
%{_bindir}/romheaders
%{_bindir}/toke
%{_datadir}/%{name}

%changelog
%autochangelog
