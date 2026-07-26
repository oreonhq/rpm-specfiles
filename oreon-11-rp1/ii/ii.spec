%global source0_hash b9d9e1eae25e63071960e921af8b217ab1abe64210bd290994aca178a8dc68d2

Name:           ii
Version:        1.8
Release:        14%{?dist}
Summary:        IRC IT, simple FIFO based IRC client
License:        MIT
URL:            http://tools.suckless.org/%{name}
Source0:        http://dl.suckless.org/tools/%{name}-%{version}.tar.gz
BuildRequires:  binutils
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  sed

%description
A minimalist FIFO and file-system-based IRC client. It creates an IRC
directory tree with server, channel and nick name directories. In every
directory a FIFO in file and a normal out file is created.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
sed -i 's!^PREFIX *=.*!PREFIX = %{_prefix}!' config.mk
sed -i 's!^CFLAGS *= \(.*\)!CFLAGS = \1 %{optflags}!' config.mk
sed -i 's!^LDFLAGS *= \(.*\)!LDFLAGS = \1 %{build_ldflags}!' config.mk
sed -i 's!^LDFLAGS *= -s \(.*\)!LDFLAGS = \1!' config.mk

%build
%make_build

%install
%make_install
rm -f %{buildroot}/%{_docdir}/%{name}/LICENSE
chmod 755 %{buildroot}/%{_bindir}/%{name}

%files
%license LICENSE
%doc CHANGES FAQ README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
