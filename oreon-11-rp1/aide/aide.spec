%global source0_hash 47ab7c696f0745911479a41f90d7ad99d26536e186d66c4aad093bc72d20ff5f
%global source2_key_fpr 2BBBD30FAAB29B3253BCFBA6F6947DAB68E7B931
Summary:        Intrusion detection environment
Name:           aide
Version:        0.19.4
Release:        1%{?dist}
URL:            https://github.com/aide/aide
License:        GPL-2.0-or-later
Source0:        https://github.com/aide/aide/releases/download/v%{version}/aide-%{version}.tar.gz
Source1:        aide-%{version}.tar.gz.asc
Source2:        gpgkey-aide.gpg
Source3:        aide.conf
Source4:        README.quickstart
Source5:        aide.logrotate
Requires:       logrotate
# oreon:deps
BuildRequires:  audit-libs-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  check-devel
BuildRequires:  e2fsprogs-devel
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  libacl-devel
BuildRequires:  libattr-devel
BuildRequires:  libcurl-devel
BuildRequires:  libgpg-error-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  nettle-devel
BuildRequires:  pcre2-devel
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  zlib-devel
# /oreon:deps
%description
AIDE (Advanced Intrusion Detection Environment) is a file integrity
checker and intrusion detection program.

%prep

%(test -z "%{source2_key_fpr}" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 key $f" >&2; exit 1; }; fpr=$(GNUPGHOME=$(mktemp -d); export GNUPGHOME; trap 'rm -rf "$GNUPGHOME"' EXIT; gpg --batch --with-colons --import-options show-only --import "$f" | awk -F: '/^fpr:/ {print toupper($10); exit}'); test "$fpr" = "%{source2_key_fpr}" || { echo "oreon: Source2 key fingerprint mismatch" >&2; exit 1; }; })
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1
cp -a %{SOURCE4} .

%build

%configure  \
  --disable-static \
  --with-config_file=%{_sysconfdir}/aide.conf \
  --without-gcrypt \
  --with-nettle \
  --with-zlib \
  --with-curl \
  --with-posix-acl \
  --with-selinux \
  --with-xattr \
  --with-e2fsattrs \
  --with-audit
%make_build
%check

make check
%install
%make_install bindir=%{_sbindir}
install -Dpm0644 -t %{buildroot}%{_sysconfdir} %{SOURCE3}
install -Dpm0644 %{SOURCE5} %{buildroot}%{_sysconfdir}/logrotate.d/aide
mkdir -p %{buildroot}%{_localstatedir}/log/aide
mkdir -p -m0700 %{buildroot}%{_localstatedir}/lib/aide
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.19.2-1
- Prepare for Oreon 11 (RP1)
