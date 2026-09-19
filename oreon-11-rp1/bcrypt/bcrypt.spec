%global source0_hash b9c1a7c0996a305465135b90123b0c63adbb5fa7c47a24b3f347deb2696d417d

Name:           bcrypt
Version:        1.1
Release:        40%{?dist}
Summary:        File encryption utility

License:        Zlib
URL:            http://%{name}.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:         bcrypt-fencepost.patch
BuildRequires:  zlib-devel gcc

BuildRequires:  %{__perl}
BuildRequires:  %{__make}
BuildRequires: make

%description
Bcrypt is a cross platform file encryption utility. Encrypted files are
portable across all supported operating systems and processors.
Passphrases must be between 8 and 56 characters and are hashed internally
to a 448 bit key. However, all characters supplied are significant. The
stronger your passphrase, the more secure your data.

In addition to encrypting your data, bcrypt will by default overwrite the
original input file with random garbage three times before deleting it in
order to thwart data recovery attempts by persons who may gain access to
your computer. Bcrypt uses the blowfish encryption algorithm published by 
Bruce Schneier in 1993.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%patch -P0 -p1 -b .fencepost

%{__perl} -pi.orig -e 's|\/man/man1|\/share/man/man1|g' Makefile

%build
%{__make} %{?_smp_mflags} CFLAGS="%{optflags}"

%install
%{__make} install PREFIX="%{buildroot}%{_prefix}"

%files
%doc README
%license LICENSE
%doc %{_mandir}/man1/bcrypt.1*
%{_bindir}/bcrypt

%changelog
%autochangelog
