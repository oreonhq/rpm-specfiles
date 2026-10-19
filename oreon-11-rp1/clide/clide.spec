%global source0_hash 615f121467cca03a9c2ceff8644d25fdc88090c01178f0eccf112127b0ef1cbe
%global commit 11c08954f983345b8a4a49f330d21085d2a87603
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Name:           clide
Version:        0.9
Release:        1%{?dist}
Summary:        Color and style highlighting program for text
License:        GPL-3.0-or-later
URL:            http://suso.suso.org/xulu/Clide
Source0:        https://github.com/deltaray/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz
Patch0:         clide-Makefile.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl-podlators
# /oreon:deps
%description
clide is a program that will colorize ASCII text on the command line using ANSI
escape sequences and user defined and predefined expressions. Searches can
include Perl Compatible Regular Expressions.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{name}-%{commit}
%patch -P0 -p1

%build

make manpages
%install
make BINDIR=%{buildroot}%{_bindir} MANDIR=%{buildroot}%{_mandir}/man1 rpminstall
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
