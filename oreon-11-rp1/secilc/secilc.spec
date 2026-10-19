%global source2_hash 4de0d98110bfa86ccc76afc8f1397226c02aa6d6496a6d1153044395f5851741
%global source1_hash 60e9df09546d7dc505819e4b87bbaf0e2421e6b46e0a91c90e7c0b947ce4a458
%global source0_hash 1fb7de005d35ae0ac6ff8f8fc955d08a15b5c1a67e961b97ef987576af0db11a
%global libsepolver 3.11-1
Name:           secilc
Version:        3.11
Release:        1%{?dist}
Summary:        The SELinux CIL Compiler
License:        BSD-2-Clause
URL:            https://github.com/SELinuxProject/selinux/wiki
Source0:        https://github.com/SELinuxProject/selinux/releases/download/%{version}/secilc-%{version}.tar.gz
Source1:        https://github.com/SELinuxProject/selinux/releases/download/%{version}/secilc-%{version}.tar.gz.asc
Source2:        https://github.com/perfinion.gpg
Requires:       libsepol >= %{libsepolver}
# oreon:deps
BuildRequires:  dblatex
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  libsepol-static
BuildRequires:  make
BuildRequires:  pandoc-pdf
BuildRequires:  texlive-mdwtools
BuildRequires:  xmlto
# /oreon:deps
%description
The SELinux CIL Compiler is a compiler that converts the CIL language as
described on the CIL design wiki into a kernel binary policy file.
Please see the CIL Design Wiki at:
http://github.com/SELinuxProject/cil/wiki/
for more information about the goals and features on the CIL language.

%package doc
Summary:        Documentation for the SELinux CIL Compiler
BuildArch:      noarch
%description doc
The SELinux CIL Compiler is a compiler that converts the CIL language as
described on the CIL design wiki into a kernel binary policy file.
Please see the CIL Design Wiki at:
http://github.com/SELinuxProject/cil/wiki/
for more information about the goals and features on the CIL language.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p 2 -n secilc-%{version}

%build

%set_build_flags
make %{?_smp_mflags} LIBSEPOL_STATIC=%{_libdir}/libsepol.a
pushd docs
make %{?_smp_mflags}
popd
%install
make %{?_smp_mflags} DESTDIR="%{buildroot}" SBINDIR="%{buildroot}%{_sbindir}" LIBDIR="%{buildroot}%{_libdir}" install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n secilc-doc -f %{oreon_filedir}/secilc-doc.list

%changelog

%autochangelog
