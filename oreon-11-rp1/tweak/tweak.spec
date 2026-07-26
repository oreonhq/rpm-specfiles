%global source0_hash 5b4c19b1bf8734d1623e723644b8da58150b882efa9f23bbe797c3922f295a1a

Name:           tweak
Version:        3.02

Release:        22%{?dist}
Summary:        An efficient hex editor
License:        MIT
URL:            http://www.chiark.greenend.org.uk/~sgtatham/tweak/

Source0:        http://www.chiark.greenend.org.uk/~sgtatham/tweak/tweak-%{version}.tar.gz
BuildRequires: make
BuildRequires:  gcc
BuildRequires:  ncurses-devel

%description
Tweak is a hex editor. It allows you to edit a file at very low level, letting
you see the full and exact binary contents of the file. It can be useful for
modifying binary files such as executables, editing disk or CD images,
debugging programs that generate binary file formats incorrectly, and many
other things.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

# Disable custom .c.o rule so we can use standard RPM macros instead
sed -i -e 's|^.c.o|.disabled.c.o|' Makefile

# Modify the location of filepaths to conform to Filesystem Hierarchy Standard
sed -i -e 's|^PREFIX=$(DESTDIR)/usr/local|PREFIX=$(DESTDIR)/usr|' Makefile
sed -i -e 's|^MANDIR=$(PREFIX)/man/man1|MANDIR=$(PREFIX)/share/man/man1|' Makefile

make %{?_smp_mflags} CFLAGS="%{optflags}"

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install

%files
%doc LICENCE
%doc btree.html
%{_bindir}/*
%{_mandir}/man1/*

%changelog
%autochangelog
