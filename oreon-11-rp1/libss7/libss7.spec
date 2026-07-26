%global source0_hash 091f1c14dcf13a094021334218cde363041816fa5b5037caee38719e4e6891c7

Name:           libss7
Version:        2.0.1
Release:        %autorelease
%global so_version 2.0
Summary:        SS7 protocol services to applications

# The Makefile is GPL-2.0-or-later, but does not contribute to the licenses of
# the binary RPMs.
License:        GPL-2.0-only WITH Asterisk-exception
SourceLicense:  %{license} AND GPL-2.0-or-later
URL:            https://www.asterisk.org/
%global src_base https://downloads.asterisk.org/pub/telephony/libss7/releases
Source0:        %{src_base}/libss7-%{version}.tar.gz
Source1:        %{src_base}/libss7-%{version}.tar.gz.asc
# Keyring with developer signatures created on 2021-08-27 with:
#   workdir="$(mktemp --directory)"
#   gpg2 --with-fingerprint libss7-2.0.1.tar.gz.asc 2>&1 |
#     awk '$2 == "using" { print "0x" $NF }' |
#     xargs gpg2 --homedir="${workdir}" \
#         --keyserver=hkps://keyserver.ubuntu.com --recv-keys
#   gpg2 --homedir="${workdir}" --export --export-options export-minimal \
#       > libss7.gpg
#   rm -rf "${workdir}"
# Inspect keys using:
#   gpg2 --list-keys --no-default-keyring --keyring ./libss7.gpg
Source2:        libss7.gpg

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  gpgverify

%description
libss7 is a userspace library that is used for providing SS7 protocol
services to applications. It has a working MTP2, MTP3, and ISUP for ITU and
ANSI style SS7, however it was written in a manner that will easily allow
support for other various national specific variants in the future.

%package        devel
Summary:        Development files for libss7
Requires:       libss7%{?_isa} = %{version}-%{release}

%description    devel
The libss7-devel package contains libraries and header files for
developing applications that use libss7.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build
%make_build

%install
%make_install libdir=%{_libdir}
find %{buildroot} -name '*.a' -print -delete

# Upstream does not include any tests.

%files
%license LICENSE
%doc ChangeLog
%doc NEWS*
%doc README
%doc libss7-%{version}-summary.*

%{_libdir}/libss7.so.%{so_version}

%files devel
%{_includedir}/libss7.h
%{_libdir}/libss7.so

%changelog
%autochangelog
