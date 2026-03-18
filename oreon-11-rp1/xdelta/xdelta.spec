Summary: A binary file delta generator
Name: xdelta
Version: 3.1.0
Release: 24%{?dist}
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License: Apache-2.0
# the latest release tarball is only in the pre-relicensing GPL repo
Source0: https://github.com/jmacd/xdelta-gpl/releases/download/v%{version}/xdelta3-%{version}.tar.gz
URL: https://github.com/jmacd/xdelta

# for testsuite
BuildRequires: make
BuildRequires:  gcc, gcc-c++
BuildRequires: ncompress
BuildRequires: xz-devel

# Man page day fixes
# ~> proposal: http://code.google.com/p/xdelta/issues/detail?id=158
# ~> private #958492
Patch1: xdelta-3.0.6-man-page-day.patch

%description
Xdelta (X for XCF: the eXperimental Computing Facility at Berkeley) is
a binary delta generator (like a diff program for binaries) and an RCS
version control replacement library. Xdelta uses a binary file delta
algorithm to replace the standard diff program used by RCS

%prep
%setup -q -n %{name}3-%{version}
%patch -P1 -p2 -b .man-page-day

%build
%configure
%make_build V=0

%install
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man1

install -m755 xdelta3 $RPM_BUILD_ROOT/%{_bindir}
install -m 644 xdelta3.1 $RPM_BUILD_ROOT/%{_mandir}/man1

# Create compat symlinks
pushd $RPM_BUILD_ROOT/%{_bindir}
ln -s xdelta3 xdelta
popd

pushd $RPM_BUILD_ROOT/%{_mandir}/man1
ln -s xdelta3.1 xdelta.1
popd

%check
./xdelta3 test

%files
%doc README.md COPYING
%{_bindir}/xdelta*
%{_mandir}/man1/xdelta*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.1.0-24
- Prepare for Oreon 11 (RP1)
