%global source0_hash e632d31b45919be41b4ab29634e20926b2bdbba4086a8817e311fb68dd17c036

Name:       makepasswd
Version:    0.5.3
Release:    36%{?dist}
Summary:    Generates (pseudo-)random passwords of a desired length

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:    GPL-3.0-only
URL:        https://github.com/khorben/makepasswd/
Source0:    http://ftp.defora.org/pub/projects/makepasswd/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires: libxcrypt-devel
BuildRequires:  gcc
BuildRequires:  docbook-style-xsl
BuildRequires:  libxslt
BuildRequires:  openssl-devel

#Patch BZ 1048269
Patch0: makepasswd-0.5.3-fix-duplicate-text-in-man-page.patch

#Patch BZ 1126076
Patch1: makepasswd-0.5.3-Avoid-a-crash-on-invalid-input-values.patch

#BZ 1771883
Patch2: makepasswd-0.5.3-default-pwdlength.patch

%description
Makepasswd generates (pseudo-)random passwords of a desired length. 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0
%patch -P1 -p1
%patch -P2 -p1

%build
make %{?_smp_mflags} CFLAGSF= CFLAGS="%{optflags}" LDFLAGS="%{__global_ldflags} -lcrypt -lcrypto"

%install
install -D -p -m 755 src/makepasswd %{buildroot}%{_bindir}/makepasswd
install -D -p -m 644 doc/makepasswd.1 %{buildroot}%{_mandir}/man1/makepasswd.1

%files
%doc COPYING
%{_mandir}/man1/makepasswd.1*
%{_bindir}/makepasswd

%changelog
%autochangelog
