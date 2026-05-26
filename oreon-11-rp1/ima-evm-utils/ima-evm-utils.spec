# If the soname gets bumped we need to ship a compat library to be able
# to bootstrap and rebuild rpm else we end up with chicken and egg problem.
%global bootstrap 0

%if 0%{bootstrap}
%global compat_soversion 4
%endif

Name:    ima-evm-utils
Version: 1.6.2
Release: 10%{?dist}
Summary: IMA/EVM support utilities
License: GPL-2.0-or-later
Url:     https://github.com/linux-integrity/
Source0:        https://github.com/linux-integrity//ima-evm-utils/releases/download/v1.6.2/ima-evm-utils-1.6.2.tar.gz

# IMA setup tools
Source2: dracut-98-integrity.conf
Source3: ima-add-sigs.sh
Source4: ima-setup.sh
Source100: policy-01-appraise-executable-and-lib-signatures
Source101: policy-02-keylime-remote-attestation
Source200: policy_list

%if 0%{bootstrap}
# compat source and patches
Source10: ima-evm-utils-1.5.tar.gz
# oreon url source checksums begin
%global source0_sha256 9346a5ccd5ca77caf6a9d2ac0d83873c04d0372414a632126df4e7a88bedff4a
%global source0_file ima-evm-utils-1.6.2.tar.gz
# oreon url source checksums end
BuildRequires: openssl-devel-engine
%endif

BuildRequires: asciidoc
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gcc
BuildRequires: keyutils-libs-devel
BuildRequires: libtool
BuildRequires: libxslt
BuildRequires: make
BuildRequires: openssl-devel
BuildRequires: tpm2-tss-devel
Requires: %{name}-libs = %{version}-%{release}
Requires: rpm-plugin-ima
Requires: keyutils
Requires: attr

%description
The Trusted Computing Group(TCG) run-time Integrity Measurement Architecture
(IMA) maintains a list of hash values of executables and other sensitive
system files, as they are read or executed. These are stored in the file
systems extended attributes. The Extended Verification Module (EVM) prevents
unauthorized changes to these extended attributes on the file system.
ima-evm-utils is used to prepare the file system for these extended attributes.

%package libs
Summary: Libraries for %{name}
License: LGPL-2.0-or-later

# to avoid ima-evm-utils and rpm-plugin-ima being installed on upgrade
# to Fedora 41 - https://bugzilla.redhat.com/show_bug.cgi?id=2319827
Obsoletes: ima-evm-utils < 1.6

%description libs
This package contains the libraries for applications to use
ima-evm-utils functionality.

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}-%{release}
Requires: %{name}-libs = %{version}-%{release}

%description devel
This package provides the header files for %{name}

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/ima-evm-utils-1.6.2.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "9346a5ccd5ca77caf6a9d2ac0d83873c04d0372414a632126df4e7a88bedff4a" || { echo "oreon: Source0 SHA256 mismatch for ima-evm-utils-1.6.2.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1

%if 0%{bootstrap}
mkdir compat/
pushd compat/
tar -zxf %{SOURCE10} --strip-components=1
popd
%endif

%build
autoreconf -vif
%configure --disable-static --disable-engine --disable-debug
%make_build

%if 0%{bootstrap}
pushd compat/
autoreconf -vif
%configure --disable-static --disable-engine --disable-debug
%make_build
popd
%endif

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete

%if 0%{bootstrap}
pushd compat/src/.libs/
install -p libimaevm.so.%{compat_soversion}.0.0 %{buildroot}%{_libdir}/libimaevm.so.%{compat_soversion}.0.0
ln -s -f %{buildroot}%{_libdir}/libimaevm.so.%{compat_soversion}.0.0 %{buildroot}%{_libdir}/libimaevm.so.%{compat_soversion}
popd
%endif

%ldconfig_scriptlets

# IMA setup tools
install -D -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/ima/dracut-98-integrity.conf

mkdir -p -m 755 $RPM_BUILD_ROOT%{_datadir}/ima/policies
while IFS= read -r policy_file
do
  install -m 644 %{_sourcedir}/policy-"$policy_file" $RPM_BUILD_ROOT%{_datadir}/ima/policies/"$policy_file"
done < %{SOURCE200}

install -D %{SOURCE3} $RPM_BUILD_ROOT%{_bindir}/ima-add-sigs
install -D %{SOURCE4} $RPM_BUILD_ROOT%{_bindir}/ima-setup

%files
%license LICENSES.txt COPYING
%doc NEWS README AUTHORS
%{_bindir}/evmctl
%{_mandir}/man1/evmctl*

# IMA setup tools
%{_datadir}/ima/policies
%{_datadir}/ima/dracut-98-integrity.conf
%{_bindir}/ima-add-sigs
%{_bindir}/ima-setup

%files libs
%license LICENSES.txt COPYING.LGPL
# if you need to bump the soname version, coordinate with dependent packages
%{_libdir}/libimaevm.so.5*
%if 0%{bootstrap}
%{_libdir}/libimaevm.so.%{compat_soversion}*
%endif

%files devel
%{_pkgdocdir}/*.sh
%{_includedir}/imaevm.h
%{_libdir}/libimaevm.so

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.6.2-10
- Prepare for Oreon 11 (RP1)
