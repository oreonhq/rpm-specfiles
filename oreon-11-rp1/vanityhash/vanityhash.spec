%global source0_hash 25a593f1dab25192e13b2ec717a9e3f8348886f3f36c22289c7e5184279a38fb

Name:           vanityhash  
Version:        1.1
Release:        32%{?dist}
Summary:        Hexadecimal hash fragment creation tool
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.finnie.org/software/%{name}/
Source0:        %{url}%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
Requires:       perl(Digest::MD2)
Requires:       perl(Digest::MD4)
Requires:       perl(Digest::MD5)
Requires:       perl(Digest::SHA)
Requires:       perl(Digest::CRC)

%description
This is a tool that can discover data to be added to the end of a file to
produce a desired hexadecimal hash fragment.  It searches a message space and
runs a hashing algorithm against the original data plus the appended data to
determine if the desired hash fragment is present.  vanityhash can run
multiple parallel workers to effectively make use of multiple processors/cores/
threads, and supports multiple hash digest types (MD5, SHA-1, SHA-256, etc).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
make %{?_smp_mflags}

# tests only loads run-time dependencies. They do not exhibit vanityhash code
# at all.
#%%check
#make test

%install
make install DESTDIR=%{buildroot} PREFIX=%{_prefix}

%files
%license COPYING
%doc ChangeLog README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
