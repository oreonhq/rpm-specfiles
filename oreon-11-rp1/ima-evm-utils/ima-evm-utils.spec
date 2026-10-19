%global source0_hash 9346a5ccd5ca77caf6a9d2ac0d83873c04d0372414a632126df4e7a88bedff4a
%global bootstrap 0
%if 0%{bootstrap}
%global compat_soversion 4
%endif
Name:    ima-evm-utils
Version: 1.6.2
Release:        1%{?dist}
Summary:        IMA/EVM support utilities
License: GPL-2.0-or-later
Url:     https://github.com/linux-integrity/
Source0:        https://github.com/linux-integrity//ima-evm-utils/releases/download/v1.6.2/ima-evm-utils-1.6.2.tar.gz
Source2: dracut-98-integrity.conf
Source3: ima-add-sigs.sh
Source4: ima-setup.sh
Source100: policy-01-appraise-executable-and-lib-signatures
Source101: policy-02-keylime-remote-attestation
Source200: policy_list
%if 0%{bootstrap}
Source10: ima-evm-utils-1.5.tar.gz
%endif
Requires: %{name}-libs = %{version}-%{release}
Requires: rpm-plugin-ima
Requires: keyutils
Requires: attr
# oreon:deps
BuildRequires:  asciidoc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  keyutils-libs-devel
BuildRequires:  libtool
BuildRequires:  libxslt
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  tpm2-tss-devel
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
install -D -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/ima/dracut-98-integrity.conf
mkdir -p -m 755 $RPM_BUILD_ROOT%{_datadir}/ima/policies
while IFS= read -r policy_file
do
  install -m 644 %{_sourcedir}/policy-"$policy_file" $RPM_BUILD_ROOT%{_datadir}/ima/policies/"$policy_file"
done < %{SOURCE200}
install -D %{SOURCE3} $RPM_BUILD_ROOT%{_bindir}/ima-add-sigs
install -D %{SOURCE4} $RPM_BUILD_ROOT%{_bindir}/ima-setup
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n ima-evm-utils-libs -f %{oreon_filedir}/ima-evm-utils-libs.list
%files -n ima-evm-utils-devel -f %{oreon_filedir}/ima-evm-utils-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.6.2-10
- Prepare for Oreon 11 (RP1)
