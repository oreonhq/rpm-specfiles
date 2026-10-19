%global source2_hash b42f189ae001f4bcb3fab8333bca6d1ea5b89962d179ab09276791fd8fd67485
%global source1_hash 5b838ee2b10da2e23b95a665fe4831dc54c62376362f6de2bed8004d60ae2ffb
%global source0_hash 274b9b919ef3152bfb3da3a13c950dd60d6e2bcd54230ffeca298d03b40d0525
%global source2_key_fpr 37D964ACC04981C75500FB9BD55D978A8A1420E4
Name:          libmnl
Version:       1.0.5
Release:        9%{?dist}
Summary:        Minimalistic Netlink user-space library
License:       LGPL-2.1-or-later
URL:           https://netfilter.org/projects/libmnl/
Source0:        https://netfilter.org/projects/libmnl/files/%{name}-%{version}.tar.bz2
Source1:        https://netfilter.org/projects/libmnl/files/%{name}-%{version}.tar.bz2.sig
Source2:        https://netfilter.org/files/coreteam-gpg-key-0xD55D978A8A1420E4.txt
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  make
# /oreon:deps
%description
libmnl is a minimalistic user-space library oriented to Netlink developers.
There are a lot of common tasks in parsing, validating, constructing of both
the Netlink header and TLVs that are repetitive and easy to get wrong.
This library aims to provide simple helpers that allows you to re-use code and
to avoid re-inventing the wheel.

%package       devel
Summary:       Development files for %{name}
Requires:      %{name}%{?_isa} = %{version}-%{release}
%package       static
Summary:       Static development files for %{name}
Requires:      %{name}-devel%{?_isa} = %{version}-%{release}
%description   devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%description   static
The %{name}-static package contains static libraries for developing
applications that use %{name}.

%prep

%(test -z "%{source2_key_fpr}" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 key $f" >&2; exit 1; }; fpr=$(GNUPGHOME=$(mktemp -d); export GNUPGHOME; trap 'rm -rf "$GNUPGHOME"' EXIT; gpg --batch --with-colons --import-options show-only --import "$f" | awk -F: '/^fpr:/ {print toupper($10); exit}'); test "$fpr" = "%{source2_key_fpr}" || { echo "oreon: Source2 key fingerprint mismatch" >&2; exit 1; }; })
%setup -q
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'

%build

%configure --enable-static
%make_build CFLAGS="%{optflags}"
%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -delete
find examples '(' -name 'Makefile.am' -o -name 'Makefile.in' ')' -delete
find examples -type d -name '.deps' -prune -exec rm -rf {} ';'
mv examples examples-%{_arch}
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libmnl-devel -f %{oreon_filedir}/libmnl-devel.list
%files -n libmnl-static -f %{oreon_filedir}/libmnl-static.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.5-9
- Prepare for Oreon 11 (RP1)
