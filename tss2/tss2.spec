#
# Spec file for IBM's TSS for the TPM 2.0
#
%{!?__global_ldflags: %global __global_ldflags -Wl,-z,relro}

%global incname ibmtss

Name:           tss2
# this is the release of the TSS library
Version:        2.3.2
# this is the release of the fedora package, goes back to 1 when version changes
Release:        4%{?dist}
Epoch:          1
Summary:        IBM's TCG Software Stack (TSS) for TPM 2.0 and related utilities

License:        BSD-3-Clause AND LicenseRef-TCGL
URL:            https://sourceforge.net/projects/ibmtpm20tss/
Source0:        https://sourceforge.net/projects/ibmtpm20tss/files/ibmtss%{version}.tar.gz

BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  gcc
BuildRequires:  openssl-devel
Requires:       openssl

%description
TSS2 is a user space Trusted Computing Group's Software Stack (TSS) for
TPM 2.0.  It implements the functionality equivalent to the TCG TSS
working group's ESAPI, SAPI, and TCTI layers (and perhaps more) but with
a hopefully far simpler interface.

It comes with about 120 "TPM tools" that can be used for rapid prototyping,
education and debugging. 

%package devel
Summary:        Development libraries and headers for IBM's TSS 2.0
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description devel
Development libraries and headers for IBM's TSS 2.0. You will need this in
order to build TSS 2.0 applications.

%prep
%autosetup -p1 -c %{name}-%{version}

%build
autoreconf -vi
%configure --disable-static --disable-tpm-1.2 --program-prefix=tss
CCFLAGS="%{optflags}" \
LNFLAGS="%{__global_ldflags}" \
%{make_build}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%ldconfig_scriptlets

# files in the tss2 package
%files
%license LICENSE
# becomes /usr/bin/tss*, the command line utilities
%{_bindir}/tss*
# becomes /usr/lib64
%{_libdir}/libibmtss.so.2
%{_libdir}/libibmtss.so.2.*
%{_libdir}/libibmtssutils.so.2
%{_libdir}/libibmtssutils.so.2.*
%attr(0644, root, root) %{_mandir}/man1/tss*.1*

# files devel is the tss2-devel package
%files devel
# becomes /usr/include/ibmtss, the headers
%{_includedir}/%{incname}
# becomes /usr/lib64
%{_libdir}/libibmtss.so
%{_libdir}/libibmtssutils.so
%doc ibmtss.docx

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.3.2-4
- Prepare for Oreon 11 (RP1)
