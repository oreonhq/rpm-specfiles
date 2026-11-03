%global source0_hash 09fd9f44da4813a3141e73d5e7cf7008e5660d0405f13d56c15e1da9dcecf828
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: p11-kit
Version: 0.26.2
Release: 2%{?dist}
Summary: PKCS#11 toolkit
License: BSD-3-Clause
URL: https://p11-glue.github.io/p11-kit/
Source0: https://github.com/p11-glue/p11-kit/releases/download/%{version}/p11-kit-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: patchelf
BuildRequires: libtasn1-devel
BuildRequires: libffi-devel
BuildRequires: pkgconf

%description
PKCS#11 toolkit

%package trust
Summary: PKCS#11 trust module and trust tool
Requires: p11-kit%{?_isa} = %{version}-%{release}
Provides: p11-kit-trust%{?_isa} = %{version}-%{release}

%description trust
The p11-kit trust module and trust tool, reading anchors from
%{_sysconfdir}/pki/ca-trust/source and %{_datadir}/pki/ca-trust-source.

%package devel
Summary: PKCS#11 toolkit
Requires: p11-kit%{?_isa} = %{version}-%{release}

%description devel
PKCS#11 toolkit

%prep
%oreon_sha256
%autosetup -n p11-kit-0.26.2 -p1

%build
%oreon_configure --disable-static --without-systemd --with-trust-paths=%{_sysconfdir}/pki/ca-trust/source:%{_datadir}/pki/ca-trust-source
%oreon_make

%install
%oreon_make_install
rm -f %{buildroot}%{_libdir}/*.la
find %{buildroot} -type f | while read -r f; do
  file -b "$f" | grep -q '^ELF' || continue
  r=$(patchelf --print-rpath "$f")
  if [ -n "$r" ]; then
    chmod u+w "$f"
    patchelf --remove-rpath "$f"
  fi
done
%oreon_filelist_devel
sed -i -e '\|/p11-kit-trust\.so$|d' -e '\|%{_bindir}/trust$|d' -e '\|/trust-extract-compat$|d' %{_builddir}/%{name}.files

%files -f %{_builddir}/%{name}.files
%license COPYING

%files trust
%{_libdir}/pkcs11/p11-kit-trust.so
%{_bindir}/trust
%{_libexecdir}/p11-kit/trust-extract-compat

%files devel -f %{_builddir}/%{name}-devel.files
