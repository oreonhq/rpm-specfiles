%global source0_hash 6f6bb415ed2fda1452da8750bcf1ca0484ac2e5ee68d58eaeccfa37cbbfd6fc9

%{!?tcl_version: %global tcl_version %(echo 'puts $tcl_version' | tclsh8)}
%{!?tcl_sitearch: %global tcl_sitearch %{_libdir}/tcl%{tcl_version}}
%global realname trf

Name:		tcl-%{realname}
Version:	2.1.4
Release:	36%{?dist}
Summary:	Tcl extension providing "transformer" commands
License:	TCL AND BSD-3-Clause AND LGPL-2.1-or-later AND GPL-2.0-or-later AND LicenseRef-Fedora-Public-Domain AND OpenSSL
URL:		http://tcltrf.sourceforge.net
# We can't use the upstream source because it includes the non-free ripemd implementation
# Source0:	http://downloads.sourceforge.net/tcl%%{realname}/%%{realname}%%{version}.tar.bz2
# To make the clean tarball, just run:
# rm -rf doc/ripemd160.man doc/html/ripemd160.html doc/html/ripemd128.html ./doc/tmml/ripemd128.tmml ./doc/tmml/ripemd160.tmml ./doc/ripemd128.man 
# ./doc/digest/ripemd.inc ./generic/ripemd/ generic/rmd1* tea.tests/rmd1* tests/rmd1*
# We also need to remove the non-free win/msvcrt.dll
# rm -rf win/msvcrt.dll
Source0:	%{realname}%{version}-noripemd.tar.bz2
# BSD licensed haval bits, included code is older and has bad license
Source1:	http://labs.calyptix.com/haval-1.1.tar.gz
Patch0:		trf2.1.3-havalfixes.patch
Patch1:		trf2.1.4-noripemd.patch
Patch2:		trf2.1.4-loadman-type-fix.patch
Patch3:		trf2.1.4-c23.patch
# Patch4:		trf2.1.4-no-ansi-args.patch
Provides:	%{realname} = %{version}-%{release}
BuildRequires:  make
BuildRequires:  gcc
# This ancient code doesn't work with tcl 9.
BuildRequires:	tcl8-devel, tk8-devel, zlib-devel, bzip2-devel, openssl-devel
Requires:	tcl(abi) = 8.6
Requires:	bzip2, zlib, openssl

%description
Trf is an extension library to the script language tcl. It provides 
transformer procedures which change the flow of bytes through a channel 
in arbitrary ways. The underlying functionality in the core is that of 
stacked channels which allows code outside of the core to intercept all 
actions (read/write) on a channel.

Among the applications of the above provided here are compression, 
charset recording, error correction, and hash generation. 

%package devel
Summary:	Development files for tcl-%{realname}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for tcl-%{realname}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{realname}%{version}
rm -rf generic/haval/ generic/haval.1996
pushd generic
tar xfz %{SOURCE1}
mv haval-1.1 haval/
ln -s haval haval.1996
popd
%patch -P0 -p1 -b .haval
%patch -P1 -p1 -b .ripemd
%patch -P2 -p1 -b .type-fix
%patch -P3 -p1 -b .c23

# Get rid of incorrect ripemd docs
rm -rf doc/digest/ripemd.inc doc/man/ripemd128.n doc/man/ripemd160.n doc/ripemd128.man doc/tmml/ripemd128.tmml doc/tmml/ripemd160.tmml

# Nuke non-modifiable doc
rm -rf doc/painless-guide-to-crc.txt

%build
%configure --with-zlib-lib-dir=%{_libdir} --with-ssl-lib-dir=%{_libdir} --with-bz2-lib-dir=%{_libdir}
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
install -d %{buildroot}%{tcl_sitearch}
mv %{buildroot}%{_libdir}/Trf%{version} %{buildroot}%{tcl_sitearch}/Trf%{version}
rm -rf %{buildroot}%{tcl_sitearch}/Trf%{version}/*.a

%files
%doc doc/ ANNOUNCE ChangeLog DESCRIPTION README*
%{tcl_sitearch}/Trf%{version}

%files devel
%{_includedir}/transform.h
%{_includedir}/trfDecls.h

%changelog
%autochangelog
