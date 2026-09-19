%global source0_hash 3457f6f3e47dd8c6704049cef81cb0c5a35cc32df9fe800b5fbb470804f0885f

Name:           tofrodos
Version:        1.7.13
Release:        27%{?dist}
Summary:        Converts text files between MSDOS and Unix file formats
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://www.thefreecountry.com/tofrodos/
Source0:        http://tofrodos.sourceforge.net/download/tofrodos-%{version}.tar.gz

BuildRequires: make
BuildRequires:	gcc

%description
Tofrodos is a text file conversion utility that converts ASCII and Unicode 
UTF-8 files between the MSDOS (or Windows) format, which traditionally have 
CR/LF (carriage return/line feed) pairs as their new line delimiters, and 
the Unix format, which usually have LFs (line feeds) to terminate each line.

It is a useful utility to have around when you have to convert files between 
MSDOS (or Windows) and Unix/Linux/BSD (and her clones and variants). It comes 
standard with a number of systems and is often found on the system as "todos",
"fromdos", "dos2unix" and "unix2dos".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn tofrodos

%build
make -C src/ TFLAG="%{optflags}" LDFLAGS="%{?__global_ldflags}" %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_mandir}/man1
make -C src/ install INSTALL="install -p" BINDIR="%{buildroot}%{_bindir}" MANDIR="%{buildroot}%{_mandir}/man1/" DESTDIR=%{buildroot}

%files
%doc COPYING readme.txt tofrodos.html
%{_bindir}/fromdos
%{_bindir}/todos
%{_mandir}/man1/fromdos.1*
%{_mandir}/man1/todos.1*

%changelog
%autochangelog
