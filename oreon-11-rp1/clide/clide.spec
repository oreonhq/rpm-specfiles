%global source0_hash 615f121467cca03a9c2ceff8644d25fdc88090c01178f0eccf112127b0ef1cbe

%global commit 11c08954f983345b8a4a49f330d21085d2a87603
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           clide
Version:        0.9
Release:        40.20160305git%{shortcommit}%{?dist}
Summary:        Color and style highlighting program for text

License:        GPL-3.0-or-later
URL:            http://suso.suso.org/xulu/Clide
Source0:        https://github.com/deltaray/clide/archive/%{commit}/clide-%{commit}.tar.gz

# Makefile changes (sent upstream):
#  1. Preserve timestamps of the clide script and man page.
#  2. Don't compress the man page (this is done automatically).
#  3. Don't install doc files (this is done automatically).
Patch0:         clide-Makefile.patch

BuildArch:      noarch

BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl-podlators
BuildRequires:  make

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

%files
%{_bindir}/clide
%doc CHANGELOG GOALS IDEAS README.md WARNING
%license COPYING LICENSE
%{_mandir}/man1/clide.1*

%changelog
%autochangelog
