%global source0_hash ca764003446222ad9dbd33bbc7d94cdb96fa72608705299b6cc8734cd3562211

Name:		pipebench
Version:	0.40
Release:	36%{?dist}
Summary:	Measures the speed of STDIN/STDOUT communication

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		http://www.habets.pp.se/synscan/programs.php?prog=%{name}

Source0:	http://www.habets.pp.se/synscan/files/%{name}-%{version}.tar.gz

## From: http://www.gnu.org/licenses/gpl-2.0.txt
Source1:	%{name}-GPLv2.txt
Patch0: pipebench-c99.patch

BuildRequires: make
BuildRequires:  gcc
%description
Measures the speed of a pipe, by sitting in the middle passing the data along
to the next process. See the included README for example usage.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
## Update the included LICENSE file to match the current FSF GPLv2 text.
## (Fixes the FSF address and updates the "GNU Library GPL" references to "GNU
## Lesser GPL.") Submitted to upstream via email (2011-08-24).
install -D -m 0644 %{SOURCE1} LICENSE

## Fix the Makefile; taken from the Gentoo ebuild and modified slightly.
sed -i Makefile \
	-e 's:CFLAGS=-Wall:CFLAGS+= -Wall:' \
	-e 's:$(CFLAGS) -o:$(LDFLAGS) &:g' \
	-e 's:/usr/local/bin/:$(DESTDIR)%{_bindir}:' \
	-e 's:/usr/local/man/man1/:$(DESTDIR)%{_mandir}/man1:'

%build
make %{?_smp_mflags} CFLAGS="%{optflags}"

%install
## Create the necessary filesystem skeleton.
mkdir -m 755 -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
make install DESTDIR=%{buildroot}

%files
%doc LICENSE README
%{_bindir}/%{name}
%{_mandir}/man?/%{name}.*

%changelog
%autochangelog
