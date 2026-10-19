%global source0_hash 4f67afcd208c07939b88aadbf21497a702ad0a07f9b5a6ce861f9f39ffe5425b
Name:           ii
Version:        2.0
Release:        1%{?dist}
Summary:        IRC IT, simple FIFO based IRC client
License:        MIT
URL:            http://tools.suckless.org/%{name}
Source0:        http://dl.suckless.org/tools/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  binutils
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  sed
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
